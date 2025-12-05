
from abc import ABC, abstractmethod
class Espectaculo(ABC):
    __nombre: str
    __fechafuncion: str
    __preciobase: int
    
    def __init__(self, nombre, fechafuncion, preciobase):
        self.__nombre = nombre
        self.__fechafuncion = fechafuncion
        self.__preciobase = preciobase
        
    def getNombre(self):
        return self.__nombre
    def getFechafuncion(self):
        return self.__fechafuncion
    def getPreciobase(self):
        return self.__preciobase
    
    @abstractmethod
    def CalculoPreciofinal(self):
        pass
    
    def mostrarDatos(self):
        print(f"Nombre del Espectaculo: {self.__nombre} - Fecha: {self.__fechafuncion}")
        print(f"Precio Final: ${self.CalculoPreciofinal()}")
    
    
    
    
    
    
    
    
    