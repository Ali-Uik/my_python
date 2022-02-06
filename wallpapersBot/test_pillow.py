from PIL import Image

with Image.open('Абстракция/photo_2021-11-03_12-01-16.jpg') as image:
    width = image.size[0]
    height = image.size[1]
    # print(width, height)
    area = (0, 0, 100, 100)
    (left, upper, right, lower) = (100, 0, 1280, 1280)
    image_corp = image.crop(area)
    image_corp.save('temp.jpeg', quality=100)
    print(image.size)
    print(image_corp.size)
