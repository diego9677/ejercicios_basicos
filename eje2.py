#2. Obtener el numero mayor de un arreglo, pero iterando este arreglo solo 1 vez. Ej [1,2,3,4,5,6,7,8,9]

numeros = [6, 8, 100, 2, 50, 1000, 25]
numeros.sort(reverse=True)

for i in numeros:
    print(i)
    break

