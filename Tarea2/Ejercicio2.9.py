def foo(x: lista):
nums=lista[0]
for i in range(len(nums)):
    nums[i] += 5
lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)
mayormenor(lista)