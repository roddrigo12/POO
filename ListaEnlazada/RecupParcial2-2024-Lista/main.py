from gestorplan import GestorPlan

def menu():
    print()
    print("MENU DE OPCIONES: ".center(60))
    op = input('''
    a. Leer en el programa principal o en el menú, una posición, de la lista, mostrar por
    pantalla qué tipo de plan se encuentra almacenado en dicha posición (usar la función
    isinstance()). El método definido en la clase lista, debe lanzar la excepción IndexError.
    El programa principal o el menú, quien haya invocado el método de la Lista, debe
    capturar la excepción y mostrar un mensaje de error “Índice fuera de rango”.
    
    b. Ingresar por teclado una cobertura geográfica y contar y mostrar la cantidad de planes
    que corresponden a la misma.
    
    c. Ingresar por teclado una cantidad de canales internacionales y mostrar el /los nombres
    de las compañías que ofrecen una cantidad mayor o igual a la ingresada.
    
    d. Para todos los planes en la lista, mostrar: tipo de plan, nombre de la compañía,
    duración del plan, cobertura geográfica e importe final. Este ítem debe resolverlo en la
    clase base.
           
    e. SALIR           
               
            Su opcion ->   ''')
    return op

if __name__ == "__main__":
    gestorP = GestorPlan()
    gestorP.cargarArchivo()
    gestorP.mostrarPlanes()
    opcion = menu().lower()
    
    
    while opcion != 'e':
        if opcion == 'a':
            posicionlista = int(input("Ingrese una posicion de la lista: "))
            try:
                gestorP.mostrarPosicion(posicionlista)            
            except IndexError:
                print("ERROR: Indice fuera de rango")
        elif opcion == 'b':
            cobertura = input("Ingrese una cobertura geografica: ")
            gestorP.contarymostrarPlanes(cobertura)
            
        elif opcion == 'c':
            CantCanalesInter = int(input("Ingrese una cantidad de canales internacionales: "))
            gestorP.mostrarmayores(CantCanalesInter)
            
        elif opcion == 'd':
            gestorP.mostrarD()
            
        opcion = menu().lower()
        
        
        
        
        