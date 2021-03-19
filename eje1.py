#1. Como multiplicar 2 números sin usar el signo de multiplicación.
n = float(input("Escribir el primer numero: "))
n2 = float(input("Escribir el segundo numero: "))
i = 1
resul = 0


if n >= n2 :
    while i <= n:
        resul = resul + n2
        i = i +1 

elif n2 > n:
    while i <= n2:
        resul = resul + n
        i = i +1 


print(resul)