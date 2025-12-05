import csv
from beneficiarios import Beneficiario

class GestorBeneficiario():
    __beneficiarios : list
    
    def __init__(self):
        self.__beneficiarios = []
        
    def agregar_beneficiario(self, unbenef):
        self.__beneficiarios.append(unbenef)
        
    def carga_archivob(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\unidad2\Ejercicio5\beneficiarios.csv") 
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        
        for fila in reader:
            unbene = Beneficiario(fila[0], fila[1], fila[2], fila[3], fila[4], int(fila[5]), float(fila[6]), int(fila[7]))
            self.agregar_beneficiario(unbene)   
            print(f"Se agregó un beneficiario: {unbene.get_nombre_benef()}, {unbene.get_apellido_benef()}")
   
        archivo.close()    
        
    def get_cantidadbenef(self, idbec): #inciso a
     cont = 0
     for benef in self.__beneficiarios:
        if benef.get_codbeca() == idbec:
            print(f"El beneficiario es: {benef.get_nombre_benef()} {benef.get_apellido_benef()}")
            cont += 1
     print(f"Cantidad total de beneficiarios con la beca {idbec}: {cont}")
     
    def informar_cantbecas(self, xdni, gestorBec): #inciso b
        encontrado = False
        i = 0
        long = len(self.__beneficiarios)
        cont = 0
        while i < long and encontrado == False:
            if self.__beneficiarios[i].getDNI() == xdni:
                encontrado = True
            i = i + 1
            
        if encontrado == True :
            for j in range(long):
                if self.__beneficiarios[j].getDNI() == xdni:
                    cont += 1
                    NyA = self.__beneficiarios[j].get_nombre_benef()+ " " + self.__beneficiarios[j].get_apellido_benef()
                    
        if cont > 1:
            print(f"El beneficiario {NyA} tiene mas de una beca. ")
        else:
            print(f"El beneficiario {NyA} no tiene mas de una beca.")
            
    def listar_benef(self):
        self.__beneficiarios.sort()
        for beneficiario in self.__beneficiarios:
            NyA = beneficiario.get_nombre_benef() + " " + beneficiario.get_apellido_benef()
            print(f"{NyA}  -  {beneficiario.get_sigladeF()}")
        
    def listar_porprom(self):
        for estudiante in self.__beneficiarios:
            if estudiante.get_promedio() > 8:
                if estudiante.get_codbeca() != 4:
                    NyA = estudiante.get_nombre_benef() + " " + estudiante.get_apellido_benef()
                    prom = estudiante.get_promedio()
                    
                    print(f"{NyA} - {prom}" )
                
                    
        
            
            

            
        
    