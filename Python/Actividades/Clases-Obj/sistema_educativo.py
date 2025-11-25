# Sistema de Institución Educativa

class Persona:
    """Clase base para todas las personas de la institución"""
    
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"


class Estudiante(Persona):
    """Clase derivada para estudiantes"""
    
    def __init__(self, nombre, edad, genero, curso, promedio=0.0):
        super().__init__(nombre, edad, genero)
        self.curso = curso
        self.promedio = promedio
        self.asignaturas = []
    
    def informacion(self):
        info_base = super().informacion()
        return f"{info_base}\nRol: Estudiante\nCurso: {self.curso}\nPromedio: {self.promedio}"
    
    def estudiar(self, asignatura=None):
        if asignatura:
            return f"{self.nombre} está estudiando {asignatura}"
        return f"{self.nombre} está estudiando"
    
    def hacer_examen(self, asignatura, nota):
        self.asignaturas.append({"asignatura": asignatura, "nota": nota})
        return f"{self.nombre} ha realizado el examen de {asignatura} - Nota: {nota}"
    
    def calcular_promedio(self):
        if not self.asignaturas:
            return 0.0
        total = sum(asig["nota"] for asig in self.asignaturas)
        self.promedio = round(total / len(self.asignaturas), 2)
        return self.promedio
    
    def mostrar_calificaciones(self):
        if not self.asignaturas:
            return f"{self.nombre} no tiene calificaciones registradas"
        
        resultado = f"Calificaciones de {self.nombre}:\n"
        for asig in self.asignaturas:
            resultado += f"  - {asig['asignatura']}: {asig['nota']}\n"
        resultado += f"Promedio: {self.calcular_promedio()}"
        return resultado


class Profesor(Persona):
    """Clase derivada para profesores"""
    
    def __init__(self, nombre, edad, genero, asignatura, años_experiencia=0):
        super().__init__(nombre, edad, genero)
        self.asignatura = asignatura
        self.años_experiencia = años_experiencia
        self.estudiantes = []
    
    def informacion(self):
        info_base = super().informacion()
        return f"{info_base}\nRol: Profesor\nAsignatura: {self.asignatura}\nExperiencia: {self.años_experiencia} años"
    
    def enseñar(self, tema=None):
        if tema:
            return f"El profesor {self.nombre} está enseñando {tema} en la clase de {self.asignatura}"
        return f"El profesor {self.nombre} está enseñando {self.asignatura}"
    
    def calificar_estudiante(self, estudiante, nota):
        return f"{self.nombre} ha calificado a {estudiante} con {nota} puntos"
    
    def preparar_clase(self):
        return f"{self.nombre} está preparando la clase de {self.asignatura}"
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        return f"{estudiante} ha sido agregado a la clase de {self.asignatura}"


class Director(Persona):
    """Clase derivada para directores"""
    
    def __init__(self, nombre, edad, genero, institucion, años_cargo=0):
        super().__init__(nombre, edad, genero)
        self.institucion = institucion
        self.años_cargo = años_cargo
        self.departamentos = []
    
    def informacion(self):
        info_base = super().informacion()
        return f"{info_base}\nRol: Director\nInstitución: {self.institucion}\nAños en el cargo: {self.años_cargo}"
    
    def supervisar(self, area=None):
        if area:
            return f"El director {self.nombre} está supervisando el área de {area}"
        return f"El director {self.nombre} está supervisando la institución {self.institucion}"
    
    def convocar_reunion(self, asunto):
        return f"{self.nombre} ha convocado una reunión sobre: {asunto}"
    
    def tomar_decision(self, decision):
        return f"El director {self.nombre} ha decidido: {decision}"
    
    def evaluar_desempeño(self, persona):
        return f"{self.nombre} está evaluando el desempeño de {persona}"
    
    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)
        return f"Departamento de {departamento} agregado a {self.institucion}"


# Ejemplo de uso
if __name__ == "__main__":
    print("=== SISTEMA DE INSTITUCIÓN EDUCATIVA ===\n")
    
    # Crear personas
    estudiante1 = Estudiante("Ana García", 16, "Femenino", "2º Bachillerato")
    estudiante2 = Estudiante("Carlos López", 17, "Masculino", "2º Bachillerato")
    
    profesor1 = Profesor("Dr. Juan Martínez", 45, "Masculino", "Matemáticas", 20)
    profesor2 = Profesor("Dra. María Rodríguez", 38, "Femenino", "Física", 12)
    
    director = Director("Lic. Roberto Sánchez", 55, "Masculino", "Instituto Cervantes", 8)
    
    # Probar estudiante
    print("--- ESTUDIANTE ---")
    print(estudiante1.informacion())
    print(estudiante1.saludar())
    print(estudiante1.estudiar("Matemáticas"))
    print(estudiante1.hacer_examen("Matemáticas", 9.5))
    print(estudiante1.hacer_examen("Física", 8.7))
    print(estudiante1.hacer_examen("Química", 9.2))
    print(estudiante1.mostrar_calificaciones())
    print()
    
    # Probar profesor
    print("--- PROFESOR ---")
    print(profesor1.informacion())
    print(profesor1.saludar())
    print(profesor1.enseñar("Ecuaciones diferenciales"))
    print(profesor1.preparar_clase())
    print(profesor1.agregar_estudiante("Ana García"))
    print(profesor1.agregar_estudiante("Carlos López"))
    print(profesor1.calificar_estudiante("Ana García", 9.5))
    print()
    
    # Probar director
    print("--- DIRECTOR ---")
    print(director.informacion())
    print(director.saludar())
    print(director.supervisar("Departamento Académico"))
    print(director.agregar_departamento("Ciencias"))
    print(director.agregar_departamento("Humanidades"))
    print(director.convocar_reunion("Mejora del rendimiento académico"))
    print(director.tomar_decision("Implementar nuevas tecnologías en las aulas"))
    print(director.evaluar_desempeño("Dr. Juan Martínez"))
    print()
    
    # Demostrar polimorfismo
    print("=== POLIMORFISMO - INFORMACIÓN DE TODOS ===")
    personas = [estudiante1, estudiante2, profesor1, profesor2, director]
    
    for persona in personas:
        print(f"\n{persona.informacion()}")
        print(persona.saludar())
