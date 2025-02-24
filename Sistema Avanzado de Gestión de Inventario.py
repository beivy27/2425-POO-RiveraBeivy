import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                return producto.to_dict()
        return "Producto no encontrado."

    def mostrar_inventario(self):
        return [producto.to_dict() for producto in self.productos.values()]

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump([p.to_dict() for p in self.productos.values()], f)
        print("Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos_cargados = json.load(f)
                for p in productos_cargados:
                    self.agregar_producto(Producto(p['id'], p['nombre'], p['cantidad'], p['precio']))
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado, se iniciará un inventario nuevo.")


def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (presione Enter para omitir): ")
            precio = input("Nuevo precio (presione Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            print(inventario.buscar_producto(nombre))
        elif opcion == "5":
            print(inventario.mostrar_inventario())
        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
