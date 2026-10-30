// Builds the ECO Design System docs into dist/ with the same folder layout as the repo,
// so the root-absolute and relative paths in the docs keep working unchanged.
import { cpSync, copyFileSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { dirname, join, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const docs = join(root, 'eco-design-system');
const out = join(root, 'dist');

// Generator sources and archived visuals are not published
const EXCLUDED = new Set(['gen', 'card-visuals-archive', '.DS_Store']);

rmSync(out, { recursive: true, force: true });

// The docs folder itself
cpSync(docs, join(out, 'eco-design-system'), {
  recursive: true,
  filter: (src) => !relative(docs, src).split(sep).some((part) => EXCLUDED.has(part)),
});

// Shared CSS, JS, Hairline animations and images the docs load from repo-root paths
for (const dir of ['components', 'hairline', 'images']) {
  cpSync(join(root, dir), join(out, dir), { recursive: true });
}

// Token file the foundation pages fetch at runtime (../../.claude/skills/eco-tokens/tokens.json)
const tokensRel = join('.claude', 'skills', 'eco-tokens', 'tokens.json');
mkdirSync(dirname(join(out, tokensRel)), { recursive: true });
copyFileSync(join(root, tokensRel), join(out, tokensRel));

// Ask search engines not to crawl or index the docs (internal site)
writeFileSync(join(out, 'robots.txt'), 'User-agent: *\nDisallow: /\n');

// Keep docs pages out of search results. A meta tag lives in the docs output only;
// a header in vercel.json would also reach the swedol-ui-prototype project.
const docsEntry = '/eco-design-system/index.html';
for (const file of htmlFiles(out)) {
  const html = readFileSync(file, 'utf8');
  writeFileSync(file, html.replace(/<head(\s[^>]*)?>/i, (tag) => `${tag}\n  <meta name="robots" content="noindex, nofollow">`));
}

// Root of the docs domain: send visitors to the docs start page.
// Plain HTML with a script and a meta refresh, so it works on every host (domain and previews)
// without a redirect rule in vercel.json, which the prototype project would also read.
writeFileSync(join(out, 'index.html'), `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="robots" content="noindex, nofollow">
  <title>ECO Design System</title>
  <link rel="canonical" href="${docsEntry}">
  <meta http-equiv="refresh" content="0; url=${docsEntry}">
  <script>location.replace('${docsEntry}');</script>
</head>
<body>
  <a href="${docsEntry}">ECO Design System</a>
</body>
</html>
`);

function htmlFiles(dir) {
  return readdirSync(dir).flatMap((name) => {
    const path = join(dir, name);
    if (statSync(path).isDirectory()) return htmlFiles(path);
    return name.endsWith('.html') ? [path] : [];
  });
}
