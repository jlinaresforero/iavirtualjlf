#Hacemos un diccionario
# diccionario = {"marca": "Ford", "modelo": "1980", "Año": "1989"}
#mejor ponerlo en renglones
diccionario = {
    "marca": "Ford", 
    "modelo": "Sedan", 
    "Año": "1989"
    }
print(len(diccionario))
print(diccionario)
diccionario["marca"] = "Mazda" #cambiar valores
print(diccionario)
diccionario.update({"año": 2018}) # si no esta igual me agrega como nuevo elemento al final
print(diccionario)
diccionario.update({"Año": 2018})
print(diccionario)
dicc2 = diccionario.copy()
#dicc2.pop(2)   #Esta generando error, no se por que.
print(dicc2)