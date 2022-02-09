from PIL import Image
from PIL import ImageDraw, ImageFont


def crop_image_to_mobile(image_path):
    with Image.open(image_path) as im:
        original_width = im.size[0]
        original_height = im.size[1]
        width = original_height // 2
        print(original_height, width)
        (left, upper, right, lower) = ((original_width - width) // 2,
                                       0,
                                       (original_width + width) // 2,
                                       original_height)
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save(f'crop_{image_path}', quality=100)


def watermark_text(image_name):
    im = Image.open(image_name)
    drawing = ImageDraw.Draw(im)
    color = (0,0,0)
    font = ImageFont.truetype('SourceSerif4-Italic-VariableFont_opsz,wght.ttf', 48)
    drawing.text((0, 0), '@abu_Ali_ibn_Rustam', fill=color, font=font)
    im.save(f'water_{image_name}')
