# Hacemos una calculadora con un menú de opciones
def sumar(a, b):
    #resultado = a + b
    return a + b

def multiplicar(a, b):
    resultado = a * b
    return resultado

def restar(a, b):
    resultado = a - b
    return resultado

def dividir(a, b):
    if b == 0:
        return "error, denominador no puede ser cero"
        print("Número no válido !")
    resultado = a / b
    return resultado

#Hacemos el menú de opciones
flag = True

while flag:
    print("===== Calcula la calculadora, escoge la operación =====")
    print("1. Sumar")
    print("2. Multiplicar")
    print("3. Restar")
    print("4. Dividir")
    print("5. Salir de la calculadora")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        x = int(input("ingrese primer numero: "))
        y = int(input("ingrese segundo numero: "))
        #sumar(x, y)
        print("resultado", sumar(x, y))

    elif opcion == "2":
        x = int(input("ingrese primer numero: "))
        y = int(input("ingrese segundo numero: "))
        print("resultado", multiplicar(x, y))

    elif opcion == "3":
        x = int(input("ingrese primer numero: "))
        y = int(input("ingrese segundo numero: "))
        print("resultado", restar(x, y))

    elif opcion == "4":
        x = int(input("ingrese primer numero: "))
        y = int(input("ingrese segundo numero: "))
        print("resultado", dividir(x, y))
        
    elif opcion == "5":
        print("Saliendo... gracias!")
        flag = False 

    else:
        print("Opción no válida. Intente de nuevo.\n")
        #flag = False

