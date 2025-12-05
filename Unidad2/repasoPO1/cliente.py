class Cliente:
    __nombre: str
    __apellido: str
    __dni: str
    __nrotarjeta: int
    __saldoant: int
    
    def __init__(self, nombre, apellido, dni, nrotarjeta, saldoant):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__nrotarjeta = nrotarjeta
        self.__saldoant = saldoant
        
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_dni(self):
        return self.__dni
    
    def get_nrotarjeta(self):
        return self.__nrotarjeta
    
    def get_saldoanterior(self):
        return self.__saldoant
    

        
        
        