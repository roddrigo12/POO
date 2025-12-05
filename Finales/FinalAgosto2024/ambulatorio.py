from paciente import Paciente

class Ambulatorio(Paciente):
    __historial: str
    __alergias: str
    __obrasocial: str
    
    def __init__(self, nombre, apellido, email, numerotelefono, historial, alergias, obrasocial):
        super().__init__(nombre, apellido, email, numerotelefono)
        self.__historial = historial
        self.__alergias = alergias
        self.__obrasocial = obrasocial
        
    def getHistorial(self):
        return self.__historial
    def getAlergias(self):
        return self.__alergias
    def getObrasocial(self):
        return self.__obrasocial
    
    def Importeacobrar(self):
        valorconsulta = super().getValorconsulta()
        descuento = 15000
        if self.__obrasocial == 'Provincia':
            plus = 5000
        elif self.__obrasocial == 'OSDE':
            plus= 2000
        else:
            plus = 10000
        importeacobrar = valorconsulta - descuento + plus
        return importeacobrar
    
    
    
    