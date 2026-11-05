"""
 EL mensaje que el envie a la IA (o prompt, como prefiera llamarle) fue:
Necesito que en python que me hagas un programa en el que crees una clase Alumno con los atributos nombre, curso y nota; que tenga un
método llamado "mostrar_datos()" y otro método denominado "esta_aprobado()" que indique si el alumno aprobó
considerando que la nota mínima es 6 (teniendo en cuenta que el usuario no puede ingresar carateres, 
ni numeros negativos ni dejar espacios en blanco). También crea dos objetos y prueba los métodos para verificar su funcionalidad, eficiencia y eficacia.
Posteriormente quiero una explicación práctica, clara, conscisa y detallada respecto al codigo que crees para realizar la actividad.

El resultado que me dio fue

             |
             |
             |
             |
             |
             V
"""

class Alumno:
    def __init__(self, nombre, curso, nota):
        self.nombre = nombre
        self.curso = curso
        self.nota = nota

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Curso: {self.curso}")
        print(f"Nota: {self.nota}")

    def esta_aprobado(self):
        if self.nota >= 6:
            print("Estado: Aprobado")
        else:
            print("Estado: Desaprobado")


# Función para validar texto
def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: no puede dejar el campo vacío.")
        else:
            return texto


# Función para validar nota
def validar_nota():
    while True:
        try:
            nota = float(input("Ingrese la nota: "))

            if nota < 0:
                print("Error: la nota no puede ser negativa.")
            else:
                return nota

        except ValueError:
            print("Error: debe ingresar un número válido.")


# Creación del primer objeto
print("=== Alumno 1 ===")
nombre1 = validar_texto("Ingrese el nombre: ")
curso1 = validar_texto("Ingrese el curso: ")
nota1 = validar_nota()

alumno1 = Alumno(nombre1, curso1, nota1)

print("\n=== Alumno 2 ===")
nombre2 = validar_texto("Ingrese el nombre: ")
curso2 = validar_texto("Ingrese el curso: ")
nota2 = validar_nota()

alumno2 = Alumno(nombre2, curso2, nota2)

# Prueba de métodos
print("\n--- DATOS DEL ALUMNO 1 ---")
alumno1.mostrar_datos()
alumno1.esta_aprobado()

print("\n--- DATOS DEL ALUMNO 2 ---")
alumno2.mostrar_datos()
alumno2.esta_aprobado()




"""

10) Considero que las partes correctas son la clase Alumno, el __init__, los métodos solicitados,
las validaciones (que si bien no eran parte del ejercicio me parecian indispensables para el programa:
que el usuario no pueda dejar espacios vacíos, ni poner letras o numeros negativos), pero... modificaría
la validación del nombre y del curso, ya que actualmente en nombre y curso podria poner solamente numeros,
lo cual estaría mal o incompleto. La solucion qeu la IA me dio a este problema (aunqeu no es el único) fue:

|
|
|
v

"""
def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: no puede dejar el campo vacío.")
        elif not texto.replace(" ", "").isalpha():
            print("Error: solo se permiten letras.")
        else:
            return texto
        
        
        
"""
Otra mejora podria ser que no solo no permita valores menores a cero, sino que no permita valores como 
500, 1560, 9824213, que actualmente si lo aceptaria el programa. Segun la IA, una solucion a esto sería 
corrigiendo el if de la validacion de notas: "if nota < 0 or nota > 10:"
"""



""" 

11) __init__ crea y carga los datos del objeto, mientras que self indica a qué objeto pertenecen esos datos.

"""
