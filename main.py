#Rodrigo Ismael Guevara Villalva E010-513 - 47047306
from gestorcurso import GestorCurso
from gestorinscripto import GestorInscripto

def menu():
    print()
    print("MENU DE OPCIONES: ".center(60))
    op = input('''
     a) Leer por teclado el dni de un inscripto, buscarlo si lo encuentra mostrar su nombre y
     apellido, e incrementar la cantidad de días que asistió en uno.          
     
     b) Leer por teclado el identificador de un curso, mostrar su denominación, y el dni,
     nombre y apellido de los inscriptos que alcanzaron el porcentaje mínimo de
     asistencias.

     c) Leer por teclado, el dni de un inscripto, si lo encuentra, mostrar: dni, nombre y
     apellido, solicitar la nota que obtuvo, modificar la nota final.          
     
     d) Para cada curso, listar denominación, cupo, y el listado de inscriptos que aprobaron el
     curso, es decir cumplen el porcentaje mínimo y la nota es mayor o igual que 7.
     
     e) Salir
             
             
        Su opcion -->  ''')
    return op

if __name__ == "__main__":
    gestorC = GestorCurso()
    gestorI = GestorInscripto()
    gestorC.cargaArchivo()
    gestorI.cargaArchivo()
    opcion = menu().lower()
    
    while opcion != 'e':
        if opcion == 'a':
            dni = input("Ingrese el dni de un inscripto: ")
            gestorI.buscarInscriptopordni(dni)
            
        elif opcion == 'b':
            idcurso = int(input("Ingrese identificador de un curso: "))
            gestorC.mostrarIncisob(idcurso, gestorI)
        
        elif opcion == 'c':
            dniinscripto = input("Ingrese dni de inscripto: ")
            gestorI.incisoC(dniinscripto)
            
        elif opcion == 'd':
            gestorC.listarporcurso(gestorI)
            
        else:
            print("Error, ingrese una opcion valida. ")
        
            
        opcion = menu().lower()
        
        
        
        