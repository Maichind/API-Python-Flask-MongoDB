class Candidatos:
    def __init__(self, numero, cedula, nombre, apellido, partido, segundaVuelta):
        self.numero = numero
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.partido = partido
        self.segundaVuelta = segundaVuelta
    
    def toDBCollection(self):
        return {
            "numero": self.numero,
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "partido": self.partido,
            "segundaVuelta": self.segundaVuelta
        }