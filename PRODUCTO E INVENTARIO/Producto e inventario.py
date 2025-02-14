# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []  # Lista para almacenar productos

    def agregar_producto(self, producto):
        # Verificar que el ID sea único
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe en el inventario.")
        else:
            self.productos.append(producto)
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id_producto == id_producto:
                if nueva_cantidad is not None:
                    p.actualizar_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.actualizar_precio(nuevo_precio)
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


# Interfaz de usuario en consola
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
