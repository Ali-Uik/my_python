class Car:
    def __init__(self, color, mark, max_speed):
        self.color = color
        self.mark = mark
        self.max_speed = max_speed

    def get_info(self):
        print(f'Машина цвета {self.color} марка {self.mark} и макс скорости {self.max_speed} км/ч')


class SuperCar(Car):
    def __init__(self, color, mark, max_speed, razgon):
        Car.__init__(self, color, mark, max_speed)
        self.razgon = razgon

    def city_speed(self):
        return self.max_speed - 60


car1 = SuperCar('Белый', 'BMW', 280, 10)
print(car1.city_speed())
