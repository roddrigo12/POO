from plan import Plan

class PlanTelefonia(Plan):
    __tipollamadas: str
    __cantminutos: int
    
    def __init__(self, nombrecompania, duracion, cobertura, preciobase, tipollamadas, cantminutos):
        super().__init__(nombrecompania, duracion, cobertura, preciobase)
        self.__tipollamadas = tipollamadas
        self.__cantminutos = cantminutos
        
    def getTipollamadas(self):
        return self.__tipollamadas
    def getCantminutos(self):
        return self.__cantminutos
    
    def CalcularImporteFinal(self):
        preciobase = super().getPreciobase()
        if "internacionales" in self.__tipollamadas:
            importefinal = preciobase + (preciobase * 20 / 100)
        elif "locales" in self.__tipollamadas:
            importefinal = preciobase - (preciobase * 7.5 / 100)
        return importefinal

    
    def mostrarTipo(self):
        return type(self).__name__
    
    
    
    