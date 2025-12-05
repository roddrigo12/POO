from claseHabitacion import Habitacion
class Hotel:
    __nombre: str
    __direccion: str
    __telefono: str
    __lista_habitaciones: list
    
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__lista_habitaciones = []
        
    def getNombre (self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono (self):
        return self.__telefono
    
    def getListaHabitaciones (self):
        return self.__lista_habitaciones
    
    def agregarhabitacion (self, numero, piso, tipodehab, precioxnoche, disp):
        unahabitacion = Habitacion(numero, piso, tipodehab, precioxnoche, disp)
        self.__lista_habitaciones.append(unahabitacion)
        
    def mostrarhotel (self):
        print (f"Hotel: {self.__nombre()}")
        for habitacion in self.__lista_habitaciones:
            print(habitacion)

#inciso b
    def reservar_habitacion(self):
        xnumero = int(input("Ingrese numero de la habitacion que desea reservar: "))
        encontrado = False
        i = 0
        while i < len(self.__lista_habitaciones) and encontrado == False:
           if self.__lista_habitaciones[i].getNumero() == xnumero:
                encontrado = True
           else:
               i = i + 1
               
        if encontrado == True:
            if   self.__lista_habitaciones[i].getDisponibilidad() == True:
                self.__lista_habitaciones[i].setDisponibilidad(False)
                print("Habitacion reservada.")
            else:
                print("La habitacion esta ocupada, reserve otra")
         
   #inciso c            
    def liberar_habitacion(self):
        xnumero = int(input("Ingrese numero de la habitacion que desea reservar: "))
        i = 0
        encontrado = False
        while i < len(self.__lista_habitaciones) and encontrado == False:
            if self.__lista_habitaciones[i].getNumero() == xnumero:
                encontrado = True
            else: 
                i = i + 1
                
        if encontrado == True:
            if self.__lista_habitaciones[i].getDisponibilidad() == False:
                self.__lista_habitaciones[i].setDisponibilidad(True)
                print("Habitaciion liberada y disponible para usar. ")
            else:
                print("La habitacion ya esta liberada. ")
                
    #d            
    def mostrarporTipo(self):
        xtipo = input("Ingrese tipo de habitacion que desea mostrar: ")
        for habitacion in self.__lista_habitaciones :
            if habitacion.getTipodeHabitacion() == xtipo:
                print(f"Numero : {habitacion.getNumero()} - Piso: {habitacion.getPiso()}")
                
    def contarHabitacionesLibres(self): #inciso e, contar habitaciones por piso
        contpiso1 = 0
        contpiso2= 0
        contpiso3 = 0
        contpiso4 = 0
        for habitacion in self.__lista_habitaciones:
         if habitacion.getDisponibilidad == True: 
            if habitacion.getTipodeHabitacion() == 1:
                contpiso1 += 1
            elif habitacion.getTipodeHabitacion() == 2:
                contpiso2 += 1
            elif habitacion.getTipodeHabitacion() == 3:
                contpiso3 += 1
            elif habitacion.getTipodeHabitacion() == 4:
                contpiso4 += 1
        print(f"En el piso 1 hay: {contpiso1} habitaciones disponibles. ")
        print(f"En el piso 2 hay: {contpiso2} habitaciones disponibles. ")
        print(f"En el piso 3 hay: {contpiso3} habitaciones disponibles. ")
        print(f"En el piso 4 hay: {contpiso4} habitaciones disponibles. ")



