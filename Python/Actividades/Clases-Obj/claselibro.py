#Ejercicios clases y objetos

#Clase Libro
class Libro:
    def __init__(self, titulo, autor, num_paginas, editorial, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion
        pass
    def descripcion(self):
        return f"'{self.titulo}' por {self.autor}, publicado en {self.anio_publicacion} por {self.editorial}, {self.num_paginas} páginas."
    #Indicamos si el libro es largo o corto
    def es_largo(self):
        if self.num_paginas > 300:
            return "largo"
        else:
            return "corto"

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417, "Editorial Sudamericana", 1967)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96, "Reynal & Hitchcock", 1943)

print(libro1.descripcion())
print(libro2.descripcion())
print(f"El libro '{libro1.titulo}' es considerado {libro1.es_largo()}.")
print(f"El libro '{libro2.titulo}' es considerado {libro2.es_largo()}.")