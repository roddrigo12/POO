class Habitacion:
    __numero: int
    __piso: int
    __tipodehab: str
    __preciopornoche: float
    __disponibilidad: bool
    
    def __init__(self, numero, piso, tipodehab, preciopornoche, disponibilidad):
        self.__numero = numero
        self.__piso = piso
        self.__tipodehab = tipodehab
        self.__preciopornoche = preciopornoche
        self.__disponibilidad = disponibilidad
        
    def __str__(self):
        return (f"Habitacion Nro: {self.__numero}, Piso: {self.__piso}, Tipo: {self.__tipodehab}")
        
    def getNumero (self):
        return self.__numero
    
    def getPiso (self):
        return self.__piso
    
    def getTipodeHabitacion (self):
        return self.__tipodehab
    
    def getPrecioporNoche (self):
        return self.__preciopornoche
    
    def getDisponibilidad (self):
        return self.__disponibilidad
    
    def setDisponibilidad(self, disp):
        self.__disponibilidad = disp
        
        
        
        
        
        
   
    
    