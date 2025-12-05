from gestormedios import GestorMedios

def menu():
    print()
    print("MENU DE OPCIONES: ".center(60))
    op = input('''
     a) Agregar medios de comunicación a la instancia de la clase de control definida antes.
     b) Leer por teclado el nombre de un programa de radio y muestre el nombre del medio de
     comunicación, la frecuencia y el horario de inicio de transmisión. 
     c) Indicar para cada medio de comunicación el nombre, la audiencia estimada y el indice de
     audiencia.          
     d) Salir         
               
        Su opcion -->   ''')
    return op

if __name__ == "__main__":
    gestorM = GestorMedios()
    gestorM.cargarCSV()
    gestorM.cargarCSVprogramas()
    
    opcion = menu().lower()
    while opcion != 'd':
        if opcion == 'a':
            gestorM.agregarManual()
            gestorM.mostrarMedios()
            
        elif opcion == 'b':
            xprograma = input("Ingrese el nombre de un programa de radio: ")
            gestorM.mostrarmedioPrograma(xprograma)
            
        elif opcion == 'c':
            gestorM.indicarmedios()
        opcion = menu().lower()
        