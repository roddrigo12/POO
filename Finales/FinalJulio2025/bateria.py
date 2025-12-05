

class Bateria:
    __patente: str
    __marca = "CATL"
    __capacidad: int
    __cargaactual: int    
    
    def __init__(self, patente, capacidad, cargaactual):
        self.__patente = patente
        self.__capacidad = capacidad
        self.__cargaactual = cargaactual
        
    def getPatente(self):
        return self.__patente
    @classmethod
    def getMarca(self):
        return self.__marca
    
    def getCapacidad(self):
        return self.__capacidad
    def getCargaactual(self):
        return self.__cargaactual

    def energiadisponible(self):
        capacidadcarga = self.__capacidad
        cargaact = self.__cargaactual
        energia = (capacidadcarga - cargaact) / 10
        return energia
    
    
    
    
    