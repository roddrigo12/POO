from plan import Plan

class Nodo:
    __plan: Plan
    __siguiente: object
    
    def __init__(self, plan):
        self.__plan = plan
        self.__siguiente = None
        
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self, plan):
        self.__siguiente = plan
        
    def getDato(self):
        return self.__plan
    
    
    
    