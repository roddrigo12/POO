
class Ingrediente:
    __nombre: str
    __cantidad: int 
    __unidad: str

    def __init__(self, nombre, cantidad, unidad):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__unidad = unidad

    def getNombre(self):
        return self.__nombre
    def getCantidad(self):
        return self.__cantidad
    def getUnidad(self):
        return self.__unidad
    def mostrarnombre(self):
        print(f"Nombre Ingrediente: {self.__nombre} - Cantidad: {self.__cantidad} - Unidad: {self.__unidad}")
    
    
 
        
    
    
    
    
    
    