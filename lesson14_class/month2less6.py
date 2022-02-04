class Computer:
    def __init__(self, owner, CPU, memory, store, monitor, age):
        self.owner = owner
        self.CPU = CPU
        self.memory = memory
        self.store = store
        self.monitor = monitor
        self.age = age

    def get_owner_info(self):
        return f'I am {self.owner} owner of CPU-{self.CPU}, where Monitor is {self.monitor}'

    def get_owner_info_print(self):
        print(f'My name is {self.owner} I am {self.age} YO')

    def __eq__(self, diff):
        return self.CPU == diff.CPU

    def __ne__(self, diff):
        return self.age != diff.age

    def __gt__(self, diff):
        return self.memory > diff.memory

    def __ge__(self, diff):
        return self.CPU >= diff.CPU

    def __lt__(self, diff):
        return self.CPU < diff.CPU

    def __le__(self, diff):
        return self.CPU <= diff.CPU


comp1 = Computer('Jonathan', 16, 256, '1TB', 'Samsung', 34)
comp2 = Computer(owner='Floyd', CPU=32, memory=128, store='2TB', monitor='LG', age=25)
print(comp1.get_owner_info())
print(comp2.get_owner_info())
comp1.get_owner_info_print()
comp2.get_owner_info_print()
print(comp1 == comp2)
print(comp1 > comp2)
print(comp1 >= comp2)
print(comp1 < comp2)
print(comp1 <= comp2)


______________________________________________________________________________
#2
class Animals:
    def __init__(self, name):
        self.name = name

    def get_info_Animals(self):
        return f'{self.name}'

    def get_info_Animals_print(self):
        print(f'{self.name}')


class Birds(Animals):
    def __init__(self, color, place, wings, nutrition):
        self.color = color
        self.place = place
        self.wings = wings
        self.nutrition = nutrition

    def get_info_birds(self):
        return f'{self.color}, {self.place}, {self.wings}, {self.nutrition}'


eagle = Birds('gray', 'mountains', 2.8, 'rats, bunnies')
hen = Birds(color='white', place='nest', wings='25cm', nutrition='seeds')


class Mammals(Animals):
    def __init__(self, color, place, size, nutrition):
        self.color = color
        self.place = place
        self.size = size
        self.nutrition = nutrition

    def get_info_mam(self):
        return f'{self.color}, {self.place}, {self.size}, {self.nutrition}'


rat = Mammals(color='gray', place='field', nutrition='seed', size='7-9 cm')
monkey = Mammals('brown', 'forest', '10-12 kg', 'fruits, leaf')


class Reptiles(Animals):
    def __init__(self, place, size, nutrition):
        self.place = place
        self.size = size
        self.nutrition = nutrition

    def get_info_rept(self):
        return f'{self.place}, {self.size}, {self.nutrition}'


snake = Reptiles('anywhere', '2 to 10 metres', 'rats and birds')
chameleon = Reptiles(place='forests', size='3-4 cm', nutrition='insects')


class Fish(Animals):
    def __init__(self, place, color, nutrition):
        self.place = place
        self.color = color
        self.nutrition = nutrition

    def get_info_fish(self):
        return f'{self.color}, {self.place}, {self.nutrition}'


perch = Fish('ocean', 'blue', 'spawn')
white_shark = Fish(color='white and grey', place='ocean', nutrition='fish')

print(eagle.get_info_birds())
print(hen.get_info_birds())
print(rat.get_info_mam())
print(monkey.get_info_mam())
print(snake.get_info_rept())
print(chameleon.get_info_rept())
print(perch.get_info_fish())
print(white_shark.get_info_fish())




