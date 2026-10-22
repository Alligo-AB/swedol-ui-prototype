// Builds the ECO Design System docs into dist/ with the same folder layout as the repo,
// so the root-absolute and relative paths in the docs keep working unchanged.
import { cpSync, copyFileSync, mkdirSync, rmSync, writeFileSync } from 'node:fs';
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
