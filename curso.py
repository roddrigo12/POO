#Rodrigo Ismael Guevara Villalva E010-513 - 47047306
class Curso:
    __idcurso: int
    __denominacion: str
    __canthorasdia:int
    __cantdias: int
    __cupomaximo: int    
    
    def __init__(self, idcurso, denominacion, canthorasdia, cantdias, cupomaximo):
        self.__idcurso = idcurso
        self.__denominacion = denominacion
        self.__canthorasdia = canthorasdia
        self.__cantdias = cantdias
        self.__cupomaximo = cupomaximo
        
    def getIdcurso(self):
        return self.__idcurso
    def getDenominacion(self):
        return self.__denominacion
    def getCanthorasdia(self):
        return self.__canthorasdia
    def getCantdias(self):
        return self.__cantdias
    def getCupomaximo(self):
        return self.__cupomaximo
    
    
    
    