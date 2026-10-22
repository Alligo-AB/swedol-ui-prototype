"""Hero banner (Storyblok widget): four tabs Design / Usage / Reference and Examples / Storyblok.
Source: the Supernova docs (screenshots in images/hero-banner-*) + Figma anatomy frames (images/hero-banner-anatomy-*).
Uses the custom page set (c['pages']) of build.py. Run from this folder: python3 gen_hero_banner_widget.py [--force]"""
from build import *
from hero_pins import PINS

SLUG = 'hero-banner-widget'

STYLE = r'''    .sb-stage.ds-fig__stage { display: block; padding: 0; min-height: 0; background: var(--color-surface-raised-primary); }   /* a screenshot or banner picture, with numbered markers on top */
    .sb-shot { position: relative; }
    .sb-shot img { display: block; width: 100%; height: auto; }
    .sb-pin { position: absolute; transform: translate(-50%, -50%); pointer-events: none; min-width: 24px; height: 24px; padding: 0 5px; font-size: 14px; line-height: 14px; letter-spacing: 0.56px; }   /* Figma Marker = Number Large, also on mobile */
    .sb-pin--red { background: var(--color-surface-danger-default); }
    .sb-box { position: absolute; border: 3px solid var(--color-border-danger-default); pointer-events: none; }
    .hb-note { display: flex; gap: var(--dimension-spacing-space-12); padding: var(--dimension-spacing-space-16); background: var(--color-surface-raised-secondary); }
    .hb-note .mo-ic { font-size: 24px; flex: 0 0 auto; color: var(--color-icon-primary); }
    .hb-note p { margin: 0; font-size: 16px; line-height: 22px; letter-spacing: 0.32px; }   /* body-md: 16/22 mobile, 17/24 from 769px */
    @media (min-width: 769px) { .hb-note p { font-size: 17px; line-height: 24px; } }
    .hb-ex-cap { margin: 0 0 var(--dimension-spacing-space-8); }
    .hb-grid { display: grid; gap: var(--dimension-spacing-space-16); grid-template-columns: minmax(0, 1fr); margin: var(--dimension-spacing-space-16) 0; }
    @media (min-width: 769px) { .hb-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--dimension-spacing-space-24); } }
    .hb-grid figure { margin: 0; }
    .hb-grid img, .hb-one img { display: block; width: 100%; height: auto; border: 1px solid var(--color-border-primary); }
    .hb-grid figcaption, .hb-one figcaption { padding-top: var(--dimension-spacing-space-8); font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .hb-grid img { width: 100%; aspect-ratio: 1139 / 780; object-fit: cover; object-position: top; }   /* every example in a grid is the same height: cropped from the bottom */
    .hb-grid img:not(.hb-alpha) { object-fit: contain; box-sizing: border-box; padding: var(--dimension-spacing-space-24); background: var(--color-surface-raised-secondary); border: 0; }   /* a banner (not a page screenshot) is shown whole, centred on the same grey and at the same height */
    .hb-grid img.hb-alpha, .hb-one img.hb-alpha { border: 0; box-sizing: border-box; padding: var(--dimension-spacing-space-32) var(--dimension-spacing-space-24) 0; background: var(--color-surface-raised-secondary); }   /* the PNG has a transparent shadow edge: it shows on the light grey, as in Supernova */
    .hb-one { margin: var(--dimension-spacing-space-16) 0; max-width: 100%; }
    .hb-one--narrow { max-width: 360px; }
    .hb-sw { display: grid; gap: var(--dimension-spacing-space-16); grid-template-columns: minmax(0, 1fr); margin: var(--dimension-spacing-space-16) 0; }
    @media (min-width: 769px) { .hb-sw { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--dimension-spacing-space-24); } }
    .hb-sw__card { margin: 0; }
    .hb-sw__stage { display: grid; place-items: center; min-height: 240px; padding: var(--dimension-spacing-space-48) var(--dimension-spacing-space-24); background: var(--color-surface-100); }
    .hb-sw__stage--light { background: var(--color-surface-raised-secondary); }
    .hb-sw__stage--grey { background: var(--color-surface-raised-secondary); }   /* the same light grey as the anatomy figures (ds-fig__stage) */
    .hb-sw__cap { display: grid; grid-template-columns: auto 1fr; gap: var(--dimension-spacing-space-4) var(--dimension-spacing-space-12); padding-top: var(--dimension-spacing-space-8); font-size: 14px; line-height: 20px; margin: 0; }
    .hb-sw__cap dt { font-weight: 600; }
    .hb-sw__cap dd { margin: 0; color: var(--color-text-tertiary); letter-spacing: 0.36px; }
    .hb-border { display: block; width: 85%; max-width: 360px; height: auto; }
    .hb-stripes { display: flex; gap: 6px; width: 80%; transform: skewX(-24deg); }
    .hb-stripes i { flex: 1; height: 12px; background: var(--hb-accent); }
    .hb-stripes i:first-child { background: linear-gradient(90deg, transparent, var(--hb-accent)); }
    .hb-swedol { --hb-accent: var(--color-accent-default); }
    .hb-tools { --hb-accent: var(--color-primitive-color-brand-tools-accent-brand); }
    .hb-pdimg { display: block; width: 220px; max-width: 80%; height: auto; }
    .hb-pd { display: flex; gap: 6px; color: var(--color-text-primary-inverted); font-size: 40px; line-height: 36px; font-style: italic; font-weight: 700; text-transform: uppercase; }
    .hb-pd i { width: 5px; background: var(--hb-accent); transform: skewX(-12deg); }
    .hb-newsimg { display: block; width: 120px; height: 120px; }
    .hb-news { display: grid; place-items: center; width: 120px; height: 120px; border-radius: 50%; font-size: 28px; line-height: 28px; font-style: italic; font-weight: 700; text-transform: uppercase; background: var(--hb-bg); color: var(--hb-fg); }
    .hb-news--white { --hb-bg: var(--color-surface-raised-primary); --hb-fg: var(--color-text-primary); }
    .hb-news--black { --hb-bg: var(--color-surface-100); --hb-fg: var(--color-text-primary-inverted); }
    .hb-news--green { --hb-bg: var(--color-accent-default); --hb-fg: var(--color-text-primary); }
    .hb-news--red { --hb-bg: var(--color-primitive-color-brand-tools-accent-brand); --hb-fg: var(--color-text-primary-inverted); }
    .hb-txt { text-align: left; }
    .hb-txt b { display: block; font-size: 12px; line-height: 14px; letter-spacing: 0.48px; text-transform: uppercase; }
    .hb-txt strong { display: block; font-size: 32px; line-height: 32px; text-transform: uppercase; }
    .hb-txt span { display: block; font-size: 16px; line-height: 22px; }
    .hb-txt--inv { color: var(--color-text-primary-inverted); }
    .hb-btns { display: flex; flex-wrap: wrap; gap: var(--dimension-spacing-space-8); }
    .hb-yn { display: inline-flex; align-items: center; gap: var(--dimension-spacing-space-8); }   /* icon and text centred on one line */
    .hb-ic { display: block; flex: 0 0 auto; font-size: 20px; line-height: 1; }
    .hb-ic--yes { color: var(--color-text-success-default); }
    .hb-ic--no { color: var(--color-text-danger-default); }
    .hb-ic--maybe { color: var(--color-text-warning-default); }
    .hb-anat .ds-callout__pin, .sb-pin { text-transform: none; }
    .hb-anat.ds-fig__stage.ds-callout { padding-right: 72px; }
    .hb-anat.ds-fig__stage.ds-callout { display: block; overflow-x: auto; }   /* mobile: the picture keeps its size, so the markers do not collide; the figure scrolls sideways */
    .hb-anat .ds-callout__art { margin: 0 auto; width: 100%; min-width: 520px; max-width: 640px; }
    .hb-anat img { display: block; width: 100%; height: auto; }
    .ds-figs + .hb-legend, .ds-figs + .ds-bullets--num { margin-top: var(--dimension-spacing-space-16); }   /* the list under a figure: 16px */
    
    .hb-legend + .ds-figs, .ds-bullets + .ds-figs { margin-top: var(--dimension-spacing-space-40); }
    .hb-dd { display: block; width: 100%; max-width: 480px; height: auto; }
    /* spacing from the user's annotation (2026-10-21), on every page of this set */
    /* one rule for pictures: whatever comes before or after a picture is 16px away; only a list or legend followed by the next picture gets 40px */
    .ds-prose > :is(.ds-h2, .ds-h3, .hb-h4, .ds-desc, .ds-bullets, .hb-note) + :is(.hb-one, .ds-figs, .hb-grid) { margin-top: var(--dimension-spacing-space-16); }
    .ds-prose > :is(.hb-one, .ds-figs, .hb-grid) + :is(.ds-h2, .ds-h3, .hb-h4, .ds-desc, .ds-bullets, .hb-note, .hb-legend) { margin-top: var(--dimension-spacing-space-16); }
    .ds-prose > .ds-desc.ds-desc:has(+ :is(.hb-one, .ds-figs, .hb-grid)), .ds-prose > .ds-bullets.ds-bullets:not(.ds-bullets--num):has(+ :is(.hb-one, .ds-figs, .hb-grid)) { margin-bottom: 0; }   /* the paragraph's own bottom margin would collapse into the 16px */
    .ds-prose > :is(.ds-bullets--num, .hb-legend) + :is(.hb-one, .ds-figs, .hb-grid) { margin-top: var(--dimension-spacing-space-40); }
    .ds-prose > .ds-figs + .ds-h3 { margin-top: var(--dimension-spacing-space-16); }   /* figure with caption, then the next heading: 16px */
    .ds-prose > .ds-bullets + .ds-h3 { margin-top: var(--dimension-spacing-space-24); }   /* list, then the next heading: 24px */
    .ds-prose > .ds-h3.ds-h3.ds-h3:has(+ .hb-h4) { margin-bottom: 0; }   /* tripled class: beats docs.css group-heading rules */
    .ds-prose > .ds-h3 + .hb-h4 { margin-top: var(--dimension-spacing-space-8); }   /* heading, then its sub-heading: 8px */
    .hb-h4 + .hb-one, .hb-h4 + .ds-figs, .hb-h4 + .hb-grid { margin-top: var(--dimension-spacing-space-16); }   /* sub-heading, then the picture: 16px */
    .hb-legend { list-style: none; margin: 0 0 var(--dimension-spacing-space-40);   /* 40px before the next figure (when a heading follows, its own margin applies) */ padding: 0; display: grid; gap: var(--dimension-spacing-space-12); }
    .hb-legend li { display: flex; align-items: flex-start; gap: var(--dimension-spacing-space-12); }
    .hb-legend .badge-number { flex: 0 0 auto; margin-top: 3px; text-transform: none; }
    .hb-legend p { margin: 0; }
    .hb-h4 { margin: var(--dimension-spacing-space-24) 0 var(--dimension-spacing-space-4); font-size: 16px; line-height: 22px; font-weight: 600; }
    .hb-why { margin: 0 0 var(--dimension-spacing-space-4); }'''


# ---- helpers ------------------------------------------------------------------------
def imgsrc(n, ext='jpg'):
    """Screenshots with a transparent shadow edge are PNG (a jpg turns the shadow black); the rest are jpg."""
    webp = os.path.exists(os.path.join(HERE, '..', '..', 'images', 'hero-banner-%s.webp' % n))
    return '/images/hero-banner-%s.%s' % (n, 'webp' if webp else ext), ' class="hb-alpha"' if webp else ''


def pic(name, alt, cap=None, ext='jpg', narrow=False):
    src, cls = imgsrc(name, ext)
    return '<figure class="hb-one%s"><img%s src="%s" alt="%s" loading="lazy" />%s</figure>' % (' hb-one--narrow' if narrow else '', cls, src, alt, ('<figcaption>%s</figcaption>' % cap) if cap else '')


def pics(items):
    """items: [(name, alt, cap)] in a two-column grid"""
    out = ''
    for n, a, c in items:
        src, cls = imgsrc(n)
        out += '<figure><img%s src="%s" alt="%s" loading="lazy" /><figcaption>%s</figcaption></figure>' % (cls, src, a, c)
    return '<div class="hb-grid">' + out + '</div>'


def sbshot(name, alt, cap=None, box=None, pins=None, red=()):
    """A Storyblok screenshot with numbered badge-number markers (percent positions from hero_pins.PINS) and an optional red box."""
    inner = '<img src="/images/hero-banner-sb-%s.webp" alt="%s" loading="lazy" />' % (name, alt)
    if box:
        inner += '<span class="sb-box" style="left:%s%%;top:%s%%;width:%s%%;height:%s%%"></span>' % box
    for lab, x, y, r in (PINS.get(name, []) if pins is None else pins):
        inner += '<span class="badge-number sb-pin%s" style="left:%s%%;top:%s%%">%s</span>' % (' sb-pin--red' if r else '', x, y, lab)
    for lab, x, y in red:
        inner += '<span class="badge-number sb-pin sb-pin--red" style="left:%s%%;top:%s%%">%s</span>' % (x, y, lab)
    return '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage sb-stage"><div class="sb-shot">%s</div></div>%s</figure></div>' % (inner, ('<figcaption class="ds-fig__cap">%s</figcaption>' % cap) if cap else '')


def badge_list(items):
    """Legend with the same number badge as the markers: items = [(label, title, text)]"""
    return '<ul class="hb-legend">' + ''.join('<li><span class="badge-number badge-number--md" aria-hidden="true">%s</span><p class="ds-desc"><strong>%s.</strong> %s</p></li>' % (l, t, x) for l, t, x in items) + '</ul>'


def note(t, icon='info'):
    t = t.replace('inline-link--large', 'inline-link--medium')   # a link is as big as the text around it: body-md in a note
    return '<div class="hb-note"><span class="mo-ic" aria-hidden="true">%s</span><p class="ds-desc">%s</p></div>' % (icon, t)


def h4(t):
    return '<h4 class="hb-h4">%s</h4>' % t


def yn(v):
    ic, cls = {'yes': ('check_circle', 'yes'), 'no': ('cancel', 'no'), 'maybe': ('warning', 'maybe')}[v]
    return '<span class="hb-yn"><span class="mo-ic hb-ic hb-ic--%s" aria-hidden="true">%s</span>%s</span>' % (cls, ic, v.capitalize())


def why(rows):
    return ''.join('<p class="ds-desc hb-why"><strong>%s:</strong> %s</p>' % r for r in rows)


def li(items):
    return bullets(items)


def L(href, text):
    return link_large(href, text)


WEB = SLUG + '-usage.html'
REFP = SLUG + '-reference.html'
SBP = SLUG + '-storyblok.html'
DESP = SLUG + '.html'

# ======================================================================================
# 1. DESIGN
# ======================================================================================
d_anat = '<h2 class="ds-h2">Anatomy</h2>' + desc('The hero banner combines an image, typography, campaign elements and call-to-action buttons into a high-impact page header. Every part is optional except the image and the title.') + \
    '<h3 class="ds-h3 ds-group">Main hero content</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout hb-anat" id="an-main" role="img" aria-label="Anatomy of the hero banner content: 1 background image, 2 brand logo, 3a discount badge, 3b campaign price, 3c old price info, 4a pre title, 4b title, 4c preamble, 5 buttons, 6 overlay"><div class="ds-callout__art"><img id="an-main-img" src="/images/hero-banner-anatomy-main.png" alt="" /></div></figure></div>' + \
    badge_list([('1', 'Background image', 'An image for a campaign, or the header of a brand or campaign page. On a Fluid hero it fills to the left and right edge of the viewport.'), ('2*', 'Brand logo, in content', 'For brand identity. *Only for brand pages, when the content is centred in breakpoint XSmall.'), ('3a', 'Discount badge', 'A red badge with the discount or a short campaign message.'), ('3b', 'Campaign price', 'The promotional price, next to the badge.'), ('3c', 'Old price info', 'The price before the discount.'), ('4a', 'Pre title', 'Categorises the content or adds context.'), ('4b', 'Title', 'The headline or campaign message.'), ('4c', 'Preamble', 'A longer description of the campaign, product or brand.'), ('5', 'Buttons', 'Compelling calls to action. One primary and, optionally, one secondary button.'), ('6', 'Visual enhancement overlay', 'A gradient that keeps the text readable on the image.')]) + \
    '<h3 class="ds-h3 ds-group">Brand elements</h3>' + desc('Brand elements are placed on the image, never in the text column. They are the Power Deal concept, brand logos and the news badge.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout hb-anat" id="an-pd" role="img" aria-label="Anatomy of the Power Deal elements: 1 border, 2 logo"><div class="ds-callout__art"><img id="an-pd-img" src="/images/hero-banner-anatomy-powerdeal.png" alt="" /></div></figure></div>' + \
    badge_list([('1', 'Power Deal border', 'A graphic that is part of the Power Deal concept. Use it only together with the Power Deal logo.'), ('2', 'Power Deal logo', 'The logo of the Power Deal concept. Always use it together with the Power Deal border to strengthen the concept. It can sit top left, top right or bottom right.')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout hb-anat" id="an-logo" role="img" aria-label="Anatomy of the brand logo: 1 brand logo"><div class="ds-callout__art"><img id="an-logo-img" src="/images/hero-banner-anatomy-logos.png" alt="" /></div></figure></div>' + \
    badge_list([('1', 'Brand logo', 'For brand identity or a campaign-specific product logo. It can sit top right, bottom right or in the content.')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout hb-anat" id="an-news" role="img" aria-label="Anatomy of the news badge: 1 news badge"><div class="ds-callout__art"><img id="an-news-img" src="/images/hero-banner-anatomy-news.png" alt="" /></div></figure></div>' + \
    badge_list([('1', 'News badge', 'A circular badge that promotes new products and other news.')])

FIGMA_HERO = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=16892-132478'
d_size = '<h2 class="ds-h2">Size</h2>' + desc('The size of the hero follows the breakpoint. The height is set per size; it is dynamic, so if the content does not fit, the hero grows to fit the content. All values come from Figma: ' + fig_link(FIGMA_HERO, 'Hero Component', 'large') + '.') + \
    table(['Size', 'Width, regular', 'Width, fluid', 'Height'], [['XLarge', '1200px', '1440px', '450px'], ['Large', '1200px', '1440px', '450px'], ['Medium', '1023px', '–', '380px'], ['Small', '704px', '–', '350px'], ['XSmall', '375px', '–', '300px']]) + \
    note('Figma has no separate XLarge frame: XLarge uses the Large frame, with the same width and height (Supernova also gives 450px). A fluid hero is drawn only for Large, and a fluid hero grows with the viewport. Small and XSmall use the mobile base styling.')

d_meas = '<h2 class="ds-h2">Measurements</h2>' + desc('Spacing, type and element sizes of a hero, read from the Figma frames for the largest and the smallest size. Medium and Small are not listed yet.') + \
    table(['Part', 'XLarge and Large (1200×450)', 'XSmall (375×300)'], [
        ['Padding (all sides)', '56px', '24px'],
        ['Content width', 'Up to 769px', 'The full width'],
        ['Gap, texts to buttons', '24px', '16px'],
        ['Gap, between text blocks', '12px', '12px'],
        ['Pre title', '18px / 18px line, 0.18px spacing (label-lg)', '16px / 18px line, 0.32px spacing (label-lg)'],
        ['Title', '55px / 50px line', '36px / 34px line (display-lg)'],
        ['Preamble', '24px / 32px line (body-xl)', '20px / 24px line (body-xl)'],
        ['Buttons', 'Large, 2 in a row, 8px gap', 'Medium, 2 in a row, 8px gap'],
        ['Brand logo, in content', '120×36px', '100×30px'],
        ['Brand logo, in the corner', '120×36px, 56px from the edges', '50×15px, 24px from the edges'],
        ['Discount badge', '24px high, 6px side padding, 20px italic text', '20px high, 5px side padding, 17px italic text'],
        ['Campaign price', '54px / 52px line', '42px / 44px line'],
        ['Old price info', '11px / 11px line', '9px / 10px line'],
        ['Power Deal border', '24px high, 730px wide', '8px high, 317px wide'],
        ['Power Deal logo', '156×79px, 56px from the left or right, 48px from the top or bottom', '95×48px, 24px from the edges'],
        ['News badge', '104px circle, 30px italic text, 40px from the top right', '64px circle, 19px italic text, 24px from the top right'],
        ['Overlay', 'A gradient at about 167°: black at 60%, 40% and 0%', 'A gradient at about 152°: the same stops']]) + \
    note('Discount badge, campaign price and old price info are the Campaign Price card. Typefaces are Breuer Condensed, see ' + L('../foundations/typography.html', 'Typography') + '.')

stripes = lambda cls: '<img class="hb-border" src="/images/hero-banner-power-deal-border-%s.svg" alt="Power Deal border" width="730" height="24" loading="lazy" />' % ('swedol' if cls == 'hb-swedol' else 'tools')   # the border as drawn in Figma (Border Placed=Top, Version=Large)
pdlogo = lambda cls: '<img class="hb-pdimg" src="/images/hero-banner-power-deal-logo-%s.svg" alt="Power Deal logo" width="220" height="112" loading="lazy" />' % ('swedol' if cls == 'hb-swedol' else 'tools')
news = lambda cls, lab: '<img class="hb-newsimg" src="/images/hero-banner-news-%s.png" alt="News badge, %s" width="120" height="120" loading="lazy" />' % (cls, cls)   # the badge as designed (cropped from the Supernova page); text and font come from the artwork


def sw(stage, label_rows, stage_cls=''):
    return '<figure class="hb-sw__card"><div class="hb-sw__stage %s" role="img" aria-label="%s">%s</div><dl class="hb-sw__cap">%s</dl></figure>' % (stage_cls, esc_attr(' / '.join(v for k, v in label_rows)), stage, ''.join('<dt>%s</dt><dd>%s</dd>' % r for r in label_rows))


d_colors = '<h2 class="ds-h2">Colors</h2>' + \
    '<h3 class="ds-h3 ds-group">Branding elements</h3>' + h4('Power Deal border') + desc('The color depends on the site where the campaign is shown. Swedol uses its accent color and Tools uses its own. The site decides, so the editor never picks it. Figma: ' + fig_link('https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=16448-139687', 'Power Deal border', 'large') + '.') + \
    '<div class="hb-sw">' + sw(stripes('hb-swedol'), [('Element', 'Power Deal border'), ('Brand', 'Swedol'), ('Color', 'Swedol accent brand')]) + sw(stripes('hb-tools'), [('Element', 'Power Deal border'), ('Brand', 'Tools'), ('Color', 'Tools accent brand')]) + '</div>' + \
    h4('Power Deal logo') + desc('The logo follows the same rule: the slash takes the accent color of the site. Figma: ' + fig_link('https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1473-44183', 'Power Deal logo', 'large') + '.') + \
    '<div class="hb-sw">' + sw(pdlogo('hb-swedol'), [('Logo', 'Power Deal, Swedol accent brand'), ('Brand', 'Swedol')]) + sw(pdlogo('hb-tools'), [('Logo', 'Power Deal, Tools accent brand'), ('Brand', 'Tools')]) + '</div>' + \
    h4('News badge') + desc('The text “NYHET!” follows the language of the country. The badge is only for promoting news. White and black work on both brands. Green belongs to Swedol and red to Tools. Figma: ' + fig_link('https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=16973-133757', 'News badge', 'large') + '.') + \
    '<div class="hb-sw">' + sw(news('white', 'Nyhet!'), [('Brand', 'Swedol &amp; Tools'), ('Color', 'White')]) + sw(news('black', 'Nyhet!'), [('Brand', 'Swedol &amp; Tools'), ('Color', 'Black')], 'hb-sw__stage--grey') + sw(news('green', 'Nyhet!'), [('Brand', 'Swedol'), ('Color', 'Swedol accent brand')], 'hb-sw__stage--grey') + sw(news('red', 'Nyhet!'), [('Brand', 'Tools'), ('Color', 'Tools accent brand')], 'hb-sw__stage--grey') + '</div>' + \
    '<h3 class="ds-h3 ds-group">Text elements</h3>' + desc('Text uses Primary (black) or Primary inverted (white). Choose the one that is most readable on the image, and test it with the overlay.') + \
    '<div class="hb-sw">' + sw('<div class="hb-txt hb-txt--inv"><b>Pre title</b><strong>Title</strong><span>Preamble</span></div>', [('Color', 'Primary inverted')]) + sw('<div class="hb-txt"><b>Pre title</b><strong>Title</strong><span>Preamble</span></div>', [('Color', 'Primary')], 'hb-sw__stage--grey') + '</div>' + \
    '<h3 class="ds-h3 ds-group">Buttons</h3>' + desc('The button group uses Primary and Secondary on a light image, and Primary inverted and Secondary inverted on a dark one. See ' + L('button.html', 'Button') + '.') + \
    '<div class="hb-sw">' + sw('<div class="hb-btns"><button type="button" class="btn btn--primary btn--lg"><span class="btn__label">Button label</span></button><button type="button" class="btn btn--secondary btn--lg"><span class="btn__label">Button label</span></button></div>', [('Color', 'Primary + Secondary'), ('Button group', '2 in a row')], 'hb-sw__stage--grey') + \
    sw('<div class="hb-btns"><button type="button" class="btn btn--primary-inverted btn--lg"><span class="btn__label">Button label</span></button><button type="button" class="btn btn--secondary-inverted btn--lg"><span class="btn__label">Button label</span></button></div>', [('Color', 'Primary inverted + Secondary inverted'), ('Button group', '2 in a row')]) + '</div>'

JS_DESIGN = r'''
  function box(img, x, y, w, h) { return function () { var r = img.getBoundingClientRect(); return { left: r.left + r.width * x / 672, top: r.top + r.height * y / 350, width: r.width * (w || 0) / 672, height: r.height * (h || 0) / 350 }; }; }
  function col(img) { return function (r) { return r.left - (img.getBoundingClientRect().left - 36); }; }   /* every badge in the figure sits in one column, 24px gap between badge and picture */
  function colR(img) { return function (r) { return img.getBoundingClientRect().right + 36 - (r.left + r.width); }; }
  function figs() {
    var m = $('#an-main-img'), p = $('#an-pd-img'), l = $('#an-logo-img'), n = $('#an-news-img');
    DK.callouts($('#an-main'), [
      { n: '1', box: box(m, 22, 14), side: 'left', len: col(m) },
      { n: '2*', box: box(m, 22, 51), side: 'left', len: col(m) },
      { n: '3a', box: box(m, 22, 90), side: 'left', len: col(m) },
      { n: '3b', box: box(m, 22, 122), side: 'left', len: col(m) },
      { n: '3c', box: box(m, 22, 149), side: 'left', len: col(m) },
      { n: '4a', box: box(m, 22, 175), side: 'left', len: col(m) },
      { n: '4b', box: box(m, 22, 210), side: 'left', len: col(m) },
      { n: '4c', box: box(m, 22, 242), side: 'left', len: col(m) },
      { n: '5', box: box(m, 22, 298), side: 'left', len: col(m) },
      { n: '6', box: box(m, 336, 348), side: 'bottom', len: 44 }
    ]);
    DK.callouts($('#an-pd'), [{ n: '1', box: box(p, 60, 8), side: 'left', len: col(p) }, { n: '2', box: box(p, 36, 60), side: 'left', len: col(p) }]);
    DK.callouts($('#an-logo'), [{ n: '1', box: box(l, 642, 48), side: 'right', len: colR(l) }]);
    DK.callouts($('#an-news'), [{ n: '1', box: box(n, 640, 72), side: 'right', len: colR(n) }]);
  }
  var imgs = $$('.hb-anat img'), left = imgs.length;
  imgs.forEach(function (i) { if (i.complete) left--; else i.addEventListener('load', function () { if (--left === 0) figs(); }); });
  if (left === 0) figs();
'''

# ======================================================================================
# 2. USAGE
# ======================================================================================
u_purpose = '<h2 class="ds-h2">The hero banner’s purpose</h2>' + desc('Hero banners are high-impact, visually dominant components that capture attention at once and carry your most important message. Use them strategically, not by default.') + \
    note('For the settings of the component, see the ' + L(SBP, 'Storyblok tab') + '. For finished banners to learn from, see ' + L(REFP, 'Reference and Examples') + '.')

u_width = '<h2 class="ds-h2">Fluid vs Regular width</h2>' + \
    '<h3 class="ds-h3 ds-group">Fluid width</h3>' + desc('The banner extends edge to edge across the whole viewport, with no side padding. It creates a full-bleed, immersive experience.') + \
    '<h3 class="ds-h3 ds-group">Regular width</h3>' + desc('The banner follows the standard page padding and keeps its spacing to the other elements on the page. It looks more contained and structured.') + \
    desc('Choosing between the two is a judgement call, and it depends on several things. The directives below help. As a rule of thumb, use the component consistently across similar page types.')

u_reg = '<h2 class="ds-h2">When to use the regular width</h2>' + \
    '<h3 class="ds-h3 ds-group">Content focused</h3>' + li(['For campaigns, for example on the home page.', 'On campaign landing pages where you do not need to bang the big drum.', 'In page content, when the banner needs to feel like part of the content flow.']) + \
    pics([('page-regular-power-tools', 'Regular width banner for a power tool campaign', 'A campaign on the home page.'), ('page-fluid-rusta', 'Regular width banner with a hi-vis photo', 'A banner in the page flow.'), ('page-ampro-bag', 'Regular width product banner above an article', 'A product banner next to content.'), ('page-regular-brands', 'Regular width banner under a brand strip', 'A banner that belongs to the content.'), ('page-regular-milwaukee', 'Regular width banner for a Milwaukee campaign', 'A campaign banner on the home page.'), ('page-regular-garden', 'Regular width seasonal banner', 'A seasonal banner.')]) + \
    li(['Limited or mediocre imagery that will not hold up at large sizes: use the regular width.', 'When users are task oriented rather than in exploration mode.', 'Do not go full width just because you can.'])

u_fluid = '<h2 class="ds-h2">When to use the fluid width</h2>' + \
    '<h3 class="ds-h3 ds-group">High impact moments</h3>' + li(['Home page hero sections where the first impression matters, such as product launches, major announcements or major campaigns.', 'You want to create a sense of scale or grandeur.', 'You are establishing a brand atmosphere before the content.', 'You break away from the structure of the rest of the page for emphasis.']) + \
    pics([('page-fluid-gesto', 'Fluid banner for a news product', 'A product launch.'), ('page-fluid-gesto-2', 'Fluid banner with the brand logo', 'A launch with the brand logo.'), ('page-fluid-power-deal', 'Fluid Power Deal banner', 'A major campaign.')]) + \
    '<h3 class="ds-h3 ds-group">Campaign landing pages that need maximum attention</h3>' + li(['Landing page headers for campaign sites, or promoting a service, or brand landing pages (for example AmPro, Bosch, Makita).', 'Landing pages that promote products.', 'Premium product positioning.', 'Brand awareness campaigns.', 'Campaign microsites.', 'Giving context for what users find further down the page, in a promoting role.']) + \
    pics([('page-brand-ampro', 'Fluid hero on a Tools brand landing page', 'A brand landing page.'), ('page-certification', 'Fluid hero on a service page', 'A service landing page.'), ('page-swedol-live', 'Fluid hero on the Swedol Live page', 'A campaign microsite.'), ('page-hivis-landing', 'Fluid hero on the landing page of a product', 'A product landing page.')])

u_consider = '<h2 class="ds-h2">When to consider</h2>' + \
    '<h3 class="ds-h3 ds-group">Content-heavy landing pages</h3>' + li(['Educational content pages', 'How-to guides or resource centres', 'Article-style landing pages', 'Multi-section content experiences', 'Blog and article', 'Category gateway page or PLP', 'Sub-category page']) + \
    why([('Consider', 'Will the hero compete with the content below, or support it? Does the page benefit from immediate visual impact, or should the content come first?'), ('Best practice', 'Make sure the hero introduces the content and does not dominate it. Use an image that represents the content or the topic.')]) + \
    '<h3 class="ds-h3 ds-group">Service or information pages</h3>' + li(['Delivery information pages', 'Customer service sections', 'About us pages', 'Store locator pages']) + \
    why([('Consider', 'Do these functional pages benefit from a hero, or does a simpler header do?'), ('Best practice', 'Use a simpler hero without heavy campaign elements. Focus on clarity over impact.')])

u_not = '<h2 class="ds-h2">When not to use</h2>' + \
    '<h3 class="ds-h3 ds-group">Content needs to be front and center</h3>' + li(['Product listing pages, where the products are the priority', 'Product detail pages, where the product information is the priority', 'Search results pages', 'Comparison or filter-heavy pages', 'Pages where users want direct access to tools or content']) + \
    why([('Why', 'A hero can push the content below the fold. If the content is why users are there, do not make them scroll past a hero first.'), ('Alternative', 'A minimal page header or breadcrumb navigation.'), ('Example', 'Product search results: users want to see products, not a banner.')]) + \
    '<h3 class="ds-h3 ds-group">You are just filling space</h3>' + li(['“We need something at the top” without a strategic purpose', 'Generic stock imagery with no message', 'Placeholder content “just because”', 'Copying hero settings without thinking']) + \
    why([('Why', 'A bad hero is worse than no hero. It adds visual weight without value and slows the user down.'), ('Alternative', 'A simple, clean page header that does not pretend to be a campaign.'), ('Example', 'Do not add a generic “Welcome to Tools” hero with stock imagery. It adds no value.')]) + \
    '<h3 class="ds-h3 ds-group">The page is transactional</h3>' + li(['Checkout pages', 'Account management pages', 'Shopping cart', 'Login and registration pages, unless it is a combined USP section that converts future users. The registration form must stay prominent and clearly visible, because the forms are the primary item.', 'Form-heavy pages']) + \
    why([('Why', 'These pages are task focused. A hero distracts from completing the transaction.'), ('Alternative', 'Minimal headers that build trust and guide the process.'), ('Example', 'No hero on checkout: users are there to buy, not to be marketed to.')]) + \
    '<h3 class="ds-h3 ds-group">The mobile experience would suffer</h3>' + li(['The hero takes up the whole mobile viewport', 'Critical content is pushed too far down on mobile', 'The hero height causes too much scrolling', 'The message is too complex for a small screen']) + \
    why([('Why', 'Mobile users should reach the content quickly. An oversized hero hurts the mobile experience.'), ('Alternative', 'Use breakpoint visibility to show a simplified hero on mobile, or skip the hero on the mobile breakpoints.')])

u_chart = '<h2 class="ds-h2">Quick reference: hero yes or no</h2>' + \
    table(['Page type', 'Use a hero?', 'Priority'], [[t, yn(v), p] for t, v, p in [('Home page', 'yes', 'High'), ('Major campaign landing page', 'yes', 'High'), ('Brand landing page', 'yes', 'High'), ('Campaign microsite', 'yes', 'High'), ('Category gateway page or PLP', 'maybe', 'Medium'), ('Sub-category page', 'maybe', 'Medium'), ('Blog or article', 'maybe', 'Low'), ('Service or information page', 'maybe', 'Low'), ('Product detail page', 'no', '–'), ('Search results', 'no', '–'), ('Checkout and cart', 'no', '–'), ('Account pages', 'no', '–')]])

def dd_img(n, alt):
    return '<img class="hb-dd" src="/images/hero-banner-dd-%s.webp" alt="%s" loading="lazy" />' % (n, alt)


u_dd = '<h2 class="ds-h2">Do’s and Don’ts</h2>' + \
    fig_pair(dd_img('regular-do', 'A regular width banner with the section top padding above it'), 'Do use the top section padding for a regular width banner that is the first item of the content.', dd_img('regular-dont', 'A regular width banner without padding above it'), 'Do not leave out the padding, unless the banner sits directly under the breadcrumbs.') + \
    fig_pair(dd_img('fluid-do', 'A fluid banner at the top of the page, without padding'), 'Always use a fluid banner without padding when it is placed at the top of the page.', dd_img('fluid-dont', 'A fluid banner with section top padding above it'), 'Never use section top padding with a fluid hero banner, or with a hero as the page content.')

DD = [
    ('Responsive design', ['Adjust the content per breakpoint when needed (use breakpoint visibility).', 'Reduce the text size on smaller breakpoints for a better fit.', 'Test the hero on real devices, not only a resized browser.', 'Consider smaller buttons on mobile.'], ['Assume the desktop design works on mobile.', 'Use the same long text on every breakpoint. The text must still make sense on a small screen.', 'Ignore how the elements stack on small screens.', 'Forget to check landscape orientation on mobile.']),
    ('Image usage', ['Think about the focal point of the image when it is a background for the text.', 'Test the image on all breakpoints before publishing.', 'Use wider images for a Fluid banner when keeping the proportions matters.', 'Pick images that support the campaign message and the brand identity.'], ['Put critical visual elements at the extreme edges of the image.', 'Use low-resolution, pixelated or unoptimised images.', 'Upload images with embedded text that repeats the hero text.', 'Use images with busy backgrounds that compete with the text.', 'Forget how horizontal cropping affects the composition.']),
    ('Text and content', ['Keep headlines short, punchy and easy to scan (5–8 words at most).', 'Use the pre title for context or category.', 'Write short, action-oriented button text.', 'Test the readability of the text on the real image.', 'Adjust the title size for each breakpoint.', 'Use correct grammar and spelling.'], ['Write long paragraphs in the preamble (keep it to 1–2 sentences).', 'Use generic button text such as “Click here” or “Learn more” without context.', 'Crowd the hero with too much text.', 'Use conflicting messages in the title and the buttons.', 'Forget to proofread before publishing.']),
    ('Color and contrast', ['Always use the overlay when the readability of the text is at risk.', 'Test both Primary and Primary inverted text with your image if you are unsure which works best.', 'Adjust the overlay opacity to balance image visibility and text legibility.', 'Choose a news badge color that suits the whole design.'], ['Use a text color that blends into the background.', 'Set the overlay opacity to 0 if the text becomes unreadable.', 'Rely on the image alone for contrast. Always test with the overlay.', 'Use the green news badge outside Swedol campaigns.', 'Use the red news badge outside Tools sites.']),
    ('Layout and alignment', ['Use left alignment for text-heavy content.', 'Think about the visual weight of all the elements when you position them.'], ['Put text over busy areas of the background image. The overlay can help.', 'Crowd the hero with too many elements in one area.', 'Ignore the natural reading flow (top to bottom, left to right).']),
    ('Campaign elements', ['Use the discount badge for clear, short messages (for example “30% OFF”).', 'Show the campaign price and the old price info together, for transparency.', 'Check that every price is correct before publishing.', 'Use campaign elements consistently across related banners.', 'Remove campaign elements promptly when the promotion ends.'], ['Use the discount badge for non-promotional content.', 'Show a campaign price without the discount badge.', 'Forget to remove expired campaign prices.', 'Use vague discount information. Always be specific.', 'Overuse campaign elements on non-promotional heroes.']),
    ('Buttons and links', ['Use Button One for the primary call to action.', 'Consider the chevron to emphasise the primary action.', 'Test every link before publishing.', 'Use relative URLs for internal links (for example <code>category/tools</code>).', 'Use <code>https://</code> for all external links.', 'Choose a button size that matches the importance of the message.'], ['Use Button overlay when you have two different actions.', 'Link to broken or outdated pages.', 'Use the same link for both buttons. It confuses users.', 'Forget to give the link a destination.', 'Use oversized buttons on mobile breakpoints by default.']),
    ('Branding elements', ['Use the Power Deal logo only for real Power Deal campaigns.', 'Turn on the Power Deal border when you use the Power Deal logo.', 'Use the news badge sparingly, for genuinely new content.'], ['Overuse the news badge. It loses its impact.', 'Use Power Deal elements for campaigns that are not Power Deal.', 'Combine too many branding elements in one hero.']),
    ('Width settings', ['Use Fluid width for edge-to-edge, high-impact campaign heroes.', 'Think about the content around the banner.'], ['Use Regular width images with the Fluid setting if you do not want the image to scale.', 'Mix width settings at random across similar page types.']),
    ('Accessibility', ['Write descriptive button text that makes sense out of context.', 'Always add an image description.'], ['Use images with embedded critical text as the only source of information.']),
    ('General best practices', ['Review all settings before publishing.', 'Use the component consistently across similar page types.', 'Keep a record of hero setups that worked, for reference.', 'Update the content regularly to keep it fresh.', 'Coordinate the hero design with the overall page strategy.'], ['Publish without testing on several devices.', 'Make last-minute changes without a review.', 'Ignore the analytics of the hero (this needs testing procedures).', 'Forget to archive or update seasonal campaign heroes.']),
]
u_dd += ''.join('<h3 class="ds-h3 ds-group">%s</h3>' % t + rules(do, dont) for t, do, dont in DD)

u_chev = '<h2 class="ds-h2">Use of the chevron on the hero button</h2>' + \
    note('This section may move to the Button documentation when the button component is done.') + \
    '<h3 class="ds-h3 ds-group">What the chevron does</h3>' + desc('The chevron (→) is a right-pointing arrow on the button. It adds visual weight and direction to the call to action, and signals forward movement. Because the hero is already prominent, the chevron is mostly cosmetic.') + \
    '<h3 class="ds-h3 ds-group">When to use the chevron</h3>' + \
    h4('Primary action emphasis') + li(['The button is the main conversion goal of the page.', 'You want maximum attention on the call to action.', 'The action is the main reason the hero exists.', 'It is the most important click on the whole page.']) + why([('Why', 'The chevron adds weight and urgency, so the primary action is unmistakable.'), ('Example', '“Shop now →” on a Black Friday hero.')]) + \
    h4('Navigational actions') + li(['The button takes users to another page or section.', 'The action moves forward in a journey (for example “Explore collection”, “View products”).', 'The button leads to a category, a product listing or a dedicated landing page.', 'The action implies progress or discovery.']) + why([('Why', 'The chevron reinforces the idea of moving forward or going somewhere.'), ('Example', '“Discover new arrivals →” leading to a product category.')]) + \
    h4('High-priority campaigns') + li(['Major seasonal sales (Swedol day, Black Friday, summer sale, holiday promotions)', 'Limited-time offers where urgency matters', 'Flash sales or time-sensitive campaigns', 'Exclusive product launches']) + why([('Why', 'The chevron adds urgency and draws the eye, which suits high-stakes campaigns.'), ('Example', '“Claim your discount →” on a 48-hour flash sale.')]) + \
    h4('Clear, confident calls to action') + li(['The button text is direct and action oriented.', 'The message is confident and assertive.', 'The action has clear, immediate value for the user.', 'There is no doubt about what happens next.']) + why([('Why', 'A strong call to action deserves a strong visual treatment. The chevron reinforces confidence.'), ('Example', '“Start shopping →”, “Get started →”, “See all deals →”.')]) + \
    h4('Single-button scenarios') + li(['There is only one button on the hero (the primary button).', 'All attention should go to one primary action.', 'The button overlay is on (the whole hero is clickable).', 'The message is singular and focused.']) + why([('Why', 'With no competing actions, the chevron adds emphasis without confusion.'), ('Example', 'A product launch hero with one clear action: “Pre-order now →”.')]) + \
    '<h3 class="ds-h3 ds-group">When not to use the chevron</h3>' + \
    h4('Already visually busy designs') + li(['The hero has many elements (discount badge, price, logo, news badge).', 'The design is complex, with overlays and several text elements.', 'More visual elements would create clutter.', 'Users may experience visual overload.']) + why([('Why', 'Sometimes simplicity performs better. The chevron can be “one thing too many”.'), ('Better approach', 'Simplify the other elements first, or skip the chevron for a cleaner look.')]) + \
    h4('Informational or soft actions') + li(['The button text is exploratory (for example “Learn more”).', 'The action is educational rather than transactional.', 'Users are browsing, not buying.', 'The call to action is passive or investigative.']) + why([('Why', 'The chevron implies urgency and forward momentum, which is wrong for casual exploration.'), ('Better without', '“Learn more” without a chevron feels less pushy for educational content.')]) + \
    h4('Subtle or minimal designs') + li(['The overall design is clean and minimalist.', 'The brand look is understated and refined.', 'The hero uses subtle typography and muted colors.', 'Less is more in the design approach.']) + why([('Why', 'The chevron adds visual complexity that may conflict with a minimal design.'), ('Consider', 'Test both versions. Sometimes a minimal design benefits from one strong visual accent.')]) + \
    h4('Secondary buttons') + li(['You use Button Two (the secondary action).', 'The button is an alternative or fallback.', 'The action has lower priority than the primary button.', 'You offer a “softer” alternative to the main call to action.']) + why([('Why', 'Only the primary action should carry maximum visual weight. Two chevrons compete.'), ('Best practice', 'Button One with a chevron, Button Two without. Example: “Shop sale →” (with chevron) and “View catalog” (no chevron).')]) + \
    h4('Passive or ambiguous calls to action') + li(['The button text is vague (“Click here”, “More info”).', 'The outcome of the click is unclear.', 'The action has no obvious value.', 'Users may be confused about what happens next.']) + why([('Why', 'A chevron on weak copy does not fix the problem. It highlights it.'), ('Better solution', 'Improve the button text first, then decide on the chevron.')]) + \
    '<h3 class="ds-h3 ds-group">Quick reference: chevron yes or no</h3>' + \
    table(['Button context', 'Use the chevron?', 'Reason'], [[t, yn(v), r] for t, v, r in [('“Shop now”', 'yes', 'Transactional, primary action'), ('“Learn more”', 'no', 'Informational, exploratory'), ('“View products”', 'yes', 'Navigational, forward movement'), ('“Discover collection”', 'yes', 'Navigational, implies a journey'), ('“Read article”', 'no', 'Content consumption, passive'), ('“Get started”', 'yes', 'Action oriented, begins a journey'), ('“Contact us”', 'no', 'Service action, not transactional'), ('“See all deals”', 'yes', 'Navigational to listings'), ('Button Two (secondary)', 'no', 'Never use on secondary actions')]])

# ======================================================================================
# 3. REFERENCE AND EXAMPLES
# ======================================================================================
def ex(sid, title, ims, what, typ, purpose, elements, cat, intro=None):
    out = '<h2 class="ds-h2">%s</h2>' % title
    if intro:
        out += desc(intro)
    for n, a, c in ims:
        out += pic(n, a, c, narrow=('mobile' in n))   # a mobile hero is shown at phone width, not full width
    out += desc('This banner is an example of a <strong>%s</strong>.' % what)
    out += h4('Type of banner') + li(typ) + h4('Purpose') + li(purpose) + h4('Elements that make this clear') + li(elements) + h4('Category in e-commerce') + li(cat)
    return (sid, out)


R = []
R.append(('intro', '<h2 class="ds-h2">Use cases and banner reference examples</h2>' + desc('The examples below are for inspiration and as a reference for how to use the hero banner. Each one shows what kind of banner it is, what it is for, which elements carry the message and which e-commerce category it belongs to.') + note('As a rule of thumb, use the component consistently across similar page types, for example custom headers on ' + L(SLUG + '.html', 'brand landing pages') + '.', 'error')))
R.append(ex('campaign-product', 'Campaign banner with a product focus', [('banner-power-deal', 'A Power Deal banner for a Hikoki impact wrench with a discount', 'A campaign banner with a product focus.')], 'campaign banner with a product focus',
            ['<strong>Campaign banner / hero banner:</strong> highlights one product, the WR36DE impact wrench from Hikoki.', '<strong>Discount banner:</strong> shows a clear price reduction (25% off), which makes it campaign oriented.', '<strong>Power Deal banner:</strong> the text POWER DEAL signals a special promotion.'],
            ['<strong>Drive sales through the discount:</strong> a clear price drop, from 3,500 SEK to 2,625 SEK.', '<strong>Highlight product benefits:</strong> a short description of the features (brushless motor, longer runtime, longer life, less maintenance).', '<strong>Conversion oriented:</strong> two clear buttons, “Shop now” for a direct purchase and “View campaign” for more offers in the same campaign.'],
            ['<strong>Price and discount:</strong> large red text with the discount and the new price.', '<strong>Product image in use:</strong> the tool in a real work environment adds credibility.', '<strong>Campaign branding:</strong> the POWER DEAL logo and the Hikoki logo give the campaign a strong identity.', '<strong>Color coding:</strong> green and yellow create energy and draw attention.'],
            ['Campaign banner (discounts and special offers)', 'Conversion-focused banner (clear calls to action)', 'Product-focused banner (a specific product with price and features)']))
R.append(ex('product-discount', 'Product banner with a discount offer', [('banner-ampro-discount', 'A product banner for an AmPro tool bag with a discount', 'A product banner with a discount offer and brand identity.')], 'product banner with a discount offer',
            ['<strong>Product banner / hero banner:</strong> highlights one product, the AmPro tool bag.', '<strong>Discount banner:</strong> “20% off” and the new price (499 SEK) show that the purpose is to sell with an offer.', '<strong>Brand banner:</strong> connected to AmPro, which reinforces the brand identity.'],
            ['<strong>Drive direct sales of one product:</strong> the button “Shop now” leads to the product page.', '<strong>Create a reason to buy:</strong> 20% off and clear pricing are strong motivators.', '<strong>Highlight product features:</strong> a short description of the material, the handle and the detachable shoulder strap.'],
            ['<strong>Background and layout:</strong> a black background with the product in focus gives a premium feel.', '<strong>Headline and subtext:</strong> the headline names the product, the subtext describes its function and material.', '<strong>Discount highlight:</strong> a red label with “20% off” and the price in large text.', '<strong>CTA button:</strong> “Shop now”, conversion focused.', '<strong>Brand logo:</strong> the AmPro logo top right for clear identity.'],
            ['Product banner (one product)', 'Discount or campaign banner (to drive sales with an offer)', 'Brand banner (linked to AmPro)']))
R.append(ex('new-product', 'Product and new product campaign banner', [('banner-ampro-new', 'A new product banner for an AmPro tool bag with a news badge', 'A product campaign banner that promotes a new product.'), ('banner-gesto-new', 'A new product banner for Gesto work shoes with a news badge and the brand logo', 'The same type of banner, with the brand logo.')], 'product campaign banner',
            ['<strong>Hero banner / product banner:</strong> draws attention to one product, here an AmPro tool bag.', '<strong>New product banner:</strong> a clear label with the text “NEW!” shows that the product is new in the range.'],
            ['<strong>Promote a new product:</strong> inform visitors about a new product and create interest.', '<strong>Conversion oriented:</strong> two clear buttons, “Shop now” for a direct purchase and “More about the product” for further information.'],
            ['<strong>Product image:</strong> a clear image of the bag shows what is sold.', '<strong>Product name and description:</strong> clear and short, the name and a short description of material and features.'],
            ['Promotional banner (campaigns, new arrivals or launches)', 'Conversion-focused banner (clear calls to action)', 'Product-focused banner (a specific product, not a general brand banner)']))
R.append(ex('seasonal', 'Seasonal campaign banner with a category focus', [('banner-seasonal-garden', 'A seasonal banner with a garden hose on grass', 'A seasonal campaign banner with a category focus.')], 'seasonal campaign banner with a category focus',
            ['<strong>Seasonal banner / hero banner:</strong> promotes products for a specific season, here spring.', '<strong>Category overview:</strong> shows a whole category (lawnmowers, leaf blowers, spades, saws and more) instead of one product.', '<strong>Inspirational banner:</strong> encourages customers to prepare for gardening and watering.'],
            ['<strong>Drive traffic to category pages:</strong> the banner leads customers to explore a range, not to buy one product.', '<strong>Create seasonal relevance:</strong> “Equip yourself for spring” connects to what customers need at this time of year.', '<strong>Broad conversion focus:</strong> the button “Equip yourself now” leads to a collection page.'],
            ['<strong>Background image:</strong> a garden hose on grass signals gardening and watering.', '<strong>Headline and subtext:</strong> a clear seasonal call to action, and a line that there are many new tools and machines for pros and private persons.', '<strong>Listed product categories:</strong> lawn mowers, leaf blowers, pest control, spades, rakes, saws.', '<strong>CTA button:</strong> leads to a broader category, not a single product.'],
            ['Seasonal banner (drive sales in a specific period)', 'Category or assortment banner (several products within a theme)', 'Inspirational banner (creates need rather than selling one item)']))
R.append(ex('clearance', 'Clearance sale banner with a campaign focus', [('banner-clearance', 'A clearance sale banner with up to 80% off', 'A clearance sale banner with a campaign focus.')], 'clearance sale banner with a campaign focus',
            ['<strong>Clearance banner / hero banner:</strong> communicates a major stock clearance.', '<strong>Discount banner:</strong> “Up to 80% off” attracts attention with big price reductions.', '<strong>Category banner:</strong> names several categories (tools, clothing, shoes, safety gear, electrical).'],
            ['<strong>Drive traffic to the clearance page:</strong> the button “Go to clearance sale” leads to a collection page with discounted products.', '<strong>Create urgency:</strong> the campaign period (3–20 Nov) and “while supplies last”.', '<strong>Reduce excess stock:</strong> the banner explains that the products are overstocked or being discontinued.'],
            ['<strong>Background image:</strong> tools in rows give a sense of a wide range.', '<strong>Headline and subtext:</strong> a strong clearance signal, and why the discounts exist and how long the campaign lasts.', '<strong>Discount highlight:</strong> “Up to 80% off” in red.', '<strong>CTA button:</strong> “Go to clearance sale”, conversion focused.'],
            ['Clearance banner (stock reduction and big discounts)', 'Campaign banner (with a clear time limit)', 'Category or assortment banner (several product groups)']))
R.append(ex('power-tools', 'Campaign banner with a category focus on power tools', [('banner-power-tools', 'A campaign banner for power tools from Hikoki', 'A campaign banner with a category focus on power tools for a specific brand.')], 'campaign banner with a category focus on power tools',
            ['<strong>Campaign banner / hero banner:</strong> promotes a campaign on power tools.', '<strong>Discount banner:</strong> “20–40% off” attracts attention with price reductions.', '<strong>Category overview:</strong> names several product types (screwdrivers, drills, impact wrenches, nail guns, polishers).'],
            ['<strong>Drive traffic to the campaign page:</strong> the button “View campaign” leads to a collection page with discounted power tools.', '<strong>Create urgency:</strong> the campaign period and “while supplies last”.', '<strong>Highlight the Hikoki brand:</strong> the campaign is clearly tied to one brand.'],
            ['<strong>Background image:</strong> a person using a Hikoki tool at work adds credibility and context.', '<strong>Headline and subtext:</strong> “Power tool campaign” as a clear signal, and the discount and the period as the subtext.', '<strong>Discount highlight:</strong> “20–40% off” in red.', '<strong>CTA button:</strong> “View campaign”, conversion focused.'],
            ['Campaign banner (discounts and time-limited offers)', 'Category or assortment banner (power tools)', 'Brand banner (linked to Hikoki)']))
R.append(ex('strong-discount', 'Strong discount focus for a product category', [('banner-milwaukee', 'A campaign banner with 40% off all chainsaws from Milwaukee', 'A campaign banner with a strong discount focus for a product category and brand.')], 'campaign banner with a strong discount focus for a specific product category',
            ['<strong>Campaign banner / hero banner:</strong> promotes a time-limited campaign.', '<strong>Discount banner:</strong> “40% off all chainsaws from Milwaukee” signals a major price reduction.', '<strong>Brand banner:</strong> tied to one brand, Milwaukee.', '<strong>Category or product banner:</strong> focuses on one product category (chainsaws, including chain saws and pruning saws).'],
            ['<strong>Drive traffic to the campaign page:</strong> the button “View campaign” leads to a collection page with discounted chainsaws.', '<strong>Create urgency:</strong> the campaign period and “while supplies last”.', '<strong>Highlight an attractive offer:</strong> 40% off is a strong reason to buy.'],
            ['<strong>Background image:</strong> a close-up of a chainsaw in use conveys power and function.', '<strong>Headline and subtext:</strong> the offer as the headline, the period and the conditions as the subtext.', '<strong>Discount label:</strong> “Campaign” in a red tag draws attention.', '<strong>CTA button:</strong> “View campaign”, conversion focused.'],
            ['Campaign banner (discounts and time-limited offers)', 'Brand banner (linked to Milwaukee)', 'Category or product banner (chainsaws)']))
R.append(ex('brand-awareness', 'Brand awareness and new product hero', [('banner-hivis-new', 'A fluid hero that introduces the HiVis range from Björnkläder', 'A product campaign with brand awareness, in the context of a fluid hero.'), ('banner-hivis-landing', 'A fluid hero on the landing page of the HiVis range', 'A brand awareness hero on the landing page of a product.')], 'product campaign with brand awareness',
            ['<strong>New product banner / hero banner:</strong> introduces a new product line, HiVis from Björnkläder.', '<strong>Brand banner:</strong> strongly tied to one brand (Björnkläder), and highlights a product series.', '<strong>Category or collection banner:</strong> focuses on a whole collection of high-visibility workwear, not one product.'],
            ['<strong>Inform about the launch and drive traffic to the collection:</strong> the button “Explore the collection” leads to a page with the full range.', '<strong>Position the product as premium and safety oriented:</strong> the text stresses maximum visibility and safety at the workplace.', '<strong>Build brand identity:</strong> through the tagline “Engineered to stand out”.'],
            ['<strong>Background image:</strong> a worker in high-visibility clothing at height signals safety and function.', '<strong>Headline and subtext:</strong> clear brand positioning, and a line that the collection is made for visibility and safety.', '<strong>New product marker:</strong> a yellow circle with “New!” draws attention.', '<strong>CTA button:</strong> “Explore the collection”, conversion focused.'],
            ['New product banner (launch of new products or collections)', 'Brand banner (linked to Björnkläder)', 'Category or collection banner (a whole series of products)']))
R.append(ex('brand-landing', 'Brand landing page hero', [('banner-ampro-fluid', 'A fluid hero for the AmPro brand landing page', 'A fluid hero that creates brand awareness on a brand landing page.'), ('banner-ampro-mobile', 'The same hero on mobile', 'The same hero on mobile.')], 'brand landing page hero',
            ['<strong>Brand banner / hero banner:</strong> clearly linked to the AmPro brand, and shows its products.', '<strong>Category or assortment banner:</strong> focuses on tools and storage solutions, not one product.', '<strong>Inspirational banner:</strong> communicates value and quality instead of a campaign or discount.'],
            ['<strong>Build brand identity and drive traffic to the AmPro range:</strong> the button “Shop AmPro” leads to a collection page with all the products of the brand.', '<strong>Position the products as premium and functional:</strong> the text “Tools and storage that make a difference” signals quality and utility.', '<strong>Create trust and interest:</strong> a tagline that stresses flexibility and solutions.'],
            ['<strong>Background image:</strong> a close-up of a tool drawer with neatly arranged wrenches conveys order, quality and precision.', '<strong>Headline and subtext:</strong> strong brand positioning, and a line that reinforces the value of the brand.', '<strong>CTA button:</strong> “Shop AmPro”, conversion focused.', '<strong>Brand logo:</strong> the AmPro logo bottom right for clear identity.'],
            ['Brand banner (strengthens the brand profile)', 'Category or assortment banner (a whole product category)', 'Inspirational banner (creates interest rather than selling one product)']))

# ======================================================================================
# 4. STORYBLOK
# ======================================================================================
S = []
S.append(('widget', '<h2 class="ds-h2">Hero widget</h2>' + desc('The hero banner is available as a widget in the admin tool Storyblok, for the content managers and content creators of our e-commerce sites. In Storyblok the widget is called <strong>Hero Responsive</strong> (technical name <code>hero responsive</code>).') + note('Before you use the tool, read the best practices in ' + L(WEB, 'Usage') + '.')))
S.append(('start', '<h2 class="ds-h2">Start</h2>' + desc('Start by adding the <strong>Hero Responsive</strong> widget to the page. In the section, choose <strong>Add block</strong> and pick Hero Responsive in the Insert block list.') + \
          sbshot('insert-block', 'The Insert block list in Storyblok with the Hero Responsive block marked', box=(75.8, 37.1, 21.2, 6.0), cap='The Hero Responsive block in the Insert block list.')))
S.append(('layout', '<h2 class="ds-h2">Layout and dimensions</h2>' + sbshot('layout', 'The Hero Responsive block in Storyblok with the Width and Image fields', cap='Width and image.') + \
          '<h3 class="ds-h3 ds-group" id="width">1. Width settings</h3>' + desc('Two settings control the width and the padding of the component:') + li(['<strong>Fluid width:</strong> extends to fill the whole viewport.', '<strong>Regular width:</strong> applies responsive padding (top, bottom, left, right) that adapts to the breakpoint.']) + \
          '<h3 class="ds-h3 ds-group" id="image-guidelines">2. Image guidelines</h3>' + h4('Recommended image dimensions') + \
          pic('width-regular-xl', 'A regular width banner with a 1200x450 image in breakpoint XLarge', 'A Regular banner with an image of 1200×450px ratio in breakpoint XLarge.', narrow=False) + \
          li(['<strong>Regular:</strong> 1200×450px. It prevents vertical cropping on the XLarge and Large breakpoints. An image of 1200×450px fits the height of every size without cropping the top and bottom. The left and right sides are cropped as the responsive behaviour starts.']) + \
          note('Horizontal cropping can happen on Regular banners. For Fluid banners, use extra wide images to avoid unwanted scaling. Remember to add an image description.') + \
          pic('width-fluid-xl', 'A fluid banner with a 1200x450 image in breakpoint XLarge', 'A Fluid banner with the same 1200×450px image in breakpoint XLarge. The top and bottom of the image are cropped.') + \
          li(['<strong>Fluid:</strong> the wider the image, the better. If keeping the proportions matters, an image of 4000×450px keeps the proportions until the viewport is 4001px wide, and it keeps them in every viewport narrower than 4000px. The drawback is the file size, which grows with the image.']) + \
          pic('width-both-xl', 'A regular and a fluid banner that use the same 3700x450 image in breakpoint XLarge', 'A Regular and a Fluid banner with the same jpg image of 3700×450px (149 kB) in breakpoint XLarge. The proportions are kept in every breakpoint narrower than 3700px.') + \
          pic('width-both-xs', 'A regular and a fluid banner in breakpoint XSmall that use the same image', 'A Regular and a Fluid banner in breakpoint XSmall, with the same image. The proportions are kept, with horizontal cropping on the left and right.', narrow=True) + \
          desc('The image size does not decrease on small screens. When that matters, for example on a page with many images, make an image for the breakpoint. A jpeg with many colors is larger than one with few.') + \
          note('The height of the hero is dynamic. If the content does not fit in the set height of the breakpoint, the hero adjusts to the content. See the heights in ' + L(DESP + '#size', 'Design') + '.')))
S.append(('breakpoint-visibility', '<h2 class="ds-h2">3. Breakpoint visibility</h2>' + sbshot('visibility-all', 'Hero Responsive with the image visible in all breakpoints', cap='Inside Hero Responsive: the image is visible in all breakpoints.') + \
          desc('This setting controls what is shown at each of the five breakpoints: <strong>XLarge, Large, Medium, Small and XSmall.</strong> It makes it possible to adjust the message, the image or the settings for each viewport or device.') + \
          sbshot('section-root', 'The section in Storyblok with two Hero Responsive items', cap='The section root.', red=[('1', 89, 55.8), ('2', 89, 62.0)]) + \
          desc('Add several <strong>Hero Responsive</strong> items in the section, to adapt the content for each breakpoint. Then add or remove the visibility items on each hero.') + \
          sbshot('visibility-3', 'The first Hero Responsive item visible in three breakpoints', cap='Hero banner visible in 3 breakpoints.', red=[('1', 92, 55)]) + desc('Here the Small and XSmall visibility items are removed.') + \
          sbshot('visibility-2', 'The second Hero Responsive item visible in XSmall and Small', cap='Banner content shown for the XSmall and Small breakpoints.', red=[('2', 85, 60.5)]) + desc('In this setup the content of the banner is optimised to be shown in the Small and XSmall breakpoints.')))
S.append(('content-positioning', '<h2 class="ds-h2">4. Content positioning</h2>' + desc('The placement of the text and the main content is set with two parameters.') + \
          '<h3 class="ds-h3 ds-group" id="vertical-alignment">4a. Vertical alignment</h3>' + sbshot('vertical', 'The Vertical Alignment field in Storyblok with the options Top, Middle and Bottom', cap='Content with the alignment “Bottom”.') + li(['Top', 'Middle', 'Bottom']) + \
          '<h3 class="ds-h3 ds-group" id="horizontal-alignment">4b. Horizontal alignment</h3>' + sbshot('horizontal', 'The Horizontal Alignment field in Storyblok with the options Left and Center', cap='Content with the alignment “Left”.', pins=[]) + \
          li(['<strong>Left:</strong> works with any vertical alignment.', '<strong>Center:</strong> only with the vertical alignment Middle (a mandatory pairing).'])))
S.append(('text-elements', '<h2 class="ds-h2">5. Text elements</h2>' + \
          '<h3 class="ds-h3 ds-group" id="text-color">5a. Text color</h3>' + desc('Choose <strong>Primary</strong> or <strong>Primary inverted</strong>, depending on which color is most readable in the context.') + sbshot('text-color', 'The Text Color field in Storyblok with Primary and Primary inverted', cap='Content with “Primary inverted”.') + \
          '<h3 class="ds-h3 ds-group" id="title-size">5b. Title size combinations</h3>' + desc('<strong>Title size:</strong> choose <strong>Large</strong>, <strong>Medium</strong> or <strong>Small</strong>. The size group affects the pre title, the title and the preamble together.') + sbshot('title-size', 'The Title Size field in Storyblok with Large, Medium and Small', cap='Content with “Large”.') + \
          '<h3 class="ds-h3 ds-group" id="pre-title">5c. Pre title</h3>' + desc('Categorise the content or add context.') + sbshot('pre-title', 'The Pre Title field in Storyblok') + \
          '<h3 class="ds-h3 ds-group" id="title">5d. Title</h3>' + desc('The main headline or the campaign message.') + sbshot('title', 'The Title field in Storyblok') + \
          '<h3 class="ds-h3 ds-group" id="preamble">5e. Preamble</h3>' + desc('A longer description of the campaign or the product.') + sbshot('preamble', 'The Preamble field in Storyblok')))
S.append(('campaign-elements', '<h2 class="ds-h2">6. Campaign elements</h2>' + \
          '<h3 class="ds-h3 ds-group" id="discount-badge">6a. Discount badge</h3>' + desc('A red badge with the discount amount or a short campaign message.') + sbshot('discount', 'The Discount Badge field in Storyblok with the text 25% Rabatt') + \
          '<h3 class="ds-h3 ds-group" id="campaign-price">6b. Campaign price</h3>' + desc('Shown directly next to the discount badge. Suited to highlight a promotional price.') + sbshot('price', 'The Campaign Price field in Storyblok') + \
          '<h3 class="ds-h3 ds-group" id="old-price-info">6c. Old price info</h3>' + desc('This field appears when the campaign price field is filled in. It shows the price before the discount, under the campaign price.') + sbshot('old-price', 'The Old Price Info field in Storyblok')))
S.append(('visual-enhancements', '<h2 class="ds-h2">7. Visual enhancements</h2>' + \
          '<h3 class="ds-h3 ds-group" id="overlay">7a. Overlay</h3>' + desc('A gradient overlay makes the text easier to read on an image.') + sbshot('overlay', 'The Overlay field in Storyblok with the gradient directions') + li(['The options are several gradient directions.', '<strong>Full</strong> covers the whole background.']) + \
          '<h3 class="ds-h3 ds-group" id="overlay-opacity">7b. Overlay opacity</h3>' + sbshot('overlay-opacity', 'The Overlay Opacity field in Storyblok with the value 80') + li(['The range is 0 (fully transparent) to 100 (fully opaque).', 'Adjust it to balance the visibility of the image and the legibility of the text.'])))
S.append(('buttons', '<h2 class="ds-h2">8. Call-to-action buttons</h2>' + sbshot('buttons', 'The button fields in Storyblok: size, text, link, chevron and overlay', cap='Button One.') + \
          h4('Button One (primary)') + ol_parts([('Button size', 'Large, Medium or Small.'), ('Button One text', 'Write a compelling call to action.'), ('Button One link', 'A URL path relative to the domain (for example <code>category/category-name</code>), or a full external URL that starts with <code>https://</code>.'), ('Chevron', 'A toggle that adds a right-pointing chevron for emphasis. See ' + L(WEB + '#use-of-the-chevron-on-the-hero-button', 'when to use it') + '.'), ('Button overlay', 'Makes the whole hero clickable, with the link of Button One.')]) + \
          h4('Button Two (secondary)') + desc('An optional secondary button with the same settings (text, link and chevron). It appears when the text field is filled in.') + sbshot('button-two', 'The Button Two Text field in Storyblok', pins=[('6', 68.2, 79.7, 0)])))
S.append(('branding', '<h2 class="ds-h2">9. Branding elements</h2>' + \
          '<h3 class="ds-h3 ds-group" id="brand-logo">9a. Brand logo</h3>' + desc('For brand identity or campaign-specific product logos. Upload the logo as an <code>.svg</code> file. If the background image has many colors or many other branding elements, use only white or black logos if you can, to avoid a cluttered look.') + sbshot('brand-logo', 'The Brand Logo and Brand Logo Position fields in Storyblok') + \
          '<h3 class="ds-h3 ds-group" id="brand-logo-position">9b. Brand logo position</h3>' + desc('This setting appears when a logo is added. The logo can sit in three places:') + ol_parts([('Top right', ''), ('Bottom right', ''), ('In content*', '*Added only for brand pages, when the content is centred with the hero in breakpoint XSmall.')]) + \
          '<h3 class="ds-h3 ds-group" id="news-badge">9c. News badge</h3>' + desc('A toggle that shows a “NEWS!” badge in a circle.') + sbshot('news-badge', 'The News Badge and News Badge Color fields in Storyblok') + \
          '<h3 class="ds-h3 ds-group" id="news-badge-color">9d. News badge color</h3>' + li(['White', 'Black', 'Green (Swedol only)', 'Red (Tools sites only)']) + desc('The Swedol and Tools colors are applied automatically for the site in use.') + \
          '<h3 class="ds-h3 ds-group" id="power-deal-logo">9e. Power Deal logo</h3>' + desc('Turns on the branding of the Power Deal campaign. The position setting is useful when the content needs the space and the logo should not make the hero use more room, and to reduce clutter.') + sbshot('pd-logo', 'The Power Deal Logo and Power Deal Logo Position fields in Storyblok') + \
          '<h3 class="ds-h3 ds-group" id="power-deal-logo-position">9f. Power Deal logo position</h3>' + li(['Top Left', 'Top Right', 'Bottom Right']) + \
          '<h3 class="ds-h3 ds-group" id="power-deal-border">9g. Power Deal border</h3>' + sbshot('pd-border', 'The Power Deal Border switch in Storyblok') + desc('The switch turns on the graphics of the Power Deal concept. The Swedol and Tools colors are applied automatically for the site in use. Use the border together with the Power Deal logo.')))
S.append(('related', '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + L(DESP, 'Design') + '</strong>. The anatomy, the sizes and the colors.</li><li><strong>' + L(WEB, 'Usage') + '</strong>. When to use a hero, fluid or regular, and the do’s and don’ts.</li><li><strong>' + L(REFP, 'Reference and Examples') + '</strong>. Finished banners to learn from.</li></ul>'))

C = dict(
    slug=SLUG, title='Hero banner', eyebrow='Components · Patterns',
    lead='The Hero banner is a versatile component for campaign features and for the headers of landing pages, on campaign pages and sites and on brand pages. It has many settings for building responsive hero sections.',
    select_menu=False, css=['badge', 'button', 'divider'], style=STYLE,
    pages=[
        dict(kind='design', suffix='', label='Design', lead='The anatomy, the sizes and the colors of the hero banner. Figma: ' + fig_link('https://www.figma.com/design/Pec5PrArnMy6XyBzRZOyRp/Supernova-ECO-DS-Assets?node-id=3890-80829', 'Main hero content') + ', ' + fig_link('https://www.figma.com/design/Pec5PrArnMy6XyBzRZOyRp/Supernova-ECO-DS-Assets?node-id=3895-5910', 'Power Deal') + ', ' + fig_link('https://www.figma.com/design/Pec5PrArnMy6XyBzRZOyRp/Supernova-ECO-DS-Assets?node-id=3895-6125', 'Brand logos') + ' and ' + fig_link('https://www.figma.com/design/Pec5PrArnMy6XyBzRZOyRp/Supernova-ECO-DS-Assets?node-id=3895-6312', 'News badge') + '.', secs=[('anatomy', d_anat), ('size', d_size), ('measurements', d_meas), ('colors', d_colors)], js=JS_DESIGN),
        dict(kind='usage', suffix='-usage', label='Usage', lead='When to use a hero banner, fluid or regular width, and the do’s and don’ts for images, text, color, buttons and branding.', secs=[('purpose', u_purpose), ('fluid-vs-regular', u_width), ('regular', u_reg), ('fluid', u_fluid), ('consider', u_consider), ('not-to-use', u_not), ('quick-reference', u_chart), ('dos-and-donts', u_dd), ('use-of-the-chevron-on-the-hero-button', u_chev)]),
        dict(kind='ref', suffix='-reference', label='Reference and Examples', lead='Finished banners to learn from, with the type, the purpose and the elements that make each one clear.', secs=R),
        dict(kind='sb', suffix='-storyblok', label='Storyblok', lead='How an editor adds and sets up the Hero Responsive widget in Storyblok. The numbers on the screenshots match the numbers in the headings.', secs=S),
    ])

if __name__ == '__main__':
    emit(C)
