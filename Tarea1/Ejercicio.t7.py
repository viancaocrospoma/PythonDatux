#7. Realiza un programa que lea 2 números por teclado y determine los siguientes
#aspectos:
#● Si los dos números son iguales
#● Si los dos números son diferentes
#● Si el primero es mayor que el segundo
#● Si el segundo es mayor o igual que el primero
n1=int(input("Primer num:"))
n2=int(input("Segundo num:"))
if n1==n2:
    print("LOS DOS NUMEROS SON IGUALES")
if n1!=n2:
  if n1>n2:
    print("EL PRIMER NUMERO ES MAYOR")
  else:
    print("EL SEGUNDO NUMERO ES MAYOR")