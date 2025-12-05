class Movimiento:
    __nrotarjetaM : int
    __fecha : str
    __descripcion: str
    __tipodemov: str
    __importe: int
    
    def __init__(self, nrotarjetaM, fecha, descripcion, tipodemov, importe):
        self.__nrotarjetaM = nrotarjetaM
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipodemov= tipodemov
        self.__importe = importe
    
    def __str__(self):
        return f"{self.__fecha:<20} | {self.__descripcion:<25} | ${self.__importe:<12.2f} | {self.__tipodemov:<5}"
        
    def get_nrotarjetaM(self):
        return self.__nrotarjetaM
    
    def get_fecha(self):
        return self.__fecha
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_tipodemov(self):
        return self.__tipodemov
    
    def get_importe(self):
        return self.__importe
    
    def __lt__ (self, otro):
        return (self.__nrotarjetaM) < ( otro.get_nrotarjetaM())
    
