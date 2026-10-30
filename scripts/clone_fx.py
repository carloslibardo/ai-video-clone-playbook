"""Efeitos de motion graphics para vídeo vertical: onda de choque, tremor de câmera, bola de luz, fogo no texto.

Dependências: pip install numpy scipy pillow

Formato esperado:
- Efeitos de quadro (shockwave_frame, shake_frame, flash_frame, chroma_frame): array float32 HxWx3,
  com H, W = 1920, 1080 (RGB, valores de 0 a 255).
- Efeitos de overlay (orb, ring, Flames.draw): um PIL.Image RGBA de 1080x1920. O canvas pode ser
  opaco ou transparente; o alfa do efeito é somado ao do canvas.

Exemplo mínimo:
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    orb(canvas, t=0.5, t0=0.0, dur=1.0, p0=(200, 1500), p1=(800, 600))
    frame = np.asarray(canvas.convert("RGB"), np.float32)
    frame = shake_frame(frame, age=0.1)
"""

import math

import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import convolve1d, gaussian_filter, map_coordinates

W, H = 1080, 1920


def _ease_out(x: float) -> float:
    x = min(max(x, 0.0), 1.0)
    return 1 - (1 - x) ** 3


def _add(canvas: Image.Image, rgb: np.ndarray, x0: int, y0: int):
    """Additive (screen-like) blend of a float RGB patch into an RGBA canvas at (x0, y0), clipped to the frame.
    The patch brightness also raises the canvas alpha, so the effect stays visible on a transparent overlay."""
    h, w = rgb.shape[:2]
    xa, ya, xb, yb = max(0, x0), max(0, y0), min(W, x0 + w), min(H, y0 + h)
    if xa >= xb or ya >= yb:
        return
    base = np.asarray(canvas.convert("RGBA").crop((xa, ya, xb, yb)), np.float32)
    patch = np.clip(rgb[ya - y0:yb - y0, xa - x0:xb - x0], 0, 255)
    base[..., :3] = 255 - (255 - base[..., :3]) * (1 - patch / 255)
    base[..., 3] = np.maximum(base[..., 3], patch.max(axis=-1))
    canvas.paste(Image.fromarray(base.astype(np.uint8)), (xa, ya))


# ---------------------------------------------------------------- frame effects


def shockwave_frame(img: np.ndarray, age: float, cx: float, cy: float, dur: float = 0.5) -> np.ndarray:
    """Refractive ring that expands from (cx, cy): pixels near the ring are pushed outward."""
    if not (0 <= age < dur):
        return img
    p = age / dur
    rad = 60 + 1500 * _ease_out(p)
    width = 90 * (1 - 0.5 * p)
    strength = 38 * (1 - p)
    yy, xx = np.mgrid[0:H:2, 0:W:2].astype(np.float32)
    dx, dy = xx - cx, yy - cy
    r = np.sqrt(dx * dx + dy * dy) + 1e-3
    push = strength * np.exp(-((r - rad) / width) ** 2)
    ux, uy = dx / r * push, dy / r * push
    ux = np.repeat(np.repeat(ux, 2, 0), 2, 1)[:H, :W]
    uy = np.repeat(np.repeat(uy, 2, 0), 2, 1)[:H, :W]
    gy, gx = np.mgrid[0:H, 0:W].astype(np.float32)
    out = np.empty_like(img)
    for c in range(3):
        out[..., c] = map_coordinates(img[..., c], [gy - uy, gx - ux], order=1, mode="nearest")
    glow = np.exp(-((np.sqrt((gx - cx) ** 2 + (gy - cy) ** 2) - rad) / (width * 0.35)) ** 2) * 120 * (1 - p)
    return np.clip(out + glow[..., None] * np.array([1.0, 0.92, 0.7], np.float32), 0, 255)


def flash_frame(img: np.ndarray, age: float, dur: float = 0.14, k: float = 0.75) -> np.ndarray:
    if not (0 <= age < dur):
        return img
    a = k * (1 - age / dur) ** 2
    return img * (1 - a) + 255 * a


def shake_frame(img: np.ndarray, age: float, dur: float = 0.32, amp: float = 22) -> np.ndarray:
    if not (0 <= age < dur):
        return img
    decay = (1 - age / dur) ** 2
    dx = int(amp * decay * math.sin(age * 2 * math.pi * 17))
    dy = int(amp * 0.7 * decay * math.cos(age * 2 * math.pi * 13))
    s = 1.0 + 0.04 * decay
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    cw, ch = W / s, H / s
    x0 = min(max((W - cw) / 2 - dx, 0.0), W - cw)
    y0 = min(max((H - ch) / 2 - dy, 0.0), H - ch)
    return np.asarray(im.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch)), np.float32)


def chroma_frame(img: np.ndarray, age: float, dur: float = 0.2, px: int = 10) -> np.ndarray:
    """RGB split that decays: sells an impact without blurring the face for long."""
    if not (0 <= age < dur):
        return img
    k = int(px * (1 - age / dur))
    if k < 1:
        return img
    out = img.copy()
    out[..., 0] = np.roll(img[..., 0], k, axis=1)
    out[..., 2] = np.roll(img[..., 2], -k, axis=1)
    return out


# ---------------------------------------------------------------- overlay effects


def _glow_sprite(r: int, core=(255, 255, 255), halo=(255, 200, 60)) -> np.ndarray:
    s = r * 4
    yy, xx = np.mgrid[-s:s + 1, -s:s + 1].astype(np.float32)
    d = np.sqrt(xx * xx + yy * yy) / r
    core_a = np.clip(1.2 - d, 0, 1) ** 1.5
    halo_a = np.exp(-(d ** 2) / 3.5) * 0.85
    rgb = core_a[..., None] * np.array(core, np.float32) + halo_a[..., None] * np.array(halo, np.float32)
    return np.clip(rgb, 0, 255)


_SPRITES: dict = {}


def orb(canvas: Image.Image, t: float, t0: float, dur: float, p0, p1, lift: float = -380, r: int = 38,
        halo=(255, 200, 60)):
    """A ball of light flying from p0 to p1 along an arc, with a fading trail; bursts on arrival."""
    age = t - t0
    if age < 0 or age > dur + 0.35:
        return
    ctrl = ((p0[0] + p1[0]) / 2, min(p0[1], p1[1]) + lift)

    def at(u):
        u = min(max(u, 0.0), 1.0)
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctrl[0] + u * u * p1[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctrl[1] + u * u * p1[1]
        return x, y

    if age <= dur:
        u = 0.5 - 0.5 * math.cos(math.pi * age / dur)
        for k in range(14, -1, -1):
            uk = u - k * 0.03
            if uk < 0:
                continue
            rk = max(5, int(r * (1 - k / 18)))
            key = (rk, halo)
            if key not in _SPRITES:
                _SPRITES[key] = _glow_sprite(rk, halo=halo)
            spr = _SPRITES[key] * (1 - k / 15) ** 1.4
            x, y = at(uk)
            _add(canvas, spr, int(x) - spr.shape[1] // 2, int(y) - spr.shape[0] // 2)
    else:
        b = (age - dur) / 0.35
        x, y = p1
        rad = int(30 + 260 * _ease_out(b))
        yy, xx = np.mgrid[-rad - 20:rad + 21, -rad - 20:rad + 21].astype(np.float32)
        ring = np.exp(-((np.sqrt(xx * xx + yy * yy) - rad) / 14) ** 2) * 255 * (1 - b)
        _add(canvas, ring[..., None] * (np.array(halo, np.float32) / 255), int(x) - rad - 20, int(y) - rad - 20)


def ring(canvas: Image.Image, t: float, t0: float, cx: float, cy: float, dur: float = 0.4, rmax: int = 320,
         color=(255, 213, 74)):
    age = t - t0
    if not (0 <= age < dur):
        return
    b = age / dur
    rad = int(20 + rmax * _ease_out(b))
    yy, xx = np.mgrid[-rad - 24:rad + 25, -rad - 24:rad + 25].astype(np.float32)
    ring_a = np.exp(-((np.sqrt(xx * xx + yy * yy) - rad) / 10) ** 2) * 255 * (1 - b)
    _add(canvas, ring_a[..., None] * (np.array(color, np.float32) / 255), int(cx) - rad - 24, int(cy) - rad - 24)


class Flames:
    """Procedural fire rising from the outline of an RGBA text image placed at (cx, top)."""

    def __init__(self, text_img: Image.Image, cx: int, top: int, height: int = 360, seed: int = 3):
        a = np.asarray(text_img.getchannel("A"), np.float32) / 255
        pad_top = height
        src = np.zeros((a.shape[0] + pad_top + 40, a.shape[1] + 80), np.float32)
        src[pad_top:pad_top + a.shape[0], 40:40 + a.shape[1]] = a
        src = np.asarray(Image.fromarray((src * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9)), np.float32) / 255
        k = np.exp(-np.arange(height) / (height * 0.33)).astype(np.float32)
        kernel = np.concatenate([np.zeros(height - 1, np.float32), k])
        heat = convolve1d(src, kernel[::-1], axis=0, mode="constant")
        self.heat = gaussian_filter(heat / (heat.max() + 1e-6), 3)
        rng = np.random.default_rng(seed)
        hh, ww = self.heat.shape
        n = gaussian_filter(rng.random((hh * 3, ww)).astype(np.float32), (22, 9), mode="wrap") * 0.6 + \
            gaussian_filter(rng.random((hh * 3, ww)).astype(np.float32), (8, 4), mode="wrap") * 0.4
        self.noise = (n - n.min()) / (n.max() - n.min())
        self.x0 = cx - ww // 2
        self.y0 = top - pad_top
        lut = np.zeros((256, 3), np.float32)
        for i in range(256):
            v = i / 255
            lut[i] = (min(255, 600 * v), max(0, min(255, 520 * (v - 0.22))), max(0, min(255, 700 * (v - 0.68))))
        self.lut = lut

    def draw(self, canvas: Image.Image, t: float, intensity: float = 1.0):
        hh, ww = self.heat.shape
        off = int(t * 520) % (hh * 2)
        n = self.noise[off:off + hh]
        sway = np.sin(np.linspace(0, 6, hh)[:, None] + t * 5) * 6
        n = np.roll(n, int(sway.mean()), axis=1)
        n = (n - n.min()) / (n.max() - n.min() + 1e-6)
        f = np.clip(self.heat * (0.25 + 1.5 * n) - 0.30, 0, 1) * 1.6 * intensity
        f = gaussian_filter(f, 1.5)
        idx = np.clip(f * 255, 0, 255).astype(np.uint8)
        rgb = self.lut[idx]
        rgb = rgb + gaussian_filter(rgb, (14, 14, 0)) * 0.6
        _add(canvas, rgb, self.x0, self.y0)
