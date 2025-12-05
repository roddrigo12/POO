from gestorespectaculo import GestorEspectaculo

def menu():
    print()
    print("MENU DE OPCIONES: ".center(60))
    op = input('''
    a)Agregar los espectáculos a la colección. (Validar que el objeto que se agrega sea un espectáculo,usar isinstance). 
    Lanzar la excepción ValueError, si se intenta agregar un espectáculo para una fecha que ya está registrada.
    
    b) Mostrar para todos los espectáculos el nombre del espectáculo, fecha y el precio final de la entrada.
    Este método debe ser definido en la superclase. La superclase debe incluir un método abstracto, que
    luego debe redefinirse en las subclases. Estas implementaciones deben garantizar la reutilización decódigo (NO DEBEN REPETIRSE SENTENCIAS).
    
    c) Listar aquellos espectáculos cuyo precio de entrada sea superior a $10.000.
    
    d) Leer por teclado una cantidad de músicos y mostrar nombre, fecha y precio final de la entrada del 
     espectáculo čuya cantidad de músicos participantes supera la cantidad dada.
     
    e) Salir      
               
        Su opcion -->   ''')
    return op

if __name__ == "__main__":
    gestorE = GestorEspectaculo()
    gestorE.CargaArchivo()
    opcion = menu().lower()
    
    while opcion != 'e':
        if opcion == 'a':
            #Ya tengo csv y ya esta hecho pero seria:
            '''tipo = input("ingrese tipo de espectaculo a cargar: ") 
             if tipo == 'C' y lo mismo para 'O'
             pedirdatos con input 
             unespectaculo = Clase(datos, datos, datos)
             llamar al metodo para agregar
             try:
             gestorE.agregarEspectaculo(unespectaculo)
             except ValueError: print etc'''
        
        elif opcion == 'b':
            gestorE.incisoB()
        elif opcion == 'c':
            gestorE.listarMayores10mil()
             
        elif opcion == 'd':
            CantidadMusicos = int(input("Ingrese una cantidad de musicos: "))
            gestorE.mostrarIncisod(CantidadMusicos)
             
        opcion = menu().lower()
        
        
        
        
        
        
        
        
        
        