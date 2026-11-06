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
    return '<a class="inline-link inline-link--large inline-link--secondary" href="%s">%s</a>' % (href, t)


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
# DESIGN (the main page of the set): anatomy, brand elements, variants. Pictures from Figma (images/ah-group-card-design-*.webp)
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
          anat('an-card', 'anatomy', 'Anatomy of an Article Highlight card: 1 image, 2 badge, 3 preheadline, 4 title, 5 supporting text, 6 list, 7 supporting text 2, 8 links, 9 date, 10 action link or button') +
          legend([
              ('1', 'Image', 'The image, a color or a video, with an optional overlay, brand elements and logo.'),
              ('2', 'Badge', 'A short label on the image, for example “Nyhet”.'),
              ('3', 'Preheadline', 'Also called eyebrow. It gives context.'),
              ('4', 'Title', 'The headline of the card.'),
              ('5', 'Supporting text 1', 'Body text before the list.'),
              ('6', 'Bulletlist', 'Bullet, numbered or checkmark list.'),
              ('7', 'Supporting text 2', 'Body text after the list.'),
              ('8', 'Links', 'Extra links, with or without icons, stacked or divided.'),
              ('9', 'Date', 'A date or another short, related note.'),
              ('10', 'Action link or button', 'The call to action of the card.')]) +
          '<h3 class="ds-h3 ds-group" id="brand-elements">Brand elements</h3>' + desc('Brand elements sit on the image, never in the footer. They are part of the picture, so they follow the image when it is cropped. The two examples show a campaign concept and a discount with a brand logo.') +
          anat('an-pd', 'brand-powerdeal', 'Anatomy of a Power Deal image: 1 Power Deal logo, 2 Power Deal border') +
          legend([('1', 'Power Deal logo', 'The logo of the Power Deal concept.'), ('2', 'Power Deal border', 'The graphic stripes at the top and bottom edge. Use it together with the logo.')]) +
          figref(FIG_AH + '24811-112608', 'Brand Elements 1') +
          anat('an-disc', 'brand-discount', 'Anatomy of a discount image: 1 discount, 2 brand logo') +
          legend([('1', 'Discount', 'A large, red campaign message, for example a percentage.'), ('2', 'Brand logo', 'For brand identity. It sits bottom right.')]) +
          figref(FIG_AH + '24811-112612', 'Brand Elements 2')))

E.append(('variants', '<h2 class="ds-h2">Variants</h2>' + desc('A card can be used in many ways, depending on how the settings are combined. The grid shows Large cards (left) and Small cards (right) with the same content, in four setups with and without footer padding, border and badge. See ' + a('ah-group-card-widget-storyblok.html#footer', '6. Card footer') + ' for the settings. Figma: ' + fig_link(FIG_AH + '549-27485', 'AH Highlight Card Variants', 'large') + '.') +
          '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage sb-stage"><div class="sb-shot"><img src="%s" alt="Four rows of cards. Each row shows two Large and two Small cards with an image, a preheadline, a title, a supporting text and a text link" loading="lazy" /></div></div></figure></div>' % (DIMG % 'variants')))

E.append(('usage', '<h2 class="ds-h2">Usage</h2>' + desc('Guidance taken from the settings of the widget. See the ' + a('ah-group-card-widget-storyblok.html', 'Storyblok tab') + ' for each field.') +
          '<h3 class="ds-h3 ds-group">Do</h3>' + li(['Use Footer Padding, Footer Border and Card Size in the same way on every card in a group or a concept.', 'Use Card Size Small in a layout with many cards.', 'Use the action link in the first place; keep the button for the one action that must stand out.', 'Keep a card that leads to an article or a campaign direct: a short title and little text.', 'Use Full Stroke Border when the image could blend into the page background.']) +
          '<h3 class="ds-h3 ds-group">Do not</h3>' + li(['Mix cards with and without Footer Padding in one group.', 'Use long lists in a card. Cards in a row get the same height, so one tall card makes the others tall.', 'Turn on Active Card and add extra links on the same card.', 'Put brand elements in the footer. They belong on the image.'])))

JS_EX = r"""
  function box(img, W, H, x, y) { return function () { var r = img.getBoundingClientRect(); return { left: r.left + r.width * x / W, top: r.top + r.height * y / H, width: 0, height: 0 }; }; }
  function col(img) { return function (r) { return r.left - (img.getBoundingClientRect().left - 36); }; }   /* every badge in a figure sits in one column, 24px gap between badge and picture */
  function colR(img) { return function (r) { return img.getBoundingClientRect().right + 36 - (r.left + r.width); }; }
  function figs() {
    var a = $('#an-card-img'), p = $('#an-pd-img'), d = $('#an-disc-img');
    var AW = 589, AH = 816, BW = 589, BH = 331, ys = [165, 36, 363, 393, 435, 515, 620, 707, 751, 779], xs = [10, 25, 25, 25, 25, 25, 25, 25, 25, 25];
    DK.callouts($('#an-card'), ys.map(function (y, i) { return { n: String(i + 1), box: box(a, AW, AH, xs[i], y), side: 'left', len: col(a) }; }));
    DK.callouts($('#an-pd'), [{ n: '1', box: box(p, BW, BH, 50, 80), side: 'left', len: col(p) }, { n: '2', box: box(p, BW, BH, 300, 8), side: 'left', len: col(p) }, { n: '2', box: box(p, BW, BH, 200, 322), side: 'left', len: col(p) }]);
    DK.callouts($('#an-disc'), [{ n: '1', box: box(d, BW, BH, 190, 170), side: 'left', len: col(d) }, { n: '2', box: box(d, BW, BH, 520, 285), side: 'right', len: colR(d) }]);
  }
  var imgs = $$('.hb-anat img'), left = imgs.length;
  imgs.forEach(function (i) { if (i.complete) left--; else i.addEventListener('load', function () { if (--left === 0) figs(); }); });
  if (left === 0) figs();
"""

C = dict(
    slug=SLUG, title='Article Highlight Group Card', eyebrow='Components · Cards',
    lead='Cards that promote articles, campaigns and brands, placed in a grid or in a carousel. A card can have an image, logos and graphics, badges, text, links and a button.',
    select_menu=False, css=['badge', 'button', 'divider', 'inline-link'], style=STYLE,
    pages=[
        dict(kind='ex', suffix='', label='Examples & Guidelines', lead='The anatomy of the card, the brand elements, the variants and when to use them.', secs=E, js=JS_EX),
        dict(kind='sb', suffix='-storyblok', label='Storyblok', lead='How an editor adds and sets up the AH Group widget (Article Highlight Group) in Storyblok, and the settings of the AH Group Card. The numbers on the screenshots match the numbers in the headings.', secs=S),
    ])

if __name__ == '__main__':
    emit(C)
