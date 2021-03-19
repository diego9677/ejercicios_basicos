#Escribir una función que aplane los arreglos en 1 nivel.
#Ejemplo arreglo1 = [1, 2, [3, 4], 5, [6, 7], 8] resultado = [1, 2, 3, 4, 5, 6, 7, 8]

arreglo1 = [1, 2, [3, 4], 5, [6, 7], 8]

def metodo (listaOriginal):
    lista=[]
    for i in listaOriginal:
        if isinstance(i,list):
            for e in i:
                lista.append(e) 
        else:
            lista.append(i)
    print(lista)

metodo(arreglo1)