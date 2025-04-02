"""nombre = input("Ingrese su nombre por favor: ")
apellido = input("Ingrese su apellido: ")
print("Gracias", nombre, " ", apellido)
# el input todo lo convierte a cadena de caracteres, incluso si son numeros
num1 = int(input("Ingrese su edad: "))
#con esto lo convierte a entero lo que se registre
#ahora hacemos una suma con valores ingresados por el usuario
num2 = int(input("Ingrese su numero favorito: "))
#ahora su podemos hacer operaciones
suma1 = num1 + num2
multiplica = num1 * num2
divide = num1 / num2
resta = num2 - num2
print(suma1)
print(multiplica)
print(divide)
print(resta)
#Fin del proceso
print("Gracias", nombre, " ", apellido, "y que tengan buena noche")
"""

#nombre=input("Ingrese un texto: ")
#cuantas=input("Ingrese el caracter a contar: ")
#nombre.upper()
#letra=(nombre.count(cuantas))
#print(letra)
#print(nombre.upper())

"""Listafrutas=input("Ingrese una lista de frutas: ") #pide la lista de terminos
fruta1=input("Cual quiere buscar: ") #pide el valor a buscar
fruta2=input("por cual la quieres reemplazar: ") #pide el valor a reemplazar
reemplazo=Listafrutas.replace(fruta1,fruta2) #método de reemplazo
print(reemplazo) #imprime la frase reemplazando el termino
"""

#ahora vamos a pregunar si es numerico el valor, devuelve valor booleano:  True, False.
"""info=input("Ingrese la información: ")
print(info.isnumeric())"""

#ahora vamos a hacer conteo de caracteres
"""Listafrutas=input("Ingrese una lista de frutas: ")
print(len(Listafrutas))
particion=split(Listafrutas)
print(particion)"""

"""
#creando listas
milista=[]
milista.append(input("Ingrese valor 1: "))
milista.append(input("Ingrese valor 2: "))
milista.append(input("Ingrese valor 3: "))
milista.append(input("Ingrese valor 4: "))
milista.append(input("Ingrese valor 5: "))
milista.append(input("Ingrese valor 6: "))
print(milista)
milista.sort()
print(milista)
sublist=milista[2:4]
print(sublist)
"""

cadena1=input("Ingrese una frase larguita: ")
print(cadena1)
#pregunta=input("¿Desea eliminar espacios en blanco?:") Aun no se como dar opciones ni leer respuestas
print(cadena1.strip()) #elimina espacios en blanco al final e inicio de la cadena
