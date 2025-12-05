from producto import Producto

class ProductoFisico(Producto):
    __direcciontienda: str
    __tasaimpuesto: float
    
    def __init__(self, codigo, nombre, preciobase, descripcion, stock, direcciontienda, tasaimpuesto):
        super().__init__(codigo, nombre, preciobase, descripcion, stock)
        self.__direcciontienda = direcciontienda
        self.__tasaimpuesto = tasaimpuesto
        
    def getDirecciontienda(self):
        return self.__direcciontienda
    def getTasaimpuesto(self):
        return self.__tasaimpuesto
    
    def calcularPrecioFinal(self):
        preciobase = super().getPreciobase()
        tasaimp = self.getTasaimpuesto()
        impuesto = preciobase * (tasaimp / 100)
        preciofinal = preciobase + impuesto
        return preciofinal
    
    def get_tipo(self):
    
        return (type(self).__name__)
    
    
    
    
    
    
    