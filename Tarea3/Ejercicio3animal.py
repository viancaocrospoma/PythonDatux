class Figura:
    def __init__(self,lados):
        self.lados=lados


class Cuadrado(Figura):
    def __init__(self, lados):
        super().__init__(lados)
    def area(self,base,altura):
        return base*altura

class Circulo(Figura):
    def __init__(self, lados):
        super().__init__(lados)
    def area(self,radio):
        return 3.14*radio*radio

class Triangulo(Figura):
    def __init__(self, lados):
        super().__init__(lados)

    def area(self,base,altura):
        return base*altura/2