from tarjetasube import TarjetaSube
class Controlador():
     __tarjetas:list   #Atributo
    
     def __init__(self):
       self.__tarjetas = []   ##lista vacía
    
     def agregar_tarjeta(self, tarjeta_sube):  ##inciso 1
       self.__tarjetas.append(tarjeta_sube)
    
     def mostrar_tarjetas(self):  ##inciso 2
      for tarjeta in self.__tarjetas:
         if (tarjeta.consultar_saldo() < 0):
            print("El numero de la tarjeta con saldo negativo es : {} " .format(tarjeta.getNumero()))
    
          
     def buscar_tarjeta(self, nro_tarjeta):      ##inciso 3
      i = 0
      encontrada = False

      while i < len(self.__tarjetas) and not encontrada:
       if self.__tarjetas[i].getNumero() == nro_tarjeta:
         print("Saldo de la tarjeta {}: {}".format(nro_tarjeta, self.__tarjetas[i].consultarSaldo()))
         encontrada = True
       else:
         i += 1
       if not encontrada:
         print("La tarjeta {} no ha sido encontrada".format(nro_tarjeta))