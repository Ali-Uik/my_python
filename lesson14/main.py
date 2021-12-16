# Классы
class User:
    type = 'human'  # Общие атрибуты класса

    # Конструктор - функция инициализации класса с заданным аргументами
    def __init__(self, name, lastname, age, work=None, salary=100000):
        self.name = name  # В моем поле name будет значение которое подали
        self.lastname = lastname
        self.age = age
        self.work = work
        self.salary = salary

    def get_user_info(self):
        return f'Меня зовут {self.name} {self.lastname}. Мне {self.age} лет'

    def get_user_info_print(self):
        print(f'Меня зовут {self.name} {self.lastname}. Мне {self.age} лет')

    # Переопределение стандартной печати класса
    def __str__(self):
        return f'Объект класса {self.__class__.__name__} С отрибутами {self.__dir__()}'

    # Функция класса которая возвращает заработок в день считать в месяце 25 дней
    def salary_day(self):
        print(f'Мой ЗП в день - {self.salary / 25}')

    def __eq__(self, other):  # == # other - другой класс
        return self.age == other.age

    def __ne__(self, other):  # !=
        return self.age != other.age

    def __gt__(self, other):  # >
        return self.age > other.age

    def __ge__(self, other):  # >=
        return self.age >= other.age

    def __lt__(self, other):  # <
        return self.age < other.age

    def __le__(self, other):  # <=
        return self.age <= other.age


# Все элементы python - объкти
# list3 = [123, 123, 123]
user1 = User('ALi', 'Rustamboev', 4, salary=1500000)
user2 = User(name='Bonu', lastname='Rustamboeva', age=8, work='IT', salary=4000000)


# print(user1.name)
# print(user2.age)
# print(user1.get_user_info())
# print(user2.get_user_info())
# user1.get_user_info_print()
# user1.salary_day()
# user2.get_user_info_print()
# user2.salary_day()

# print(user1)
# print(user2)

# print(hasattr(user1, 'name'))
# print(hasattr(user1, 'friends'))
# print(getattr(user1, 'name'))  # Получает значение атрибута
# print(getattr(user1, 'friends', 'Такого атрибута нет'))  # Получает значение атрибута, если нет - стандарт

# print(user1 == user2)
# print(user1 != user2)
# print(user1 > user2)
# print(user1 >= user2)
# print(user1 < user2)
# print(user1 <= user2)


# Наследование

class Student(User):  # Класс студент наследовается от класса User
    def __init__(self, name, lastname, age, work=None, salary=100000, univer='TATU'):
        User.__init__(self, name, lastname, age, work, salary)  # super.__init__(name, lastname, age, work, salary)
        self.univer = univer

    def __str__(self):
        return f'Студент универа {self.univer}'


superstuden = Student('Jamshid', 'Tursunov', 34, univer='Inha')
print(superstuden.salary_day())  # Вызов метода вручную
print(superstuden)
