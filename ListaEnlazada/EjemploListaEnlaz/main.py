from lista import Lista
from profesor import Profesor

def testLista():
    lista = Lista()
    profesor = Profesor(414214502, 'Gomez', 'Rodrigo')
    lista.agregarProfesor(profesor)
    profesor2 = Profesor(39213221, 'Guevara', 'Luisito') #El ultimo que agrego queda primero, seria insercion por cabeza
    lista.agregarProfesor(profesor2)
    profesor3 = Profesor(214528172, 'Lopez', 'Emanuel')
    lista.agregarProfesor(profesor3)
    lista.listarDatosProfesores()

    lista.EliminarporDni(39213221)
    print('Luego de Borrar\n')
    lista.listarDatosProfesores()
    
if __name__ == "__main__":
    testLista()
    
    
    