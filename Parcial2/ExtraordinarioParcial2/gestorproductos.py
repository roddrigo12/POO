from productoonline import ProductoOnline
from productofisico import ProductoFisico
from producto import Producto
import csv
class GestorProductos:
    __listaProductos: list
    
    def __init__(self):
        self.__listaProductos = []
        
    def agregarProducto(self, unproducto):
        if isinstance(unproducto, Producto):
            self.__listaProductos.append(unproducto)
            print("Producto agregado. ")
        else:
            raise ValueError
        
    def cargarArchivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\ExtraParcial2\productos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            if fila[0] == "O":
                unonline = ProductoOnline(fila[1], fila[2], int(fila[3]), fila[4], int(fila[5]), fila[6], int(fila[7]), fila[8], int(fila[9]))
                try:
                    self.agregarProducto(unonline)
                except ValueError:
                    print("ERROR. No es un producto")
            elif fila[0] == "F":
                unfisico = ProductoFisico(fila[1], fila[2], int(fila[3]), fila[4], int(fila[5]), fila[10], float(fila[11]))
                try:
                    self.agregarProducto(unfisico)
                except ValueError:
                    print("ERRROR. no es un producto. ")
        archivo.close()
        
    def RealizarVenta(self, nombreProducto):
        i = 0
        encontrado = False
        while i < len(self.__listaProductos) and not encontrado:
            if self.__listaProductos[i].getNombre() == nombreProducto:
                encontrado = True
            else:
                i+= 1
        if encontrado == True:
            CantaVender = int(input(f"Ingrese cuantos {nombreProducto} quiere comprar. "))
            if self.__listaProductos[i].getStock() > CantaVender:
                print("Venta realizada. ")
                self.__listaProductos[i].setStock(CantaVender)
            else:
                print("No se puede realizar la venta por falta de stock. ")
        else:
            print("No se encontro el producto. ")
            
    #c
    def mostrarIncisoc(self):
        for producto in self.__listaProductos:
            if isinstance(producto, ProductoOnline):
                if producto.getPorcentajedescuento() > 10:
                    if producto.getEnviogratis() == "Si":
                        print(f"Nombre del producto: {producto.getNombre()}")
                        
    #d
    def mostrarIncisod(self):
        for producto in self.__listaProductos:
            producto.MostrarD()
            
            
            
            
            