#vamos a hacer listas
frutas = ["papaya", "manzana", "piña", "banano"] #Lista de 4 elementos
print(frutas[2]) #Toma la posicion 2 de la lista, 0, 1, 2, etc.
cuantos=len(frutas) #Da la longitud de la lista
print(cuantos)
print(frutas[1:3]) #Toma la posicion 1 (0, 1, 2, 3), y luego la 3 con el segundo barrido 1, 2, 3

frutas.append("uva")
print(frutas)
frutas2 = frutas.copy() #saca una copia de la lista
frutas3=frutas #quedan siendo la misma lista frutas4 y frutas, no se recomienda, sino sacarle copia
