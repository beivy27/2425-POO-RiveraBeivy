# Clase Libro que utiliza un constructor (__init__) y un destructor (__del__)
class Libro:
    def __init__(self, titulo, autor):
        """
        Constructor de la clase Libro.
        Inicializa los atributos del objeto con el título y el autor del libro.
        """
        self.titulo = titulo
        self.autor = autor
        print(f"Libro '{self.titulo}' por {self.autor} ha sido creado.")

    def __del__(self):
        """
        Destructor de la clase Libro.
        Realiza tareas de limpieza, como liberar recursos o informar al usuario.
        """
        print(f"El libro '{self.titulo}' por {self.autor} ha sido eliminado.")

# Clase ConexiónBaseDatos que simula una conexión y su cierre
class ConexiónBaseDatos:
    def __init__(self, nombre_bd):
        """
        Constructor de la clase ConexiónBaseDatos.
        Establece una conexión simulada a una base de datos.
        """
        self.nombre_bd = nombre_bd
        print(f"Conexión establecida con la base de datos '{self.nombre_bd}'.")

    def __del__(self):
        """
        Destructor de la clase ConexiónBaseDatos.
        Cierra la conexión simulada con la base de datos.
        """
        print(f"Conexión con la base de datos '{self.nombre_bd}' cerrada.")

# Programa principal que demuestra el uso de constructores y destructores
if __name__ == "__main__":
    # Creación de objetos usando constructores
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
    libro2 = Libro("1984", "George Orwell")

    db_conexion = ConexiónBaseDatos("BibliotecaVirtual")

    # Eliminación explícita de objetos (opcional, el recolector de basura lo hace automáticamente)
    del libro1
    del db_conexion

    print("Fin del programa.")
