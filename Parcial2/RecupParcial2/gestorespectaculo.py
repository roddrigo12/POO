from obras import Obras
from concierto import Concierto
import csv

class GestorEspectaculo:
    __listaEspectaculos: list
    
    def __init__(self):
        self.__listaEspectaculos = []
        
    def agregarEspectaculo(self, unespec):
        fecha = unespec.getFechafuncion()
        i = 0
        encontrado = False
        while i < len(self.__listaEspectaculos) and encontrado == False:
            if self.__listaEspectaculos[i].getFechafuncion() == fecha:
                encontrado = True
                raise ValueError
            else:
             i+= 1
        if encontrado == False:
            self.__listaEspectaculos.append(unespec)
        
    def CargaArchivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\RecupParcial2\espectaculos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            if fila[0] == "C":
                unconcierto = Concierto(fila[1], fila[2], int(fila[3]), fila[6], int(fila[7]))
                self.agregarEspectaculo(unconcierto)
                print("Concierto agregado")
            elif fila[0] == "O":
                unaobra = Obras(fila[1], fila[2], int(fila[3]), fila[4], int(fila[5]))
                self.agregarEspectaculo(unaobra)
                print("Obra agregada")
        archivo.close()
        
    def incisoB(self):
        for espectaculo in self.__listaEspectaculos:
            espectaculo.mostrarDatos()
            
    def listarMayores10mil(self):
        for espectaculo in self.__listaEspectaculos:
            precioentrada = espectaculo.CalculoPreciofinal()
            if precioentrada > 10000:
                print(f"Nombre Espectaculo: {espectaculo.getNombre()} - Precio Entrada: {precioentrada}")
                
    def mostrarIncisod(self, CantidadMusicos):
        hay = False
        for espectaculo in self.__listaEspectaculos:
            if isinstance(espectaculo, Concierto):
                if espectaculo.getCantmusicos() > CantidadMusicos:
                    hay = True
                    print(f"Nombre: {espectaculo.getNombre()} - Fecha: {espectaculo.getFechafuncion()} - Precio Final: {espectaculo.CalculoPreciofinal()}")
                    
        if not hay:
            print("No hay conciertos que superen la cantidad de musicos ingresada.") 
                    
                    
                    
                    
                    