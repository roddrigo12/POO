from gestorbiblio import GestorBiblio

def menu():
    print()
    print("Menu de opciones: ".center(60))
    op = input('''
               
    a) Agregar Libro: Permitir a la biblioteca agregar un nuevo libro a su colección.
    b) Eliminar Libro: Permitir a la biblioteca eliminar un libro de su colección.
    c) Para un Titulo de libro ingresado por teclado, mostrar nombre de la biblioteca en la
    que se encuentra, nombre del Autor y Género
    d) Listar Libros: Mostrar el nombre de todos los libros disponibles en la biblioteca.               
    e) Salir           
               
               
      Seleccione su opcion -->     ''')
    return op
    
if __name__ == "__main__":
    gestorB = GestorBiblio()
    gestorB.carga_archivo()
    opcion = menu().lower()
    
    while opcion != 'e':
        if opcion == 'a':
            biblio = input("Ingrese nombre de la biblioteca donde agregara libro: ")
            posicion = gestorB.buscar_biblio(biblio)
            if posicion != -1:
                gestorB.incisoa(posicion)
        elif opcion == 'b':
            biblio = input("Ingrese nombre de la biblioteca donde eliminara libro: ")
            posicion = gestorB.buscar_biblio(biblio)
            if posicion != -1:
                gestorB.incisob(posicion)
                
        elif opcion == 'c':
            titulolib = input("Ingrese titulo del libro a buscar en las bibliotecas: ")
            gestorB.incisoc(titulolib)
            
        elif opcion == 'd':
            biblio = input("Ingrese nombre de la biblioteca donde listara los libros: ")
            posicion = gestorB.buscar_biblio(biblio)
            if posicion != -1:
                gestorB.mostrarD(posicion)
                
                
        opcion = menu().lower()
        
        
        
        
        