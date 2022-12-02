#10.Realizar un programa que calcule la penalidad por la mora de una deuda,sabiendo que si se
#demora de 1 día a 10 se le agrega el 5% , si se demora hasta 30 días se le agrega 8% y pasando
#el rango máximo se le agrega un 10%.
dia=int(input("Ingrese días:"))
penalidad=0.0
if dia>0 and dia<11:
    penalidad= dia + dia*5/100
    print("Mi penalidad es " + str(penalidad))
elif dia>11 and dia<31:
    penalidad= dia + dia*8/100
    print("Mi penalidad es " + str(penalidad))
else:
    penalidad= dia + dia*10/100
    print("Mi penalidad es " + str(penalidad))

