from vehiculo import Vehiculo

class Vanes(Vehiculo):
    __tipocarroceria: str
    
    def __init__(self, marca, modelo, anio, capac, num, dist, tarifa, tipocarroceria):
        super().__init__(marca, modelo, anio, capac, num, dist, tarifa)
        self.__tipocarroceria = tipocarroceria
    
    def getTipocarroceria(self):
        return self.__tipocarroceria
    
    def getTarifaServicio(self):
        tarifabase = super().getTarifabase()
        if self.__tipocarroceria == "minivan":
            total = tarifabase - (tarifabase * 10 / 100)
        else:
            total = tarifabase + (tarifabase * 2.5 / 100)
        return total
    
    
    
    