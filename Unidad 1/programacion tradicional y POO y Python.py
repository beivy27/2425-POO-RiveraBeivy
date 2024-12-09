# Programa basado en programación tradicional

def ingresar_temperaturas():
    """Función para ingresar las temperaturas diarias."""
    temperaturas = []
    for i in range(7):  # Una semana tiene 7 días
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Función para calcular el promedio semanal."""
    return sum(temperaturas) / len(temperaturas)

def main():
    print("Programa para calcular el promedio semanal del clima (Programación Tradicional)")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Llamar a la función principal
if __name__ == "__main__":
    main()
# Programa basado en programación orientada a objetos (POO)

class Clima:
    """Clase que representa la información diaria del clima."""
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Método para ingresar las temperaturas diarias."""
        for i in range(7):  # Una semana tiene 7 días
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Método para calcular el promedio semanal."""
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    print("Programa para calcular el promedio semanal del clima (POO)")
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Llamar a la función principal
if __name__ == "__main__":
    main()
