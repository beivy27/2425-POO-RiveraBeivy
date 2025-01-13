# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.__edad = edad

    # Getter para el atributo nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para el atributo nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def presentarse(self):
        return f"Hola, soy {self.__nombre} y tengo {self.__edad} años."

# Clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera

    # Sobrescritura del método presentarse (Polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.get_nombre()}, estudio {self.carrera}."

# Clase adicional para demostrar polimorfismo
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    # Sobrescritura del método presentarse (Polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.get_nombre()}, profesor de {self.asignatura}."

# Crear instancias de las clases
persona = Persona("Carlos", 35)
estudiante = Estudiante("Ana", 20, "Ingeniería en Sistemas")
profesor = Profesor("Dr. Fernández", 50, "Programación Orientada a Objetos")

# Demostración de encapsulación
print(persona.presentarse())
persona.set_nombre("Luis")  # Modificando el nombre usando el setter
print(persona.presentarse())

# Demostración de herencia y polimorfismo
print(estudiante.presentarse())
print(profesor.presentarse())
