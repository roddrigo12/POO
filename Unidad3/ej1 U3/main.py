from gestorhotel import GestorHotel
def menu():
    print()
    print ("Menu de opciones".center(60))
    op = input('''
a) Agregar habitaciones al hotel
b) Reservar habitación
c) Liberar habitación
d) Mostrar número y piso de las habitaciones de un tipo
e) Mostrar cantidad de habitaciones libres por piso
f) Mostrar listado de habitaciones
z) SALIR 
        Su opcion ---> ''')
    
    return op

if __name__ == "__main__":
    gestorH=GestorHotel()
    gestorH.carga_archivo()
    op = menu().lower()
    
    while op != 'z':
        if op == 'a':
            xhotel = input("Ingrese nombre de hotel: ")
            l = gestorH.buscarhot(xhotel)
            if (l != -1):
                gestorH.incisoA(l)
        
        elif op == 'b':
            xhotel = input("Ingrese nombre de hotel donde reservara habitacion: ")
            i = gestorH.buscarhot(xhotel)
            if i != -1:
                gestorH.incisob(i)                
        
        elif op == 'c':
            xhotel = input("Ingrese nombre del hotel para liberar habitacion: ")
            i = gestorH.buscarhot(xhotel)
            if i != -1:
                gestorH.incisoc(i)
                
        elif op == 'd':
            xhotel = input("Ingrese nombre del hotel para mostrar numero y tipo de las habitaciones por tipo:  ")
            i = gestorH.buscarhot(xhotel)
            if i != -1:
                gestorH.incisod(i)
                
        elif op == 'e':
            xhotel = input("Ingrese nombre de hotel: ")
            i = gestorH.buscarhot(xhotel)
            if i != -1:
                gestorH.incisoe(i)
            
                
        op = menu().lower()