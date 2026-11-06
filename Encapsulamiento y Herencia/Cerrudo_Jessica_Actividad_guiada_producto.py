

class Producto:
    def __init__(self, nombre, tipo, precio, stock):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.__stock = 0
        self.set_stock(stock)

    def get_stock(self):
        return self.__stock

    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Stock inválido")

    def mostrar_datos(self):
        print(self.nombre, "-", self.tipo, "- $", self.precio)
        print("Stock:", self.get_stock())

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Cantidad inválida")
        elif cantidad <= self.__stock:
            self.__stock -= cantidad
            print("Venta realizada")
        else:
            print("Stock insuficiente")

    # Agrega unidades al stock, siempre que la cantidad sea positiva.
    def reponer(self, cantidad):
        if cantidad > 0:
            self.__stock = self.__stock + cantidad
            print("Reposición realizada")
        else:
            print("Cantidad inválida")


class Alimento(Producto):
    def __init__(self, nombre, precio, stock, vencimiento):
        super().__init__(nombre, "Alimento", precio, stock)
        self.vencimiento = vencimiento

    def mostrar_vencimiento(self):
        print("Vence:", self.vencimiento)


class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, "Electrónico", precio, stock)
        self.garantia_meses = garantia_meses

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Garantía:", self.garantia_meses, "meses")






""" --------------------------------------------------
 1. Recordamos cómo funciona el stock
 Predicción:
 Stock inicial: 8 unidades.
 Después de vender(3): quedan 5.
 Después de vender(10): siguen quedando 5, porque no hay stock suficiente.
 Después de set_stock(-5): siguen quedando 5, porque el stock negativo es inválido.
 --------------------------------------------------------------------------------------
"""
producto = Producto("Arroz", "Alimento", 2000, 8)

print("PARTE 1: PRUEBAS DE STOCK")
producto.vender(3)
print("Stock después de vender 3:", producto.get_stock())

producto.vender(10)
print("Stock después de intentar vender 10:", producto.get_stock())

producto.set_stock(-5)
print("Stock después de intentar establecer -5:", producto.get_stock())



""" --------------------------------------------------
 2. Completamos y probamos el método reponer()
------------------------------------------------------
"""
print("\nPARTE 2: REPOSICIÓN")
producto.reponer(5)
print("Stock después de reponer 5:", producto.get_stock())

producto.reponer(-2)
print("Stock después de intentar reponer -2:", producto.get_stock())

"""
--------------------------------------------------------------------------------
--> Respuesta:
 La segunda reposición no debe modificar el stock porque la cantidad es negativa.
 El método solo permite reponer cantidades mayores que cero.
 ----------------------------------------------------------------------------
"""




""" --------------------------------------------------
# 3. Usamos la clase hija Alimento
------------------------------------------------------
"""
leche = Alimento("Leche", 1500, 10, "30/10/2026")

print("\nPARTE 3: OBJETO ALIMENTO")
# a) Mostrar sus datos.
leche.mostrar_datos()

# b) Mostrar su vencimiento.
leche.mostrar_vencimiento()

# c) Vender dos unidades.
leche.vender(2)

# d) Reponer cuatro unidades.
leche.reponer(4)

# e) Consultar y mostrar el stock final.
print("Stock final de leche:", leche.get_stock())


""" --------------------------------------------------
4. Explicación:
 1. El método reponer() se escribe dentro de la clase Producto.
 2. Leche se puede usar porque Alimento hereda de Producto.
 3. Si el stock es 8:
    - reponer(5) suma 5 unidades y deja el stock en 13.
    - set_stock(5) reemplaza el stock por 5 unidades.
-----------------------------------------------------------
"""
