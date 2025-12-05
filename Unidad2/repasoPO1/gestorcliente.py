import csv
from cliente import Cliente

class GestorCliente:
    __clientes : list
    
    def __init__(self):
        self.__clientes = []
        
    def agregar_cliente(self, uncliente):
        self.__clientes.append(uncliente)
        
    def carga_archivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\unidad2\repasoPO1\ClientesAbril2024.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            uncliente = Cliente(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]))
            self.agregar_cliente(uncliente)
            print(f"Cliente cargado.  Nombre: {uncliente.get_nombre()} - Apellido : {uncliente.get_apellido()}")
        archivo.close()
        #inciso A
    def buscar_cliente(self, xdni, gestorM):
        encontrado = 0
        i = 0
        long = len(self.__clientes)
        while i < long and encontrado == False :
            if self.__clientes[i].get_dni() == xdni:
                encontrado = True
                saldoanterior = self.__clientes[i].get_saldoanterior()
                nrotarjeta = self.__clientes[i].get_nrotarjeta()
                saldoactual = gestorM.obtener_saldoactual(nrotarjeta, saldoanterior)
            else:
             i = i + 1
        
        if encontrado == True:
            print(f"\n Listado de movimientos: ")
            NyA = self.__clientes[i].get_nombre() + " " + self.__clientes[i].get_apellido()
            print(f"Nombre : {NyA}         -       Tarjeta : {nrotarjeta}")
            print(f"Saldo anterior: {saldoanterior}")
            print("Movimientos :")
            gestorM.listar_movimientos(nrotarjeta)    
            print(f"\n Saldo actualizado: {saldoactual}")
            
        else:
            print("No se encontro el dni ingresado. ")
        #inciso B    
    def buscar_portarjeta(self, nrotarjeta, gestorM):
        i = 0
        encontrado = 0
        long = len(self.__clientes)
        while i < long and encontrado == False:
            if self.__clientes[i].get_nrotarjeta() == nrotarjeta:
                encontrado = True
                cantmovimientos = gestorM.obtener_movimiento(nrotarjeta)
                NyA = self.__clientes[i].get_nombre() + " " + self.__clientes[i].get_apellido()
            else:
                i = i + 1
        if encontrado == True:
            if cantmovimientos >= 1:
                print(f"El cliente {NyA} tuvo movimientos")
            elif cantmovimientos == 0:
                print("El cliente no tuvo movimientos en abril.")
                    
        else :
            print("El cliente con esa tarjeta no se encontro.")
        
            
            
  