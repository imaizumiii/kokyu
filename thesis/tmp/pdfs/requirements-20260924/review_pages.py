from pathlib import Path
from PIL import Image, ImageDraw

directory = Path(__file__).resolve().parent
pages = sorted(directory.glob('page-*.png'))
for start in range(0, len(pages), 8):
    batch = pages[start:start + 8]
    sheet = Image.new('RGB', (1244, 908), 'white')
    draw = ImageDraw.Draw(sheet)
    for offset, page in enumerate(batch):
        with Image.open(page) as source:
            thumbnail = source.copy()
        thumbnail.thumbnail((301, 422))
        x = (offset % 4) * 311 + 5
        y = (offset // 4) * 454 + 24
        sheet.paste(thumbnail, (x, y))
        draw.text((x + 8, y - 18), f'PDF page {start + offset + 1}', fill='black')
    output = directory / f'overview-{start // 8 + 1}.png'
    sheet.save(output)
    print(output.name)
