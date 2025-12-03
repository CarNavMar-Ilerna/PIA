import pickle
import os


class Empleado:
    _contador_empleados = 0
    
    def __init__(self, empresa, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo
        Empleado._contador_empleados += 1
        self._num_empleado = Empleado._contador_empleados
        self._empresa = empresa
    
    def get_nombre(self):
        return self._nombre
    
    def get_sueldo(self):
        return self._sueldo
    
    def get_num_empleado(self):
        return self._num_empleado
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_sueldo(self, sueldo):
        self._sueldo = sueldo
    
    def __str__(self):
        return f"Empleado #{self._num_empleado}: {self._nombre}, Sueldo: {self._sueldo}€"
    
    def aumentar_sueldo(self, porcentaje):
        aumento = self._sueldo * (porcentaje / 100)
        self._sueldo += aumento
        return self._sueldo
    
    def despedir(self):
        self._empresa.despide_empleado(self._num_empleado - 1)


class Empresa:
    def __init__(self, nombre, tamaño):
        self._nombre = nombre
        self._tamaño = tamaño
        self._empleados = [None] * tamaño
    
    def get_nombre(self):
        return self._nombre
    
    def get_tamaño(self):
        return self._tamaño
    
    def get_empleado(self, indice):
        if 0 <= indice < self._tamaño:
            return self._empleados[indice]
        return None
    
    def despide_empleado(self, indice):
        if 0 <= indice < self._tamaño:
            empleado_despedido = self._empleados[indice]
            self._empleados[indice] = None
            guardar_empleados(self)
            return empleado_despedido
        return None
    
    def nuevo_empleado(self, nombre, sueldo):
        empleado = Empleado(self, nombre, sueldo)
        for i in range(self._tamaño):
            if self._empleados[i] is None:
                self._empleados[i] = empleado
                guardar_empleados(self)
                return empleado
        print(f"No hay espacio disponible en la empresa {self._nombre}")
        return None
    
    def __str__(self):
        empleados_activos = [emp for emp in self._empleados if emp is not None]
        return f"Empresa: {self._nombre}, Tamaño: {self._tamaño}, Empleados activos: {len(empleados_activos)}"


def guardar_empleados(empresa):
    empleados_activos = [emp for emp in empresa._empleados if emp is not None]
    with open('MisEmpleados.dat', 'wb') as archivo:
        pickle.dump(empleados_activos, archivo)


def cargar_empleados(empresa):
    if os.path.exists('MisEmpleados.dat'):
        with open('MisEmpleados.dat', 'rb') as archivo:
            empleados = pickle.load(archivo)
            for i, emp in enumerate(empleados):
                if i < empresa._tamaño:
                    emp._empresa = empresa
                    empresa._empleados[i] = emp
                    if emp._num_empleado > Empleado._contador_empleados:
                        Empleado._contador_empleados = emp._num_empleado
            return len(empleados)
    return 0


def main():
    print("=== Sistema de Gestión de Empresa y Empleados ===\n")
    
    empresa = Empresa("TechCorp", 10)
    
    num_cargados = cargar_empleados(empresa)
    
    if num_cargados == 0:
        print("No se encontró archivo de empleados. Creando empleados iniciales...\n")
        empresa.nuevo_empleado("Ana García", 30000)
        empresa.nuevo_empleado("Carlos López", 35000)
        empresa.nuevo_empleado("María Rodríguez", 32000)
        empresa.nuevo_empleado("Juan Martínez", 38000)
        empresa.nuevo_empleado("Laura Sánchez", 33000)
        print("5 empleados iniciales creados.\n")
    else:
        print(f"Se cargaron {num_cargados} empleados desde el archivo.\n")
    
    print(empresa)
    print("\n--- Lista de empleados actuales ---")
    for i in range(empresa.get_tamaño()):
        emp = empresa.get_empleado(i)
        if emp is not None:
            print(emp)
    
    print("\n--- Dando de alta a 2 empleados adicionales ---")
    emp1 = empresa.nuevo_empleado("Pedro Fernández", 31000)
    emp2 = empresa.nuevo_empleado("Sofía Ruiz", 34000)
    if emp1:
        print(f"Añadido: {emp1}")
    if emp2:
        print(f"Añadido: {emp2}")
    
    print("\n--- Lista actualizada de empleados ---")
    for i in range(empresa.get_tamaño()):
        emp = empresa.get_empleado(i)
        if emp is not None:
            print(emp)
    
    print("\n--- Dando de baja a un empleado ---")
    empleado_a_despedir = empresa.get_empleado(2)
    if empleado_a_despedir:
        print(f"Despidiendo a: {empleado_a_despedir}")
        empleado_a_despedir.despedir()
    
    print("\n--- Lista final de empleados ---")
    for i in range(empresa.get_tamaño()):
        emp = empresa.get_empleado(i)
        if emp is not None:
            print(emp)
    
    print(f"\n{empresa}")
    print("\nTodos los cambios han sido guardados en 'MisEmpleados.dat'")


if __name__ == "__main__":
    main()
