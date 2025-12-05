from gestorcliente import GestorCliente
from gestormovimiento import GestorMovimiento

def menu():
    print()
    print("MENU DE OPCIONES:  ".center(60))
    op = input('''
     a) Ingresar dni de un cliente para actualizar su saldo.
     b) Ingresar numero de tarjeta para informar sus movimientos
     c) Ordenar por numero de tarjeta
     d) Salir          
      Su opcion -->   ''')
    return op

if __name__ == "__main__":
    gestorC = GestorCliente()
    gestorM = GestorMovimiento()
    gestorC.carga_archivo()
    gestorM.carga_archivo()
    opcion = menu().lower()
    
    while opcion != 'd':
        if opcion == 'a':
            xdni = input("Ingrese dni de un cliente:  ")
            gestorC.buscar_cliente(xdni, gestorM)
            
        elif opcion == 'b':
            xnrotarjeta = int(input("Ingrese un numero de tarjeta: "))
            gestorC.buscar_portarjeta(xnrotarjeta, gestorM)
        
        elif opcion == 'c':
            gestorM.ordenar_portarjeta()
        opcion = menu().lower()


