# Lista que anida diccionarios de productos

listainventario = []
inventario = {}

# Menú interactivo
while True:
    print("===== Menú de Inventario =====")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Mostrar todos los productos")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        # Agregar producto
        nombre = input("Ingrese el nombre del producto: ")
        
        # Verificar si el producto ya está en el inventario
        if nombre in inventario:
            print(f"El producto '{nombre}' ya está en el inventario.")
            continuar = input("¿Desea actualizar la cantidad y precio? (s/n): ")
            if continuar.lower() == "s":
                precio = float(input("Ingrese el nuevo precio del producto: "))
                cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                inventario[nombre]["precio"] = precio
                inventario[nombre]["cantidad"] = cantidad
                print(f"Producto '{nombre}' actualizado.\n")
            else:
                print("No se realizó ninguna actualización.\n")
        else:
            # Si no está en el inventario, agregarlo
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}
            listainventario.append(inventario)
            print(f"Producto '{nombre}' agregado al inventario.\n")
    
    elif opcion == "2":
        # Buscar producto
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
        if nombre_buscar in inventario:
            producto = inventario[nombre_buscar]
            print(f"Producto encontrado: {nombre_buscar} -> Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
        else:
            print("Producto no encontrado.\n")
    
    elif opcion == "3":
        # Mostrar todos los productos
        if len(listainventario) == 0:
            print("El inventario está vacío.\n")
        else:
            print("Inventario de productos:")
            print(listainventario)
            break
    
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Intente de nuevo.\n")