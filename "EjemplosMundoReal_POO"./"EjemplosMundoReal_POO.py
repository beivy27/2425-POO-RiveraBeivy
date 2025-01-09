# Clase para representar una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (Ej. Individual, Doble)
        self.precio = precio  # Precio por noche
        self.disponible = True  # Estado de disponibilidad

    def reservar(self):
        """Marca la habitación como no disponible."""
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada exitosamente.")
        else:
            print(f"Habitación {self.numero} no está disponible.")

    def liberar(self):
        """Marca la habitación como disponible."""
        self.disponible = True
        print(f"Habitación {self.numero} ahora está disponible.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio} por noche - {estado}"


# Clase para gestionar las reservas del hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del hotel
        self.habitaciones = []  # Lista de habitaciones

    def agregar_habitacion(self, habitacion):
        """Añade una nueva habitación al hotel."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """Muestra todas las habitaciones del hotel."""
        print(f"Listado de habitaciones en el hotel {self.nombre}:")
        for habitacion in self.habitaciones:
            print(habitacion)

    def buscar_habitacion_disponible(self, tipo):
        """Busca y retorna la primera habitación disponible del tipo especificado."""
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo and habitacion.disponible:
                return habitacion
        return None


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear un hotel
    hotel = Hotel("Hotel Paraíso")

    # Agregar habitaciones al hotel
    hotel.agregar_habitacion(Habitacion(101, "Individual", 50))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
    hotel.agregar_habitacion(Habitacion(103, "Suite", 120))

    # Mostrar las habitaciones disponibles
    hotel.mostrar_habitaciones()

    # Reservar una habitación
    habitacion_a_reservar = hotel.buscar_habitacion_disponible("Doble")
    if habitacion_a_reservar:
        habitacion_a_reservar.reservar()

    # Mostrar las habitaciones después de la reserva
    hotel.mostrar_habitaciones()

    # Liberar la habitación
    habitacion_a_reservar.liberar()

    # Mostrar las habitaciones nuevamente
    hotel.mostrar_habitaciones()
