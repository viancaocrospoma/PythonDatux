def es_mul(nume1:int, nume2:int):
    return nume1*nume2 
num1 = int(input('Ingrese primer num: '))
num2 = int(input('Ingrese segundo num: '))

if num1>0 and num2 >0:
    mu=es_mul(num1, num2)
    print(mu)
else:
    print('LOS NUMEROS NO SE PUEDEN MULTIPLICAR')