from medio import Medio
from programa import Programa
class Radio(Medio):
    __frecuencia: str
    __listaProgramas: list
    
    def __init__(self, nombre, audiencia, frecuencia):
        super().__init__(nombre, audiencia)
        self.__frecuencia = frecuencia
        self.__listaProgramas = []
    def getFrecuencia(self):
        return self.__frecuencia
    
    def agregarPrograma(self, nombre, horainicio, horafin):
        unPrograma = Programa(nombre, horainicio, horafin)
        self.__listaProgramas.append(unPrograma)
        
    def buscarporNombre(self, xprograma):
        i = 0
        encontrado = False
        while i < len(self.__listaProgramas) and not encontrado:
            if self.__listaProgramas[i].getNombre().strip().lower() == xprograma.strip().lower():
                encontrado = True
            else:
                i += 1
        if encontrado:
            print(f"Nombre del medio: {super().getNombre()} - Audiencia: {super().getAudiencia()} - Frecuencia: {self.__frecuencia}")
            print(f"Horario de inicio: {self.__listaProgramas[i].getHorainicio()}")
        return encontrado


        
    def CalculoIndice(self):
        audiencia = super().getAudiencia()
        cantprogramas = len(self.__listaProgramas)
        indice = (audiencia / cantprogramas)
        return indice
        
        
        
        
        