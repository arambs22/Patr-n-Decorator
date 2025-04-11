from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def get_descripcion(self):
        pass

    @abstractmethod
    def get_precio(self):
        pass

class Espresso(Bebida):
    def get_descripcion(self):
        return "Espresso"

    def get_precio(self):
        return 2.00

class BebidaDecorador(Bebida):
    def __init__(self, bebida):
        self._bebida = bebida

class Leche(BebidaDecorador):
    def get_descripcion(self):
        return self._bebida.get_descripcion() + " + Leche"

    def get_precio(self):
        return self._bebida.get_precio() + 0.75

class Canela(BebidaDecorador):
    def get_descripcion(self):
        return self._bebida.get_descripcion() + " + Canela"

    def get_precio(self):
        return self._bebida.get_precio() + 0.75

class Chocolate(BebidaDecorador):
    def get_descripcion(self):
        return self._bebida.get_descripcion() + " + Chocolate"

    def get_precio(self):
        return self._bebida.get_precio() + 1.00

pedido = Chocolate(Canela(Leche(Espresso())))
print("Pedido:", pedido.get_descripcion())
print("Precio: $", pedido.get_precio())