"""Article Highlight Group Card (Storyblok widget AH Group): the Storyblok page, built like the Hero banner widget pages.
Source: the editor's own screenshots (images/AhGroupCard_*, cropped by crop_ah_group_card.py into images/ah-group-card-sb-*.webp),
the component schema pulled with the Storyblok CLI (article-highlight-group, -group-slide, -group-card) and the editor's text.
The other tabs (Design / Usage / Reference and Examples) are not built yet; when they are, add them to C['pages'] before this one.
Uses the custom page set (c['pages']) of build.py. Run from this folder: python3 gen_ah_group_card_widget.py [--force]"""
from build import *
from gen_hero_banner_widget import STYLE as HERO_STYLE, note, h4, li
from ah_pins import AH_PINS

SLUG = 'ah-group-card-widget'

STYLE = HERO_STYLE + r'''
    /* legend, Figma link, next example: 16px / 32px below 769px, 24px / 48px from 769px */
    .ds-prose > .hb-legend:has(+ .ds-desc) { margin-bottom: 0; }
    .ds-prose > .hb-legend + .ds-desc { margin-top: var(--dimension-spacing-space-16); }
    .ds-prose > .hb-legend + .ds-desc + .ds-figs { margin-top: var(--dimension-spacing-space-32); }
    @media (min-width: 769px) {
      .ds-prose > .hb-legend + .ds-desc { margin-top: var(--dimension-spacing-space-24); }
      .ds-prose > .hb-legend + .ds-desc + .ds-figs { margin-top: var(--dimension-spacing-space-48); }
    }
    /* Specifications figure: the card footer (Figma 24811-111461). Padding 16px below 640px, 24px from 640px; the Breakpoint toggle forces it (body[data-bp]) */
    .ahm-foot { width: 280px; display: flex; flex-direction: column; align-items: flex-start; padding: var(--dimension-spacing-space-16); background: var(--color-background-primary); color: var(--color-text-primary); }
    @media (min-width: 640px) { .ahm-foot { padding: var(--dimension-spacing-space-24); } }
    body[data-bp="mobile"] .ahm-foot { padding: var(--dimension-spacing-space-16); }
    body[data-bp="desktop"] .ahm-foot { padding: var(--dimension-spacing-space-24); }
    .ahm-pre { font-size: 16px; line-height: 16px; letter-spacing: 0.64px; font-weight: 500; text-transform: uppercase; color: var(--color-text-tertiary); padding-bottom: var(--dimension-spacing-space-8); }   /* alt-label-md */
    .ahm-title { font-size: 24px; line-height: 28px; font-weight: 600; padding-bottom: var(--dimension-spacing-space-8); }   /* title-lg */
    .ahm-body { margin: 0; font-size: 17px; line-height: 24px; letter-spacing: 0.32px; padding-bottom: var(--dimension-spacing-space-24); }   /* body-md */
    .ahm-link { display: inline-flex; align-items: center; gap: var(--dimension-spacing-space-4); font-size: 17px; line-height: 24px; letter-spacing: 0.32px; }
    .ahm-link .mo-ic { font-size: 20px; }
    .ahm-foot--flush { padding: var(--dimension-spacing-space-8) 0 0; }   /* Footer Padding off: only the space above the preheadline */
    @media (min-width: 640px) { .ahm-foot--flush { padding: var(--dimension-spacing-space-12) 0 0; } }
    @media (min-width: 769px) { .ahm-foot--flush { padding: var(--dimension-spacing-space-16) 0 0; } }
    body[data-bp="mobile"] .ahm-foot--flush { padding: var(--dimension-spacing-space-8) 0 0; }
    body[data-bp="desktop"] .ahm-foot--flush { padding: var(--dimension-spacing-space-16) 0 0; }
    .ahm-blk { display: block; width: 280px; background: var(--color-background-primary); color: var(--color-text-primary); }
    .ahm-blk.ahm-pre { color: var(--color-text-tertiary); }
    .ahm-blk.ahm-date { color: var(--color-text-secondary); }
    .ahm-body--gap { padding-bottom: var(--dimension-spacing-space-16); }   /* to the list: 16px; Large card desktop 20px (Figma 20161-55854; no spacing token for 20) */
    @media (min-width: 769px) { .ahm-body--lg { padding-bottom: 20px; } }
    body[data-bp="mobile"] .ahm-body--lg { padding-bottom: var(--dimension-spacing-space-16); }
    body[data-bp="desktop"] .ahm-body--lg { padding-bottom: 20px; }
    .ahm-li { display: flex; align-items: flex-start; gap: var(--dimension-spacing-space-4); font-size: 17px; line-height: 24px; letter-spacing: 0.32px; padding-bottom: var(--dimension-spacing-space-8); }   /* body-md */
    .ahm-li .mo-ic { font-size: 20px; margin-top: 2px; }
    .ahm-group { padding-bottom: var(--dimension-spacing-space-16); }   /* space above the action link: Small card 16 / 24 from 640px; Large card 16 / 24 / 32 from 769px */
    @media (min-width: 640px) { .ahm-group { padding-bottom: var(--dimension-spacing-space-24); } }
    @media (min-width: 769px) { .ahm-group--lg { padding-bottom: var(--dimension-spacing-space-32); } }
    body[data-bp="mobile"] .ahm-group { padding-bottom: var(--dimension-spacing-space-16); }
    body[data-bp="desktop"] .ahm-group { padding-bottom: var(--dimension-spacing-space-24); }
    body[data-bp="desktop"] .ahm-group--lg { padding-bottom: var(--dimension-spacing-space-32); }
    .ahm-date { padding-bottom: var(--dimension-spacing-space-8); }
    .ahw { margin-bottom: var(--dimension-spacing-space-16); }
    .ahw-list { margin: var(--dimension-spacing-space-4) 0 0; padding-left: var(--dimension-spacing-space-16); }
    /* Footer layout figure (Figma 20161-55854). Mobile first: Small-XSmall values, desktop (769px+) per card size; body[data-bp] forces them */
    .ahl { width: 260px; display: flex; flex-direction: column; align-items: stretch; background: var(--color-background-primary); color: var(--color-text-primary); margin-right: 40px; }
    .ahl .ahl-obj { display: block; margin: 0; }
    .ahl-pre { display: flex; align-items: center; gap: var(--dimension-spacing-space-8); padding-bottom: var(--dimension-spacing-space-8); font-size: 14px; line-height: 14px; letter-spacing: 0.56px; font-weight: 500; text-transform: uppercase; color: var(--color-text-tertiary); }   /* alt-label-md */
    .ahl-divider { width: 1px; height: 14px; background: var(--color-border-primary); }
    .ahl-title { padding-bottom: var(--dimension-spacing-space-8); font-weight: 600; }
    .ahl--lg .ahl-title { font-size: 22px; line-height: 24px; }   /* headline-sm */
    .ahl--sm .ahl-title { font-size: 20px; line-height: 24px; }   /* title-lg */
    .ahl-txt, .ahl-list, .ahl-link, .ahl-stack, .ahl-divided { font-size: 16px; line-height: 22px; letter-spacing: 0.32px; }   /* body-md */
    .ahl-gap { padding-bottom: var(--dimension-spacing-space-16); }
    .ahl-end { padding-bottom: var(--dimension-spacing-space-16); }   /* space above the date: 16px XSmall, 24px Small, 24 / 32px desktop */
    @media (min-width: 640px) { body:not([data-bp="mobile"]) .ahl-end { padding-bottom: var(--dimension-spacing-space-24); } }
    body[data-bp="desktop"] .ahl-end { padding-bottom: var(--dimension-spacing-space-24); }
    .ahl-list { display: flex; flex-direction: column; gap: var(--dimension-spacing-space-8); }
    .ahl-list span { display: flex; align-items: baseline; gap: var(--dimension-spacing-space-8); }
    .ahl-list span::before { content: ''; width: 5px; height: 5px; border-radius: 50%; background: currentColor; flex: none; transform: translateY(-3px); }   /* bullet, size from Figma's 6px prefix */
    .ahl-stack { display: flex; flex-direction: column; align-items: flex-start; gap: var(--dimension-spacing-space-12); }
    .ahl-divided { display: flex; flex-wrap: wrap; align-items: center; gap: var(--dimension-spacing-space-12) var(--dimension-spacing-space-8); }
    .ahl-sep { width: 1px; height: 16px; background: var(--color-surface-20); }
    .ahl-link { display: inline-flex; align-items: center; gap: var(--dimension-spacing-space-4); }
    .ahl-link .mo-ic { font-size: 20px; }
    .ahl-date { padding-bottom: var(--dimension-spacing-space-8); font-size: 14px; line-height: 14px; letter-spacing: 0.56px; font-weight: 500; text-transform: uppercase; color: var(--color-text-secondary); }   /* alt-label-md */
    @media (min-width: 769px) {
      body:not([data-bp="mobile"]) .ahl--lg { width: 335px; } body:not([data-bp="mobile"]) .ahl--sm { width: 284px; }   /* content widths of the Figma variants */
      body:not([data-bp="mobile"]) .ahl-pre,body:not([data-bp="mobile"]) .ahl-date { font-size: 16px; line-height: 16px; letter-spacing: 0.64px; } body:not([data-bp="mobile"]) .ahl-divider { height: 16px; }
      body:not([data-bp="mobile"]) .ahl--lg .ahl-title { font-size: 28px; line-height: 32px; } body:not([data-bp="mobile"]) .ahl--sm .ahl-title { font-size: 24px; line-height: 28px; }
      body:not([data-bp="mobile"]) .ahl--lg :is(.ahl-txt, .ahl-list, .ahl-link, .ahl-stack, .ahl-divided) { font-size: 20px; line-height: 28px; letter-spacing: 0.18px; }   /* body-lg */
      body:not([data-bp="mobile"]) .ahl--sm :is(.ahl-txt, .ahl-list, .ahl-link, .ahl-stack, .ahl-divided) { font-size: 17px; line-height: 24px; letter-spacing: 0.32px; }   /* body-md */
      body:not([data-bp="mobile"]) .ahl--lg .ahl-gap { padding-bottom: 20px; }   /* Figma gap 20, no spacing token for 20 */
      body:not([data-bp="mobile"]) .ahl--lg .ahl-end { padding-bottom: var(--dimension-spacing-space-32); }
      body:not([data-bp="mobile"]) .ahl--lg .ahl-link { gap: var(--dimension-spacing-space-8); } body:not([data-bp="mobile"]) .ahl--lg .ahl-link .mo-ic { font-size: 24px; }
    }
    body[data-bp="desktop"] .ahl--lg { width: 335px; } body[data-bp="desktop"] .ahl--sm { width: 284px; }   /* content widths of the Figma variants */
    body[data-bp="desktop"] .ahl-pre,body[data-bp="desktop"] .ahl-date { font-size: 16px; line-height: 16px; letter-spacing: 0.64px; } body[data-bp="desktop"] .ahl-divider { height: 16px; }
    body[data-bp="desktop"] .ahl--lg .ahl-title { font-size: 28px; line-height: 32px; } body[data-bp="desktop"] .ahl--sm .ahl-title { font-size: 24px; line-height: 28px; }
    body[data-bp="desktop"] .ahl--lg :is(.ahl-txt, .ahl-list, .ahl-link, .ahl-stack, .ahl-divided) { font-size: 20px; line-height: 28px; letter-spacing: 0.18px; }   /* body-lg */
    body[data-bp="desktop"] .ahl--sm :is(.ahl-txt, .ahl-list, .ahl-link, .ahl-stack, .ahl-divided) { font-size: 17px; line-height: 24px; letter-spacing: 0.32px; }   /* body-md */
    body[data-bp="desktop"] .ahl--lg .ahl-gap { padding-bottom: 20px; }   /* Figma gap 20, no spacing token for 20 */
    body[data-bp="desktop"] .ahl--lg .ahl-end { padding-bottom: var(--dimension-spacing-space-32); }
    body[data-bp="desktop"] .ahl--lg .ahl-link { gap: var(--dimension-spacing-space-8); } body[data-bp="desktop"] .ahl--lg .ahl-link .mo-ic { font-size: 24px; }
    .ahm-badge { display: inline-flex; align-items: center; padding: var(--dimension-spacing-space-4) 5px; background: var(--color-surface-raised-primary); box-shadow: var(--shadow-elevation-b-20); color: var(--color-text-primary); font-size: 16px; line-height: 16px; letter-spacing: 0.16px; font-weight: 600; text-transform: uppercase; }   /* 5px side padding: Figma Stand Alone Card Badge, no spacing token for 5 */
    .ah-narrow { max-width: 480px; }   /* a cropped settings panel is shown at its own size, not stretched over the page width */
    .ds-figs--one .ah-narrow .sb-shot img { width: 100%; }
    .ah-pair .sb-stage { height: 100%; }
    .ds-prose > :is(.ds-h2, .ds-h3, .hb-h4, .ds-desc, .ds-bullets, .hb-note) + .ah-pair, .ds-prose > .ah-pair + :is(.hb-h4, .ds-desc, .ds-bullets, .hb-note, .hb-legend) { margin-top: var(--dimension-spacing-space-16); }
    .ds-prose > .ds-figs + :is(.ds-h2, .ds-h3) { margin-top: var(--dimension-spacing-space-32); }   /* a new heading after a picture (single, pair or trio) and its caption: 32px mobile, 48px from 769px (overrides the 16px of the Hero banner set) */
    @media (min-width: 769px) { .ds-prose > .ds-figs + :is(.ds-h2, .ds-h3) { margin-top: var(--dimension-spacing-space-48); } }
    .ds-prose > .ds-desc.ds-desc:has(+ .ah-pair), .ds-prose > .ds-bullets.ds-bullets:not(.ds-bullets--num):has(+ .ah-pair) { margin-bottom: 0; }
    .ah-pair.ds-figs { align-items: start; }
    .sb-pin { white-space: nowrap; }   /* sub-numbered badges such as 7d-3 stay on one line, also at the edge of a picture */
    @media (min-width: 769px) { .ah-trio.ah-pair { grid-template-columns: repeat(3, 1fr); } }   /* three settings pictures side by side */
    .ds-prose > :is(.ds-figs, .ah-pair) + :is(.ds-figs, .ah-pair) { margin-top: var(--dimension-spacing-space-16); }
    .ds-prose > .ds-table-wrap + :is(.ds-desc, .ds-h3, .hb-note, .ds-figs, .ah-pair) { margin-top: var(--dimension-spacing-space-16); }   /* the table's own bottom edge: 16px to what follows */
    .ds-prose > :is(.ds-desc, .ds-bullets, .ds-figs, .ah-pair) + .ds-table-wrap { margin-top: var(--dimension-spacing-space-16); }
    .ds-prose > .ds-desc.ds-desc:has(+ .ds-table-wrap) { margin-bottom: 0; }
    code { font-size: 0.9em; }'''

IMG = '/images/ah-group-card-sb-%s.webp'
BP = '../foundations/layout-breakpoints.html'


def img(name, alt, box=None, pins=None):
    inner = '<img src="%s" alt="%s" loading="lazy" />' % (IMG % name, alt)
    if box:
        inner += '<span class="sb-box" style="left:%s%%;top:%s%%;width:%s%%;height:%s%%"></span>' % box
    for lab, x, y in AH_PINS.get(pins or name, []):   # the number of the heading next to the area it describes (pins: another key in AH_PINS, when one picture is used under two headings)
        inner += '<span class="badge-number sb-pin" style="left:%s%%;top:%s%%">%s</span>' % (x, y, lab)
    return '<div class="ds-fig__stage sb-stage"><div class="sb-shot">%s</div></div>' % inner


def cap(c):
    return ('<figcaption class="ds-fig__cap">%s</figcaption>' % c) if c else ''


def shot(name, alt, c=None, box=None, narrow=True):
    """One picture of the Storyblok editor (a cropped settings panel is narrow, a page or a card preview is wide)."""
    return '<div class="ds-figs ds-figs--one"><figure class="ds-fig%s">%s%s</figure></div>' % (' ah-narrow' if narrow else '', img(name, alt, box), cap(c))


def pair(a, a_alt, b, b_alt, ca=None, cb=None, pb=None):
    """Settings on the left, the result on the right (two columns from 769px)."""
    return '<div class="ds-figs ah-pair"><figure class="ds-fig">%s%s</figure><figure class="ds-fig">%s%s</figure></div>' % (img(a, a_alt), cap(ca), img(b, b_alt, pins=pb), cap(cb))


def half(name, alt, c=None):
    """One settings picture at the width of the left picture in a pair (half the width from 769px)."""
    return '<div class="ds-figs ah-pair"><figure class="ds-fig">%s%s</figure></div>' % (img(name, alt), cap(c))


def trio(items):
    """Three settings pictures side by side (items: three (name, alt, caption)); one column below 769px."""
    return '<div class="ds-figs ah-pair ah-trio">%s</div>' % ''.join('<figure class="ds-fig">%s%s</figure>' % (img(n, a), cap(c)) for n, a, c in items)


def dont(name, alt, c, pins=None):
    return '<div class="ds-figs ds-figs--one"><figure class="ds-fig ds-fig--dont">%s<figcaption class="ds-fig__cap"><span class="ds-fig__ic" aria-hidden="true">cancel</span>%s</figcaption></figure></div>' % (img(name, alt, pins=pins), c)


def h3(id_, t):
    return '<h3 class="ds-h3 ds-group" id="%s">%s</h3>' % (id_, t)


def a(href, t):
    return '<a class="inline-link inline-link--secondary" href="%s">%s</a>' % (href, t)


S = []
# ======================================================================================
S.append(('widget', '<h2 class="ds-h2">AH Group widget</h2>' + desc('The Article Highlight Group Card is available as a widget in the admin tool Storyblok, for the content managers and content creators of our e-commerce sites. It promotes articles, campaigns and brands with cards that are placed in a grid or in a carousel. In Storyblok the widget is called <strong>AH Group</strong> (technical name <code>article-highlight-group</code>).') +
          desc('The widget is built from three blocks:') +
          table(['Block', 'Technical name', 'Used for'], [
              ['AH Group', '<code>article-highlight-group</code>', 'The container. It sets the layout (grid or carousel) and the number of columns or slides.'],
              ['AH Group Slide Item', '<code>article-highlight-group-slide</code>', 'One slide of a carousel. It holds one or two cards.'],
              ['AH Group Card', '<code>article-highlight-group-card</code>', 'The card itself: image, logos, badges, text, links and button.'],
          ]) +
          desc('The appearance of a card is controlled only by its settings. Different combinations of the settings give cards for different purposes.')))

S.append(('start', '<h2 class="ds-h2">Start</h2>' + desc('Start by adding a section to the page, or pick an existing one, and place the AH Group widget in it. In the section, choose <strong>Add Block</strong> under Components and pick <strong>AH Group</strong> in the Insert block list. It is in the folder <em>(3) Organisms</em>.') +
          shot('section-add', 'The section in Storyblok with the Components list and the Add Block button', 'Add Block in the Components list of the section.') +
          shot('insert-block', 'The Insert block list in Storyblok with AH Group marked', 'AH Group in the Insert block list.', box=(11.5, 37.2, 84.5, 4.4))))

S.append(('layout', '<h2 class="ds-h2">1. Layout</h2>' + desc('<strong>Layout</strong> is required. Choose <strong>Grid</strong> or <strong>Carousel</strong>.') +
          shot('layout-options', 'The Layout field in Storyblok with the options Grid and Carousel', 'The Layout field.') +
          pair('grid-example', 'Cards in a grid with four columns and two rows', 'carousel-example', 'Cards in a carousel', '<strong>Grid</strong> places the cards in ordered rows and columns.', '<strong>Carousel</strong> places the cards in the carousel component.') +
          desc('Depending on the choice you add <strong>AH Group Card</strong> directly in the widget (Grid) or <strong>AH Group Slide Item</strong> (Carousel). The settings that do not belong to the choice are hidden:') +
          table(['Layout', 'Settings shown'], [
              ['Grid', 'Grid Columns, Equal Gutter, Cards'],
              ['Carousel', 'Carousel Slides, Slides, Title, Supporting Title, Navigation Text, Link'],
          ]) +
          desc('After that the work is almost the same for both. This page starts with Grid. Carousel is described in ' + a('#carousel', '9. Carousel') + '.')))

S.append(('grid', '<h2 class="ds-h2">2. Grid settings</h2>' + \
          h3('grid-columns', '2a. Grid Columns') + desc('Choose <strong>2, 3 or 4</strong> columns. That is the number of cards in a row. The default is 4. The number of cards in a row is lower on smaller screens:') +
          shot('grid-columns', 'The Grid Columns field in Storyblok with the options 4, 3 and 2', 'The Grid Columns field.') +
          table(['Grid Columns', 'XL', 'L', 'M', 'S', 'XS'], [
              ['4', '4', '4', '3', '2', '1'],
              ['3', '3', '3', '3', '2', '1'],
              ['2', '2', '2', '2', '2', '1'],
          ]) +
          desc('The table shows cards in a row per breakpoint. See the breakpoints in ' + a(BP, 'Layout') + '.') +
          shot('grid-example', 'A grid with four columns and two rows of cards', 'Grid Columns 4 on a wide screen.', narrow=False) +
          h3('equal-gutter', '2b. Equal Gutter') + desc('Sets the horizontal space between the rows to the same size as the vertical space between the cards. Useful when there are many identical cards, for example a grid of brand logos.')))

S.append(('add-card', '<h2 class="ds-h2">3. Add the card</h2>' + desc('Add a card with <strong>Add AH Group Card</strong> under Cards. A card can be built with many different settings and in many ways. It is the combination of the settings that gives the card its purpose. The settings are described in the next sections.') +
          shot('add-card', 'The Cards list in Storyblok with the Add AH Group Card button', 'Add AH Group Card.') +
          desc('Fill in <strong>Link</strong>, the URL of the card, at the top of the card. The button of the card (see ' + a('#show-button', '8b. Show Button') + ') becomes available when the URL is filled in.') +
          desc('Turn on <strong>Active Card</strong> to make the whole card the link. The whole card links to the card URL, and the title and the button show their hover state when the card is hovered. A card with Active Card should have no other links: do not add links (see ' + a('#links', '7e. Links') + ') to it.')))

S.append(('image', '<h2 class="ds-h2">4. Image</h2>' + \
          h3('image-section', '4a. Image Section') + desc('<strong>Image Section</strong> is required. Here you add the image of the card.') +
          shot('image-section', 'The Image Section and Image/Video fields in Storyblok', 'Image Section with “Image/Video” and an image.') +
          li(['<strong>Image/Video:</strong> add an image or a video.', '<strong>Color:</strong> the image holder becomes black or white. Useful to promote a brand with a logo (see ' + a('#brand-logo', '5c')  + ').', '<strong>Hidden:</strong> the card has no image holder.']) + \
          h3('image-color', '4b. Image Color') + desc('Shown when Image Section is <strong>Color</strong>. Choose <strong>Black</strong> or <strong>White</strong>.') +
          pair('image-section-color', 'The Image Section field with the option Color and the Image Color field set to Black', 'image-color', 'The Image Color field with the options Black and White', 'Image Section “Color”.', 'Image Color “Black” or “White”.') + \
          h3('image-aspect', '4c. Image Aspect') + desc('The image can be shown in different crops, called ratios: <strong>3:2, 16:9 or 1:1</strong>. Select the card with the ratio you want. In a layout with many cards, an image in 16:9 saves more space than an image in 1:1.') +
          pair('image-aspect', 'The Image Aspect field with the options 3:2, 16:9 and 1:1', 'ratios', 'Three cards with the ratios 1:1, 3:2 and 16:9', 'Image Aspect.', 'The ratios 1:1, 3:2 and 16:9.') + \
          h3('lazyload', '4d. Image Lazyload') + desc('When the page loads:') +
          li(['Only the images at the top of the page load at once.', 'The other images wait.', 'When the user scrolls down, the images load one after another.']) +
          shot('lazyload-video', 'The Image Lazyload, Youtube and Videoly fields in Storyblok', 'Image Lazyload, Youtube and Videoly.') + \
          h3('video', '4e. Youtube and Videoly') + desc('Add the video you want to show in the image holder. <strong>Youtube</strong> takes the video ID, for example <code>StBj0vHMesk</code>.')))

S.append(('brand-elements', '<h2 class="ds-h2">5. Overlay and brand elements</h2>' + \
          h3('overlay', '5a. Overlay') + desc('Adds a layer on top of the image. Use it to bring out something on the image, like graphics or a logo, or to change the image for another reason. Choose <strong>Full</strong>, <strong>Left</strong> or <strong>Right</strong>.') +
          pair('overlay', 'The Overlay field in Storyblok with the options Full, Left and Right', 'overlay-preview', 'Three cards with a black overlay on the images', 'Overlay.', 'Overlay “Full” with the opacity 100.') + \
          h3('overlay-opacity', '5b. Overlay Opacity') + desc('Sets how transparent the overlay is, from 0 to 100. 0 is fully transparent and 100 is fully black.') +
          pair('overlay-opacity', 'The Overlay Opacity field with the value 70', 'overlay-opacity-preview', 'Three cards with an overlay of the opacity 70', 'Overlay Opacity 70.', 'The result.') + \
          h3('brand-logo', '5c. Brand Logo') + desc('Adds a logo or other graphics on the image. There are two places, and each has its own field:') +
          li(['<strong>Brand Logo Center:</strong> in the middle of the image.', '<strong>Brand Logo Bottom Right:</strong> in the bottom right corner of the image.', '<strong>Brand Logo Bottom Right Size:</strong> <strong>Large</strong> or <strong>Small</strong>. It controls the size of the logo, so that logos of different shapes get a more even feel.']) +
          pair('brand-logo', 'The Brand Logo Center, Brand Logo Bottom Right and Size fields in Storyblok', 'brand-logo-preview', 'Three cards with a centred logo and a logo in the bottom right corner', 'The Brand Logo fields.', 'A centred logo and logos in the bottom right corner.') + \
          h3('power-deal', '5d. Power Deal') + desc('<strong>Power Deal Logo</strong> and <strong>Power Deal Border</strong> promote the Power Deal concept. Each has a color, <strong>Green</strong> or <strong>Red</strong>. Use the logo and the border together. The content scales with the image format.') +
          pair('power-deal', 'The Power Deal Logo and Power Deal Border fields in Storyblok', 'power-deal-preview', 'A card with the Power Deal logo and border', 'The Power Deal fields.', 'A card with the Power Deal logo and border.') + \
          h3('news-badge', '5e. News Badge') + desc('Switch it on to push or strengthen a piece of news. The text uses our font, so you can change the label to something else if you want. The default is “Nyhet”. The badge has a fixed size for each breakpoint (see ' + a(BP, 'Layout') + ').') +
          pair('news-badge', 'The News Badge switch and the Badge Label field with the text Nyhet', 'news-badge-preview', 'A card with the news badge “Nyhet”', 'News Badge with the default label.', 'The result.') +
          pair('news-badge-label', 'The Badge Label field with the text Vi är bäst', 'news-badge-label-preview', 'A card with the news badge “Vi är bäst”', 'A changed label.', 'The result.')))

S.append(('footer', '<h2 class="ds-h2">6. Card footer</h2>' + \
          h3('footer-section', '6a. Footer Section') + desc('Switch it on to add content in the footer of the card. The switch turns on more settings further down the settings column, from ' + a('#preheadline', '7a. Preheadline') + ' on.') +
          pair('footer-settings', 'The Footer Section, Footer Padding, Footer Border and Card Size fields', 'footer-preview', 'Two cards, the right one with footer padding and a border', 'Footer Section, Footer Padding and Footer Border on.', 'The right card with padding and border.', pb='footer-preview-6a') + \
          h3('footer-padding', '6b. Footer Padding') + desc('Gives the text in the footer padding, that is air around it. Use it in the same way on every card in a group of cards in a section, or in a concept. Do not mix cards with and without it.') +
          dont('footer-preview', 'Two cards, one with footer padding and a border and one without', 'Do not mix cards with and without Footer Padding in one group.', pins='footer-preview-6b') + \
          h3('footer-border', '6c. Footer Border') + desc('The border gives a more premium feel. Use it when Footer Padding is on. Do not use it with text unless the card has enough padding.') + \
          h3('card-size', '6d. Card Size') + desc('<strong>Large</strong> or <strong>Small</strong>. It sets the size of the text inside the card. The sizes are fixed and adapt to smaller screens: <strong>Large</strong> gets the same size as <strong>Small</strong> when the viewport reaches breakpoint-sm. In a layout with many cards, use <strong>Small</strong>.') +
          pair('footer-card-size', 'The Card Size field with the value Large', 'card-size-preview', 'Two cards, the left one Small and the right one Large', 'Card Size “Large”.', 'Left: Small. Right: Large.')))

S.append(('text', '<h2 class="ds-h2">7. Text content</h2>' + desc('The settings in this section appear when <strong>Footer Section</strong> is on.') + \
          h3('preheadline', '7a. Preheadline') + desc('Also called eyebrow or pre title. It categorises the content or adds context. It is optional, but use it in the same way in a group of cards or in a concept. Write one item per line. The items are shown next to each other with a divider.') +
          pair('preheadline-title', 'The Preheadline, Title and Supporting Text 1 fields in Storyblok', 'preheadline-card', 'A card with the preheadline EcoVadis, a title and a supporting text', 'Preheadline, Title and Supporting Text 1.', 'The same fields in the card.') + \
          h3('title', '7b. Title') + desc('The descriptive headline of the card. It is often the most important part of a card.') + \
          h3('supporting-text-1', '7c. Supporting Text 1 and 2') + desc('Space for body text. <strong>Supporting Text 1</strong> comes before the list (see ' + a('#bulletlist', '7d. Bulletlist') + ') and <strong>Supporting Text 2</strong> after it.') + \
          pair('supporting-text-2', 'The Bulletlist Variant and Supporting Text 2 fields in Storyblok', 'preheadline-card', 'A card with a supporting text above the list and one after it', 'Supporting Text 2, after the list.', 'Supporting Text 1 (7c-1) above the list and Supporting Text 2 (7c-2) after it.', pb='supporting-card') + \
          h3('bulletlist', '7d. Bulletlist') + desc('Write one item per line. There are three kinds of lists: <strong>Bullet</strong>, <strong>Numbered</strong> and <strong>Checkmark</strong>. Use lists sparingly in a card. They take a lot of space, and cards in the same row get the same height, so a card with little content gets the height of the cards with more. A card that leads to a full article or a campaign should be direct.') +
          trio([('bulletlist', 'The Bulletlist and Bulletlist Variant fields in Storyblok with Bullet chosen', 'Bulletlist and Variant “Bullet”.'), ('bulletlist-checkmark', 'The Bulletlist Variant field with Checkmark chosen', 'Variant “Checkmark”.'), ('bulletlist-numbered', 'The Bulletlist Variant field with Numbered chosen', 'Variant “Numbered”.')]) + \
          shot('bulletlist-preview', 'Three cards with a list: Bullet, Checkmark and Numbered', 'Left to right: Variant “Bullet”, “Checkmark” and “Numbered”.', narrow=False) + \
          h3('links', '7e. Links') + desc('Add more links, with or without icons, that help the user to do a task or give context. Add them with <strong>Add Inline link</strong>. <strong>Links Layout</strong> is <strong>Stacked</strong> or <strong>Divided</strong>. Stacked gives a more separated look. Divided saves space. If you add extra links, make sure <strong>Active Card</strong> is not turned on (see ' + a('#add-card', '3. Add the card') + ').') +
          pair('links-layout', 'The Links list and the Links Layout field with Stacked and Divided', 'links-layout-preview', 'Two cards with the links “Glömt lösenord?” and “Bli kund”: divided on the left, stacked on the right', 'Links and Links Layout.', 'Left: Links Layout “Divided”. Right: Links Layout “Stacked”.') +
          h3('date', '7f. Date') + desc('Meant first of all to show a date clearly, for example when a campaign ends or the last day to sign up. It can also be used for another short clarification.') + \
          pair('date-field', 'The Date field with the text “Gäller tom 31 oktober”', 'date-cards', 'Two cards with the date “Gäller t.o.m 31 oktober” above the action link and above the button', 'The Date field.', 'The date above an action link and above a button.')))

S.append(('button', '<h2 class="ds-h2">8. Background and button</h2>' + \
          h3('background-color', '8a. Background Color') + desc('Changes the color of the footer of the card, <strong>White</strong> or <strong>Grey</strong>. Useful when the cards are placed on different backgrounds.') +
          pair('background-color', 'The Background Color field with the options White and Grey', 'background-preview', 'Cards on a white and a grey background', 'Background Color.', 'Top: cards with a grey footer on a white background. Bottom: cards with a white footer on a grey background.') + \
          h3('show-button', '8b. Show Button') + desc('The option becomes available when the URL of the card is filled in. Then you fill in <strong>Button Label</strong> and choose the type.') +
          pair('button-fields', 'The Show Button, Button Label, Button Type and Button Icon fields', 'links-preview-pair', 'Two cards: one with the button “Logga in” and the same card without a button', 'The button fields.', 'Left: a card with a primary button. Right: the Show Button switch not activated.') + \
          h3('button-type', '8c. Button Type') + desc('Choose the container of the call to action: a button or an action link. Use the action link in the first place.') +
          shot('button-settings', 'The Button Label, Button Type and Button Icon fields in Storyblok', 'Button Type “Primary”.') + \
          h3('button-icons', '8d. Button Icon Before and Button Icon After') + desc('Use icons to strengthen the message or the call to action. A calm icon, like the arrow, helps an action link without taking over.') +
          pair('date-button', 'The Date, Button and Button Icon fields with the icon Percent discount', 'date-preview', 'Two cards with a date: one with the action link “Utforska kampanjen” and one with the button “Se erbjudandet”, both with an icon', 'The Date and the button settings.', 'Cards with a date and an action link or a button with an icon.') + \
          h3('full-stroke-border', '8e. Full Stroke Border') + desc('A border that frames the whole card. It overrides the Footer Border. Use it when the background of the image could blend into the background of the page, for a better frame. Switch it on when the footer border is off, to keep the hover effect on the image holder, when using only a single image.') +
          pair('stroke-border', 'The Full Stroke Border switch with the note that it overrides the Footer Border', 'stroke-preview', 'Two cards with a border around the whole card', 'Full Stroke Border on.', 'The result.') + \
          shot('brand-card', 'A card with a border around the whole card, showing only the Gesto logo', 'A card with only a single logo and Full Stroke Border on.', narrow=True)))

S.append(('carousel', '<h2 class="ds-h2">9. Carousel</h2>' + desc('Choose <strong>Carousel</strong> as the Layout (see ' + a('#layout', '1. Layout') + '). The cards are then placed in slides.') + \
          h3('carousel-slides', '9a. Carousel Slides') + desc('Choose how many cards are shown at once in the first view of the carousel, <strong>2 to 5</strong>. The default is 5.') +
          shot('carousel-layout', 'The Layout field set to Carousel and the Carousel Slides field with the options 5, 4, 3 and 2', 'Carousel Slides.') + \
          h3('slide-item', '9b. Add a slide') + desc('Add a slide with <strong>Add AH Group Slide Item</strong> under Slides.') +
          shot('carousel-slide-item', 'The Slides list with the Add AH Group Slide Item button', 'Add AH Group Slide Item.') + \
          h3('slide-card', '9c. Add a card') + desc('Open the slide and add a card with <strong>Add AH Group Card</strong> under Cards.') +
          shot('carousel-add-card', 'A slide item with the Cards list and the Add AH Group Card button', 'Add AH Group Card in the slide.') + \
          h3('carousel-card', '9d. The card') + desc('After that the work is as usual. Continue with ' + a('#image-section', '4. Image') + '.') +
          shot('carousel-card-fields', 'The fields of an AH Group Card inside a slide', 'The card in a slide.') +
          h3('carousel-heading', '9e. Title, Supporting Title, Navigation Text and Link') + desc('A carousel can have its own heading: <strong>Title</strong> and <strong>Supporting Title</strong> above the cards. <strong>Navigation Text</strong> and <strong>Link</strong> give a link next to the title, for example to a knowledge base.') +
          shot('carousel-page-example', 'A carousel with the heading Guider & artiklar, a supporting text and the link Mer i kunskapsbanken', 'A carousel with a heading and a link.', narrow=False) + \
          h3('two-rows', '9f. Two rows') + desc('Each slide item can hold <strong>two cards</strong>, one over the other. Then the carousel gets two rows.') +
          pair('slide-cards-panel', 'A slide item with one card', 'slide-two-cards', 'A carousel where the first slide has one card that fills the height', 'A slide with one card.', 'The first slide has one card.') +
          pair('slide-two-cards-panel', 'A slide item with two cards', 'slide-two-rows', 'A carousel where the first slide has two cards, one over the other', 'A slide with two cards.', 'Two cards in the first slide.')))


# ======================================================================================
# DESIGN (the main page of the set): anatomy, brand elements, usage. Pictures from Figma (images/ah-group-card-design-*.webp)
# ======================================================================================
DIMG = '/images/ah-group-card-design-%s.webp'
FIG_AH = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id='


def anat(id_, name, label):
    """Anatomy figure with side markers (DK.callouts, as on the Hero banner Design page); the markers are placed by JS_EX."""
    return '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout hb-anat" id="%s" role="img" aria-label="%s"><div class="ds-callout__art"><img id="%s-img" src="%s" alt="" /></div></div></figure></div>' % (id_, label, id_, DIMG % name)


def legend(items):
    return '<ul class="hb-legend">' + ''.join('<li><span class="badge-number badge-number--md" aria-hidden="true">%s</span><p class="ds-desc"><strong>%s.</strong> %s</p></li>' % x for x in items) + '</ul>'


def figref(url, text):
    return desc('Figma: ' + fig_link(url, text, 'large') + '.')


E = []
E.append(('anatomy', '<h2 class="ds-h2">Anatomy</h2>' + desc('A card is built from an image holder and a footer. Every part except the image is optional. Figma: ' + fig_link(FIG_AH + '24811-111461', 'Article Highlight Card Prototypes for Anatomy', 'large') + '.') +
          anat('an-card', 'anatomy', 'Anatomy of an Article Highlight card: 1 image, 2 overlay, 3 badge, 4 preheadline, 5 title, 6 supporting text, 7 list, 8 supporting text 2, 9 links, 10 date, 11 action link or button') +
          legend([
              ('1', 'Image', 'The image, a color or a video, with optional brand elements and logo See ' + a('ah-group-card-widget-storyblok.html#image', '4. Image') + '.'),
              ('2', 'Overlay', 'An optional dark layer over the whole image or one side of it, so text and graphics stand out. See ' + a('ah-group-card-widget-storyblok.html#overlay', '5a. Overlay') + '.'),
              ('3', 'Badge', 'A short label on the image, for example “Nyhet” See ' + a('ah-group-card-widget-storyblok.html#news-badge', '5e. News Badge') + '.'),
              ('4', 'Preheadline', 'Also called eyebrow. It gives context See ' + a('ah-group-card-widget-storyblok.html#preheadline', '7a. Preheadline') + '.'),
              ('5', 'Title', 'The headline of the card See ' + a('ah-group-card-widget-storyblok.html#title', '7b. Title') + '.'),
              ('6', 'Supporting text 1', 'Body text before the list See ' + a('ah-group-card-widget-storyblok.html#supporting-text-1', '7c. Supporting Text 1 and 2') + '.'),
              ('7', 'Bulletlist', 'Bullet, numbered or checkmark list See ' + a('ah-group-card-widget-storyblok.html#bulletlist', '7d. Bulletlist') + '.'),
              ('8', 'Supporting text 2', 'Body text after the list See ' + a('ah-group-card-widget-storyblok.html#supporting-text-1', '7c. Supporting Text 1 and 2') + '.'),
              ('9', 'Links', 'Extra links, with or without icons, stacked or divided See ' + a('ah-group-card-widget-storyblok.html#links', '7e. Links') + '.'),
              ('10', 'Date', 'A date or another short, related note See ' + a('ah-group-card-widget-storyblok.html#date', '7f. Date') + '.'),
              ('11', 'Action link or button', 'The call to action of the card See ' + a('ah-group-card-widget-storyblok.html#button', '8. Background and button') + '.')]) +
          '<h3 class="ds-h3 ds-group" id="brand-elements">Brand elements</h3>' + desc('Brand elements sit on the image, never in the footer. They are part of the picture, so they follow the image when it is cropped. The two examples show a campaign concept and a discount with a brand logo.') +
          anat('an-pd', 'brand-powerdeal', 'Anatomy of a Power Deal image: 1 Power Deal logo, 2 Power Deal border') +
          legend([('1', 'Power Deal logo', 'The logo of the Power Deal concept See ' + a('ah-group-card-widget-storyblok.html#power-deal', '5d. Power Deal') + '.'), ('2', 'Power Deal border', 'The graphic stripes at the top and bottom edge. Use it together with the logo See ' + a('ah-group-card-widget-storyblok.html#power-deal', '5d. Power Deal') + '.')]) +
          figref(FIG_AH + '24811-112608', 'Power Deal Concept') +
          anat('an-disc', 'brand-discount', 'Anatomy of an image with graphic elements: 1 main graphic, 2 corner graphic') +
          legend([('1', 'Main graphic', 'A large graphic in the middle of the image, for example a campaign message such as a percentage, or a logo.'), ('2', 'Corner graphic', 'A smaller graphic bottom right, for example a brand logo or another graphic See ' + a('ah-group-card-widget-storyblok.html#brand-logo', '5c. Brand Logo') + '.')]) +
          figref(FIG_AH + '24811-112612', 'Graphic Elements')))

E.append(('usage', '<h2 class="ds-h2">Usage</h2>' + desc('A card can be used in many ways, depending on how the settings are combined. Guidance taken from the settings of the widget. See the ' + a('ah-group-card-widget-storyblok.html', 'Storyblok tab') + ' for each field.') +
          '<h3 class="ds-h3 ds-group">Do</h3>' + li(['Use Footer Padding, Footer Border and Card Size in the same way on every card in a group or a concept.', 'Use Card Size Small in a layout with many cards.', 'Use the action link in the first place; keep the button for the one action that must stand out.', 'Keep a card that leads to an article or a campaign direct: a short title and little text.', 'Use Full Stroke Border when the image could blend into the page background.']) +
          '<h3 class="ds-h3 ds-group">Do not</h3>' + li(['Mix cards with and without Footer Padding in one group.', 'Use long lists in a card. Cards in a row get the same height, so one tall card makes the others tall.', 'Turn on Active Card and add extra links on the same card.', 'Put brand elements in the footer. They belong on the image.'])))

JS_EX = r"""
  function box(img, W, H, x, y) { return function () { var r = img.getBoundingClientRect(); return { left: r.left + r.width * x / W, top: r.top + r.height * y / H, width: 0, height: 0 }; }; }
  function col(img) { return function (r) { return r.left - (img.getBoundingClientRect().left - 36); }; }   /* every badge in a figure sits in one column, 24px gap between badge and picture */
  function colR(img) { return function (r) { return img.getBoundingClientRect().right + 36 - (r.left + r.width); }; }
  function figs() {
    var a = $('#an-card-img'), p = $('#an-pd-img'), d = $('#an-disc-img');
    var AW = 589, AH = 816, BW = 589, BH = 331, ys = [165, 270, 36, 363, 393, 435, 515, 620, 707, 751, 779], xs = [10, 40, 25, 25, 25, 25, 25, 25, 25, 25, 25];   /* 2 = overlay: the dark left side of the image */
    DK.callouts($('#an-card'), ys.map(function (y, i) { return { n: String(i + 1), box: box(a, AW, AH, xs[i], y), side: 'left', len: col(a) }; }));
    DK.callouts($('#an-pd'), [{ n: '1', box: box(p, BW, BH, 50, 80), side: 'left', len: col(p) }, { n: '2', box: box(p, BW, BH, 300, 8), side: 'left', len: col(p) }, { n: '2', box: box(p, BW, BH, 200, 322), side: 'left', len: col(p) }]);
    DK.callouts($('#an-disc'), [{ n: '1', box: box(d, BW, BH, 190, 170), side: 'left', len: col(d) }, { n: '2', box: box(d, BW, BH, 520, 285), side: 'right', len: colR(d) }]);
  }
  var imgs = $$('.hb-anat img'), left = imgs.length;
  imgs.forEach(function (i) { if (i.complete) left--; else i.addEventListener('load', function () { if (--left === 0) figs(); }); });
  if (left === 0) figs();
"""

# SPECIFICATIONS: measures from the Figma frames (24811-111461 card, 24811-112608 Power Deal, 24811-112612 Graphic Elements) and the
# size/breakpoint matrix the user sent 2026-11-06. The values measured on UAT were checked against Figma by the user (2026-11-06) and match.
P = []
P.append(('card', '<h2 class="ds-h2">Card</h2>' + desc('The card is an image holder with a footer below it. Figma: ' + fig_link(FIG_AH + '24811-111461', 'Article Highlight Card', 'large') + ' (589px wide).') +
          table(['Part', 'Value'], [
              ['Image', 'Full width, aspect ratio 16:9 (589×331px in Figma)'],
              ['Background', '--color-background-primary'],
              ['Footer border (half stroke)', '1px --color-border-primary on the left, right and bottom of the footer'],
              ['Card border (full stroke)', '1px --color-border-primary around the whole card (setting Full Stroke Border)'],
              ['Corners', 'Sharp, no radius'],
          ])))

MARKS = ('<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b>')


def mitem(n, name, subject):
    """One item of a measurement figure: subject is the real markup with class measure__subject; measure.js reads its padding."""
    return '<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj">%s%s</div></div>' % (n, name, subject, MARKS)


def mfig(label, items, cap):
    return ('<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="%s">%s</div></div>'
            '<figcaption class="ds-fig__cap">%s</figcaption></figure></div>') % (label, ''.join(items), cap)


FOOT_INNER = ('<span class="ahm-pre">Preheadline</span><span class="ahm-title">Title</span><p class="ahm-body">Supporting text that gives a sense of length.</p>'
              '<span class="ahm-link">Action link <span class="mo-ic" aria-hidden="true">chevron_right</span></span>')
BP_TOOL = toolbar([('mb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')])
CAP_BP = ' Change the Breakpoint at the top of the section to see the mobile values.'

def warning(title, items):
    """Weak Warning inline notification (eco-inline-notification, notifications.css): a deviation in the build that the developers must fix."""
    body = '<span class="inline-notification__title">%s</span>' % title + '<ul class="ahw-list">' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
    return ('<div class="inline-notification inline-notification--warning inline-notification--weak ahw" role="note"><div class="inline-notification__base"><div class="inline-notification__left-border"></div>'
            '<div class="inline-notification__container"><div class="inline-notification__inner"><div class="inline-notification__header">'
            '<span class="material-symbols-outlined inline-notification__icon" aria-hidden="true">warning</span><div class="inline-notification__text">%s</div>'
            '</div></div></div></div></div>') % body


def lobj(cls, inner):
    """One block of the footer layout figure: the block is the subject, its padding-bottom is the space to the next block (as in Figma)."""
    return '<div class="measure__obj ahl-obj"><div class="%s measure__subject">%s</div>%s</div>' % (cls, inner, MARKS)


def layout(size):
    ch = '<span class="mo-ic" aria-hidden="true">chevron_right</span>'
    return ('<div class="ahl ahl--%s">' % size +
            lobj('ahl-pre', '<span>Preheadline</span><i class="ahl-divider" aria-hidden="true"></i><span>Preheadline</span>') +
            lobj('ahl-title', 'Title') +
            lobj('ahl-txt ahl-gap', 'Supporting text.') +
            lobj('ahl-list ahl-gap', '<span>List item level 1</span><span>Item</span><span>Item</span>') +
            lobj('ahl-txt ahl-gap', 'Supporting text.') +
            lobj('ahl-stack ahl-gap', '<span class="ahl-link">Text link ' + ch + '</span><span class="ahl-link">Text link ' + ch + '</span>') +
            lobj('ahl-divided ahl-end', '<span class="ahl-link">Text link ' + ch + '</span><i class="ahl-sep" aria-hidden="true"></i><span class="ahl-link">Text link ' + ch + '</span>') +
            lobj('ahl-date', 'Date') +
            '<div class="ahl-link ahl-last">Text link ' + ch + '</div></div>')


P.append(('measurements', '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('The footer padding: the space between the edge of the footer and its content. It is the same for both card sizes. All numbers in the figures are read from the parts themselves.') +
          BP_TOOL +
          mfig('Footer padding, with and without the setting Footer Padding', [
              mitem(1, 'Footer Padding on', '<div class="ahm-foot measure__subject">' + FOOT_INNER + '</div>'),
              mitem(2, 'Footer Padding off', '<div class="ahm-foot ahm-foot--flush measure__subject">' + FOOT_INNER + '</div>')],
              'The card footer at true size. Without Footer Padding only the space above the preheadline is left.' + CAP_BP) +
          table(['Footer Padding', 'Large (1024px+)', 'Medium (769–1023px)', 'Small (640–768px)', 'XSmall (0–639px)'], [
              ['On, all four sides', '24px', '24px', '24px', '16px'],
              ['Off, above the preheadline', '16px', '16px', '12px', '8px'],
              ['Off, sides and bottom', '0', '0', '0', '0'],
          ]) + desc('The same for the Large and the Small card, per ' + a(BP, 'breakpoint') + '.') +
          '<h3 class="ds-h3 ds-group">Footer layout</h3>' + warning('Deviations on UAT (2026-11-07)', ['Date: the letter spacing is 0.2px. Figma and alt-label-md say 0.64px on desktop and 0.56px on mobile.', 'Space above the date at XSmall: 16px on UAT and in the size matrix, 24px in the Figma component (Small-XSmall). The page shows 16px until the right value is decided.']) + desc('The whole footer with every part turned on, per card size, with the type and the space below each part. Figma: ' + fig_link(FIG_AH + '24857-13630', 'Article Highlight Group Card font settings', 'large') + '. The footer padding is left out here (see above).') +
          mfig('Footer layout of the Large and the Small card', ['<div class="measure__item"><span class="measure__name">%d · %s</span>%s</div>' % (i + 1, t, layout(z)) for i, (t, z) in enumerate([('Large card', 'lg'), ('Small card', 'sm')])], 'Type and spacing at true size.' + CAP_BP) +
          '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('Space between the parts of the footer. Each part carries the space below it, as in Figma: ' + fig_link(FIG_AH + '24857-13630', 'Article Highlight Group Card font settings', 'large') + '. The figure uses the type of the Small card.') +
          mfig('Space below each part of the card footer', [
              mitem(1, 'Preheadline', '<span class="ahm-blk ahm-pre measure__subject">Preheadline</span>'),
              mitem(2, 'Title', '<span class="ahm-blk ahm-title measure__subject">Title</span>'),
              mitem(3, 'Supporting text, Small card', '<p class="ahm-blk ahm-body ahm-body--gap measure__subject">Supporting text before a list.</p>'),
              mitem(4, 'Supporting text, Large card', '<p class="ahm-blk ahm-body ahm-body--gap ahm-body--lg measure__subject">Supporting text before a list.</p>'),
              mitem(5, 'List item', '<span class="ahm-blk ahm-li measure__subject"><span class="mo-ic" aria-hidden="true">check</span>List item</span>'),
              mitem(6, 'Text group, Small card', '<p class="ahm-blk ahm-body ahm-group measure__subject">The last text before the action link.</p>'),
              mitem(7, 'Text group, Large card', '<p class="ahm-blk ahm-body ahm-group ahm-group--lg measure__subject">The last text before the action link.</p>'),
              mitem(8, 'Date', '<span class="ahm-blk ahm-pre ahm-date measure__subject">Date</span>')],
              'The shaded area below each part is the space to the next part.' + CAP_BP) +
          table(['Between', 'Space'], [
              ['Preheadline and title', '8px'],
              ['Two preheadlines', '8px, with a 1px divider (border-primary) as high as the text: 16px desktop, 14px mobile'],
              ['Title and supporting text', '8px'],
              ['Supporting text, list, supporting text 2 and links', 'Large card 20px desktop; Small card 16px; both 16px mobile'],
              ['List items', '8px; bullet to text 8px'],
              ['Stacked links', '12px between links'],
              ['Divided links', '8px between links in a row, 12px between rows; divider 1×16px surface-20'],
              ['Link icon', 'Large card desktop: 24px, 8px to the text; otherwise 20px, 4px to the text'],
              ['Date and action link or button', '8px'],
              ['Button', 'The ECO ' + a('button.html', 'Button') + ', Primary, Small (40px desktop, 32px mobile); its own measures are on the Button page'],
          ]) +
          '<h3 class="ds-h3">Space above the date, action link or button</h3>' + desc('The space below the last text: above the date when there is one, otherwise above the action link or the button. From the size matrix in Figma.') +
          table(['Card size', 'Large (1024px+)', 'Medium (769–1023px)', 'Small (640–768px)', 'XSmall (0–639px)'], [
              ['Large', '32px', '32px', '24px', '16px'],
              ['Small', '24px', '24px', '24px', '16px'],
          ]) + desc('Cards in a row get the same height, so the action link moves to the bottom of the card and the space above it can be larger.') +
          '<h3 class="ds-h3 ds-group">Badge</h3>' + desc('The badge on the image.') +
          mfig('Padding of the badge', [mitem(1, 'Badge', '<span class="ahm-badge measure__subject">Nyhet</span>')], 'The badge at true size. It sits 24px from the top and left edge of the image.') ))

P.append(('typography', '<h2 class="ds-h2">Typography</h2>' + desc('Text styles in the footer per card size. The styles change size at 769px (see ' + a('../foundations/typography.html', 'Typography') + '). Figma: ' + fig_link(FIG_AH + '24857-13630', 'Article Highlight Group Card font settings', 'large') + ' (component ' + fig_link(FIG_AH + '20161-55854', 'Card / Base / Content', 'large') + ').') +
          table(['Part', 'Large card', 'Small card', 'Color'], [
              ['Preheadline', 'alt-label-md, uppercase (16/16, 14/14 mobile)', 'alt-label-md, uppercase (16/16, 14/14 mobile)', '--color-text-tertiary'],
              ['Title', 'headline-sm (28/32, 22/24 mobile)', 'title-lg (24/28, 20/24 mobile)', '--color-text-primary'],
              ['Supporting text, list, links', 'body-lg 20/28 desktop, body-md 16/22 mobile', 'body-md (17/24, 16/22 mobile)', '--color-text-primary'],
              ['Date', 'alt-label-md, uppercase (16/16, 14/14 mobile), letter spacing 0.64px (0.56px mobile)', 'alt-label-md, uppercase (16/16, 14/14 mobile), letter spacing 0.64px (0.56px mobile)', '--color-text-secondary'],
              ['Action link', 'As the supporting text, chevron 20px', 'As the supporting text, chevron 20px', '--color-text-primary'],
          ])))

P.append(('image-elements', '<h2 class="ds-h2">Image elements</h2>' + desc('Position and size of what sits on the image. Figma: ' + fig_link(FIG_AH + '24811-112608', 'Power Deal Concept', 'large') + ' and ' + fig_link(FIG_AH + '24811-112612', 'Graphic Elements', 'large') + '. Sizes are for a 589px wide card.') +
          table(['Element', 'Position', 'Size and style'], [
              ['Badge', '24px from the top and left', 'Padding 4px 5px, --color-surface-raised-primary, elevation-b-20, text 16/16 bold uppercase'],
              ['News badge', '16px from the top and right', '80×80px'],
              ['Overlay (Left)', 'Over the whole image', 'Black gradient, 60% at the left edge, 40% at 42%, transparent at 84%'],
              ['Power Deal logo', '32px from the left, 54px from the top', '143×72px'],
              ['Power Deal border', 'Top left and bottom right edge', '22px high'],
              ['Main graphic', 'Centred', '236×118px'],
              ['Corner graphic (brand logo)', 'About 24px from the bottom and right', '99×48px'],
          ])))

JS_SPEC = r"""
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });
"""

C = dict(
    slug=SLUG, title='Article Highlight Group Card', eyebrow='Components · Cards',
    lead='Cards that promote articles, campaigns and brands, placed in a grid or in a carousel. A card can have an image, logos and graphics, badges, text, links and a button.',
    select_menu=False, css=['badge', 'button', 'divider', 'inline-link'], pre_css=['../notifications.css?v=22'], style=STYLE,
    pages=[
        dict(kind='ex', suffix='', label='Examples & Guidelines', lead='The anatomy of the card, the brand elements and when to use them.', secs=E, js=JS_EX),
        dict(kind='spec', suffix='-specifications', label='Specifications', lead='Measures of the card, the footer, the text and the elements on the image, per card size and breakpoint, from Figma.', secs=P, js=JS_SPEC),
        dict(kind='sb', suffix='-storyblok', label='Storyblok', lead='How an editor adds and sets up the AH Group widget (Article Highlight Group) in Storyblok, and the settings of the AH Group Card. The numbers on the screenshots match the numbers in the headings.', secs=S),
    ])

if __name__ == '__main__':
    emit(C)
