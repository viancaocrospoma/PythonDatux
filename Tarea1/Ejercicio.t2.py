#2.Calcule el área de un círculo con radio ingresado desde el teclado.
radio=float(input("ingrese radio:"))
pi=3.14
if radio>=0:
   print(pi*(radio**2))
else: 
   print("Ese circulo no existe: ")   
