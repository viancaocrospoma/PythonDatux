#12.Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es
#vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle
#que no se puede procesar el dato.
let=input("Escribe la Letra:")
if len(let)==1:
    print("Es una letra")
else:
    if let=="a" or let=="e" or let=="i" or let=="o" or let=="u":
        print("Es una vocal")
