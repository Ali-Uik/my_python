class Computer:
    def __init__(self, owner, CPU, OS, RAM, HDD, monitor):
        self.owner = owner
        self.CPU = CPU
        self.OS = OS
        self.RAM = RAM
        self.HDD = HDD
        self.monitor = monitor

    def __str__(self):
        return f'Владелец:{self.owner}\n' \
               f'Процессор:{self.CPU}\n' \
               f'Операционная система:{self.OS}\n' \
               f'Оперативная памят:{self.RAM} GB\n' \
               f'HDD:{self.HDD} TB\n' \
               f'Монитор:{self.monitor}'

    def owner_info(self):
        return f'Владелец этого комп.а {self.owner}'

    def __eq__(self, other):
        return self.RAM == other.RAM

    def __ne__(self, other):
        return self.RAM != other.RAM

    def __gt__(self, other):
        return self.RAM > other.RAM

    def __ge__(self, other):
        return self.RAM >= other.RAM

    def __lt__(self, other):
        return self.RAM < other.RAM

    def __le__(self, other):
        return self.RAM <= other.RAM


comp1 = Computer('Ali', 'Core i9', 'Lunix', 64, 1, 'LG 27er')
comp2 = Computer('Bonu', 'Core i11', 'MacOS', 128, 2, 'Immer')

print(comp1)
print(comp2)
# print(comp2)
if comp1 == comp2:
    print(f'{comp1.owner}нинг компининг ОЗУси {comp2.owner}нинг компининг ОЗУсига тенг')
elif comp1 != comp2:
    print(f'{comp1.owner}нинг компининг ОЗУси {comp2.owner}нинг компининг ОЗУсига тенг эмас')
elif comp1 > comp2:
    print(f'{comp1.owner}нинг компининг ОЗУси {comp2.owner}нинг компининг ОЗУсидан катта')
elif comp1 >= comp2:
    print(f'{comp1.owner}нинг компининг ОЗУси {comp2.owner}нинг компининг ОЗУсидан катта ёки тенг')
elif comp1 < comp2:
    print(f'{comp1.owner}нинг компининг ОЗУси {comp2.owner}нинг компининг ОЗУсидан кичик')
elif comp1 <= comp2:
    print(f'{comp1.owner}нинг компининг ОЗУси {comp2.owner}нинг компининг ОЗУсидан кичик ёки тенг')

# print(comp1 == comp2)
# print(comp1 < comp2)
# print(comp1 <= comp2)
