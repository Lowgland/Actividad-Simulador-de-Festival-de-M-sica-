from abc import ABC, abstractmethod

class Artista(ABC):
    def __init__(self, nombre, genero, popularidad):
        self.nombre=nombre
        self.genero=genero
        self.popularidad=popularidad

    def presentarse(self):
        print(f"Hola! Soy {self.nombre}")

    @abstractmethod
    def actuar(self):
        pass

    def despedirse(self):
        print(f"El artista: {self.nombre} se despide")

