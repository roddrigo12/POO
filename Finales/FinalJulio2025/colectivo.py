from vehiculo import Vehiculo

class Colectivo(Vehiculo):
    __nombreempresa: str
    __capacidad: int
    __tipocombustible: str

    def __init__(self, patente, cap, km, nombreempresa, capacidad, tipocombustible):
        super().__init__(patente, cap, km)
        self.__nombreempresa = nombreempresa
        self.__capacidad = capacidad   
        self.__tipocombustible = tipocombustible
        
        
    def getNombreempresa(self):
        return self.__nombreempresa
    def getCapacidad(self):
        return self.__capacidad
    def getTipocombustible(self):
        return self.__tipocombustible
    
    def Calculoconsumo(self):
        kmarecorrer = super().getKmarecorrer()
        if self.__tipocombustible == "gasoil":
            consumo = (kmarecorrer * 0.2)
        elif self.__tipocombustible == "gnc":
            consumo = (kmarecorrer * 15 / 100)
        return consumo
    
    
    
    
    