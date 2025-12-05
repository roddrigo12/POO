import csv
from departamento import Departamento
from accidente import Accidente
class ManejadorDpto:
    __lista : list #Lista de departamentos

    def __init__(self):
        self.__lista = []
    
    def agregar_depto(self, depto):
        self.__lista.append(depto)
    
    def cargar_departamentos(self): #desde el csv
        archivo = open('Departamentos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unDepa = Departamento(fila[0], fila[1]) #Crea una instancia y llama al agregar enviando la instancia
                self.agregar_depto(unDepa)
        archivo.close()
        
    def mostrar_pordepto(self, mes, tabla):
        for departamento in self.__lista:
            print(f"El nombre del departamento es : {departamento} y la cantidad de accidentes es: {self.__lista[departamento][mes]}")
            