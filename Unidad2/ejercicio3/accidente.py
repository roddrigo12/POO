class Accidente :
    __tabla : list
    
    def __init__(self):
        self.__tabla = []    ##Arreglo bidimensional
    
    def inicializar_Tabla (self, filas= 19, columnas=12):
        for i in range(filas):
            for j in range (columnas):
                self.__tabla [i][j]=0
                
    def cargar_tabla(self, departamento, mes, cantidad):
        self.__tabla [departamento-1][mes-1] += cantidad
    
    