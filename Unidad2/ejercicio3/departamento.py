class Departamento:
    __numero: int 
    __nombre : str
    
    def __init__(self, nro, nomb):
        self.__numero = nro
        self.__nombre = nomb
        
    def __str__(self):
        return f"Nombre de departamento: {self.__nombre} , Numero de departamento : {self.__numero}" 
    
    def get_Nombre(self):
        return self.__nombre
    
    def set_Nombre(self, otronomb): 
        self.__nombre = otronomb
        
    def get_numero(self):
        return self.__numero
    
    def set_numero(self, otronum):
        self.__numero =  otronum
        