from artista.clase_base import Artista

class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular=cancion_mas_popular

    def actuar(self):
        print(f"{self.nombre} canta su exito {self.cancion_mas_popular} con gran energia")

    def presentarse(self):
        return super().presentarse() 
    
    def despedirse(self):
        return super().despedirse()

    