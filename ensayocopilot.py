print("Hola mundo")
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Ejemplo de uso
celsius = float(input("Introduce los grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
