#Verificar si es que un string es un palíndromo.

pali = input("Escriba para verficar: ")

nombre=pali[::-1]

if pali == nombre:
    print("Es palidromo")
else :
    print("no es palidromo")
