from producto import Producto

class ProductoOnline(Producto):
    __URLimagen : str
    __porcentajedescuento: int
    __enviogratis: str
    __costoenvio: int
    
    def __init__(self, codigo, nombre, preciobase, descripcion, stock, url, porcentaje, envio, costoenvio):
        super().__init__(codigo, nombre, preciobase, descripcion, stock)
        self.__URLimagen = url
        self.__porcentajedescuento = porcentaje
        self.__enviogratis = envio
        self.__costoenvio = costoenvio
        
    def getURLimagen(self):
        return self.__URLimagen
    def getPorcentajedescuento(self):
        return self.__porcentajedescuento
    def getEnviogratis(self):
        return self.__enviogratis
    def getCostoenvio(self):
        return self.__costoenvio
    
    def calcularPrecioFinal(self):
        preciobase = super().getPreciobase()
        porcentajedescuento = self.__porcentajedescuento
        descuento = preciobase * (porcentajedescuento / 100)
        if self.__enviogratis == "Si":
            preciofinal = preciobase - descuento
        else:
            preciofinal = preciobase + self.__costoenvio - descuento
        return preciofinal
    
    def get_tipo(self):
        return (type(self).__name__)
    
    
    
    
    