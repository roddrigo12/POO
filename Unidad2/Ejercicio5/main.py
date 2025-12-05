from gestorbecas import GestorBecas
from gestorbeneficiario import GestorBeneficiario

def menu():
    print()
    print("MENU DE OPCIONES: ".center(60))
    op= input('''
     a) Leer por teclado un tipo de Beca, e informar los beneficiarios de dicha beca y el
     importe total que debe disponer la Secretaría para el pago de dicha Beca   
 
     b) Leer por teclado un dni, informar si el beneficiario tiene más de una beca,
     mostrando nombre y apellido   
     
     c) Listar los beneficiarios, ordenados de mayor a menor por Facultad.
     
     d) Listar nombre, apellido y promedio de los estudiantes, que poseyendo un
        promedio mayor que 8, no poseen beca de ayuda económica. 
     
     z) SALIR
                          
     Su opcion --->    ''')
    
    return op

if __name__ == "__main__":
    gestorBec = GestorBecas()
    gestorBene = GestorBeneficiario()
    gestorBec.carga_archivo()
    gestorBene.carga_archivob()
    opcion = menu().lower()
    
    while opcion != 'z':
        if opcion == 'a':
            tipobeca = input("Ingrese un tipo de beca : Fotocopia , Transporte , Ayuda Economica : ")
            gestorBec.buscar_beca_portipo(tipobeca, gestorBene)
        
        elif opcion == 'b' :  
            xdni = input("Ingrese un dni : ")
            gestorBene.informar_cantbecas(xdni, gestorBec)    
        
        elif opcion == 'c' :
            gestorBene.listar_benef()
        
        elif opcion == 'd':
            gestorBene.listar_porprom()
              
        
        
        opcion = menu().lower()
            
            
            