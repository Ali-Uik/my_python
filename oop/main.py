class Point:  # классни аниклаб олдик, PEP8 стандарти буйича класснинг номи бош харф билан бошланиши керак.
    '''Класснинг таърифи. Таърифни __doc__ функцияси оркали чакиришимиз мумкин'''
    color = 'red'  # класнинг атрибутлари ёки свойствалари
    circle = 2

    def set_coords(self):
        print('Вызив метода set_coords' + str(self))


pt = Point()
pt.set_coords()