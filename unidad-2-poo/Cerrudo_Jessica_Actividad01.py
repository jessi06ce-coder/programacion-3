"""
Entrega actividad 1
"""
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def Mostrar_Datos(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Páginas:", self.paginas)
        
    def es_largo(self):
      if self.paginas > 0:
        if self.paginas > 300:
            print("Libro extenso")
        else:
            print("Libro breve")
      else:
          print("Un libro no puede tener menos de 0 paginas o ser una letra")
          
Libro1 = Libro("Posesion", "Stephen King", 482)
Libro1.Mostrar_Datos()
Libro1.es_largo()

Libro2 = Libro("El Hombre de la Máscara de Hierro", "Alejandro Dumas", 298)
Libro2.Mostrar_Datos()
Libro2.es_largo()




"""
 El unico problema que tuve al hacerlo que hizo que tuviera que revisarlo, 
fue que a la hora de llamar lo métodos me olvidé de ponerlo los "()", y que tuve que basarme en el ejemplo 
para poder realizar el codigo (es decir, no es que con leer la actividad yo pensé todas las lineas de codigo,
me basé en el ejemplo de la clase Producto del pdf)
"""
    
