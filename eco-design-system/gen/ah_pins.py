# pin positions (percent of the picture) for the Article Highlight Group Card Storyblok page: name -> [(label, x, y)]
# the labels are the numbers of the headings; x is the left edge column next to the field labels, y the label row; computed from the crop boxes of crop_ah_group_card.py
# (every crop starts about 40px before the labels, so the pin fits beside them; when a crop changes, y must be recomputed, y = label row in the crop box)
AH_PINS = {
 'image-section': [('4a', 5.1, 8.7)],
 'image-section-color': [('4b', 5.1, 80.7)],
 'image-color': [('4b', 5.1, 57.0)],
 'image-aspect': [('4c', 5.6, 11.2)],
 'lazyload-video': [('4d', 5.6, 8.3), ('4e', 5.6, 35.9), ('4e', 5.6, 78.3)],
 'overlay': [('5a', 5.3, 7.7), ('5b', 5.3, 78.1)],
 'overlay-opacity': [('5b', 5.3, 64.5)],
 'brand-logo': [('5c', 5.3, 7.0), ('5c', 5.3, 39.2), ('5c', 5.3, 71.3)],
 'power-deal': [('5d', 5.3, 6.7), ('5d', 5.3, 58.3)],
 'news-badge': [('5e', 5.3, 15.8), ('5e', 5.3, 62.1)],
 'news-badge-label': [('5e', 5.3, 13.5), ('5e', 5.3, 61.8)],
 'footer-settings': [('6a', 5.3, 8.4), ('6b', 5.3, 32.2), ('6c', 5.3, 55.9)],
 # footer-preview is used under 6a and under 6b: one pin set for each place (percent of the 1100x1000 picture)
 'footer-preview-6a': [('6a', 13.6, 33.8), ('6b', 93.6, 92.5), ('6c', 51.5, 79.0)],   # 6a in the footer text of the left card, 6b in the air of the right card, 6c on its border
 'footer-preview-6b': [('6b', 44.5, 93.0), ('6b', 93.6, 92.5)],   # the footer padding of both cards: none on the left, air on the right
 'card-size-preview': [('6d', 16.5, 34.0), ('6d', 65.8, 34.0)],   # 6d next to the text of each card
 'footer-card-size': [('6d', 5.3, 79.1)],
 'preheadline-title': [('7a', 3.4, 4.4), ('7b', 3.4, 46.9), ('7c-1', 41.0, 67.8)],
 'preheadline-card': [('7a', 27.6, 39.5), ('7b', 86.8, 44.0), ('7c-1', 92.3, 53.3)],   # the card of 7d-1: preheadline, title and supporting text (percent of the 507x812 crop)
 # 7c has two places for supporting text: Supporting Text 1 (7c-1, above the list) and Supporting Text 2 (7c-2, after the list)
 'supporting-text-2': [('7c-2', 40.0, 43.6)],
 'supporting-card': [('7c-1', 92.3, 53.3), ('7c-2', 47.3, 85.5)],   # on the card crop preheadline-card (507x812)
 'bulletlist': [('7d', 5.3, 6.4), ('7d-1', 5.3, 74.7)],   # the Bulletlist field and the chosen variant (Bullet); the variant pins match the cards in bulletlist-preview, in the same order
 'bulletlist-numbered': [('7d-3', 5.3, 64.6)],
 'bulletlist-checkmark': [('7d-2', 5.3, 79.8)],
 'links-date': [('7e', 5.3, 7.5), ('7f', 5.3, 67.5)],
 'background-button': [('8a', 5.3, 6.4), ('8b', 5.3, 32.8), ('8c', 5.3, 80.3)],
 'links-layout': [('7e', 5.3, 3.1), ('7e', 5.3, 64.1)],
 'button-fields': [('8b', 5.3, 4.5)],
 'inline-link-settings': [('7e', 5.3, 18.6), ('7e', 5.3, 48.3)],
 'date-field': [('7f', 5.6, 20.0)],
 'links-preview-pair': [('8b', 22.0, 90.2)],   # 8b next to the button of the left card (the right card has no button: Show Button off)
 'background-preview': [('8a', 2.8, 5.5), ('8a', 2.8, 55.0)],   # 8a on the left margin of each background (white band, grey band)
 'date-cards': [('7f', 25.6, 85.9), ('7f', 76.6, 82.9)],   # 7f to the right of the date text on each card
 'links-layout-preview': [('7e', 36.4, 74.2), ('7e', 74.3, 77.3)],   # 7e to the right of the links on each card (one pin per link group, so the stacked links do not get overlapping pins)
 'bulletlist-preview': [('7d-1', 33.6, 61.0), ('7d-2', 64.7, 61.0), ('7d-3', 94.0, 61.0)],   # 7d-1/-2/-3 on the right border of each card, between the list and the text below; the same label marks the chosen variant in the UI picture (1 Bullet, 2 Checkmark, 3 Numbered)
 'date-button': [('8d', 5.6, 64.8), ('8d', 5.6, 78.0)],
 'date-preview': [('8d', 55.9, 45.3), ('8d', 55.9, 94.9)],   # 8d next to the icon of the action link and of the button (same 8d as the two icon fields)
 'links-pdf': [('7e', 5.1, 5.5), ('7e', 5.1, 71.9)],
 # 8e on the lower left corner of each card that shows the border (stroke-preview: the Smart Service card only, the red Milwaukee card has no visible border; brand-card: one)
 'stroke-preview': [('8e', 51.7, 91.6)],
 'brand-card': [('8e', 6.0, 90.6)],
 'stroke-border': [('8e', 5.1, 71.9)],
 'background-color': [('8a', 4.8, 43.3)],
 'button-settings': [('8c', 4.8, 35.8)],
 'layout-options': [('1', 4.5, 55.3)],
 'grid-columns': [('2a', 4.5, 30.9), ('2b', 4.5, 87.2)],
 'add-card': [('3', 88.0, 42.0)],
 'carousel-layout': [('9a', 4.5, 58.2)],
 'carousel-slide-item': [('9b', 4.5, 83.5)],
 'carousel-add-card': [('9c', 4.5, 79.5)],
 'slide-cards-panel': [('9f', 4.5, 51.7)],
 'slide-two-cards-panel': [('9f', 4.5, 50.0)],
}
