#Rodrigo Ismael Guevara Villalva E010-513 - 47047306
from inscripto import Inscripto
import numpy as np
import csv

class GestorInscripto:
    __dimension: int
    __incremento: int
    __cantidad: int
    __arregloInscriptos: np.ndarray
    
    def __init__(self):
        self.__dimension = 9
        self.__incremento= 4
        self.__cantidad = 0
        self.__arregloInscriptos = np.empty(self.__dimension, dtype=Inscripto)
    
    def agregarInscripto(self, uninscripto):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloInscriptos.resize(self.__dimension)
        self.__arregloInscriptos[self.__cantidad] = uninscripto
        self.__cantidad += 1
        print("Inscripto agregado correctamente. ")
        
    def cargaArchivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\pythonn\ExtraPO1 2025\inscripciones.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            uninscripto = Inscripto(fila[0], fila[1], int(fila[2]), int(fila[3]), int(fila[4]))
            self.agregarInscripto(uninscripto)
        archivo.close()
    #a    
    def buscarpordni(self, dni):
        posicion = -1
        encontrado = False
        i = 0
        while i < len(self.__arregloInscriptos) and encontrado == False:
            if self.__arregloInscriptos[i].getDni() == dni:
                encontrado = True
                posicion = i
            else:
                i += 1
        return posicion
    
    def buscarInscriptopordni(self, dni):
        i = self.buscarpordni(dni)
        if i >= 0:
            print(f"Apellido y Nombre: {self.__arregloInscriptos[i].getApellidoynombre()}")
            self.__arregloInscriptos[i].setCantdiasasistio()
            print("Cantidad de dias actualizada")
            print(f"Cantidad de dias que asistio: {self.__arregloInscriptos[i].getCantdiasasistio()}")
        else:
                print("No se encontro el dni ingresado. ")
            
    #b
    def mostrarporporcentaje(self, idcurso, cantdiasdictado):
        for inscripto in self.__arregloInscriptos:
            if inscripto.getIdcurso() == idcurso:
                porcentajeasist = (cantdiasdictado * 70) / 100
                if inscripto.getCantdiasasistio() > porcentajeasist:
                    print(f"Apellido y Nombre: {inscripto.getApellidoynombre()}")
                    print(f"Dni: {inscripto.getDni()}")
                    
    
    #c 
    
    def  incisoC(self, dniinscripto):
        i = self.buscarpordni(dniinscripto)
        if i >= 0:
            inscripto = self.__arregloInscriptos[i]
            print(f"Apellido y Nombre: {inscripto.getApellidoynombre()} - Dni: {dniinscripto}")
            print(f"Nota anterior: {inscripto.getNotafinal()}")
            nota = int(input("Ingrese nota final: "))
            inscripto.setNotafinal(nota)
            print(f"Ahora su nota final es: {inscripto.getNotafinal()}")
        else:
            print("No se encontro el inscripto con ese dni. ")
            
    #d
    def ordenar(self):
        self.__arregloInscriptos.sort()
        
    def mostrarInscriptosaprobados(self, idcurso, cantdiasdictado):
        for inscripto in self.__arregloInscriptos:
            porcentajeasist = (cantdiasdictado * 70) / 100
            if inscripto.getIdcurso() == idcurso:
                if inscripto.getNotafinal() >= 7 and inscripto.getCantdiasasistio() > porcentajeasist:
                    print(inscripto) 
            
            
            
            
            