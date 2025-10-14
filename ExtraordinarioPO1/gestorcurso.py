#Rodrigo Ismael Guevara Villalva E010-513 - 47047306
from curso import Curso
import csv

class GestorCurso:
    __cursos: list
    
    def __init__(self):
        self.__cursos = []
        
    def agregarCurso(self, uncurso):
        self.__cursos.append(uncurso)
        print("Curso agregado correctamente. ")
        
    def cargaArchivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\pythonn\ExtraPO1 2025\cursos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            uncurso = Curso(int(fila[0]), fila[1], int(fila[2]), int(fila[3]), int(fila[4]))
            self.agregarCurso(uncurso)
        archivo.close()
    #b    
    def mostrarIncisob(self, idcurso, gestorI):
        i = 0
        encontrado = False
        while i < len(self.__cursos) and encontrado == False:
            if self.__cursos[i].getIdcurso() == idcurso:
                encontrado = True
            else:
                i+= 1
        if encontrado == True:
            cantdiasdictado = self.__cursos[i].getCantdias()
            print(f"Denominacion: {self.__cursos[i].getDenominacion()}")
            gestorI.mostrarporporcentaje(idcurso, cantdiasdictado)
        else:
            print("No se encontro el curso del cual ingreso id. ")        
    
    #d        
    def listarporcurso(self, gestorI):
        gestorI.ordenar()
        for curso in self.__cursos:
            print("-"*50)
            print(f"Denominacion del curso: {curso.getDenominacion()} - Cupo: {curso.getCupomaximo()}")
            idcurso = curso.getIdcurso()
            cantdiasdictado = curso.getCantdias()
            gestorI.mostrarInscriptosaprobados(idcurso, cantdiasdictado)
            
            
            
            