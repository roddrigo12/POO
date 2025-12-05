class Beca:
    __id: int
    __tipo: str
    __importe: float
    
    def __init__(self, xid, xtipo, ximp):
        self.__id = xid
        self.__tipo = xtipo
        self.__importe = ximp
        
    def get_id(self):
        return self.__id
    
    
    def get_tipo(self):
        return self.__tipo
    
    def get_importe(self):
        return self.__importe
    
    
    