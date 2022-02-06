from PIL import Image

im = Image.open('Абстракция/abstraktsiya_forma_ostrie_figurka_101902_2560x1440.jpg')
print(im.size)
original_height = im.size[1]
original_width = im.size[0]
print(original_width, original_height)
height = im.size[1]
width = height // 2
print(height, width)
# new_image = im.crop((
#     original_height//2, original_width//2,original_height//2,original_width//2
# ))
# print(height, width)
# new_image.save('temp.jpg', quality=100)
