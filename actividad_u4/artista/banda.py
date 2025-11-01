from artista.clase_base import Artista

class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes=integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra")

    def presentarse(self):
        return super().presentarse() 
    
    def despedirse(self):
        return super().despedirse()
