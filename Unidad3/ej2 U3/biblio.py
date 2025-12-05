class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __listalibros: list
    
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listalibros = []
        
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_telefono(self):
        return self.__telefono
    
    def agregarLibroaBiblioteca(self, unlibro):
        self.__listalibros.append(unlibro)
        print("Libro agregado")
        
    def eliminarLibro(self):
        xlibro = input("Ingrese nombre del libro que desea eliminar: ")
        i = 0
        encontrado = False
        while i < len(self.__listalibros) and encontrado == False:
            if self.__listalibros[i].get_titulo() == xlibro:
                del self.__listalibros[i]
                print("Libro eliminado. ")
            else: 
                i += 1
                
    def buscarlibro(self, titulolibro):
        i = 0
        encontrado = False
        while i < len(self.__listalibros) and encontrado == False:
            if self.__listalibros[i].get_titulo() == titulolibro:
                encontrado = True
            else:
                i += 1
        if encontrado == True:
            print(f"Autor: {self.__listalibros[i].get_autor()} - Genero: {self.__listalibros[i].get_genero()}")
            return self.__listalibros[i].get_titulo()
        
    def mostrarLibros(self):
        for libro in self.__listalibros:
            print(libro)
        
        
        