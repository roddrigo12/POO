from movimiento import Movimiento
import numpy as np
import csv

class GestorMovimiento:
    __dimension: int
    __cantidad: int
    __incremento: int
    __arregloMov: np.ndarray
    
    def __init__(self, xdim = 21):
        self.__dimension = xdim
        self.__cantidad = 0
        self.__incremento = 10
        self.__arregloMov = np.empty(self.__dimension, dtype=Movimiento)
        
    def carga_movimiento(self, unmov):
        if self.__dimension > self.__cantidad:
            self.__arregloMov[self.__cantidad] = unmov
            self.__cantidad += 1
    
    def carga_archivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\unidad2\repasoPO1\MovimientosAbril2024.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        
        for fila in reader:
            unmov = Movimiento(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]))
            self.carga_movimiento(unmov)
            print(f"Movimiento cargado. Fecha: {unmov.get_fecha()}, Descripcion: {unmov.get_descripcion()}")
        archivo.close()
        
    def obtener_saldoactual(self, nrotarjeta, saldoant) :
        saldoant = 0
        for i in range(self.__cantidad): #Inciso A
            if self.__arregloMov[i].get_nrotarjetaM() == nrotarjeta :
                if self.__arregloMov[i].get_tipodemov() == 'C':
                    creditos = self.__arregloMov[i].get_importe()
                    saldoant+= creditos
                elif self.__arregloMov[i].get_tipodemov() == 'P':
                    pago = self.__arregloMov[i].get_importe()
                    saldoant -= pago
        return saldoant
    
    def listar_movimientos(self, nrotarjeta):
       print(f"{'Fecha':<20} | {'Descripcion':<25} | {'$ Importe':<12}  | {'Tipo':<5}")
       for i in range(self.__cantidad):
            if self.__arregloMov[i].get_nrotarjetaM() == nrotarjeta:
                print(self.__arregloMov[i])
     #inciso B           
    def obtener_movimiento(self, nrotarjeta):
        cont = 0
        for i in range(self.__cantidad):
            if self.__arregloMov[i].get_nrotarjetaM() == nrotarjeta :
                cont += 1
        return cont
    

    def ordenar_portarjeta(self):
        self.__arregloMov.sort()
        print("Movimientos ordenados. ")
        for i in range(self.__cantidad):
            print(f"{self.__arregloMov[i]}  - {self.__arregloMov[i].get_nrotarjetaM()}")
                
           
