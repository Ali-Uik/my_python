from pprint import pprint

x = "Mike"


# pprint(dir(x))

class Cars:
    def __init__(self, color, weight, height):
        self.color = color
        self.weight = weight
        self.height = height

    # def __str__(self):
    #     return f'{self.color},{self.weight},{self.height}'


car1 = Cars('white', 5.30, 1.5)
print(car1.color)
