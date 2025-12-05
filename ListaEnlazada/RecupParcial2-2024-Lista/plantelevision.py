from plan import Plan

class PlanTelevision(Plan):
    __cantcanalesNacionales: int
    __cantcanalesInter: int
    
    def __init__(self, nombrecompania, duracion, cobertura, preciobase, cantcanalesn, cantcanalesi):
        super().__init__(nombrecompania, duracion, cobertura, preciobase)
        self.__cantcanalesNacionales = cantcanalesn
        self.__cantcanalesInter = cantcanalesi
  
    def getCantcanalesnacionales(self):
        return self.__cantcanalesNacionales
    
    def getCantcanalesinter(self):
        return self.__cantcanalesInter
    
    def CalcularImporteFinal(self):
        preciobase = super().getPreciobase()
        if self.__cantcanalesInter > 10:
            importefinal = preciobase + (preciobase * 15 / 100)
        else:
            importefinal = preciobase
        return importefinal
    
    def mostrarTipo(self):
        return type(self).__name__
    
    
    
    
    