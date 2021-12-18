class Figura:
    def __init__(self):
        class Triangle:
            def __init__(self, a, b, c):
                self.a = a
                self.b = b
                self.c = c

            def p_of_t(self):
                return self.a + self.b + self.c


print(Figura())
