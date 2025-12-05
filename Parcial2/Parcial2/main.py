from gestorreceta import GestorReceta

def menu():
    print()
    print("MENU DE OPCIONES: ".center(60))
    op = input('''
     a) Crear y agregar recetas al gestor. En el metodo agregarReceta usar isisnstance() para validar si el objeto a agregar 
     pertenece a la clase Receta, en caso de que no, lanzar la excepcion TypeError. Controlar la excepcion donde corresponda.
     
     b) Agregar ingredientes a una receta.
     
     c) Dado el nombre de una receta y una posicion ingresada por teclado, mostrar el ingrediente que se encuentra en esa posicion
     dentro de la lista de ingredientes. Usar index error y mostrar mensaje "No existe un ingrediente en esa posicion"
     
     d) Dado un nombre de ingrediente ingresado por teclado, mostrar todas las recetas que lo contienen.
     
     e) SALIR
     
     Su opcion -->          ''')
    return op

if __name__ == "__main__":
    gestorR = GestorReceta()
    gestorR.cargarArchivo()
    gestorR.mostrarTodasRecetas()
    opcion = menu().lower()
    
    while opcion != 'e':
        if opcion == 'a':
            pass
        elif opcion == 'b':
            print("El inciso a y b ya estan hechos con el csv") #Pero seria agregar manualmente todo
        elif opcion == 'c':
            NombreRec = input("Ingrese nombre de una receta: ")
            posicion = int(input("Ingrese una posicion de la lista: "))
            i= gestorR.BuscarRecporNombre(NombreRec)
            if i != -1:
                try:
                    gestorR.buscarposicion(posicion, i)
                except IndexError:
                    print("ERROR. No existe un ingrediente en esa posicion. ")
            else:
                print("No se encontro la receta ")
                
        elif opcion == 'd':
            nombreingrediente = input("Ingrese nombre de un ingrediente: ")
            gestorR.MostrarRecporIng(nombreingrediente)
                
                
                
        opcion = menu().lower()
        
        
        
        
        