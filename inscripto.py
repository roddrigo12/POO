#Rodrigo Ismael Guevara Villalva E010-513 - 47047306
class Inscripto:
    __dni: str
    __apellidoynombre: str
    __idcurso: int
    __cantdiasasistio: int
    __notafinal: int
    
    def __init__(self, dni, apellidoynombre, idcurso, cantdiasasistio=0, notafinal=0):
        self.__dni = dni
        self.__apellidoynombre = apellidoynombre
        self.__idcurso = idcurso
        self.__cantdiasasistio = cantdiasasistio
        self.__notafinal = notafinal
    
    def getDni(self):
        return self.__dni
    def getApellidoynombre(self):
        return self.__apellidoynombre
    def getIdcurso(self):
        return self.__idcurso
    def getCantdiasasistio(self):
        return self.__cantdiasasistio
    def getNotafinal(self):
        return self.__notafinal
    
    def setCantdiasasistio(self):
        self.__cantdiasasistio += 1
        
    def setNotafinal(self, nota):
        self.__notafinal = nota
        
    def __lt__(self, otro):
        return self.__apellidoynombre < otro.getApellidoynombre()
    def __str__(self):
        return f"Apellido y Nombre: {self.__apellidoynombre} - Dni: {self.__dni} - Cantidad de dias que asistio: {self.__cantdiasasistio} - Nota final: {self.__notafinal}"
    
    
    
    