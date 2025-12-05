from abc import ABC, abstractmethod

class Paciente(ABC):
    __nombre: str
    __apellido: str
    __email: str
    __numerotelefono: str
    __valorconsulta = 15000
    
    def __init__(self, nombre, apellido, email, numerotelefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__numerotelefono = numerotelefono
        
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getEmail(self):
        return self.__email
    def getNumerotelefono(self):
        return self.__numerotelefono
    @classmethod
    def getValorconsulta(cls):
        return cls.__valorconsulta
    
    @abstractmethod
    def Importeacobrar(self):
        pass
     
    @classmethod 
    def setValorconsulta(self, nuevovalor):
        self.__valorconsulta = nuevovalor
        
    
    
    
    