x = int(input("Ingrese un numero: "))
if x == 15:
    print("el numero es 15")
    print("el numero no es 16")

while x <= 15:
    print(x)
    x += 1
    if x == 12:
        break 

tabla=int(input("Introduzca la tabla que desee imprimir: "))
i = 1
while i <= 10:
    #print(i*tabla)
    print(tabla, "*", i, "=", i*tabla)
    i += 1

Frutas=["banana","manzana","melon","pera","papaya"]
tamano = len(Frutas)
i=0
while i < tamano:
    print(Frutas[i])
    i += 1
    