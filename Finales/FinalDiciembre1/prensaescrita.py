from medio import Medio

class PrensaEscrita(Medio):
    __periodicidad: str
    __cantsecciones: int
    
    def __init__(self,nombre, audiencia, periodicidad, cant):
        super().__init__(nombre, audiencia)
        self.__periodicidad = periodicidad
        self.__cantsecciones = cant
        
    def getPeriodicidad(self):
        return self.__periodicidad
    def getCantsecciones(self):
        return self.__cantsecciones
    
    def CalculoIndice(self):
        if self.__periodicidad == 'mensual':
            audiencia = super().getAudiencia()
            indice = audiencia / self.__cantsecciones
        elif self.__periodicidad == 'semanal':
            audiencia = super().getAudiencia()
            indice = audiencia / (self.__cantsecciones * 4)
        return indice
        
    
    
    
    
    
    
    