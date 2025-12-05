from tarjetasube import TarjetaSube
from controlador import Controlador
def Prueba():
    lista = Controlador()
    
    for i in range (3):
        saldo = float (input("Ingrese Saldo de la tarjeta: "))
        numero= int (input ("Ingrese numero de la tarjeta sube: "))
        tarjeta = TarjetaSube(saldo, numero)  ##Creación de instancia
        print(tarjeta)  ##Se muestra la instancia
        lista.agregar_tarjeta(tarjeta)
        lista.mostrar_tarjetas() #inciso2
        numero= int(input("Ingrese numero de la tarjeta SUBE a buscar:  "))
        lista.buscar_tarjeta(numero) #inciso3
    
        print("El saldo actual de la tarjeta es : $ {} " .format (tarjeta.consultar_saldo()))
        
        importe = float (input("Ingrese el monto a cargar a la tarjeta sube:  "))
        tarjeta.cargar_saldo(importe)
        print("El saldo ahora es de: $ {} " .format (tarjeta.consultar_saldo()))
        
        pasaje = float (input("Ingrese valor del pasaje : "))
        aux= tarjeta.pagar_pasaje(pasaje)
        if(aux < 0):
            print("No se pudo realizar el pago. Saldo insuficiente ")
        else:
            print("El saldo actual de la tarjeta es :  $ {}" .format(tarjeta.consultar_saldo()))
        