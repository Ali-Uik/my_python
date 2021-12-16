# Классы
class User:
    type = 'human'  # Общие атрибуты класса

    # Конструктор - функция инициализации класса с заданным аргументами
    def __init__(self, name, lastname, age):
        self.name = name  # В моем поле name будет значение которое подали
        self.lastname = lastname
        self.age = age


user1 = User('ALi', 'Rustamboev', 4)
user2 = User(name='Bonu', lastname='Rustamboeva', age=8)

print(user1.name)
print(user2.age)
