from medio import Medio
from prensaescrita import PrensaEscrita
from radio import Radio
from programa import Programa
from datetime import datetime
import csv

class GestorMedios:
    __listaMedios: list
    
    def __init__(self):
        self.__listaMedios = []
        
    def agregarMedio(self, unmedio):
        self.__listaMedios.append(unmedio)
       
            
    def cargarCSV(self):
        archivoM = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\ParaFinal\PFinal\FinalDiciembre1\Medios.csv")
        readerM = csv.reader(archivoM, delimiter=",")
        for filaM in readerM:
            if filaM[0] == 'R':
                frecuencia = filaM[3]
                unaradio = Radio(filaM[1], int(filaM[2]), frecuencia)
                self.agregarMedio(unaradio)
            elif filaM[0] == 'P':
                unaprensa = PrensaEscrita(filaM[1], int(filaM[2]), filaM[3], int(filaM[4]))
                self.agregarMedio(unaprensa)
        archivoM.close()
    
    def cargarCSVprogramas(self):
        archivoP = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\ParaFinal\PFinal\FinalDiciembre1\Programas.csv")
        readerP = csv.reader(archivoP, delimiter=",")
        for filaP in readerP:
            i = 0
            encontrado = False
            while i < len(self.__listaMedios) and not encontrado:
                if isinstance(self.__listaMedios[i], Radio):
                    if self.__listaMedios[i].getFrecuencia() == filaP[0]:
                        encontrado = True
                        nombre= filaP[1]
                        horainiciostr = filaP[2]
                        horafinstr = filaP[3]
                        try:
                            horainiciodt = datetime.strptime(horainiciostr, "%H:%M").time()
                            horafindt= datetime.strptime(horafinstr, "%H:%M").time()
                            self.__listaMedios[i].agregarPrograma(nombre, horainiciodt, horafindt)
                        except ValueError:
                            print("Error. Horario inválido para el programa")     
                i += 1
                            
    def agregarManual(self):
        nombre = input("Ingrese nombre del medio: ")
        audiencia = int(input("Ingrese audiencia: "))
        tipo = input("Ingrese tipo de medio(Radio o Prensa): ")
        if tipo.lower() == 'radio':
            frecuencia = input("Ingrese frecuencia: ")
            unaradio = Radio(nombre, audiencia, frecuencia)
            self.agregarMedio(unaradio)
        elif tipo.lower() == 'prensa':
            periodicidad = input("Ingrese periodicidad: ")
            cantsecciones = int(input("Ingrese cantidad de secciones: "))
            unaprensa = PrensaEscrita(nombre, audiencia, periodicidad, cantsecciones )
            self.agregarMedio(unaprensa)
            
    def mostrarMedios(self):
        for medio in self.__listaMedios:
            print(f"Nombre: {medio.getNombre()} - Audiencia: {medio.getAudiencia()} ")
            
    def mostrarmedioPrograma(self, xprograma):
        encontrado = False
        i = 0
        while i < len(self.__listaMedios) and not encontrado:
            if isinstance(self.__listaMedios[i], Radio):
                encontrado = self.__listaMedios[i].buscarporNombre(xprograma)
            
            i+= 1
        if encontrado == True:
            print("Se encontro el programa.")
        else:
            print("No se encontro el programa ")
                
                
     #c           
    def indicarmedios(self):
       for medio in self.__listaMedios:
           print(f"Nombre del medio: {medio.getNombre()} - Audiencia Estimada: {medio.getAudiencia()} - Indice de Audiencia: {medio.CalculoIndice()}") 
           print("-"*100)   
                
                
            
            
            
            
            
            
            