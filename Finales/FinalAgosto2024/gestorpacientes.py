from nodo import Nodo
from hospitalizado import Hospitalizado
from ambulatorio import Ambulatorio
from paciente import Paciente
import csv

class GestorPacientes:
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
        
    def insertarFinal(self, unpaciente):
        nuevonodo = Nodo(unpaciente)
        if self.__comienzo is None:
            self.__comienzo = nuevonodo
        else:
            aux = self.__comienzo
            while aux is not None:
                anterior = aux
                aux = aux.getSiguiente()
            anterior.setSiguiente(nuevonodo)
        self.__actual = self.__comienzo
        self.__tope += 1
        print("Paciente agregado exitosamente. ")
    
    def cargarArchivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\ParaFinal\PFinal\FinalAgosto2024\pacientes.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            if fila[0] == 'O':
                unambulatorio = Ambulatorio(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
                self.insertarFinal(unambulatorio)
            elif fila[0] == 'H':
                unhospitalizado = Hospitalizado(fila[1], fila[2], fila[3], fila[4], int(fila[5]), fila[6], fila[7], int(fila[8]), int(fila[9]))
                self.insertarFinal(unhospitalizado)
        archivo.close()
        
    def indicarcantidad(self):
        contNeumonia = 0
        contAmbulatorios= 0
        for paciente in self:
            if isinstance(paciente, Hospitalizado):
                if paciente.getDiagnostico() == 'Neumonia':
                    contNeumonia += 1
            elif isinstance(paciente, Ambulatorio):
                contAmbulatorios += 1
        print(f"Cantidad de pacientes hospitalizados con neumonia: {contNeumonia} - Cantidad de ambulatorios en la clinica: {contAmbulatorios}")
        
        
    def mostrarimporte(self):
        for paciente in self:
            print(f"Paciente {paciente.getNombre()} {paciente.getApellido()}")
            print(f"Importe a cobrar: {paciente.Importeacobrar()}")
            print("-"*50)
            
    def mostrarporPosicion(self, posicion):
        if posicion >= 0 and posicion < self.__tope:
            i = 0
            aux = self.__comienzo
            while i < posicion:
                aux = aux.getSiguiente()
                i += 1
            if isinstance(aux.getDato(), Ambulatorio):
                print("El paciente de la posicion ingresada es de tipo Ambulatorio. ")
            elif isinstance(aux.getDato(), Hospitalizado):
                print("El paciente es de tipo Hospitalizado. ")
    
    def cambiarvalor(self, nuevovalor):
        for paciente in self:
            Paciente.setValorconsulta(nuevovalor)
            print(f"Ahora el valor de consulta es: {paciente.getValorconsulta()}")