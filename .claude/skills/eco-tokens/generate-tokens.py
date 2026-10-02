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
    - css/base/typography.css + css/base/dimension.css + css/mobiletypography/dimension.css
                              -> responsive type scale, fused mobile+desktop per token

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


# Typography is now exported by Supernova as semantic type-scale tokens plus two
# dimension themes:
#   css/base/typography.css              -> canonical type-scale names + descriptions
#   css/base/dimension.css               -> desktop/base type dimensions
#   css/mobiletypography/dimension.css   -> mobile type dimensions
#
# Older package versions encoded mobile/desktop directly in Tailwind class names.
# Do not parse tailwind/typography.css for responsiveness: current exports use class
# names such as typography-type-scale-design-tokens-body-body-lg and no longer carry
# a mobile/desktop scope there.
TYPE_SCALE_PREFIX = "type-scale-design-tokens-"
TYPE_PROPS = ("font-weight", "font-size", "line-height", "letter-spacing")


def fallback_value(value):
    """Return a CSS var() fallback when present, otherwise the literal value."""
    m = re.search(r'var\(\s*--[^,]+,\s*([^\)]+)\)', value)
    return m.group(1).strip() if m else value.strip()


def normalize_typography_value(prop, value):
    value = fallback_value(value)
    # Supernova currently serializes semantic font-weight dimensions as e.g. 500px.
    # CSS font-weight itself is unitless, and the previous tokens.json contract was too.
    if prop == "font-weight":
        m = re.fullmatch(r'([0-9]+(?:\.[0-9]+)?)px', value)
        if m:
            return m.group(1)
    return value


def typography_dimensions(dist, theme_path):
    css = read(dist, theme_path)
    declarations = {name: value for name, value, _ in extract_declarations(css, "dimension")}
    result = {}
    for name in declarations:
        for prop in TYPE_PROPS:
            prefix = f"{prop}-"
            if name.startswith(prefix):
                token_name = name[len(prefix):]
                result.setdefault(token_name, {})[prop] = normalize_typography_value(
                    prop, declarations[name]
                )
                break
    return result


def parse_typography(dist):
    type_css = read(dist, "css/base/typography.css")
    mobile_dims = typography_dimensions(dist, "css/mobiletypography/dimension.css")
    desktop_dims = typography_dimensions(dist, "css/base/dimension.css")

    # The type-scale file is the source of truth for which semantic typography styles
    # actually exist. This deliberately excludes the separate `modifiers-*` tokens.
    styles = {}
    for name, _, comment in extract_declarations(type_css, "typography"):
        if not name.startswith(TYPE_SCALE_PREFIX):
            continue
        short_name = name[len(TYPE_SCALE_PREFIX):]
        if short_name.startswith("modifiers-"):
            continue
        # Current Supernova export contains a redundant category segment only for
        # alt-label (`alt-label-alt-label-lg`). Normalize it to the public token name.
        short_name = re.sub(r'^alt-label-alt-label-', 'alt-label-', short_name)
        styles[short_name] = comment or None

    typography = {}
    for name in styles:
        mp = mobile_dims.get(name, {})
        dp = desktop_dims.get(name, {})
        if not mp and not dp:
            continue
        # Keep the established ECO contract: mobile is complete; desktopOverride only
        # contains values that differ at the existing 769px breakpoint.
        base = mp or dp
        diff = {k: v for k, v in dp.items() if base.get(k) != v}
        entry = {"mobile": base, "desktopOverride": diff, "breakpoint": "769px"}
        if styles[name]:
            entry["description"] = styles[name]
        typography[name] = entry
    return dict(sorted(typography.items()))

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
                "dist/css/base/typography.css",
                "dist/css/mobiletypography/dimension.css",
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
