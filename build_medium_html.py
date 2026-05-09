#!/usr/bin/env python3
"""
build_medium_html.py  —  Convert conjugate_priors_medium.md → self-contained HTML
                          for Medium import via URL.

All equation PNGs are embedded as base64 data URIs so the file is completely
self-contained — no external dependencies.

Usage:
    python3 build_medium_html.py

Output:
    article/conjugate_priors_medium_import.html   (self-contained, ~1MB)

Medium import steps:
    1. Commit + push this file to GitHub
    2. Go to:
         https://htmlpreview.github.io/?https://github.com/getgaurav2/conjugate-priors-cybersecurity/blob/main/article/conjugate_priors_medium_import.html
    3. Copy that URL
    4. medium.com → write a story → (···) menu → Import a story → paste the URL
"""

import base64
import pathlib
import re
import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension

ROOT     = pathlib.Path(__file__).parent
IN_MD    = ROOT / 'article' / 'conjugate_priors_medium.md'
IMG_DIR  = ROOT / 'article' / 'equation_images'
OUT_HTML = ROOT / 'article' / 'conjugate_priors_medium_import.html'


def embed_images(html: str) -> tuple[str, int]:
    """Replace equation_images/fname.png src attrs with base64 data URIs."""
    count = 0

    def replace(m):
        nonlocal count
        fname = m.group(1)
        fpath = IMG_DIR / fname
        if not fpath.exists():
            return m.group(0)
        b64 = base64.b64encode(fpath.read_bytes()).decode()
        count += 1
        return f'src="data:image/png;base64,{b64}"'

    html = re.sub(r'src="equation_images/([^"]+)"', replace, html)
    return html, count


def convert():
    md_text = IN_MD.read_text()

    body_html = markdown.markdown(
        md_text,
        extensions=[
            TableExtension(),
            FencedCodeExtension(),
            'nl2br',
        ]
    )

    body_html, n_embedded = embed_images(body_html)

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Understanding Conjugate Priors Through Real-World Cybersecurity Data</title>
</head>
<body>
{body_html}
</body>
</html>"""

    OUT_HTML.write_text(html)
    size_kb = OUT_HTML.stat().st_size // 1024

    print(f'Converted {IN_MD.name} → {OUT_HTML.name}  ({size_kb} KB)')
    print(f'  {n_embedded}/55 equation images embedded as base64')
    print()
    print('Steps to get a public URL for Medium import:')
    print()
    print('  1. Commit + push this file:')
    print('       git add article/conjugate_priors_medium_import.html')
    print('       git commit -m "add self-contained Medium import HTML"')
    print('       git push')
    print()
    print('  2. Your import URL will be:')
    print('       https://htmlpreview.github.io/?https://github.com/getgaurav2/conjugate-priors-cybersecurity/blob/main/article/conjugate_priors_medium_import.html')
    print()
    print('  3. medium.com → write a story → (···) menu → Import a story → paste that URL')


if __name__ == '__main__':
    convert()
