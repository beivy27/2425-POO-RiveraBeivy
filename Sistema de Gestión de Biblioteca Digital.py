# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para atributos inmutables
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []  # Lista para almacenar libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.usuario_id}) - Libros prestados: {len(self.libros_prestados)}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.ids_usuarios = set()  # Conjunto para almacenar IDs únicos de usuarios

    # Métodos para libros
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya existe en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no se encontró en la biblioteca.")

    # Métodos para usuarios
    def registrar_usuario(self, usuario):
        if usuario.usuario_id not in self.ids_usuarios:
            self.usuarios[usuario.usuario_id] = usuario
            self.ids_usuarios.add(usuario.usuario_id)
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def eliminar_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            del self.usuarios[usuario_id]
            self.ids_usuarios.remove(usuario_id)
            print(f"Usuario con ID {usuario_id} eliminado.")
        else:
            print("Usuario no encontrado.")

    # Métodos para préstamos
    def prestar_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[usuario_id]
            libro = self.libros.pop(isbn)  # Remueve el libro del catálogo
            usuario.libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios:
            usuario = self.usuarios[usuario_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # Devuelve el libro a la biblioteca
                    print(f"Libro devuelto: {libro} por {usuario.nombre}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    # Métodos de búsqueda
    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, usuario_id):
        if usuario_id in self.usuarios:
            usuario = self.usuarios[usuario_id]
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []


# Pruebas del sistema
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Agregar libros
    libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "Ficción", "12345")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "67890")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("María López", "002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar y devolver libros
    biblioteca.prestar_libro("001", "12345")
    print("Libros prestados a Juan Pérez:", biblioteca.listar_libros_prestados("001"))
    biblioteca.devolver_libro("001", "12345")
    print("Libros prestados a Juan Pérez después de la devolución:", biblioteca.listar_libros_prestados("001"))

    # Buscar libros
    print("Resultados de búsqueda por autor 'Gabriel García Márquez':",
          biblioteca.buscar_libro("autor", "Gabriel García Márquez"))
