"""
a = int(input("Ingrese su edad: "))
if a > 0 and a < 6:
    print("Eres un bebé")
    print("Adora a tu mamita")
elif a >= 6 and a < 12:
    print("Eres un niño")
    print("Empiezas a tener amigos para toda la vida")
elif a >= 12 and a < 18:
    print("Ya eres adolescente")
    print("Estas en los años maravillosos")
elif a >= 18 and a < 26:
    print("Ya eres mayor de edad, adulto joven")
    print("ya puedes votar")
elif a >= 26 and a < 60:
    print("ya puedes pagar tu casa")
    print("ya puedes casarte")
elif a >= 60 and a <= 130:
    print("Puedes planear tu retiro")
    print("Agradece cada dia de vida")
else:
    print("Edad incorrecta")
print(a)
"""
dia = int(input("Ingrese un numero entre 1 y 7: "))
if dia == 1:
    print("El dia de la semana es LUNES")
elif dia == 2:
    print("El dia de la semana es MARTES")
elif dia == 3:
    print("El dia de la semana es MIERCOLES")
elif dia == 4:
    print("El dia de la semana es JUEVES")
elif dia == 5:
    print("El dia de la semana es VIERNES")
elif dia == 6:
    print("El dia de la semana es SABADO")
elif dia == 7:
    print("El dia de la semana es DOMINGO")
else:
    print("Número incorrecto ! Intenta de nuevo")