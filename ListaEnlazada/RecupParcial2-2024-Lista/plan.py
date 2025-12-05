from abc import ABC, abstractmethod

class Plan(ABC):
    __nombrecompania: str
    __duracionplan: int
    __cobertura: str
    __preciobase: int
    
    def __init__(self, nombrecompania, duracion, cobertura, preciobase):
        self.__nombrecompania = nombrecompania
        self.__duracionplan = duracion
        self.__cobertura = cobertura
        self.__preciobase = preciobase
        
    def getNombrecompania(self):
        return self.__nombrecompania
    def getDuracionplan(self):
        return self.__duracionplan
    def getCobertura(self):
        return self.__cobertura
    def getPreciobase(self):
        return self.__preciobase
    
    def __str__(self):
        return f"Nombre Compañia: {self.__nombrecompania} - Duracion plan: {self.__duracionplan} - Cobertura: {self.__cobertura}"
    
    @abstractmethod
    def CalcularImporteFinal(self):
        pass
    
    @abstractmethod
    def mostrarTipo(self):
        pass
    
    def mostrarIncisod(self):
        print(f"Tipo de plan: {self.mostrarTipo()} - Nombre de la Compañia: {self.__nombrecompania} - Duracion del plan: {self.__duracionplan} ")
        print(f"Cobertura geografica: {self.__cobertura} - Importe Final: ${self.CalcularImporteFinal()}")
        print("-"*50)
        
        
        
        
        
        