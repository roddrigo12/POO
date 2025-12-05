from paciente import Paciente

class Hospitalizado(Paciente):
    __numero: int
    __fechaingreso: str
    __diagnostico: str
    __cantdias: int
    __importedescart: int
    
    def __init__(self, nombre, apellido, email, numerotelefono, numero, fechaingreso, diagnostico, cantdias, importedesc):
        super().__init__(nombre, apellido, email, numerotelefono)
        self.__numero = numero
        self.__fechaingreso = fechaingreso
        self.__diagnostico = diagnostico
        self.__cantdias  = cantdias
        self.__importedescart = importedesc
        
    def getNumero(self):
        return self.__numero
    
    def getFechaingreso(self):
        return self.__fechaingreso
    def getDiagnostico(self):
        return self.__diagnostico
    def getCantdias(self):
        return self.__cantdias
    def getImportedescart(self):
        return self.__importedescart
    
    def Importeacobrar(self):
        valorconsulta = super().getValorconsulta()
        cantdiasinternado = self.__cantdias
        importedesc = self.__importedescart
        importeacobrar = valorconsulta + (cantdiasinternado * 150000 + importedesc)
        return importeacobrar
    
    
    
    
    