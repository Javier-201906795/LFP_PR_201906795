class Producto_V:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        

    def nombre(self):
        return self.nombre
    
    def precio(self):
        return self.precio
    
    def cantidad(self):
        return self.cantidad

    def imprimir(self):
        resumen = {"Nombre": self.nombre, "Precio": self.precio, "Cantidad": self.cantidad}
        return resumen

    def setnombre(self, nombre):
        self.nombre = nombre
    
    def setprecio(self, precio):
        self.precio = precio
    
    def setcantidad(self, cantidad):
        self.cantidad = cantidad