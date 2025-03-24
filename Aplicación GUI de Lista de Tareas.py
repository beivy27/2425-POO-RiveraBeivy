import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Lista para almacenar las tareas
tareas = []

# ======== Funciones de manejo de eventos ========

def añadir_tarea(event=None):
    tarea = entrada.get().strip()
    if tarea:
        tareas.append({"texto": tarea, "completada": False})
        actualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")

def marcar_completada():
    seleccion = lista.curselection()
    if seleccion:
        indice = seleccion[0]
        tareas[indice]["completada"] = not tareas[indice]["completada"]
        actualizar_lista()
    else:
        messagebox.showinfo("Selecciona una tarea", "Selecciona una tarea para marcarla.")

def eliminar_tarea():
    seleccion = lista.curselection()
    if seleccion:
        indice = seleccion[0]
        del tareas[indice]
        actualizar_lista()
    else:
        messagebox.showinfo("Selecciona una tarea", "Selecciona una tarea para eliminarla.")

def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea in tareas:
        texto = tarea["texto"]
        if tarea["completada"]:
            texto += " ✔"
        lista.insert(tk.END, texto)

# ======== Componentes de la GUI ========

# Campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=10, padx=10, fill=tk.X)
entrada.bind("<Return>", añadir_tarea)  # Evento: tecla Enter

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

btn_añadir = tk.Button(frame_botones, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
lista = tk.Listbox(ventana, font=("Arial", 12), height=15)
lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Evento adicional opcional: doble clic en tarea para marcar como completada
lista.bind("<Double-Button-1>", lambda e: marcar_completada())

# Iniciar el loop principal
ventana.mainloop()
