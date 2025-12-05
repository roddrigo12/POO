from biblio import Biblioteca
from libro import Libro
import csv
class GestorBiblio:
    __listaBibliotecas: list
    
    def __init__(self):
        self.__listaBibliotecas = []
        
    def agregar_biblioteca(self, unabiblio):
        if isinstance(unabiblio, Biblioteca):
            self.__listaBibliotecas.append(unabiblio)
        else:
            raise TypeError
        
    def carga_archivo(self):
        archivo = open(r"C:\Users\rodri\OneDrive\Escritorio\Rodri facultad\POO\unidad3\ej2 U3\Biblioteca.csv")
        reader = csv.reader(archivo, delimiter=";")
        i = -1
        for fila in reader:
            if len(fila)== 3:
                unabiblio = Biblioteca(fila[0], fila[1], fila[2]) 
                try:
                    self.agregar_biblioteca(unabiblio)
                    i += 1
                except TypeError:
                    print("Error de tipo al cargar la biblioteca")
            else:
                titulo = fila[0]
                autor = fila[1]
                isbn = fila[2]
                genero = fila[3]
                unlibro = Libro(titulo, autor, isbn, genero)
                self.__listaBibliotecas[i].agregarLibroaBiblioteca(unlibro)
        archivo.close()
        
    def buscar_biblio(self, nombrebiblio):
        i = 0
        posicion = -1
        encontrado = False
        while i < len(self.__listaBibliotecas) and encontrado == False:
            if self.__listaBibliotecas[i].get_nombre() == nombrebiblio:
                posicion = i
                encontrado = True
            else:
                i += 1
        return posicion
    
    #a
    def incisoa(self, i):
        titulo = input("Ingrese titulo del libro a agregar: ")
        autor = input("Ingrese autor del libro: ")
        isbn = input("Ingrese isbn del libro: ")
        genero = input("Ingrese genero del libro: ")
        unlibro = Libro(titulo, autor, isbn, genero)
        self.__listaBibliotecas[i].agregarLibroaBiblioteca(unlibro)
      
    #b
    def incisob(self, i):
        self.__listaBibliotecas[i].eliminarLibro()
               
               
    #c
    def incisoc(self, titulolibro):
        i = 0
        encontrado =  False
        while i < len(self.__listaBibliotecas) and encontrado == False:
            librobuscado = self.__listaBibliotecas[i].buscarlibro(titulolibro)
            if librobuscado == titulolibro:
                encontrado = True
            else: 
                i = i + 1
        if encontrado == True:
            print(f"Libro encontrado en la biblioteca {self.__listaBibliotecas[i].get_nombre()}")
        else:
            print("No se encontro el libro en las bibliotecas.")
                   
    def mostrarD(self, i):
        self.__listaBibliotecas[i].mostrarLibros()
               
               