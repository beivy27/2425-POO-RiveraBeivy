# Programa: Calculadora de Área de un Círculo
# Descripción: Este programa calcula el área de un círculo basado en el radio proporcionado por el usuario.
# Utiliza diferentes tipos de datos (integer, float, string, boolean) y sigue las convenciones de nomenclatura snake_case.

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): Radio del círculo.

    Retorna:
    float: Área del círculo.
    """
    pi = 3.14159  # Constante matemática Pi
    return pi * (radio ** 2)


# Función principal
def main():
    """
    Función principal del programa.
    Solicita al usuario el radio del círculo, valida el dato y calcula el área.
    """
    print("Bienvenido a la Calculadora de Área de un Círculo")

    # Entrada del usuario
    entrada_valida = False  # Booleano para validar la entrada
    while not entrada_valida:
        try:
            radio = float(input("Por favor, ingrese el radio del círculo (número positivo): "))
            if radio > 0:
                entrada_valida = True
            else:
                print("El radio debe ser un número positivo. Inténtelo nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    # Cálculo del área
    area = calcular_area_circulo(radio)

    # Salida de resultados
    print(f"El área del círculo con radio {radio} es: {area:.2f}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
