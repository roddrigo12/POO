from abc import ABC, abstractmethod

class Medio(ABC):
    __nombre: str
    __audiencia: int
    
    def __init__(self, nombre, audiencia):
        self.__nombre = nombre
        self.__audiencia = audiencia
        
    def getNombre(self):
        return self.__nombre
    def getAudiencia(self):
        return self.__audiencia
    
    
    @abstractmethod
    def CalculoIndice(self):
        pass
    
    
    
    
    
    