# class Figure:
#     def __init__(self, name, a, b):
#         self.name = name
#         self.a = a
#         self.b = b
#
#     def print_info(self):
#         return f'Figura nomi {self.name}. Tomonlari {self.a} va {self.b}'
#
#     def square_of_rectangle(self):
#         return f'Yuzasi: {self.a * self.b}'
#
#
# figura1 = Figure('kvadrat', 5, 5)
# figura2 = Figure('to\'g\'ri t\'ortburchak',10,5)
# print(figura1.print_info())
# print(figura1.square_of_rectangle())
# print(figura2.print_info())
# print(figura2.square_of_rectangle())

a = float(input('a-ni kiriting: '))
b = float(input('b-ni kiriting: '))
c = float(input('c-ni kiriting: '))
r = float(input('r-ni kiriting: '))

FIGURE1 = 'Uchberchak'
FIGURE2 = 'To\'rtburchak'
FIGURE3 = 'Kvadrat'
FIGURE4 = 'Doira'


class Figure:
    def __init__(self, name):
        self.name = name

    def get_figure_info(self):
        return f'Figuraning nomi: {self.name.title()}'


class Quadrangle(Figure):
    def __init__(self, a, b, name):
        Figure.__init__(self, name)
        self.a = a
        self.b = b

    def square_of_quadrangle(self):
        return self.a * self.b

    def perimeter_of_quadrangle(self):
        return 2 * (self.a + self.b)


class Triangle(Figure):
    def __init__(self, a, b, c, name):
        Figure.__init__(self, name)
        self.a = a
        self.b = b
        self.c = c


if a and b:
    if a == b:
        figure1 = Quadrangle(a, b, FIGURE3)
        print(
            f'Figura: {FIGURE3},Yuzasi:{figure1.square_of_quadrangle()},Perimetri: {figure1.perimeter_of_quadrangle()}')

    else:
        figure1 = Quadrangle(a, b, FIGURE2)
        print(
            f'Figura:{FIGURE2}, Yuzasi:{figure1.square_of_quadrangle()},Perimetri:{figure1.perimeter_of_quadrangle()}')

elif a and b and c:
    print(f'Figura:{FIGURE1}')

# figure1 = Triangle(10, 20, 'kvadrat')
# print(figure1.get_figure_info())
# print(figure1.square_of_triangle())
# # figure1 = Figure('kvadrat')
# # print(figure1.get_figure_info())
