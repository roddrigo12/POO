from ingrediente import Ingrediente

class Receta:
    __nombre: str
    __categoria: str
    __listaingredientes: list 

    def __init__(self, nombre, categoria):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__listaingredientes = []
    
    def getNombre(self):
        return self.__nombre
    def getCategoria(self):
        return self.__categoria

    def agregarIngrediente(self, nombre, cantidad, unidad):
        uningrediente =  Ingrediente(nombre, cantidad, unidad)
        self.__listaingredientes.append(uningrediente) #Se crea aca la instancia en la composicion
        print("Ingrediente cargado")
    
    def mostrarIngredientes(self, posicion):
        self.__listaingredientes[posicion].mostrarnombre()
        
    def buscarIngrediente(self, nombreingrediente):
        i = 0
        encontrado = False
        while i < len(self.__listaingredientes) and not encontrado:
            if self.__listaingredientes[i].getNombre() == nombreingrediente:
                encontrado = True
            else:
                i+= 1
        if encontrado == True:
            print(f"Nombre de la receta que contiene el ingrediente : {self.getNombre()}")
        
        
        
        
        
        
        
        


    