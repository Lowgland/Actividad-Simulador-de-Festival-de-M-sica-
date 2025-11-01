from artista.clase_base import Artista

class Dj(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo=estilo

    def actuar(self):
        print(f"El Dj {self.nombre} mezcla temas del estilo: {self.estilo}, haciendo vibrar al publico")

    def presentarse(self):
        return super().presentarse() 
    
    def despedirse(self):
        return super().despedirse()
