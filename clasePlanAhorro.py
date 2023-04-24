class PlanAhorro:
    def __init__(self, codigo = 0, modelo = '', version = '', valor = 0, cuotas = 0, licitacion = 0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
        self.__cuotas = cuotas
        self.__licitacion = licitacion
        
    def actualizarValor(self, nuevoValor):
        self.__valor = nuevoValor

    def importeCuota(self):
        self.__valorCuota = (self.__valor / self.__cuotas) * 0.10
        return self.__valorCuota

    def getCodigo(self):
        return self.__codigo
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version
    
    def getValor(self):
        return self.__valor
    
    def getCuotas(self):
        return self.__cuotas
    
    def getLicitacion(self):
        return self.__licitacion
    
    def modificarLicitacion(self, nuevacifra):
        self.__licitacion = nuevacifra

