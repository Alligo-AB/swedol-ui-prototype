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
    P('6a','image-section',3,250,392,650)
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
    P('15a','preheadline-title',27,430,404,925)
    P('16a','bulletlist',27,80,404,520)
    P('16b','bulletlist-numbered',27,300,404,520)
    P('16c','bulletlist-checkmark',27,300,404,520)
    P('16a','links-date',27,700,404,940)
    P('16a','background-button',27,940,404,1330)
    P('17a','links-layout',27,225,404,640)
    P('17a','button-fields',27,860,404,1345)
    P('17b','inline-link-settings',27,70,404,430)
    P('18a','date-button',44,310,404,1075)
    P('19a','links-pdf',-1,640,394,950)
    P('19a','stroke-border',-1,1070,394,1365)
    P('20a','background-color',-28,455,385,760)
    P('20a','button-settings',-28,762,385,1430)
    # --- panels (fractions) ---
    frac('1','section-add',.775,.162,.945,.527)
    frac('2','insert-block',.735,.104,.953,.945)
    frac('3','layout-options',.766,.428,.935,.655)
    frac('4','grid-columns',.766,.542,.935,.778)
    frac('4','add-card',.766,.753,.935,.86)
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
    frac('22e','carousel-example',.06,.28,.93,.90,maxw=1300)
    frac('22f','carousel-page-example',.02,.17,.98,.97,maxw=1400)
    # --- previews (preview coords) ---
    for n,nm in [('7','ratios'),('8','overlay-preview'),('9','overlay-opacity-preview'),('10','brand-logo-preview'),('11','power-deal-preview'),('12','news-badge-preview'),('13','news-badge-label-preview')]:
        PV(n,nm,115,178,655,385)
    PV('14b','footer-preview',235,145,700,535)
    PV('15b','card-size-preview',235,145,700,550)
    PV('16a','bulletlist-preview',118,185,365,572)
    PV('17c','links-preview',235,147,470,462)
    PV('18b','date-preview',245,150,480,430)
    PV('19b','stroke-preview',215,155,705,490)
    frac('20b','background-preview',.08,.09,.99,.95,maxw=1400)
