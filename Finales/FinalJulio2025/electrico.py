from vehiculo import Vehiculo
from bateria import Bateria
class Electrico(Vehiculo):
    __autonomiakm: int
    __listabaterias: list
    __eficienciakwh: float
    
    def __init__(self, patente, cap, km, autonomiakm, eficienciakwh):
        super().__init__(patente, cap, km)
        self.__autonomiakm = autonomiakm
        self.__eficienciakwh = eficienciakwh
        self.__listabaterias = []
        
    def getAutonomia(self):
        return self.__autonomiakm
    def getEficiencia(self):
        return self.__eficienciakwh
    
    def agregarBateria(self, patente, capacidad, carga):
        unabateria = Bateria(patente, capacidad, carga)   #Composicion
        self.__listabaterias.append(unabateria)
        print(f"Bateria agregada a vehiculo con patente {patente}")


    def Calculoconsumo(self):
        km = super().getKmarecorrer()
        eficiencia = self.__eficienciakwh
        consumo = km * eficiencia
        return consumo        
    
    def getEnergiaBaterias(self):
        sumador = 0
        for bateria in self.__listabaterias:
            sumador += bateria.energiadisponible()
        return sumador
    
    
    
    
    
    



