#definir funciones
def suma():  #suma es un nombre que yo le puse
    print("Johana mucho ánimo")
    print("Super tu vida")

def suerte():
    suerte = int(input("Ingrese su número de suerte: "))
    print(suerte)
#para llamar a la función

suma() #asi se llama la función
suerte() 

#ahora llamando funciones con parámetros y argumentos
def lasuma(a,b):
    resultado = a + b
    return resultado

x = int(input("Ingrese primer numero: "))
y = int(input("Ingrese segundo valor: "))

lasuma(x, y)