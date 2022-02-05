from PIL import Image

im = Image.open('Абстракция/abstraktsiya_forma_ostrie_figurka_101902_2560x1440.jpg')
original_height = im.size[0]
original_width = im.size[1]
height = im.size[1]
width = height // 2
new_image = im.crop((
    original_height//2, original_width//2,original_height//2,original_width//2
))
print(height, width)
new_image.save('temp.jpg', quality=100)
