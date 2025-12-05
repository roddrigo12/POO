from nodo import Nodo
import csv
from plantelefonia import PlanTelefonia
from plantelevision import PlanTelevision
from plan import Plan

class GestorPlan:
    __comienzo: Nodo
    __indice : int
    __tope: int
    __actual: Nodo
    
    def __init__(self):
        self.__comienzo = None
        self.__indice = 0
        self.__tope = 0
        self.__actual = None
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
        
    def agregarPlan(self, xplan):
        nodo = Nodo(xplan)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        print("Plan cargado")
        
    def cargarArchivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\PracticandoFinalPOO\RecupParcial2-2024-Lista\planes.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            if fila[0] == 'M':
                unatelefonia = PlanTelefonia(fila[1], int(fila[2]), fila[3], int(fila[4]), fila[5], int(fila[6]))
                self.agregarPlan(unatelefonia)
            elif fila[0] == 'T':
                unatelevision = PlanTelevision(fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[7]), int(fila[8]))
                self.agregarPlan(unatelevision)
        archivo.close()
        
    def mostrarPlanes(self):
        actual = self.__comienzo
        while actual != None:
            print(actual.getDato())
            actual = actual.getSiguiente()
            
    
    #a    
    def mostrarPosicion(self, posicionlista):
        if posicionlista > 0 and posicionlista < self.__tope:
            indice = 0
            actual = self.__actual
            while actual is not None and indice < posicionlista:
                actual = actual.getSiguiente()
                indice += 1
            if indice == posicionlista and actual is not None:
                if isinstance(actual, PlanTelefonia):
                    print(f"El plan de la posicion {posicionlista} es de tipo Telefonia ") 
                else:
                    print(f"El plan de la posicion {posicionlista} es de tipo Television") 
        else:
            raise IndexError
        
    #b 
    def contarymostrarPlanes(self, cobertura):
        cont = 0
        for plan in self:
            if plan.getCobertura() == cobertura:
                cont += 1
        print(f"Hay {cont} planes correspondientes a la cobertura ingresada. ")
    #c    
    def mostrarmayores(self, CantCanalesInter):
        for plan in self:
            if isinstance(plan, PlanTelevision):
                if plan.getCantcanalesinter() > CantCanalesInter:
                    print(f"Nombre de la compañia: {plan.getNombrecompania()}")
    
    #d
    def mostrarD(self):
        for plan in self:
            plan.mostrarIncisod()
            
            
            
            
            
            