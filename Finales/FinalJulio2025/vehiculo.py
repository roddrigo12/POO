#RODRIGO ISMAEL GUEVARA VILLALVA E010 - 513  47.047.306  EXaMEN FINAL JULIO

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    __patente:str
    __capacidad: int
    __kmarecorrer: float
    
    def __init__(self, patente, cap, km):
        self.__patente = patente
        self.__capacidad = cap
        self.__kmarecorrer = km
        
    def getPatente(self):
        return self.__patente
    
    def getCapacidad(self):
        return self.__capacidad
    def getKmarecorrer(self):
        return self.__kmarecorrer
    
    @abstractmethod
    def Calculoconsumo(self):
        pass
    
    
    
    
    