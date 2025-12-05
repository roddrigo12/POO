#RODRIGO ISMAEL GUEVARA VILLALVA E010 - 513  47.047.306  EXaMEN FINAL JULIO
from gestorvehiculos import GestorVehiculos

def menu():
    print()
    print("MENU DE OPCIONES: ".center(60))
    op = input('''
     a. Leer desde el archivo “Vehículos.csv”, los datos de los distintos tipos de vehículo, y
    agregarlos al principio de la lista que implementa el Gestor el primer carácter de cada fila,
    Agregar las baterías a los vehículos eléctricos que correspondan (misma patente). 
    
    b. Leer por teclado una distancia en km, listar la patente de los vehículos eléctricos que pueden
    realizar el recorrido con la energía disponible de todas las baterías.
    
    c. Mostrar para todos los vehículos: patente, cantidad de pasajeros, tipo de vehículo y el
    consumo para recorrer.
    
    d. Leer por teclado los datos de un nuevo vehículo colectivo, y una posición de la lista, si la
    posición existe (mayor que 0, cabeza la lista, y menor que la cantidad de elementos de la
    lista), se agrega en la posición indicada, en caso de que la posición no exista se debe lanzar la
    excepción IndexError en el método del Gestor de Vehículos. Esta excepción debe controlarla
    en el programa principal.           
                
    e. SALIR           
               
        Su opcion -->  ''')
    return op

if __name__ == "__main__":
    gestorV = GestorVehiculos()
    opcion = menu().lower()
    
    while opcion != 'e':
        if opcion == 'a': #Siempre se debe ejecutar primero esta opcion
                gestorV.cargarCSVvehiculos()
                gestorV.cargarCSVbaterias()
        elif opcion == 'b':
            distancia = int(input("Ingrese una distancia: "))
            gestorV.listarelectricos(distancia)
            
        elif opcion == 'c':
            gestorV.mostrarTodos()  
            
        elif opcion == 'd':
            patente = input("Ingrese patente: ")
            capacidad = int(input("Ingrese capacidad de pasajeros: "))
            kmarecorrer= float(input("Ingrese cantidad de km a recorrer: "))
            nombreempresa = input("Ingrese nombre de empresa: ")
            capacidadcomb= int(input("Ingrese capacidad de combustible: "))
            tipocombustible = input("Ingrese tipo de combustible: (gasoil o gnc): ")
            posicionlista = int(input("Ingrese posicion de la lista(de 0 a 3): "))
            try:
                gestorV.agregarnuevoColectivo(patente, capacidad, kmarecorrer, nombreempresa, capacidadcomb, tipocombustible, posicionlista)
            except IndexError:
                print("ERROR: Posicion ingresada no valida. ")
        
        else:
            print("ERROR: OPCION INVALIDA. ")
            
            
        
        opcion = menu().lower()