"""producto = {
    "nombre": input("Ingrese el nombre del producto: "),
    "precio": float(input("Ingrese el precio del producto: ")),
    "cantidad": int(input("Ingrese la cantidad disponible: ")),
    "categoria": input("Ingrese la categoría del producto: ")  # Cuarto componente
}

# Mostrar el diccionario resultante
print("\nInformación del producto:")
print(producto)"""

"""
#solucion con diccionario:
productos = {}  # Diccionario para almacenar los productos
contador = 1    # Contador para asignar un ID único a cada producto

while True:
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    # Guardar el producto en el diccionario con un ID único
    productos[contador] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    
    contador += 1  # Incrementar el ID para el siguiente producto

    if input("¿Agregar otro producto? (s/n): ").strip().lower() != 's':
        break

print("\nProductos registrados:")
for id_producto, datos in productos.items():
    print(f"ID {id_producto}: {datos}")"""

# Lista que almacenará todos los productos
inventario = []
flag = True

# Menú interactivo
while flag:
    print("===== Menú de Inventario =====")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Mostrar todos los productos")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        # Agregar producto
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario.append(producto)
        print(f"Producto '{nombre}' agregado al inventario.\n")
        #print(f(producto))
    
    elif opcion == "2":
        # Buscar producto
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for producto in inventario:
            if producto["nombre"].lower() == nombre_buscar.lower():
                print(f"Producto encontrado: {producto}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.\n")
    
    elif opcion == "3":
        # Mostrar todos los productos
        if len(inventario) == 0:
            print("El inventario está vacío.\n")
        else:
            print("Inventario de productos:")
            for producto in inventario:
                print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
        #    print()
            #flag = False

    elif opcion == "4":
        print("Saliendo del programa...")
        flag = False
        break
    
    else:
        print("Opción no válida. Intente de nuevo.\n")
        flag = False
