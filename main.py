from PIL import Image

img = Image.open('./image.png')

largura, altura = img.size

def rgb_para_hex(rgb):
    r, g, b = rgb[:3]
    return f"#{r:02X}{g:02X}{b:02X}"

css = f"""
<style>
    .container {{
        display: grid;
        grid-template-columns: repeat({largura}, 1px);
        grid-template-rows: repeat({altura}, 1px);
        gap: 0;
    }}
    .container div {{
        width: 1px;
        height: 1px;
        border: 0; /* Remova a borda para ficar igual ao pixel */
        box-sizing: border-box;
    }}
</style>
"""

pixels_html = []
for y in range(altura):
    for x in range(largura):
        pixel = rgb_para_hex(img.getpixel((x, y)))
        pixels_html.append(f'<div style="background-color: {pixel};"></div>')

pixels_html_str = "\n".join(pixels_html)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Imagem Pixelada</title>
    {css}
</head>
<body>
    <div class="container">
        {pixels_html_str}
    </div>
</body>
</html>
"""

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Arquivo output.html gerado com sucesso!")
