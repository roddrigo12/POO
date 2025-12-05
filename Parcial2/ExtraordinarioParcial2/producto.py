from abc import ABC, abstractmethod

class Producto(ABC):
    __codigo: str
    __nombre: str
    __preciobase: int
    __descripcion: str
    __stock: int
    
    def __init__(self, codigo, nombre, preciobase, descripcion, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__preciobase = preciobase
        self.__descripcion = descripcion
        self.__stock = stock
        
    def getCodigo(self):
        return self.__codigo    
        
    def getNombre(self):
        return self.__nombre
    def getPreciobase(self):
        return self.__preciobase
    def getDescripcion(self):
        return self.__descripcion
    def getStock(self):
        return self.__stock
    def setStock(self, cantvendida):
        self.__stock -= cantvendida
    
    @abstractmethod
    def calcularPrecioFinal(self):
        pass
    
    @abstractmethod
    def get_tipo(self):
        pass
    
    def MostrarD(self):
        print(f"Nombre: {self.__nombre} - Precio Total: {self.calcularPrecioFinal()} - Tipo: {self.get_tipo()}")
        
        
        
        
        
        