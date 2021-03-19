#3. Iterando un arreglo solamente 1 vez, escribir una función que elimine los 0, False y los None


def metodo(letra):
    e = 0
    for i in letra:
        if i == False or i == None or i == "0":
            del letra[e]
        e +=1
    print(letra)

metodo([False,"Hola","Pepe",True,None,"50","0","Si",False])

