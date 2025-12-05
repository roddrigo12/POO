class Libro:
    __titulo: str
    __autor: str
    __isbn: str
    __genero: str
    
    def __init__(self, titulo, autor, isbn, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__genero = genero
        
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_isbn(self):
        return self.__isbn
    
    def get_genero(self):
        return self.__genero
    
    def __str__(self):
        return f"Titulo del libro: {self.__titulo}"
    
        
        
        
        