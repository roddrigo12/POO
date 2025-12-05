class TarjetaSube:
    __saldo: float
    __numero: int

    # Constructor que inicializa los atributos
    def __init__(self, saldo, numero):
        self.__numero = numero
        self.__saldo = saldo

    # Método para obtener el número de la tarjeta
    def getNumero(self):
        return self.__numero

    # Método para mostrar la información de la tarjeta
    def __str__(self):
        return "Saldo: ${:.2f}  - Número: {}".format(self.__saldo, self.__numero)

    # Método para consultar el saldo de la tarjeta
    def consultar_saldo(self):
        return self.__saldo

    # Método para cargar saldo en la tarjeta
    def cargar_saldo(self, imp):
     if(imp > 0):
       self.__saldo += imp
    # Método para pagar el pasaje (deduce el saldo)
    def pagar_pasaje(self, imp):
     aux = 1
     if(self.__saldo >= imp):
       self.__saldo -= imp
     else:
       aux = -1
     return aux