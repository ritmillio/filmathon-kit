#!/usr/bin/env python3
"""First 6 seconds (S1 Birth) of "A Life in One Room", built on the designer's room sketch.

Test render for direction only: placeholder items are drawn in code. The real items come from the designer.
  python3 first6.py stills 0.5 1.8 3.3 5.5     -> PNG stills in ./stills
  python3 first6.py render out.mp4             -> silent video, 24 fps held on twos
"""
import math, random, subprocess, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H, FPS, SS = 1920, 1080, 24, 2
SECS = 6.0

def hx(h): return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], dtype=np.float32) / 255
PAL = {k: hx(v) for k, v in dict(navy='#0f1d44', ultra='#2a4a8f', snow='#a9c1e6', frost='#dce8f8',
                                  gold='#e0a42b', amber='#f3c98b', brown='#6b3f17', wood='#c58a45').items()}
def mixc(a, b, t): return a * (1 - t) + b * t
def dark(c, k=0.45): return c * (1 - k)
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def sstep(a, b, x):
    u = clamp((x - a) / (b - a)); return u * u * (3 - 2 * u)
def backout(u):
    c1 = 1.70158; c3 = c1 + 1; return 1 + c3 * (u - 1) ** 3 + c1 * (u - 1) ** 2
def rgba(c, a=255): return tuple(int(clamp(float(x)) * 255) for x in c) + (a,)

# ---------------------------------------------------------------- geometry from the sketch
BACK_L, BACK_R = 515, 1410
BASE_Y = 714
FLOOR_L, FLOOR_R = (0, 1072), (1920, 1075)
WIN_GLASS = [(597, 0), (1312, 0), (1312, 488), (600, 488)]
WIN_FRAME = [(566, 0), (1345, 0), (1360, 508), (572, 508)]
SILL = [(557, 490), (1378, 490), (1378, 538), (557, 538)]
RUG = [(640, 835), (1245, 830), (1370, 992), (472, 1003)]
PATCHES = [
    [(545, 1005), (520, 975), (560, 915), (615, 860), (640, 835), (672, 845), (668, 900), (630, 960), (585, 995)],
    [(772, 968), (778, 880), (790, 850), (830, 840), (870, 838), (872, 900), (860, 960), (830, 992), (795, 1003), (772, 990)],
    [(1000, 1020), (1002, 965), (1005, 900), (1020, 853), (1050, 850), (1068, 880), (1070, 960), (1055, 1015), (1030, 1022)],
    [(1208, 838), (1235, 840), (1280, 900), (1305, 950), (1295, 990), (1272, 1020), (1255, 985), (1235, 930), (1215, 880)],
]
CRADLE_POS = (905, 975)
BEAR_POS = (1135, 500)
LAMP_POS = (350, 985)

def poly_mask(pts, blur=0):
    im = Image.new('L', (W, H), 0)
    ImageDraw.Draw(im).polygon(pts, fill=255)
    if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
    return np.asarray(im, dtype=np.float32) / 255

def lerp_pt(a, b, u): return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)

def build():
    rng = np.random.default_rng(7)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    back = poly_mask([(BACK_L, 0), (BACK_R, 0), (BACK_R, BASE_Y), (BACK_L, BASE_Y)])
    left = poly_mask([(0, 0), (BACK_L, 0), (BACK_L, BASE_Y), FLOOR_L])
    right = poly_mask([(BACK_R, 0), (W, 0), (W, FLOOR_R[1]), (BACK_R, BASE_Y)])
    floor = np.clip(1 - back - left - right, 0, 1)
    c_back = mixc(PAL['navy'], PAL['ultra'], 0.45)
    c_side = mixc(PAL['navy'], PAL['ultra'], 0.22)
    c_floor = mixc(PAL['wood'] * 0.30, PAL['navy'], 0.42)
    img = back[..., None] * c_back + left[..., None] * c_side + right[..., None] * c_side + floor[..., None] * c_floor
    # wall gradient: darker toward the top, soft pool of light below the window
    g = 0.72 + 0.28 * np.clip(yy / 700, 0, 1)
    img *= np.where(floor > 0.5, 1.0, g)[..., None]
    # window glass: night sky gradient, moon glow, stars
    glass = poly_mask(WIN_GLASS)
    t = np.clip(yy / 488, 0, 1)[..., None]
    sky = mixc(PAL['navy'], PAL['ultra'], t * 0.9)
    moon = np.exp(-(((xx - 1190) / 170) ** 2 + ((yy - 140) / 150) ** 2))[..., None]
    sky = sky + PAL['snow'] * moon * 0.30
    for _ in range(26):
        sx, sy = rng.uniform(620, 1290), rng.uniform(20, 470)
        r = rng.uniform(1.5, 3.2)
        sky += PAL['frost'] * np.exp(-(((xx - sx) ** 2 + (yy - sy) ** 2) / (r * r)))[..., None] * 0.5
    img = img * (1 - glass[..., None]) + sky * glass[..., None]
    frame_m = np.clip(poly_mask(WIN_FRAME) - glass, 0, 1)
    c_frame = mixc(PAL['wood'], PAL['navy'], 0.55) * 0.95
    img = img * (1 - frame_m[..., None]) + c_frame * frame_m[..., None]
    for x0, x1 in ((946, 964),):
        m = poly_mask([(x0, 0), (x1, 0), (x1, 492), (x0, 492)])
        img = img * (1 - m[..., None]) + c_frame * m[..., None]
    for y0, y1 in ((256, 285),):
        m = poly_mask([(600, y0), (1312, y0), (1312, y1), (600, y1)])
        img = img * (1 - m[..., None]) + c_frame * m[..., None]
    sillm = poly_mask(SILL)
    c_sill = mixc(PAL['wood'], PAL['snow'], 0.18) * 0.62
    img = img * (1 - sillm[..., None]) + c_sill * sillm[..., None]
    # rug: seven stripes in perspective
    for k in range(7):
        a0, a1 = k / 7, (k + 1) / 7
        q = [lerp_pt(RUG[0], RUG[1], a0), lerp_pt(RUG[0], RUG[1], a1), lerp_pt(RUG[3], RUG[2], a1), lerp_pt(RUG[3], RUG[2], a0)]
        col = mixc(PAL['ultra'], PAL['navy'], 0.30) if k % 2 == 0 else mixc(PAL['ultra'], PAL['snow'], 0.10) * 0.85
        m = poly_mask(q)
        img = img * (1 - m[..., None]) + col * m[..., None]
    # painted brush streaks, about -12 degrees
    tex_im = Image.new('L', (W, H), 128)
    td = ImageDraw.Draw(tex_im)
    ang = math.radians(-12)
    for _ in range(2600):
        x, y = rng.uniform(-100, W), rng.uniform(-100, H)
        L = rng.uniform(220, 820); wd = int(rng.uniform(14, 46))
        v = int(128 + rng.uniform(-40, 40))
        td.line([(x, y), (x + L * math.cos(ang), y + L * math.sin(ang))], fill=v, width=wd)
    tex_im = tex_im.filter(ImageFilter.GaussianBlur(3))
    tex = (np.asarray(tex_im, dtype=np.float32) - 128) / 128
    # warm-lit version of the plate
    lum = (img[..., 0] * 0.3 + img[..., 1] * 0.59 + img[..., 2] * 0.11)[..., None]
    warm_tone = lum * PAL['amber'] * 3.4 + PAL['wood'] * 0.06
    lit = np.clip(img * 0.22 + warm_tone * 0.78 + PAL['gold'] * 0.05, 0, 1)
    # warm light entering from the open door, off frame to the right
    wedge = poly_mask([(W, 775), (W, 1080), (430, 1045), (560, 880)], blur=34)
    wall_glow = np.clip((xx - 1250) / 670, 0, 1) ** 1.3 * np.clip(back + right, 0, 1) * 0.75
    M = np.maximum(wedge, wall_glow).astype(np.float32)
    # the four light patches from the sketch, with a painted irregular edge
    pm = Image.new('L', (W, H), 0)
    pd = ImageDraw.Draw(pm)
    for poly in PATCHES:
        jp = [(x + rng.uniform(-5, 5), y + rng.uniform(-5, 5)) for x, y in poly]
        pd.polygon(jp, fill=255)
    pm = pm.filter(ImageFilter.GaussianBlur(2.2))
    patch = np.asarray(pm, dtype=np.float32) / 255
    # lamp glow
    G = np.exp(-(((xx - LAMP_POS[0]) / 260) ** 2 + ((yy - 810) / 230) ** 2)).astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    vig = (1 - 0.30 * np.clip(r, 0, 1.4) ** 2).astype(np.float32)
    return dict(cold=img.astype(np.float32), lit=lit.astype(np.float32), M=M, patch=patch, G=G, tex=tex, vig=vig)

# ---------------------------------------------------------------- lines and shapes (drawn at 2x, jittered every drawing)
def jline(d, pts, col, w, rnd, amp=1.6, step=45):
    out = []
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        for k in range(n):
            u = k / n
            out.append((x0 + (x1 - x0) * u + rnd.uniform(-amp, amp), y0 + (y1 - y0) * u + rnd.uniform(-amp, amp)))
    out.append((pts[-1][0] + rnd.uniform(-amp, amp), pts[-1][1] + rnd.uniform(-amp, amp)))
    d.line([(x * SS, y * SS) for x, y in out], fill=col, width=max(1, int(w * SS)), joint='curve')

def draw_room_lines(rnd):
    im = Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    arch = (8, 16, 44, 215)
    wood = (46, 30, 22, 235)
    for pts in ([(519, 0), (513, 712)], [(1410, 0), (1408, 712)], [(508, 713), (1396, 717)],
                [(508, 713), (0, 1072)], [(1410, 713), (1920, 1075)]):
        jline(d, pts, arch, 4, rnd)
    for pts in ([(566, 0), (572, 508)], [(597, 0), (600, 488)], [(1342, 0), (1360, 508)], [(1312, 0), (1312, 488)],
                [(947, 0), (947, 495)], [(963, 0), (963, 495)], [(600, 257), (1312, 257)], [(600, 285), (1312, 285)],
                [(557, 490), (1378, 490), (1378, 538), (557, 538), (557, 490)], [(570, 506), (1362, 506)]):
        jline(d, pts, wood, 4, rnd, amp=1.3)
    jline(d, RUG + [RUG[0]], (14, 24, 60, 230), 4, rnd)
    for k in range(1, 7):
        jline(d, [lerp_pt(RUG[0], RUG[1], k / 7), lerp_pt(RUG[3], RUG[2], k / 7)], (14, 24, 60, 150), 2.5, rnd)
    # floorboards fanning from a vanishing point, drawn as broken dashes
    vp = (960, 380)
    for xb in range(-400, 2400, 150):
        for s in np.arange(0.0, 1.0, 0.11):
            if rnd.random() < 0.35: continue
            y0 = BASE_Y + (1080 - BASE_Y) * s; y1 = y0 + 34
            x0 = vp[0] + (xb - vp[0]) * (y0 - vp[1]) / (1080 - vp[1]); x1 = vp[0] + (xb - vp[0]) * (y1 - vp[1]) / (1080 - vp[1])
            xl = 508 - (y0 - 713) * (508 / 359); xr = 1410 + (y0 - 713) * (510 / 362)
            if xl + 6 < x0 < xr - 6 and not (RUG[0][0] - 10 < x0 < RUG[2][0] + 10 and 826 < y0 < 1006):
                jline(d, [(x0, y0), (x1, y1)], (8, 16, 40, 120), 2.2, rnd, amp=0.8, step=60)
    return im

def T(pts, ox, oy, sx, sy, rot):
    c, s = math.cos(rot), math.sin(rot); out = []
    for x, y in pts:
        x *= sx; y *= sy
        out.append((ox + x * c - y * s, oy + x * s + y * c))
    return out

def rotp(pts, px, py, ang):
    c, s = math.cos(ang), math.sin(ang)
    return [(px + (x - px) * c - (y - py) * s, py + (x - px) * s + (y - py) * c) for x, y in pts]

def ell(cx, cy, rx, ry, n=30, a0=0.0, a1=2 * math.pi, rot=0.0):
    out = []
    for i in range(n + (0 if abs(a1 - a0 - 2 * math.pi) < 1e-6 else 1)):
        a = a0 + (a1 - a0) * i / n
        x, y = rx * math.cos(a), ry * math.sin(a)
        out.append((cx + x * math.cos(rot) - y * math.sin(rot), cy + x * math.sin(rot) + y * math.cos(rot)))
    return out

def shape(d, pts, fill, rnd, w=3.2, amp=1.1):
    pts = [(x + rnd.uniform(-amp, amp), y + rnd.uniform(-amp, amp)) for x, y in pts]
    P = [(x * SS, y * SS) for x, y in pts]
    d.polygon(P, fill=rgba(fill))
    d.line(P + [P[0]], fill=rgba(dark(fill)), width=int(w * SS), joint='curve')

# ---------------------------------------------------------------- items (placeholders, drawn by code)
def pop(t, t0, dur=0.42):
    if t < t0: return None
    u = clamp((t - t0) / dur); s = backout(u); k = math.sin(u * math.pi) * 0.16
    return s * (1 + k), s * (1 - k)

def draw_items(t, rnd, L):
    im = Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    dim = lambda c: mixc(c, PAL['navy'], 0.62 * (1 - L))
    # ---- lamp (always there, eyes closed until 4.0 s)
    lo = sstep(4.0, 4.28, t) * (1 - 0.9 * (sstep(5.15, 5.22, t) - sstep(5.3, 5.38, t)))
    lean = 0.07 * sstep(4.7, 5.3, t)
    br = 1 + 0.012 * math.sin(t * 2 * math.pi)
    lx, ly = LAMP_POS; ls = 1.05
    base = ell(0, -8, 48, 11)
    stem = [(-6, -10), (6, -10), (5, -112), (-5, -112)]
    shade = [(-58, -112), (58, -112), (38, -196), (-38, -196)]
    shade_col = dim(PAL['amber']); wood_col = dim(PAL['wood'] * 0.8)
    shape(d, T(base, lx, ly, ls, ls * br, lean), wood_col, rnd)
    shape(d, T(stem, lx, ly, ls, ls * br, lean), wood_col, rnd)
    shape(d, T(shade, lx, ly, ls, ls * br, lean), shade_col, rnd)
    for ex in (-18, 18):
        if lo < 0.12:
            arc = ell(ex, -156, 11, 7, n=12, a0=0.15, a1=math.pi - 0.15)
            jline(d, T(arc, lx, ly, ls, ls * br, lean), rgba(dark(shade_col, 0.6)), 3, rnd, amp=0.4, step=12)
            continue
        eye = ell(ex, -152, 12, 12)
        shape(d, T(eye, lx, ly, ls, ls * br, lean), dim(PAL['frost']), rnd, w=2.4)
        px = ex + 4 * sstep(4.7, 5.3, t); py = -152 + 2 * sstep(4.7, 5.3, t)
        shape(d, T(ell(px, py, 5.5, 5.5, n=16), lx, ly, ls, ls * br, lean), dim(PAL['navy']), rnd, w=1.6, amp=0.4)
        lid_h = 24 * (1 - lo)
        if lid_h > 0.6:
            lid = [(ex - 13, -165), (ex + 13, -165), (ex + 13, -165 + lid_h), (ex - 13, -165 + lid_h)]
            shape(d, T(lid, lx, ly, ls, ls * br, lean), shade_col, rnd, w=2.6, amp=0.5)
    # ---- cradle (pops 2.2 s), blanket (2.9 s), mobile (2.6 s)
    cp = pop(t, 2.2)
    if cp:
        sx, sy = cp
        rock = 0.0
        if t >= 3.0:
            rock = 0.055 * math.exp(-(t - 3.0) * 0.55) * math.sin((t - 3.0) * 7.0)
            sy *= 1 + 0.07 * math.exp(-(t - 3.0) * 9) * math.sin((t - 3.0) * 30)
        cx, cy = CRADLE_POS
        wood = dim(mixc(PAL['wood'], PAL['navy'], 0.18)); wood_d = dim(PAL['wood'] * 0.62)
        hood_c = dim(mixc(PAL['ultra'], PAL['snow'], 0.30))
        rocker = ell(0, -6, 176, 15)
        basket = [(-152, -18), (0, -6), (152, -18), (184, -108), (0, -102), (-184, -108)]
        hood = ell(-98, -104, 88, 84, n=26, a0=math.pi, a1=2 * math.pi)
        shape(d, T(rocker, cx, cy, sx, sy, rock), wood_d, rnd)
        shape(d, T(hood, cx, cy, sx, sy, rock), hood_c, rnd)
        shape(d, T(basket, cx, cy, sx, sy, rock), wood, rnd)
        trim = [(-176, -88), (176, -88), (184, -108), (-184, -108)]
        shape(d, T(trim, cx, cy, sx, sy, rock), dim(PAL['ultra']), rnd, w=2.4)
        bp = pop(t, 2.9, 0.4)
        if bp:
            bs = bp[0]
            bump = ell(40, -108, 118, 34, n=26, a0=math.pi, a1=2 * math.pi)
            bump = [(x * bs, (y + 108) * bs - 108) for x, y in bump]
            shape(d, T(bump, cx, cy, sx, sy, rock), dim(PAL['frost'] * 0.94), rnd)
            fold = ell(60, -112, 70, 14, n=18, a0=math.pi, a1=2 * math.pi)
            fold = [(x * bs, (y + 112) * bs - 112) for x, y in fold]
            jline(d, T(fold, cx, cy, sx, sy, rock), rgba(dark(dim(PAL['frost']))), 2.4, rnd, amp=0.6, step=30)
        mp = pop(t, 2.6, 0.45)
        if mp:
            ms = mp[0]
            sway = 0.0 if t < 3.0 else 0.18 * math.exp(-(t - 3.0) * 0.35) * math.sin((t - 3.0) * 4.6)
            pole = [(150, -110), (150, -300), (110, -338), (30, -338)]
            pole = [(150 + (x - 150) * ms, -110 + (y + 110) * ms) for x, y in pole]
            for a in range(len(pole) - 1):
                jline(d, T([pole[a], pole[a + 1]], cx, cy, sx, sy, rock), rgba(dark(dim(PAL['wood']))), 5, rnd, amp=0.8, step=30)
            hangs = [(40, 'gold', 62), (78, 'frost', 84), (112, 'snow', 56)]
            for hx_, col, ln in hangs:
                px_, py_ = 40 + (hx_ - 40) * ms, -338 + 0
                s1 = (px_, py_); s2 = (px_, py_ + ln * ms)
                ang = sway * (1 + hx_ / 200)
                pts2 = rotp([s1, s2], s1[0], s1[1], ang)
                jline(d, T(pts2, cx, cy, sx, sy, rock), rgba(dark(dim(PAL['wood']))), 2.6, rnd, amp=0.5, step=30)
                end = pts2[1]
                if col == 'gold':
                    sh = [(end[0], end[1] - 8 * ms), (end[0] + 14 * ms, end[1] + 10 * ms), (end[0], end[1] + 28 * ms), (end[0] - 14 * ms, end[1] + 10 * ms)]
                elif col == 'frost':
                    sh = ell(end[0], end[1] + 10 * ms, 13 * ms, 13 * ms, n=18)
                else:
                    sh = ell(end[0], end[1] + 10 * ms, 15 * ms, 11 * ms, n=18, rot=0.5)
                shape(d, T(sh, cx, cy, sx, sy, rock), dim(PAL[col]), rnd, w=2.4, amp=0.6)
    # ---- teddy bear: set on the sill at 3.7 s with a soft plop
    if t >= 3.4:
        u = clamp((t - 3.4) / 0.30)
        drop = 150 * (1 - u * u) if u < 1 else 0.0
        sq = 0.0
        if t >= 3.7: sq = 0.17 * math.exp(-(t - 3.7) * 6.5) * math.cos((t - 3.7) * 14)
        sx_, sy_ = 0.86 * (1 + sq * 0.8), 0.86 * (1 - sq)
        breath = 1 + 0.012 * math.sin((t - 3.7) * 2 * math.pi)
        sy_ *= breath
        bx, by = BEAR_POS; by = by - drop
        tilt = -0.14 * sstep(4.3, 5.0, t)
        fur = PAL['wood']; fur_l = PAL['amber']; fur_d = PAL['wood'] * 0.82
        T_ = lambda p: T(p, bx, by, sx_, sy_, 0.0)
        shape(d, T_(ell(-30, -14, 23, 15)), fur_d, rnd)
        shape(d, T_(ell(30, -14, 23, 15)), fur_d, rnd)
        shape(d, T_(ell(0, -54, 43, 45)), fur, rnd)
        shape(d, T_(ell(0, -48, 25, 29)), fur_l, rnd)
        shape(d, T_(ell(-45, -60, 14, 27, rot=0.35)), fur, rnd)
        shape(d, T_(ell(45, -60, 14, 27, rot=-0.35)), fur, rnd)
        head = lambda p: T_(rotp(p, 0, -100, tilt))
        shape(d, head(ell(-27, -142, 13, 13, n=18)), fur, rnd)
        shape(d, head(ell(27, -142, 13, 13, n=18)), fur, rnd)
        shape(d, head(ell(-27, -142, 6.5, 6.5, n=12)), fur_l, rnd, w=1.8, amp=0.4)
        shape(d, head(ell(27, -142, 6.5, 6.5, n=12)), fur_l, rnd, w=1.8, amp=0.4)
        shape(d, head(ell(0, -112, 35, 33)), fur, rnd)
        shape(d, head(ell(0, -102, 17, 13)), fur_l, rnd, w=2.4)
        shape(d, head(ell(0, -108, 6, 4.2, n=14)), PAL['brown'], rnd, w=1.8, amp=0.3)
        for ex in (-13, 13):
            shape(d, head(ell(ex, -120, 5.8, 5.8, n=14)), PAL['navy'], rnd, w=1.6, amp=0.3)
            shape(d, head(ell(ex - 1.8, -122, 1.8, 1.8, n=8)), PAL['frost'], rnd, w=0.6, amp=0.1)
    # ---- dust motes in the warm light
    if t >= 1.5:
        r2 = random.Random(5)
        fade = sstep(1.5, 2.2, t) * (1 - sstep(5.2, 6.0, t))  # already has t
        for _ in range(34):
            x0, y0 = r2.uniform(620, 1880), r2.uniform(760, 1040)
            ph = r2.uniform(0, 6.28); rad = r2.uniform(1.6, 3.6)
            x = x0 + 14 * math.sin(t * 0.9 + ph) - 14 * (t - 1.5); y = y0 - 22 * (t - 1.5) + 6 * math.sin(t * 1.3 + ph)
            a = int(150 * fade * (0.5 + 0.5 * math.sin(t * 2 + ph)))
            d.ellipse([(x - rad) * SS, (y - rad) * SS, (x + rad) * SS, (y + rad) * SS], fill=rgba(PAL['amber'], max(a, 0)))
    return im

# ---------------------------------------------------------------- compose
def over(out, im):
    a = np.asarray(im.resize((W, H), Image.LANCZOS), dtype=np.float32) / 255
    return out * (1 - a[..., 3:4]) + a[..., :3] * a[..., 3:4]

def frame(P, t, seed):
    rnd = random.Random(1000 + seed)
    cold, lit = P['cold'], P['lit']
    amb = 0.10 * sstep(2.0, 3.2, t) + 0.06 * sstep(4.0, 5.0, t)
    I = sstep(1.4, 1.9, t) * (1 - 0.30 * sstep(2.5, 3.5, t))
    base = cold + (lit - cold) * amb
    f = base + (lit - base) * (P['M'] * I)[..., None]
    s = sstep(1.5, 2.2, t)
    pcol = mixc(PAL['snow'], PAL['gold'], s)
    pal_a = 0.40 * sstep(0.2, 1.0, t) * (1 - s) + 0.88 * s
    pm = (P['patch'] * pal_a)[..., None]
    f = f * (1 - pm) + pcol * pm
    glow = sstep(4.0, 4.5, t) * (1 + 0.04 * math.sin(t * 9.0))
    f = f + (lit - f) * (P['G'] * 0.85 * glow)[..., None] + PAL['gold'] * (P['G'] * 0.10 * glow)[..., None]
    L = sstep(1.4, 2.0, t)
    f = over(f, draw_room_lines(rnd))
    f = over(f, draw_items(t, rnd, L))
    beat = 0.0
    if 0.5 <= t < 5.6:
        ph = (t - 0.5) % 1.0
        beat = 0.035 * (math.exp(-ph * 14) + 0.6 * math.exp(-abs(ph - 0.3) * 18))
    e = (0.16 + 0.84 * sstep(0.0, 1.3, t)) * (1 + beat)
    f = f * e
    f = f * (1 + 0.075 * P['tex'][..., None]) * P['vig'][..., None]
    rng = np.random.default_rng(500 + seed)
    f = f + rng.normal(0, 0.022, (H, W, 1)).astype(np.float32)
    return (np.clip(f, 0, 1) * 255).astype(np.uint8)

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'stills'
    P = build()
    if mode == 'stills':
        os.makedirs('stills', exist_ok=True)
        for tt in [float(x) for x in sys.argv[2:]] or [0.5, 1.8, 3.3, 5.5]:
            Image.fromarray(frame(P, tt, int(tt * 12))).save(f'stills/t{tt:04.1f}.png')
            print('still', tt)
    else:
        out = sys.argv[2] if len(sys.argv) > 2 else 'first6_silent.mp4'
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
               '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '16', '-preset', 'medium', out]
        pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        n_unique = int(SECS * FPS / 2)
        for i in range(n_unique):
            t = i * 2 / FPS
            fr = frame(P, t, i).tobytes()
            pr.stdin.write(fr); pr.stdin.write(fr)
            if i % 12 == 0: print(f'{t:.1f}s', flush=True)
        pr.stdin.close(); pr.wait()
        print('wrote', out)

if __name__ == '__main__':
    main()
