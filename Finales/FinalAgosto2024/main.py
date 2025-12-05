from gestorpacientes import GestorPacientes
from hospitalizado import Hospitalizado
from ambulatorio import Ambulatorio

def menu():
    print()
    print("MENU DE OPCIONES: ".center(60))
    op = input('''
     a. Insertar objetos al final de la colección. 
    
    b. Indicar la cantidad de pacientes hospitalizados, cuyo diagnóstico es
    neumonía; y la cantidad de pacientes ambulatorios que posee la clínica.
    
    c. Mostrar el importe cobrado por la clínica, a todos los pacientes.
    
    d. En el programa principal o en el menú, leer por teclado un valor entero,
    que representa una posición de la lista, e indicar qué tipo de paciente se
    encuentra en esa posición. 
    
    e. En el programa principal o en el menú, leer por teclado un nuevo valor
    de consulta, cambiarlo para todos los objetos de la lista   
    
    f. Salir       
        Su opcion -->  ''')
    return op

if __name__ == "__main__":
    gestorP = GestorPacientes()
    opcion = menu().lower()
    
    while opcion != 'f':
        if opcion == 'a':
            gestorP.cargarArchivo()
        elif opcion == 'b':
            gestorP.indicarcantidad()
        elif opcion == 'c':
            gestorP.mostrarimporte()
        elif opcion == 'd':
            posicion = int(input("Ingrese posicion de la lista: "))
            gestorP.mostrarporPosicion(posicion)
        elif opcion == 'e':
            nuevovalor = float(input("Ingrese nuevo valor de consulta: "))
            gestorP.cambiarvalor(nuevovalor)
            
        opcion = menu().lower()
        
        
        