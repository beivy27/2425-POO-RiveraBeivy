import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
        self.listbox.pack(pady=10)

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.destroy())

    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor, ingresa una tarea.")

    def complete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            task_text = self.listbox.get(index)
            if not task_text.startswith("[✔] "):
                self.listbox.delete(index)
                self.listbox.insert(index, f"[✔] {task_text}")
        else:
            messagebox.showinfo("Seleccionar Tarea", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected[0])
        else:
            messagebox.showinfo("Seleccionar Tarea", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
