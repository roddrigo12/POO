from gestorproductos import GestorProductos
def menu():
    print()
    print("MENU DE OPCIONES: ".center(60))
    op = input('''
     a) Agregar productos a la coleccion, validar que el objeto que se intenta agregar sea un producto, usar isinnstance y ValueError          
     b) Realizar la venta de un producto, validar que el producto se encuentre en stock, si se puede realizar la venta, actualizar el stock.
     c) Mostrar el nombre de todos los productos de venta online que tengan un descuento mayor al 10% y que el costo de envio sea gratis
     d) Mostrar para todos los productos Nombre, tipo de producto y precio total. Este metodo debe ser definido en la superclase. 
     La superclase debe incluir los metodos abstractos que crea necesario. Para mostrar el tipo de producto defina el sig metodo          
     e) SALIR         
               
        Su opcion -->  ''' )
    return op

if __name__ == "__main__":
    gestorP = GestorProductos()
    gestorP.cargarArchivo()
    opcion = menu().lower()
    while opcion != 'e':
        if opcion == 'a':
            print("Ya esta hecho con el csv. ")
        elif opcion == 'b':
            nombreProducto = input("Ingrese nombre del producto que quiere comprar: ")
            gestorP.RealizarVenta(nombreProducto)
            
        elif opcion == 'c':
            gestorP.mostrarIncisoc()
            
        elif opcion == 'd':
            gestorP.mostrarIncisod()
            
        opcion = menu().lower()