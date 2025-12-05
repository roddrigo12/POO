from gestorvehiculo import GestorVehiculos

def menu():
    print("MENU DE OPCIONES: ".center(60))
    op = input('''
     a. Agregar vehículos a la colección
     b. Dada una posición de la lista: Mostrar por pantalla qué tipo de vehículo se encuentra
     almacenado en dicha posición (usar la función isinstance()).
     c. Mostrar la canttidad de vehículos de cada tipo.
     d. Recorrer la colección y mostrar para todos los Vehículos: modelo, año de fabricación,
     capacidad de pasajeros y la tarifa del servicio.          
     e. SALIR           
               
         Su opcion -->      ''')
    return op

if __name__ == "__main__":
    gestorV = GestorVehiculos()
    gestorV.CargarArchivo()
    opcion = menu().lower()
    
    while opcion != 'e':
        if opcion == 'a':
            print("da paja")
        elif opcion == 'b':
            posicion = int(input("Ingrese una posicion de la lista: "))
            gestorV.mostrarporPosicion(posicion)
            
        elif opcion == 'c':
            gestorV.mostrarVehiculosporTipo()
            
        elif opcion == 'd':
            gestorV.recorrercoleccion()
        opcion = menu().lower()
        
        
        
        
        