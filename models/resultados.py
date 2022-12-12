class Resultados:
    def __init__(self, mesa, nombre, votos, nombre2, votos2):
        self.mesa = mesa
        self.nombre = nombre
        self.votos = votos
        self.nombre2 = nombre2
        self.votos2 = votos2
    
    def toDBCollection(self):
        return {
            "mesa": self.mesa,
            "nombre": self.nombre,
            "votos": self.votos,
            "nombre2": self.nombre2,
            "votos2": self.votos2
        }