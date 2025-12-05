from espectaculo import Espectaculo


class Obras(Espectaculo):
    __nombredirector: str
    __duracion: int
    
    def __init__(self, nombre, fechafuncion, preciobase, nombredirector, duracion):
        super().__init__(nombre, fechafuncion, preciobase)
        self.__nombredirector = nombredirector
        self.__duracion = duracion
        
    def getNombredirector(self):
        return self.__nombredirector
    
    def getDuracion(self):
        return self.__duracion
    
    def CalculoPreciofinal(self):
        preciobase = super().getPreciobase()
        duracion = self.__duracion
        precioentrada = preciobase + (duracion * 10)
        return precioentrada
    
    
    
    
    