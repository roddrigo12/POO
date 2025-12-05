from abc import ABC, abstractmethod

class Vehiculo:
    __marca: str
    __modelo: str
    __aniofabricacion: str
    __capacidadpasajeros: int
    __numeroplazas: int
    __distanciarecorrida: int
    __tarifabase: int
    
    def __init__(self, marca, modelo, anio, capac, num, dist, tarifa):
        self.__marca = marca
        self.__modelo = modelo
        self.__aniofabricacion = anio
        self.__capacidadpasajeros = capac
        self.__numeroplazas = num
        self.__distanciarecorrida = dist
        self.__tarifabase= tarifa
        
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getAniofabricacion(self):
        return self.__aniofabricacion
    def getCapacidad(self):
        return self.__capacidadpasajeros
    def getNumeroplazas(self):
        return self.__numeroplazas
    def getDistanciarecorrida(self):
        return self.__distanciarecorrida
    def getTarifabase(self):
        return self.__tarifabase
    
    @abstractmethod
    def getTarifaServicio(self):
        pass

    def incisod(self):
        print(f"Modelo: {self.__modelo} - Año de fabricacion: {self.__aniofabricacion} - Capacidad: {self.__capacidadpasajeros}")
        print(f"Tarifa del Servicio: {self.getTarifaServicio()}")
        
        
        
        