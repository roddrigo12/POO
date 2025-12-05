from datetime import datetime
class Programa:
    __nombre: str
    __horainicio: datetime
    __horafin: datetime
    
    def __init__(self, nombre, horainicio, horafin):
        self.__nombre = nombre
        self.__horainicio = horainicio
        self.__horafin = horafin
        
    def getNombre(self):
        return self.__nombre
    def getHorainicio(self):
        return self.__horainicio
    def getHorafin(self):
        return self.__horafin
    
    
    
    
    
    