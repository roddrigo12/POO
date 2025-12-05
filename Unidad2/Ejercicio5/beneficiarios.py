class Beneficiario:
    __dni: str
    __nombre: str
    __apellido: str
    __carrera: str
    __sigladeF: str
    __añocursa: int
    __promedio: float
    __codBeca: int
    
    def __init__(self, xdni, xnomb, xapell, xcarre, xsigla, xaño, xprom, xcod):
        self.__dni = xdni
        self.__nombre = xnomb
        self.__apellido = xapell
        self.__carrera = xcarre
        self.__sigladeF = xsigla
        self.__añocursa = xaño
        self.__promedio = float(xprom)
        self.__codBeca = xcod
    
    def get_nombre_benef(self):
        return self.__nombre
    
    def get_apellido_benef(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def get_codbeca(self):
        return self.__codBeca
    
    def get_sigladeF(self):
        return self.__sigladeF
    
    def __lt__ (self, otro):

        return self.__sigladeF > otro.get_sigladeF()

    def get_promedio(self):
        return self.__promedio
    
    