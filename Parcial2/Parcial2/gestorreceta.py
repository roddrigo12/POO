from receta import Receta
from ingrediente import Ingrediente
import csv

class GestorReceta:
    __listaRecetas: list

    def __init__(self):
        self.__listaRecetas = []

    def agregarReceta(self, unareceta):
        if isinstance(unareceta, Receta):
            self.__listaRecetas.append(unareceta)
            print("Receta cargada. ")
        else:
            raise TypeError

    def cargarArchivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\Parcial2\recetas.csv")
        reader = csv.reader(archivo, delimiter=";")
        i = -1
        for fila in reader:
            if len(fila) == 2:
                unareceta = Receta(fila[0], fila[1])
                try:
                    self.agregarReceta(unareceta)
                except TypeError:
                    print("El objeto a agregar no es una Receta. ")    
                i += 1
            elif len(fila) == 3:
                nombre = fila[0]
                cantidad = fila[1]
                unidad = fila[2]
                self.__listaRecetas[i].agregarIngrediente(nombre, cantidad, unidad)
        archivo.close()
        
    def mostrarTodasRecetas(self):
        for receta in self.__listaRecetas:
            print(f"Nombre de Receta: {receta.getNombre()}")
            print("-"*50)
        
        
    def BuscarRecporNombre(self, NombreRec):
        i = 0
        posicion = -1
        encontrado = False
        while i < len(self.__listaRecetas) and not encontrado:
            if self.__listaRecetas[i].getNombre() == NombreRec:
                encontrado = True
                posicion = i
            else:
                i+= 1
        return posicion
        
    def buscarposicion(self, posicion, i):
        encontrado = False
        if posicion >= 0 and posicion < len(self.__listaRecetas):
                self.__listaRecetas[i].mostrarIngredientes(posicion)
                encontrado = True
        else:
            raise IndexError
        
    def MostrarRecporIng(self, nombreingrediente):
        for receta in self.__listaRecetas:
             receta.buscarIngrediente(nombreingrediente)
                
                
                
                
                
        