import tkinter as tk
from tkinter import messagebox

# Función para agregar elementos a la lista
def agregar_elemento():
    elemento = entrada_texto.get()
    if elemento:
        lista.insert(tk.END, elemento)  # Agrega el elemento al final de la lista
        entrada_texto.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")  # Muestra una alerta si el campo está vacío

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Borra todos los elementos de la lista

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos - GUI Básica")  # Título de la ventana
ventana.geometry("400x300")  # Establece tamaño de la ventana

# Etiqueta para el campo de entrada
etiqueta = tk.Label(ventana, text="Ingrese un elemento:")
etiqueta.pack(pady=5)

# Campo de texto para ingresar datos
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botón para agregar un elemento a la lista
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack(pady=5)

# Etiqueta para la lista de elementos
titulo_lista = tk.Label(ventana, text="Elementos agregados:")
titulo_lista.pack(pady=5)

# Lista para mostrar elementos agregados
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=5)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar la ejecución de la aplicación
ventana.mainloop()
