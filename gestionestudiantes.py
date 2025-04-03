def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar nuevo estudiante")
    print("2. Calcular promedio de calificaciones")
    print("3. Mostrar estudiantes con promedio superior a un valor")
    print("4. Buscar estudiante")
    print("5. Salir del programa")

def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre completo del estudiante: ").strip().title()  # Convertir a mayúscula inicial
    edad = input("Ingrese la edad del estudiante: ").strip()
    if not edad.isdigit() or int(edad) <= 0:
        print("Edad inválida. Intente nuevamente.")
        return
    edad = int(edad)
    
    calificaciones = input("Ingrese las calificaciones separadas por comas (0.0 a 5.0): ").strip()
    try:
        calificaciones = [float(nota) for nota in calificaciones.split(",") if 0.0 <= float(nota) <= 5.0]
        if not calificaciones:
            raise ValueError
    except ValueError:
        print("Calificaciones inválidas. Intente nuevamente.")
        return
    
    estudiantes.append({"nombre": nombre, "edad": edad, "calificaciones": calificaciones})
    print(f"Estudiante {nombre} agregado exitosamente.")

def calcular_promedios(estudiantes):
    print("\n--- Promedio de Calificaciones ---")
    for estudiante in estudiantes:
        promedio = sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"]) if estudiante["calificaciones"] else 0
        print(f"{estudiante['nombre']}: {promedio:.2f}")

def mostrar_superiores(estudiantes):
    try:
        limite = float(input("Ingrese el valor límite del promedio: "))
    except ValueError:
        print("Valor límite inválido. Intente nuevamente.")
        return
    
    print("\n--- Estudiantes con promedio superior a", limite, "---")
    for estudiante in estudiantes:
        promedio = sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"]) if estudiante["calificaciones"] else 0
        if promedio > limite:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio: {promedio:.2f}, Calificaciones: {len(estudiante['calificaciones'])}")

def buscar_estudiante(estudiantes):
    termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()
    print("\n--- Resultados de la búsqueda ---")
    resultados = [est for est in estudiantes if termino in est["nombre"].lower()]
    if resultados:
        for estudiante in resultados:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificaciones: {estudiante['calificaciones']}")
    else:
        print("No se encontraron coincidencias.")

def main():
    estudiantes = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            calcular_promedios(estudiantes)
        elif opcion == "3":
            mostrar_superiores(estudiantes)
        elif opcion == "4":
            buscar_estudiante(estudiantes)
        elif opcion == "5":
            print("Gracias, vuelva pronto, ha sido un placer servirle.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()