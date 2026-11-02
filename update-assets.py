#!/usr/bin/env python3
"""Sematkan gambar dan logo di folder img ke img/assets.js.

index.html bisa dibuka langsung (double-click, file://) karena gambar dibaca dari
assets.js. Jalankan ulang script ini setiap kali PNG di folder img diganti:

    python3 update-assets.py
"""
import base64
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
files = {
    "backdrop": root / "img" / "backdrop.png",
    "alas": root / "img" / "alas.png",
    "logoMoox": root / "img" / "logo-moox.svg",
    "mooAxela": root / "img" / "moo-axela.svg",
    "mooAxaka": root / "img" / "moo-axaka.svg",
    "alt2Backdrop": root / "img" / "alt2" / "backdrop.png",
    "alt2Alas": root / "img" / "alt2" / "alas.png",
    "alt3Backdrop": root / "img" / "alt3" / "backdrop.png",
    "alt3Alas": root / "img" / "alt3" / "alas.png",
}
MIME = {".png": "image/png", ".svg": "image/svg+xml", ".jpg": "image/jpeg"}

data = {}
for key, path in files.items():
    if path.exists():
        data[key] = f"data:{MIME[path.suffix.lower()]};base64," + base64.b64encode(path.read_bytes()).decode()
        print(f"ok   {path.relative_to(root)}")
    else:
        print(f"skip {path.relative_to(root)} (tidak ada)")

out = root / "img" / "assets.js"
out.write_text("// Dibuat otomatis oleh update-assets.py, jangan diedit manual.\n"
               "window.MOOX_ASSETS = " + json.dumps(data) + ";\n")
print(f"tulis {out.relative_to(root)}")
