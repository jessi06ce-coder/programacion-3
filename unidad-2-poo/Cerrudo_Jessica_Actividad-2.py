class Mascota:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
  def mostrar_datos(self):
    print("Nombre:", self.nombre)
    print("Edad:", self.edad)
    
mascota1 = Mascota("Luna", 4)
mascota1.mostrar_datos()

"""
1) El error principal es la ausencia de "self" para que guarde los atributos (tanto al inciar las funciones, como al establecer los atributos en sí)
2) dentro de los parentesis al crear e iniciar las funciones ya que sino no puede darle los atributos a los objetos incluso si dentro le ponemos el "self.nombre", que ya depaso
 aprovecho a aclarar que tambien faltaba allí para que se puedan guardar los valores así como tambien "llamar" a los valores almacenados en esos atributos en la funcion mostrar_datos.
 (Si en el print no aclaramos self.nombre al "llamar" no nos tomaría el atributo sino que buscaria una variable llamada nombre).
3) Se usa para dar los valores iniciales a los atributos (nombre, edad) de un objeto (mascota1).
4) La diferencia principal radica en la pertenencia: una variable no pertenece a un objeto, sin embargo, un atributo pertenece a un objeto.
"""
