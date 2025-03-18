import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesario para el DatePicker
import csv


# Función para agregar eventos a la agenda
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        guardar_eventos()
        entry_fecha.set_date("")
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")


# Función para eliminar eventos seleccionados
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        respuesta = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar el evento seleccionado?")
        if respuesta:
            for item in seleccionado:
                tree.delete(item)
            guardar_eventos()
    else:
        messagebox.showwarning("Selección Vacía", "Selecciona un evento para eliminar.")


# Función para guardar eventos en un archivo CSV
def guardar_eventos():
    with open("agenda.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha", "Hora", "Descripción"])
        for row in tree.get_children():
            writer.writerow(tree.item(row)['values'])


# Función para cargar eventos desde un archivo CSV
def cargar_eventos():
    try:
        with open("agenda.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                tree.insert("", "end", values=row)
    except FileNotFoundError:
        pass


# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Contenedor principal
frame_principal = tk.Frame(root, padx=10, pady=10)
frame_principal.pack(expand=True, fill="both")

# Frame para entrada de datos
frame_entrada = tk.Frame(frame_principal)
frame_entrada.pack(pady=10, fill="x")

# Etiquetas y campos de entrada
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada, width=30)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Frame para botones
frame_botones = tk.Frame(frame_principal)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).pack(side="left", padx=5)
tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento).pack(side="left", padx=5)
tk.Button(frame_botones, text="Salir", command=root.quit).pack(side="left", padx=5)

# Frame para lista de eventos
frame_lista = tk.Frame(frame_principal)
frame_lista.pack(fill="both", expand=True)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(fill="both", expand=True)

# Cargar eventos guardados
cargar_eventos()

# Ejecutar aplicación
root.mainloop()
