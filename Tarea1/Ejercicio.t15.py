#Realice un Menú interactivo que tenga las opciones de saludar ,una operación matemática y
#salir
print("**********BIENVENIDO AL MENU**********")          
print("-Elija una opcion \n1) Saludar\n2) Operacion matematica\n3) Salir")
opcion = int(input("Introduce un número: ") )     
if opcion == 1:
    print("Hola, que tal:D")
if opcion == 2:
    num1 = float(input("Introduce el primer número: ") )
    num2 = float(input("Introduce el segundo número: ") )
    print("El producto de",num1,"*",num2,"es",num1*num2)
if opcion == 3:
    print("Gracias por entrar:D")
