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

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Cantidad inválida")
        elif cantidad <= self.__stock:
            self.__stock -= cantidad
            print("Venta realizada")
        else:
            print("Stock insuficiente")

    def reponer(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad
            print("Reposición realizada")
        else:
            print("Cantidad inválida")

    def mostrar_datos(self):
        print(self.nombre, "-", self.tipo, "- $", self.precio)
        print("Stock:", self.get_stock())

    def calcular_precio_final(self):
        # Los productos genéricos conservan su precio original.
        return self.precio
