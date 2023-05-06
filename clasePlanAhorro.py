class PlanAhorro:
    
    __cuotas = 60
    __licitacion = 10
    
    def __init__(self, codigo = 0, modelo = '', version = '', valor = 0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
        
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
    
    @classmethod
    def getCuotas(cls):
        return cls.__cuotas
    
    @classmethod
    def getLicitacion(cls):
        return cls.__licitacion
    
    @classmethod
    def modificarLicitacion(cls, nuevacifra):
        cls.__licitacion = nuevacifra



