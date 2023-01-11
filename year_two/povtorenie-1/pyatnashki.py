from PIL import Image

with Image.open("image.bmp") as im:
    parts = [[] for _ in range(4)]
    x, y = im.size
    size = [x // 4, y // 4]
    for i in range(4):
        for j in range(4):
            if i == 3 and j == 3:
                break
            left = size[0] * i
            top = size[1] * j
            right = size[0] + size[0] * i
            bottom = size[1] + size[1] * j
            parts[i].append(im.crop((left, top, right, bottom)))
            parts[i][j].save(f"image{j + 1}{i + 1}.bmp")
