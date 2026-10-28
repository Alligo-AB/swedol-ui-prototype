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
    .ds-prose > :is(.ds-h2, .ds-h3, .hb-h4, .ds-desc, .ds-bullets, .hb-note) + .ah-pair, .ds-prose > .ah-pair + :is(.ds-h2, .ds-h3, .hb-h4, .ds-desc, .ds-bullets, .hb-note, .hb-legend) { margin-top: var(--dimension-spacing-space-16); }
    .ds-prose > .ds-desc.ds-desc:has(+ .ah-pair), .ds-prose > .ds-bullets.ds-bullets:not(.ds-bullets--num):has(+ .ah-pair) { margin-bottom: 0; }
    .ah-pair.ds-figs { align-items: start; }
    .ds-prose > :is(.ds-figs, .ah-pair) + :is(.ds-figs, .ah-pair) { margin-top: var(--dimension-spacing-space-16); }
    .ds-prose > .ds-table-wrap + :is(.ds-desc, .ds-h3, .hb-note, .ds-figs, .ah-pair) { margin-top: var(--dimension-spacing-space-16); }   /* the table's own bottom edge: 16px to what follows */
    .ds-prose > :is(.ds-desc, .ds-bullets, .ds-figs, .ah-pair) + .ds-table-wrap { margin-top: var(--dimension-spacing-space-16); }
    .ds-prose > .ds-desc.ds-desc:has(+ .ds-table-wrap) { margin-bottom: 0; }
    code { font-size: 0.9em; }'''

IMG = '/images/ah-group-card-sb-%s.webp'
BP = '../foundations/layout-breakpoints.html'


def img(name, alt, box=None):
    inner = '<img src="%s" alt="%s" loading="lazy" />' % (IMG % name, alt)
    if box:
        inner += '<span class="sb-box" style="left:%s%%;top:%s%%;width:%s%%;height:%s%%"></span>' % box
    for lab, x, y in AH_PINS.get(name, []):   # the number of the heading next to the area it describes
        inner += '<span class="badge-number sb-pin" style="left:%s%%;top:%s%%">%s</span>' % (x, y, lab)
    return '<div class="ds-fig__stage sb-stage"><div class="sb-shot">%s</div></div>' % inner


def cap(c):
    return ('<figcaption class="ds-fig__cap">%s</figcaption>' % c) if c else ''


def shot(name, alt, c=None, box=None, narrow=True):
    """One picture of the Storyblok editor (a cropped settings panel is narrow, a page or a card preview is wide)."""
    return '<div class="ds-figs ds-figs--one"><figure class="ds-fig%s">%s%s</figure></div>' % (' ah-narrow' if narrow else '', img(name, alt, box), cap(c))


def pair(a, a_alt, b, b_alt, ca=None, cb=None):
    """Settings on the left, the result on the right (two columns from 769px)."""
    return '<div class="ds-figs ah-pair"><figure class="ds-fig">%s%s</figure><figure class="ds-fig">%s%s</figure></div>' % (img(a, a_alt), cap(ca), img(b, b_alt), cap(cb))


def dont(name, alt, c):
    return '<div class="ds-figs ds-figs--one"><figure class="ds-fig ds-fig--dont">%s<figcaption class="ds-fig__cap"><span class="ds-fig__ic" aria-hidden="true">cancel</span>%s</figcaption></figure></div>' % (img(name, alt), c)


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
          desc('Fill in <strong>Link</strong>, the URL of the card, at the top of the card. The button of the card (see ' + a('#show-button', '8b. Show Button') + ') becomes available when the URL is filled in.')))

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
          pair('footer-settings', 'The Footer Section, Footer Padding, Footer Border and Card Size fields', 'footer-preview', 'Two cards, the right one with footer padding and a border', 'Footer Section, Footer Padding and Footer Border on.', 'The right card with padding and border.') + \
          h3('footer-padding', '6b. Footer Padding') + desc('Gives the text in the footer padding, that is air around it. Use it in the same way on every card in a group of cards in a section, or in a concept. Do not mix cards with and without it.') +
          dont('footer-preview', 'Two cards, one with footer padding and a border and one without', 'Do not mix cards with and without Footer Padding in one group.') + \
          h3('footer-border', '6c. Footer Border') + desc('The border gives a more premium feel. Use it when Footer Padding is on. Do not use it with text unless the card has enough padding.') + \
          h3('card-size', '6d. Card Size') + desc('<strong>Large</strong> or <strong>Small</strong>. It sets the size of the text inside the card. The sizes are fixed and adapt to smaller screens: <strong>Large</strong> gets the same size as <strong>Small</strong> when the viewport reaches breakpoint-sm. In a layout with many cards, use <strong>Small</strong>.') +
          pair('footer-card-size', 'The Card Size field with the value Large', 'card-size-preview', 'Two cards, the left one Small and the right one Large', 'Card Size “Large”.', 'Left: Small. Right: Large.')))

S.append(('text', '<h2 class="ds-h2">7. Text content</h2>' + desc('The settings in this section appear when <strong>Footer Section</strong> is on.') + \
          h3('preheadline', '7a. Preheadline') + desc('Also called eyebrow or pre title. It categorises the content or adds context. It is optional, but use it in the same way in a group of cards or in a concept. Write one item per line. The items are shown next to each other with a divider.') +
          shot('preheadline-title', 'The Preheadline, Title and Supporting Text 1 fields in Storyblok', 'Preheadline, Title and Supporting Text 1.') + \
          h3('title', '7b. Title') + desc('The descriptive headline of the card. It is often the most important part of a card.') + \
          h3('supporting-text-1', '7c. Supporting Text 1') + desc('Space for body text.') + \
          h3('bulletlist', '7d. Bulletlist') + desc('Write one item per line. There are three kinds of lists: <strong>Bullet</strong>, <strong>Numbered</strong> and <strong>Checkmark</strong>. Use lists sparingly in a card. They take a lot of space, and cards in the same row get the same height, so a card with little content gets the height of the cards with more. A card that leads to a full article or a campaign should be direct.') +
          pair('bulletlist', 'The Bulletlist and Bulletlist Variant fields in Storyblok', 'bulletlist-preview', 'A card with a bullet list', 'Bulletlist and Bulletlist Variant.', 'Variant “Bullet”.') +
          pair('bulletlist-numbered', 'The Bulletlist Variant field with Numbered chosen', 'bulletlist-checkmark', 'The Bulletlist Variant field with Checkmark chosen', 'Variant “Numbered”.', 'Variant “Checkmark”.') + \
          h3('supporting-text-2', '7e. Supporting Text 2') + desc('Space for body text after a list.') + \
          h3('links', '7f. Links') + desc('Add more links, with or without icons, that help the user to do a task or give context. Add them with <strong>Add Inline link</strong>. <strong>Links Layout</strong> is <strong>Stacked</strong> or <strong>Divided</strong>. Stacked gives a more separated look. Divided saves space.') +
          pair('links-layout', 'The Links list and the Links Layout field with Stacked and Divided', 'links-preview', 'A card with the divided links “Glömt lösenord?” and “Bli kund”', 'Links and Links Layout.', 'Links Layout “Divided”.') +
          pair('links-pdf', 'The Links list with a link to a PDF and the Links Layout “Stacked”', 'inline-link-settings', 'The settings of an inline link: icon before, icon after and target', 'A link with Links Layout “Stacked”.', 'The settings of one link.') + \
          h3('date', '7g. Date') + desc('Meant first of all to show a date clearly, for example when a campaign ends or the last day to sign up. It can also be used for another short clarification.')))

S.append(('button', '<h2 class="ds-h2">8. Background and button</h2>' + \
          h3('background-color', '8a. Background Color') + desc('Changes the color of the footer of the card, <strong>White</strong> or <strong>Grey</strong>. Useful when the cards are placed on different backgrounds.') +
          pair('background-color', 'The Background Color field with the options White and Grey', 'background-preview', 'Cards on a white and a grey background', 'Background Color.', 'Cards with a grey footer on a grey background.') + \
          h3('show-button', '8b. Show Button') + desc('The option becomes available when the URL of the card is filled in. Then you fill in <strong>Button Label</strong> and choose the type.') +
          pair('button-fields', 'The Show Button, Button Label, Button Type and Button Icon fields', 'links-preview', 'A card with the button “Logga in”', 'The button fields.', 'A card with a primary button.') + \
          h3('button-type', '8c. Button Type') + desc('Choose the container of the call to action: a button or an action link. Use the action link in the first place.') +
          shot('button-settings', 'The Button Label, Button Type and Button Icon fields in Storyblok', 'Button Type “Primary”.') + \
          h3('button-icons', '8d. Button Icon Before and Button Icon After') + desc('Use icons to strengthen the message or the call to action. A calm icon, like the arrow, helps an action link without taking over.') +
          pair('date-button', 'The Date, Button and Button Icon fields with the icon Percent discount', 'date-preview', 'A card with a date and the button “Utforska kampanjen” with an icon', 'The Date and the button settings.', 'A card with a date and a button with an icon.') + \
          h3('full-stroke-border', '8e. Full Stroke Border') + desc('A border that frames the whole card. It overrides the Footer Border. Use it when the background of the image could blend into the background of the page, for a better frame. Switch it on when the footer border is off, to keep the hover effect on the image holder.') +
          pair('stroke-border', 'The Full Stroke Border switch with the note that it overrides the Footer Border', 'stroke-preview', 'Two cards with a border around the whole card', 'Full Stroke Border on.', 'The result.')))

S.append(('carousel', '<h2 class="ds-h2">9. Carousel</h2>' + desc('Choose <strong>Carousel</strong> as the Layout (see ' + a('#layout', '1. Layout') + '). The cards are then placed in slides.') + \
          h3('carousel-slides', '9a. Carousel Slides') + desc('Choose how many cards are shown at once in the first view of the carousel, <strong>2 to 5</strong>. The default is 5.') +
          shot('carousel-layout', 'The Layout field set to Carousel and the Carousel Slides field with the options 5, 4, 3 and 2', 'Carousel Slides.') + \
          h3('slide-item', '9b. Add a slide') + desc('Add a slide with <strong>Add AH Group Slide Item</strong> under Slides.') +
          shot('carousel-slide-item', 'The Slides list with the Add AH Group Slide Item button', 'Add AH Group Slide Item.') + \
          h3('slide-card', '9c. Add a card') + desc('Open the slide and add a card with <strong>Add AH Group Card</strong> under Cards.') +
          shot('carousel-add-card', 'A slide item with the Cards list and the Add AH Group Card button', 'Add AH Group Card in the slide.') + \
          h3('carousel-card', '9d. The card') + desc('After that the work is as usual. Continue with ' + a('#image-section', '4. Image') + '.') +
          shot('carousel-card-fields', 'The fields of an AH Group Card inside a slide', 'The card in a slide.') +
          shot('carousel-example', 'Three cards in a carousel', 'Cards in a carousel.', narrow=False) + \
          h3('carousel-heading', '9e. Title, Supporting Title, Navigation Text and Link') + desc('A carousel can have its own heading: <strong>Title</strong> and <strong>Supporting Title</strong> above the cards. <strong>Navigation Text</strong> and <strong>Link</strong> give a link next to the title, for example to a knowledge base.') +
          shot('carousel-page-example', 'A carousel with the heading Guider & artiklar, a supporting text and the link Mer i kunskapsbanken', 'A carousel with a heading and a link.', narrow=False) + \
          h3('two-rows', '9f. Two rows') + desc('Each slide item can hold <strong>two cards</strong>, one over the other. Then the carousel gets two rows.') +
          pair('slide-cards-panel', 'A slide item with one card', 'slide-two-cards', 'A carousel where the first slide has one card that fills the height', 'A slide with one card.', 'The first slide has one card.') +
          pair('slide-two-cards-panel', 'A slide item with two cards', 'slide-two-rows', 'A carousel where the first slide has two cards, one over the other', 'A slide with two cards.', 'Two cards in the first slide.')))

C = dict(
    slug=SLUG, title='Article Highlight Group Card', eyebrow='Components · Cards',
    lead='Cards that promote articles, campaigns and brands, placed in a grid or in a carousel. A card can have an image, logos and graphics, badges, text, links and a button.',
    select_menu=False, css=['badge', 'button', 'divider', 'inline-link'], style=STYLE,
    pages=[
        dict(kind='sb', suffix='-storyblok', label='Storyblok', lead='How an editor adds and sets up the AH Group widget (Article Highlight Group) in Storyblok, and the settings of the AH Group Card. The numbers on the screenshots match the numbers in the headings.', secs=S),
    ])

if __name__ == '__main__':
    emit(C)
