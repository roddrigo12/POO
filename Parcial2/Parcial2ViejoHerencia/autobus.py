from vehiculo import Vehiculo

class Autobus(Vehiculo):
    __tiposervicio: str
    __turno: str
    
    def __init__(self, marca, modelo, anio, capac, num, dist, tarifa, tiposervicio, turno):
        super().__init__(marca, modelo, anio, capac, num, dist, tarifa)
        self.__tiposervicio = tiposervicio
        self.__turno = turno
        
    def getTiposervicio(self):
        return self.__tiposervicio
    def getTurno(self):
        return self.__turno
    
    def getTarifaServicio(self):
        tarifabase = super().getTarifabase()
        if self.__turno == "noche" and self.__tiposervicio == "turismo":
            total = tarifabase + (tarifabase * 20 / 100)
        else:
            total = tarifabase + (tarifabase * 5 / 100)
        return total





