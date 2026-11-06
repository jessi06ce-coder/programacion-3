from producto import Producto
from alimento import Alimento
from electronico import Electronico
from ropa import Ropa


# --------------------------------------------------
# CREACIÓN DE OBJETOS
# --------------------------------------------------

leche = Alimento("Leche", 2000, 10, "30/10/2026")
notebook = Electronico("Notebook", 800000, 4, 12)
cuaderno = Producto("Cuaderno", "Librería", 5000, 20)

remera = Ropa("Remera", 12000, 8, "M", "Remera")
pantalon = Ropa("Pantalón", 25000, 5, "40", "Pantalón")

productos = [leche, notebook, cuaderno, remera, pantalon]


# --------------------------------------------------
# EJERCICIO 1 Y 2: POLIMORFISMO Y PRECIOS FINALES
# --------------------------------------------------

print("===== PRECIOS FINALES =====")
for producto in productos:
    print(producto.nombre, "- Precio final: $", producto.calcular_precio_final())


# Mostrar los datos de cada producto.
print("\n===== DATOS DE LOS PRODUCTOS =====")
for producto in productos:
    producto.mostrar_datos()
    print("------------------------------")


""" --------------------------------------------------
 EJERCICIO 3: VENTAS, REPOSICIÓN Y STOCK
 Se realizan las operaciones sobre Notebook.
""" --------------------------------------------------

print("\n===== PRUEBAS DE STOCK: NOTEBOOK =====")

print("Stock inicial:", notebook.get_stock())

print("\nVenta válida de 2 unidades:")
print("Stock antes:", notebook.get_stock())
notebook.vender(2)
print("Stock después:", notebook.get_stock())

print("\nIntento de vender 5 unidades:")
print("Stock antes:", notebook.get_stock())
notebook.vender(5)
print("Stock después:", notebook.get_stock())

print("\nReposición de 3 unidades:")
print("Stock antes:", notebook.get_stock())
notebook.reponer(3)
print("Stock después:", notebook.get_stock())


# --------------------------------------------------
# INFORME COMPLETO: STOCK Y PRECIO FINAL
# --------------------------------------------------

print("\n===== INFORME DE PRODUCTOS =====")
valor_total_inventario = 0

for producto in productos:
    precio_final = producto.calcular_precio_final()
    stock = producto.get_stock()
    valor_producto = stock * precio_final
    valor_total_inventario += valor_producto

    print("Nombre:", producto.nombre)
    print("Tipo:", producto.tipo)
    print("Stock:", stock)
    print("Precio final por unidad: $", precio_final)
    print("Valor del stock: $", valor_producto)
    print("------------------------------")

print("VALOR TOTAL DEL INVENTARIO: $", valor_total_inventario)


# --------------------------------------------------
# PRODUCTO DE MAYOR PRECIO FINAL (SIN max())
# --------------------------------------------------

producto_mas_caro = productos[0]

for producto in productos:
    if producto.calcular_precio_final() > producto_mas_caro.calcular_precio_final():
        producto_mas_caro = producto

print("\n===== PRODUCTO DE MAYOR PRECIO FINAL =====")
print("Producto:", producto_mas_caro.nombre)
print("Precio final: $", producto_mas_caro.calcular_precio_final())


"""--------------------------------------------------
 PREGUNTAS PARA DEFENDER EL PROGRAMA
 --------------------------------------------------

 1. Heredar un método significa recibir y poder utilizar un método
    definido en la clase padre. Sobrescribirlo significa crear en la
    clase hija otro método con el mismo nombre, que reemplaza su
    comportamiento para esa clase.

 2. Porque todas las clases hijas heredan de Producto y tienen un
    método llamado calcular_precio_final(). Python ejecuta la versión
    correspondiente al objeto. Esto es polimorfismo.

 3. super().__init__(...) ejecuta el constructor de Producto e inicializa
    los atributos compartidos: nombre, tipo, precio y stock.

 4. vender(5) resta cinco unidades si hay stock suficiente.
    reponer(5) suma cinco unidades al stock.
    set_stock(5) reemplaza el stock actual por cinco unidades.

 5. Ejemplos:
    Encapsulamiento: self.__stock = 0
    Herencia: class Alimento(Producto):
    Polimorfismo: producto.calcular_precio_final() dentro del for,
    porque cada objeto utiliza su propia versión del método.

 6. main.py es el punto de entrada: importa las clases, crea objetos,
    organiza la lista, ejecuta pruebas y muestra resultados.
    Separamos las clases en archivos distintos para organizar el
    proyecto, facilitar su mantenimiento y separar responsabilidades.
"""
