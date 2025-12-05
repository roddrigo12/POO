from accidente import Accidente
from departamento import Departamento
from manejadordepto import ManejadorDpto

if __name__ == '__main__' :
    manejador = ManejadorDpto()
    tabla = Accidente()
    
    mes = int(input("Ingrese numero de mes de los accidentes : "))
    depto = int(input("Ingrese numero de departamento de los accidentes : "))
    cant = int(input("Ahora ingrese cantidad de accidentes: "))
    tabla.cargar_tabla(depto, mes, cant)
    
    xmes = int(input("Ingrese numero de mes para ver accidentes en todos los deptos : "))
    manejador.mostrar_pordepto(xmes, tabla) ##Envio tabla que es instancia de la clase que tiene los accidentes
    
    
    
    