#!/usr/bin/env python3
"""
Regenerates tokens.json from an alligo-design-tokens dist/ folder.

Usage:
    python3 generate-tokens.py --dist /path/to/alligo-design-tokens/dist
    python3 generate-tokens.py --dist /path/to/alligo-design-tokens/dist --out tokens.json

Where to get a dist/ folder:
    - Clone https://github.com/Alligo-AB/alligo-design-tokens and point --dist at its dist/ folder, or
    - `npm pack alligo-design-tokens@latest` in a scratch folder and unpack the tarball, then point
      --dist at <unpacked>/package/dist

What this reads (all from dist/, no primitives, no dist/tailwind color/measure files --
those have a known duplicate-segment naming bug upstream, see SKILL.md):
    - css/base/color.css      -> semantic color tokens (--color-primitive-* excluded)
    - css/base/dimension.css  -> spacing scale (--dimension-spacing-space-*) + radius
    - css/base/border.css     -> border-width shorthand tokens
    - css/base/shadow.css     -> elevation/shadow tokens
    - tailwind/typography.css -> responsive type scale, fused mobile+desktop per class,
                                  using the same size-word mapping as Magento's typography-plugin.js
                                  (x-large->xl, large->lg, medium->md, small->sm, x-small->xs)

Declaration extraction is two-pass and deliberately avoids a single "optional leading
comment" regex: matching `(?:/\*...\*/\s*)?--token-name: value;` in one pass is unsafe --
a non-greedy comment group will backtrack PAST any run of uncommented declarations to
reach the next real comment further down the file, silently swallowing every declaration
in between as "comment text". That exact bug dropped 5 real shadow tokens
(elevation-t-20 through elevation-t-100, which have no comment of their own and sit right
after the file's uncommented header block) during initial development of this script.
Instead: pass 1 finds every declaration with an unambiguous regex (no comments involved,
so nothing can be swallowed); pass 2 looks only at the bounded gap of text between two
consecutive declarations to see if a comment belongs to the second one.

Diff the output against the previous tokens.json before committing -- a renamed or removed
token should be a deliberate, reviewed change, not a silent one.
"""
import re, json, os, argparse, sys


def read(dist, path):
    full = os.path.join(dist, path)
    if not os.path.isfile(full):
        sys.exit(f"Expected file not found: {full}\nCheck --dist points at the dist/ folder itself.")
    with open(full, encoding="utf-8") as f:
        return f.read()


def extract_declarations(css, prefix):
    """
    Two-pass, comment-safe extraction of `--{prefix}-name: value;` declarations.
    Returns a list of (name, value, comment) tuples, in file order.
    Pass 1: find every declaration with a regex that never looks at comments, so nothing
    can be lost to comment-group backtracking.
    Pass 2: for each declaration, look at the text between the end of the previous
    declaration (or start of file) and the start of this one; if it contains a
    `/* ... */` comment, that comment belongs to this declaration.
    """
    decl_re = re.compile(rf'(--{prefix}-[a-zA-Z0-9-]+):\s*([^;]+);')
    matches = list(decl_re.finditer(css))
    results = []
    prev_end = 0
    for m in matches:
        gap = css[prev_end:m.start()]
        comment_match = re.search(r'/\*(.*?)\*/\s*$', gap, re.DOTALL)
        comment = re.sub(r'\s+', ' ', comment_match.group(1)).strip() if comment_match else ""
        name = m.group(1)[len(f"--{prefix}-"):]
        value = m.group(2).strip()
        results.append((name, value, comment))
        prev_end = m.end()
    return results


def parse_colors(dist):
    css = read(dist, "css/base/color.css")
    colors = {}
    for name, value, comment in extract_declarations(css, "color"):
        if name.startswith("primitive-"):
            continue
        fallback_match = re.search(r'#[0-9a-fA-F]{3,8}', value)
        literal = fallback_match.group(0) if fallback_match else value
        if len(comment) > 160:
            comment = comment[:157] + "..."
        colors[name] = {"var": f"--color-{name}", "value": literal, "description": comment or None}
    return colors


def parse_spacing(dist):
    css = read(dist, "css/base/dimension.css")
    spacing = {}
    for name, value, _ in extract_declarations(css, "dimension"):
        m = re.match(r'spacing-space-(\d+)$', name)
        if not m:
            continue
        n = m.group(1)
        rem_match = re.search(r'([\d.]+rem)', value)
        spacing[f"space-{n}"] = {"var": f"--dimension-{name}", "px": f"{n}px",
                                  "value": rem_match.group(1) if rem_match else value}
    return dict(sorted(spacing.items(), key=lambda kv: int(kv[0].split('-')[1])))


def parse_radius_border(dist):
    dim_css = read(dist, "css/base/dimension.css")
    radius = {}
    for name, value, _ in extract_declarations(dim_css, "dimension"):
        m = re.match(r'radius-([a-z0-9-]+)$', name)
        if not m:
            continue
        rem_match = re.search(r'([\d.]+rem)', value)
        radius[m.group(1)] = {"var": f"--dimension-{name}", "value": rem_match.group(1) if rem_match else value}

    border_css = read(dist, "css/base/border.css")
    borders = {}
    for name, value, _ in extract_declarations(border_css, "border"):
        borders[name] = {"var": f"--border-{name}", "value": value}
    return radius, borders


def parse_shadows(dist):
    css = read(dist, "css/base/shadow.css")
    shadows = {}
    for name, value, comment in extract_declarations(css, "shadow"):
        shadows[name] = {"var": f"--shadow-{name}", "value": value, "description": comment or None}
    return shadows


# (.+?) is deliberately non-greedy: a greedy (.+) prefers the LONGEST possible
# category match, which mis-splits e.g. "body-x-large" as category="body-x",
# size="large" (since "large" alone also matches the alternation) instead of the
# correct category="body", size="x-large". Confirmed this dropped body-xl and
# headline-xl entirely (silently renamed to body-x-lg / headline-x-lg) during
# initial development. Non-greedy tries the shortest category first and stops at
# the first dash-boundary whose tail satisfies the full SIZES alternation, which
# is always the linguistically correct split for every category name actually
# used in this token set (display, headline, title, label, alt-label, body).
SIZE_MAP = {"x-large": "xl", "large": "lg", "medium": "md", "small": "sm", "x-small": "xs"}
SIZES = "|".join(SIZE_MAP.keys())
RESPONSIVE_RE = re.compile(rf'^typography-(mobile|desktop)-(.+?)-({SIZES})$')


def parse_props(block):
    props = {}
    for line in block.strip().split(";"):
        line = line.strip()
        if not line or ":" not in line:
            continue
        prop, _, val = line.partition(":")
        prop, val = prop.strip(), val.strip()
        if prop in ("font-family", "font-style", "text-indent"):
            continue
        props[prop] = val
    return props


def parse_typography(dist):
    css = read(dist, "tailwind/typography.css")
    mobile, desktop = {}, {}
    for m in re.finditer(r'\.(typography-[a-z0-9-]+)\s*\{([^}]+)\}', css):
        full_class, block = m.group(1), m.group(2)
        rm = RESPONSIVE_RE.match(full_class)
        if not rm:
            continue
        scope, category, size = rm.group(1), rm.group(2), rm.group(3)
        short_name = f"{category}-{SIZE_MAP[size]}"
        props = parse_props(block)
        (mobile if scope == "mobile" else desktop)[short_name] = props

    all_names = sorted(set(mobile) | set(desktop))
    typography = {}
    for name in all_names:
        mp, dp = mobile.get(name, {}), desktop.get(name, {})
        diff = {k: v for k, v in dp.items() if mp.get(k) != v}
        typography[name] = {"mobile": mp, "desktopOverride": diff, "breakpoint": "769px"}
    return typography


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dist", required=True, help="Path to alligo-design-tokens dist/ folder")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "tokens.json"),
                     help="Output path for tokens.json (default: alongside this script)")
    args = ap.parse_args()

    tokens = {
        "$meta": {
            "source": "alligo-design-tokens",
            "generatedFrom": [
                "dist/css/base/color.css",
                "dist/css/base/dimension.css",
                "dist/css/base/border.css",
                "dist/css/base/shadow.css",
                "dist/tailwind/typography.css",
            ],
            "note": ("Semantic tokens only (primitives excluded). Typography entries follow the same "
                      "mobile-base + desktop-diff convention as the Magento typography-plugin.js, fused "
                      "at the 769px breakpoint. Regenerate with generate-tokens.py whenever "
                      "alligo-design-tokens publishes a new version -- do not hand-edit values."),
            "npmPackage": "alligo-design-tokens",
            "cdnUrlUsedInThisRepo": "https://unpkg.com/alligo-design-tokens@latest/dist/css/index.css",
        },
        "color": dict(sorted(parse_colors(args.dist).items())),
        "spacing": parse_spacing(args.dist),
        **dict(zip(("radius", "border"), parse_radius_border(args.dist))),
        "shadow": dict(sorted(parse_shadows(args.dist).items())),
        "typography": parse_typography(args.dist),
    }

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=2, ensure_ascii=False)

    print(f"color: {len(tokens['color'])}  spacing: {len(tokens['spacing'])}  "
          f"radius: {len(tokens['radius'])}  border: {len(tokens['border'])}  "
          f"shadow: {len(tokens['shadow'])}  typography: {len(tokens['typography'])}")
    print(f"written to {args.out}")


if __name__ == "__main__":
    main()
