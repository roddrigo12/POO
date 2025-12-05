from vehiculo import Vehiculo
from vanes import Vanes
from autobus import Autobus
import csv

class GestorVehiculos:
    __listavehiculos: list
    
    def __init__(self):
        self.__listavehiculos = []
        
    def agregarVehiculo(self, unvehiculo):
        if isinstance(unvehiculo, Vehiculo):
            self.__listavehiculos.append(unvehiculo)
            print("Vehiculo agregado")
        else:
            raise TypeError
    
    def CargarArchivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\ParaFinal\PFinal\Parcial2ViejoHerencia\vehiculos.csv")
        reader = csv.reader(archivo, delimiter=",")
        next(reader)
        for fila in reader:
            if fila[0] == 'A':
                unautobus = Autobus(fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]), int(fila[7]), fila[8], fila[9])
                try:
                    self.agregarVehiculo(unautobus)
                except TypeError:
                    print("ERROR. EL OBJETO NO ES DE TIPO VEHICULO")
            elif fila[0] == 'V':
                unvan = Vanes(fila[1], fila[2], int(fila[3]), int(fila[4]),int( fila[5]), int(fila[6]), int(fila[7]), fila[10])
                try:
                    self.agregarVehiculo(unvan)
                except TypeError:
                    print("ERROR. EL OBJETO NO ES DE TIPO VEHICULO. ")
        archivo.close()
        
    def mostrarporPosicion(self, posicion):
        vehiculo = self.__listavehiculos[posicion]
        if isinstance(vehiculo, Autobus):
            print("El vehiculo en esa posicion de la lista es un autobus.")
        else:
            print("El vehiculo en esa posicion de la lista es un Van. ")
            
    #c
    def mostrarVehiculosporTipo(self):
        contVan = 0
        contAutobus = 0
        for vehiculo in self.__listavehiculos:
            if isinstance(vehiculo, Autobus):
                contAutobus+= 1
            else:
                contVan+= 1
        print(f"Hay {contAutobus} vehiculos del tipo Autobus, y {contVan} del tipo Van")
        
    def recorrercoleccion(self):
        for vehiculo in self.__listavehiculos:
            vehiculo.incisod()
        
        
        
        
        
        