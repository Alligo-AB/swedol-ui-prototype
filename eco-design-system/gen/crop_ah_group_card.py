"""Crop the AhGroupCard_* browser screenshots (images/, full browser windows) into the pictures of the AH Group Card Storyblok page
(images/ah-group-card-sb-*.webp, white background, WebP). Coordinates: see the P / PV / frac helpers. Run: python3 crop_ah_group_card.py (needs Pillow)."""
import os
import sys
from PIL import Image
IMG = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'images')) + '/'
OUT=sys.argv[1] if len(sys.argv)>1 else IMG
def load(n):
    im=Image.open(IMG+'AhGroupCard_%s.png'%n)
    bg=Image.new('RGB',im.size,'white'); bg.paste(im,mask=im.split()[3]); return bg
def save(name,im,maxw=1100):
    if im.width>maxw: im=im.resize((maxw,int(im.height*maxw/im.width)),Image.LANCZOS)
    im.save(OUT+'ah-group-card-sb-%s.webp'%name,quality=86,method=6); print(name,im.size)
def frac(n,name,x0,y0,x1,y1,**k):
    im=load(n); W,H=im.size; save(name,im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H))),**k)
def tile(n,name,xt0,yt0,xt1,yt1,**k):
    """panel contact-sheet coordinates (470px wide tile = crop .74W..965W, from .08H)"""
    im=load(n); W,H=im.size; s=470/(.225*W)
    save(name,im.crop((int(.74*W+xt0/s),int(.08*H+yt0/s),int(.74*W+xt1/s),int(.08*H+yt1/s))),**k)
def prev(n,name,xt0,yt0,xt1,yt1,k0=0,**k):
    """preview contact-sheet coordinates (900px wide tile = crop .02W..76W, from .07H)"""
    im=load(n); W,H=im.size; s=900/(.74*W)
    save(name,im.crop((int(.02*W+xt0/s),int(.07*H+yt0/s),int(.02*W+xt1/s),int(.07*H+yt1/s))),**k)
if __name__=='__main__':
    P=tile; PV=prev
    # --- panels (tile coords) ---
    P('6a','image-section',3,360,392,650)   # starts at the Image Section label: the Link field moved to the add-card picture
    P('6b','image-section-color',3,330,392,790)
    P('6c','image-color',3,400,392,830)
    P('6d','image-aspect',46,585,402,800)
    P('6d','lazyload-video',46,805,402,1095)
    P('8','overlay',30,735,404,1045)
    P('9','overlay-opacity',30,735,404,935)
    P('10','brand-logo',30,655,404,1170)
    P('11','power-deal',30,750,404,1110)
    P('12','news-badge',30,1118,404,1295)
    P('13','news-badge-label',30,1020,404,1190)
    P('14a','footer-settings',27,70,404,415)
    P('15a','footer-card-size',27,70,404,415)
    save('preheadline-title',Image.open(IMG+'AhGroupCard_35.png').convert('RGB'))   # Storyblok, Preheadline, Title and Supporting Text 1 (2026-11-04)
    save('supporting-text-2',Image.open(IMG+'AhGroupCard_36.png').convert('RGB'))   # Storyblok, Bulletlist Variant and Supporting Text 2 (2026-11-04)
    save('preheadline-card',Image.open(IMG+'AhGroupCard_30.png').convert('RGB').crop((0,0,507,812)))   # the first card (Bullet, 7d-1) of the three-card screenshot, to show the fields of 7a
    P('16a','bulletlist',27,80,404,520)
    P('16b','bulletlist-numbered',27,300,404,520)
    P('16c','bulletlist-checkmark',27,300,404,520)
    P('16a','links-date',27,700,404,940)
    P('16a','background-button',27,940,404,1330)
    P('17a','links-layout',27,225,404,640)
    P('17a','button-fields',27,860,404,1345)
    P('17b','inline-link-settings',27,70,404,430)
    P('18a','date-button',44,310,404,1075)
    P('18a','date-field',44,310,404,400)   # the Date field alone, for 7g. Date
    P('19a','links-pdf',-1,640,394,950)
    P('19a','stroke-border',-1,1070,394,1365)
    P('20a','background-color',-28,455,385,760)
    P('20a','button-settings',-28,762,385,1430)
    # --- panels (fractions) ---
    frac('1','section-add',.775,.162,.945,.527)
    frac('2','insert-block',.735,.104,.953,.945)
    frac('3','layout-options',.766,.428,.935,.655)
    frac('4','grid-columns',.766,.542,.935,.778)
    # add-card: the Add AH Group Card button on top, below it the Link field, the Active Card switch and its helper text of the new card
    def _crop(n,x0,y0,x1,y1):
        im=load(n); W,H=im.size; return im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
    top=_crop('4',.766,.753,.935,.86)
    link=load('3b').crop((24,40,800,445))   # Link field, Active Card switch and its helper text (Storyblok, 2026-11-03)
    link=link.resize((top.width,int(link.height*top.width/link.width)),Image.LANCZOS)
    gap=16; comp=Image.new('RGB',(top.width,top.height+gap+link.height),'white')
    comp.paste(top,(0,0)); comp.paste(link,(0,top.height+gap)); save('add-card',comp)
    save('brand-card',Image.open(IMG+'AhGroupCard_23.png').convert('RGB'),maxw=700)   # UAT page, card with only a logo (Gesto) and a full stroke border (2026-11-04)
    frac('22a','carousel-layout',.732,.53,.925,.903)
    frac('22b','carousel-slide-item',.727,.247,.93,.468)
    frac('22c','carousel-add-card',.727,.35,.93,.604)
    # --- whole-window pictures (no browser chrome) ---
    frac('21','grid-example',.10,.28,.70,.94,maxw=1300)
    frac('21','grid-columns-panel',.745,.20,.945,.62,maxw=700)
    frac('22d','carousel-card-fields',.745,.14,.945,.69,maxw=700)
    frac('22g','slide-two-cards',.08,.37,.72,.65,maxw=1300)
    frac('22g','slide-cards-panel',.737,.16,.945,.80,maxw=700)
    frac('22h','slide-two-rows',.08,.37,.72,.65,maxw=1300)
    frac('22h','slide-two-cards-panel',.737,.18,.945,.80,maxw=700)
    # UAT page Article-Highlight-Group-Card (2026-11-04): carousel with the next arrow; 31a has the arrow but also the mouse pointer, 31b is clean, so the pointer area is taken from 31b
    _p=Image.open(IMG+'AhGroupCard_31a.png').convert('RGB'); _q=Image.open(IMG+'AhGroupCard_31b.png').convert('RGB')
    _box=(478,384,512,422); _p.paste(_q.crop(_box),_box[:2])
    save('carousel-page-example',_p,maxw=1400)                          # with the heading and the link (9e)
    save('carousel-example',_p.crop((0,100,_p.width,_p.height)),maxw=1300)   # the cards, the arrow and the progress line
    # --- previews (preview coords) ---
    for n,nm in [('7','ratios'),('8','overlay-preview'),('9','overlay-opacity-preview'),('10','brand-logo-preview'),('11','power-deal-preview'),('12','news-badge-preview'),('13','news-badge-label-preview')]:
        PV(n,nm,115,178,655,385)
    save('footer-preview',Image.open(IMG+'AhGroupCard_33.png').convert('RGB'),maxw=1100)   # UAT /erik page: the left card without footer padding and border, the right one with both (2026-11-04)
    save('card-size-preview',Image.open(IMG+'AhGroupCard_34.png').convert('RGB'),maxw=1100)   # UAT /erik page: Card Size Small on the left, Large on the right, both with padding and border (2026-11-04)
    _b=Image.open(IMG+'AhGroupCard_30.png').convert('RGB'); _bc=Image.new('RGB',(_b.width+96,_b.height+96),'white'); _bc.paste(_b,(48,48)); save('bulletlist-preview',_bc,maxw=1100)   # UAT /erik page: three cards with a list (2026-11-04); 48px white around so the badges fit on the card borders
    PV('17c','links-preview',235,147,470,462)
    save('links-layout-preview',Image.open(IMG+'AhGroupCard_29.png').convert('RGB'),maxw=1100)   # UAT /erik page: Links Layout Divided and Stacked, one screenshot (2026-11-04)
    _a=Image.open(OUT+'ah-group-card-sb-links-preview.webp').convert('RGB')   # card with the button
    _n=Image.open(IMG+'AhGroupCard_26.png').convert('RGBA'); _bg=Image.new('RGB',_n.size,'white'); _bg.paste(_n,mask=_n.split()[3]); _n=_bg   # the same card without a button (2026-11-04)
    _a=_a.crop((41,40,811,1091))                                 # tight on the card border: 770x1051
    _n=_n.crop((43,54,811,1144))                                 # tight on the card border: 768x1090
    _n=Image.merge('RGB',[x for x in _n.split()])
    _n=_n.crop((0,0,_n.width,900)).copy(), _n.crop((0,940,_n.width,_n.height))   # cut 40px of the empty white below the links: both cards get the same height, as in a real card row
    _m=Image.new('RGB',(768,1050),'white'); _m.paste(_n[0],(0,0)); _m.paste(_n[1],(0,900)); _n=_m.resize((770,1051),Image.LANCZOS)
    _pad=16; _g=32
    _c=Image.new('RGB',(2*770+_g+2*_pad,1051+2*_pad),'white'); _c.paste(_a,(_pad,_pad)); _c.paste(_n,(_pad+770+_g,_pad)); save('links-preview-pair',_c,maxw=1100)
    _a=Image.open(IMG+'AhGroupCard_25a.png').convert('RGB'); _b=Image.open(IMG+'AhGroupCard_25b.png').convert('RGB')   # same two cards side by side, for 7g. Date
    _c=Image.new('RGB',(_a.width+_b.width+32,_a.height),'white'); _c.paste(_a,(0,0)); _c.paste(_b,(_a.width+32,0)); save('date-cards',_c,maxw=1100)
    _a=Image.open(IMG+'AhGroupCard_25a.png').convert('RGB'); _b=Image.open(IMG+'AhGroupCard_25b.png').convert('RGB')   # UAT /erik page: two cards with a date, one above the other (2026-11-04)
    _c=Image.new('RGB',(_a.width,_a.height+_b.height+16),'white'); _c.paste(_a,(0,0)); _c.paste(_b,(0,_a.height+16)); save('date-preview',_c,maxw=700)
    _sp=Image.open(IMG+'AhGroupCard_24.png').convert('RGB'); _sp=_sp.resize((1100,int(_sp.height*1100/_sp.width)),Image.LANCZOS)
    _sh=int(1100*584/782)   # same height as the settings picture beside it (782x584), white above and below
    _c=Image.new('RGB',(1100,_sh),'white'); _c.paste(_sp,(0,(_sh-_sp.height)//2)); save('stroke-preview',_c,maxw=1100)   # UAT /erik page, Milwaukee and Smart Service cards with Full Stroke Border (2026-11-04)
    save('background-preview',Image.open(IMG+'AhGroupCard_27.png').convert('RGB'),maxw=1100)   # UAT page, white and grey background rows (2026-11-04)
