from producto import Producto


class Ropa(Producto):
    def __init__(self, nombre, precio, stock, talle, categoria):
        super().__init__(nombre, "Ropa", precio, stock)
        self.talle = talle
        self.categoria = categoria

    def mostrar_talle(self):
        print("Talle:", self.talle)

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Categoría:", self.categoria)
        self.mostrar_talle()

    def calcular_precio_final(self):
        # Descuento del 15 %.
        return self.precio * 0.85
