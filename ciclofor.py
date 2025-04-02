frutas = ["manzana", "pera", "melon", "patilla"]

#ciclo con while (necesita incremental)
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

#ciclo con for
for item in frutas:
    print(item)

# hacer rangos secuenciales
for x in range(2, 20, 2):
    print(x) 

#loops anidados
cosas = ["mesa", "zapato", "ventana"]
caract = ["grande", "bonito", "cuadrada"]
for x in cosas:
    for y in caract:
        print(x,y)
    
