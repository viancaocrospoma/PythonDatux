class producto:
    # Constructor de clase
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

        print('Se ha creado el producto: ', self.nombre)
    def __str__(self):
        return 'El producto {} esta {} soles'.format(self.nombre, self.precio) 

class Catalogo:

    listaproductos = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, nombre):
        self.listaproductos.append(nombre)

    def agregar(self, p):  # p será un objeto Pelicula
        self.listaproductos.append(p)

    def mostrar(self):
        for p in self.listaproductos:
            print(p)  # Print toma por defecto str(p)

p=producto("llanta",287)
p1=producto("lunas",2023)
p2=producto("frenos",319)

c1=Catalogo(p)
c1.agregar(p1)
c1.agregar(p2)
print("se va mostrar la lista")
c1.mostrar()