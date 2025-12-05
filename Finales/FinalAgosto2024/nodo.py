from paciente import Paciente

class Nodo:
    __paciente: Paciente
    __siguiente: object
    
    def __init__(self, unpaciente):
        self.__paciente = unpaciente
        self.__siguiente = None
        
    def getSiguiente(self):
        return self.__siguiente
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getDato(self):
        return self.__paciente
    
    
    
    
    