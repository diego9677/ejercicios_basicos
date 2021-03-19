#Escribir una función que cuente la cantidad de veces que se repite una palabra.
palabra = ["rolo","si","hola","javier","si","hola","pepe","rolo","javier","si"]

def metodo(lista):
    numero = 0
    resultado =""
    for i in palabra:
        for e in palabra:
            if i == e :
                numero +=1
        resultado += i + " se repite " + str(numero) + " veces \n"
        numero = 0
        for h in palabra:
            if h == i :
                palabra.remove(h)
        palabra.insert(0,"")      
    print(resultado)

metodo(palabra)


























 
                                                                                                                                                                                                                                                                                                                                                                                                                    