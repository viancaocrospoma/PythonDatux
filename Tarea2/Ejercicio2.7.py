def retor_mayor(num1,num2):
    if num1>num2:
        mayor=num1
    else:
        mayor=num2
    return mayor
 
valor1=int(input("Ingrese el primer valor:"))
valor2=int(input("Ingrese el segundo valor:"))
print(retor_mayor(valor1,valor2))