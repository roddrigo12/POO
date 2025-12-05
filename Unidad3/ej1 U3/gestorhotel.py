from clasehotel import Hotel
import csv
class GestorHotel:
    __listaH: list
    
    def __init__(self):
        self.__listaH = []
        
    def carga_archivo (self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\unidad3\ej1 U3\Hoteles.csv")
        reader = csv.reader (archivo, delimiter=';')
        i = 0
        for fila in reader:
            if len(fila) == 3: #Detecta si tiene 3 columnas, es un hotel
                hotel = Hotel (fila[0], fila[1], fila[2])
                self.__listaH.append(hotel)
                i += 1
            else: 
                numero = int(fila[0])
                piso = int(fila[1])
                tipodehab = fila[2]
                precioxnoche = float(fila[3])
                if fila[4] == "True":
                    disp = True
                elif fila[4] == "False":
                    disp = False
                self.__listaH[i-1].agregarhabitacion(numero, piso, tipodehab, precioxnoche, disp) #Diferencia entre composicion y agregacion
        archivo.close()
    
    def buscarhot (self, xhotel):
        i = 0
        valor = -1
        encontrado = False
        long = len(self.__listaH)
        while encontrado == False and i < long :
            print(f"Comparando con: '{self.__listaH[i].getNombre()}'")
            print(f"Entrada del usuario: '{xhotel}'")

            if self.__listaH[i].getNombre() == xhotel:
                valor = i
                encontrado = True
                print ("Hotel encontrado.")
            else:
                i += 1
        return valor
    
    def incisoA (self, i):

        numero = int(input("Ingrese numero de habitacion: "))
        piso = int(input("Ingrese piso de habitacion: "))
        tipodehab = input("Ingrese tipo de habitacion: ")
        precioxnoche= float(input("Ingrese precio por noche: "))
        disp = True
        self.__listaH[i].agregarhabitacion(numero, piso, tipodehab, precioxnoche, disp)
        print ("Habitacion agregada correctamente.")
        self.__listaH[i].mostrarhotel()
        
    def incisob(self, i):
        self.__listaH[i].reservar_habitacion()
        
    def incisoc(self, i):
        self.__listaH[i].liberar_habitacion()
        
    def incisod(self, i):
        self.__listaH[i].mostrarporTipo()
        
    def incisoe(self, i):
        self.__listaH[i].contarHabitacionesLibres()


                    


