#!/usr/bin/env python3
"""Sematkan img/backdrop.png dan img/alas.png ke img/assets.js.

index.html bisa dibuka langsung (double-click, file://) karena gambar dibaca dari
assets.js. Jalankan ulang script ini setiap kali PNG di folder img diganti:

    python3 update-assets.py
"""
import base64
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
files = {"backdrop": root / "img" / "backdrop.png", "alas": root / "img" / "alas.png"}

data = {}
for key, path in files.items():
    if path.exists():
        data[key] = "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode()
        print(f"ok   {path.relative_to(root)}")
    else:
        print(f"skip {path.relative_to(root)} (tidak ada)")

out = root / "img" / "assets.js"
out.write_text("// Dibuat otomatis oleh update-assets.py, jangan diedit manual.\n"
               "window.MOOX_ASSETS = " + json.dumps(data) + ";\n")
print(f"tulis {out.relative_to(root)}")
