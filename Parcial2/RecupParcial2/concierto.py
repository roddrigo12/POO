from espectaculo import Espectaculo

class Concierto(Espectaculo):
    __banda: str
    __cantmusicos: int
    
    def __init__(self, nombre, fechafuncion, preciobase, banda, cantmusicos):
        super().__init__(nombre,fechafuncion, preciobase)
        self.__banda = banda
        self.__cantmusicos = cantmusicos
        
    def getBanda(self):
        return self.__banda
    def getCantmusicos(self):
        return self.__cantmusicos
    
    def CalculoPreciofinal(self):
        base = super().getPreciobase()
        cantmusicos = self.__cantmusicos
        precioentrada = base + (cantmusicos * 500)
        return precioentrada
    
    
    
    
    