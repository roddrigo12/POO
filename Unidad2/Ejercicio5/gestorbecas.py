import csv
from becas import Beca

class GestorBecas():
    __becas : list
    
    def __init__(self):
        self.__becas = []
        
    def agregar_beca(self, unabeca):
        self.__becas.append(unabeca)
        
    def carga_archivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\unidad2\Ejercicio5\becas.csv")  
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            unabeca = Beca(int(fila[0]), fila[1], int(fila[2]))
            self.agregar_beca(unabeca)  
            print("Se agrego una beca.", unabeca.get_tipo(), unabeca.get_id())
        archivo.close()
        
    def buscar_beca_portipo(self, xtipo, gestorbenef):
        i = 0
        encontrado = False
        long = len(self.__becas)

        while i < long and not encontrado:
            if self.__becas[i].get_tipo().lower() == xtipo.lower():
                idbeca = self.__becas[i].get_id()
                importe = self.__becas[i].get_importe()
                gestorbenef.get_cantidadbenef(idbeca)
                print(f"El importe de la beca de tipo {xtipo} es: {importe}")
                encontrado = True
            i += 1

        if not encontrado:
            print(f"No se encontró ninguna beca del tipo {xtipo}.")
            
            
            
            
    
        