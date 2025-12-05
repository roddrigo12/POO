#RODRIGO ISMAEL GUEVARA VILLALVA E010 - 513  47.047.306  EXaMEN FINAL JULIO

from nodo import Nodo
from colectivo import Colectivo
from electrico import Electrico
from bateria import Bateria
import csv

class GestorVehiculos:
    __comienzo: Nodo
    __indice: int
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
        
    def agregarVehiculo(self, unvehiculo):
        nuevonodo = Nodo(unvehiculo)
        nuevonodo.setSiguiente(self.__comienzo)
        self.__comienzo = nuevonodo
        self.__actual = nuevonodo
        self.__tope += 1
        print("Vehiculo agregado exitosamente.")
    #a    
    def cargarCSVvehiculos(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\ParaFinal\FinalJulio2025\Vehiculos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            if fila[0] == 'C':
                uncolectivo = Colectivo(fila[1], int(fila[2]), float(fila[3]), fila[4], int(fila[5]), fila[6])
                self.agregarVehiculo(uncolectivo)
            elif fila[0] == 'E':
                unelectrico = Electrico(fila[1], int(fila[2]), float(fila[3]), int(fila[4]), float(fila[6]))
                self.agregarVehiculo(unelectrico)
        archivo.close()
                        
    def cargarCSVbaterias(self):
        archivoB= open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\ParaFinal\FinalJulio2025\Baterias.csv")
        readerB = csv.reader(archivoB, delimiter=";")
        next(readerB)
        for filaB in readerB:
            patente = filaB[0]
            capacidad = int(filaB[1])
            carga = int(filaB[2])
            aux = self.__comienzo
            while aux is not None:
                vehiculo = aux.getDato()
                if isinstance(vehiculo, Electrico) and vehiculo.getPatente() == patente:
                    vehiculo.agregarBateria(patente, capacidad, carga ) #Composicion
                aux = aux.getSiguiente() 
    #b            
    def listarelectricos(self, distancia):
        print("Patente de vehiculos electricos que pueden realizar el recorrido con su energia disponible:")
        for vehiculo in self:
            if isinstance(vehiculo, Electrico):
                energiadisponible = vehiculo.getEnergiaBaterias()
                if energiadisponible >= distancia:
                    print(f"Patente del vehiculo: {vehiculo.getPatente()}")
                    print("-"*50)
    
    #c
    def mostrarTodos(self):
        for vehiculo in self:
            print(f"Patente: {vehiculo.getPatente()} - Cantidad de pasajeros: {vehiculo.getCapacidad()}")
            if isinstance(vehiculo, Electrico):
                print("El vehiculo es de tipo Electrico")
            elif isinstance(vehiculo, Colectivo):
                print("El vehiculo es de tipo Colectivo. ")
            print(f"Consumo para recorrer: {vehiculo.Calculoconsumo()}")
            print("-"* 50)
            
    #d
    def agregarnuevoColectivo(self, patente, capacidad, kmarecorrer, nombreempresa, capacidadcomb, tipocombustible, posicionlista):
        if posicionlista >= 0 and posicionlista < self.__tope:
            uncolectivo = Colectivo(patente, capacidad, kmarecorrer, nombreempresa, capacidadcomb, tipocombustible)
            nodonuevo = Nodo(uncolectivo)
            if posicionlista == 0:
                nodonuevo.setSiguiente(self.__comienzo)
                self.__comienzo = nodonuevo
            else:
                aux = self.__comienzo
                i = 0
                while aux is not None and i < posicionlista:
                    anterior = aux
                    aux = aux.getSiguiente()
                    i += 1
                nodonuevo.setSiguiente(aux)
                anterior.setSiguiente(nodonuevo)
            self.__tope += 1
            print(f"El vehiculo se agrego en la posicion {posicionlista} de la lista. ")
            self.mostrarListaV()
        else:
            raise IndexError
        
    def mostrarListaV(self):
        for vehiculo in self:
            print(f"Patente: {vehiculo.getPatente()}")
            
            
            
            