import csv
from clasePlanAhorro import PlanAhorro as PA
class ManejadorPlanAhorro:
    def __init__(self):
        self.__listaPlanes = []

    def cargarLista(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            cod = int(fila[0])
            mod = str(fila[1])
            ver = str(fila [2])
            val = float(fila[3])
            plan = PA(cod,mod,ver,val)
            self.__listaPlanes.append(plan)
        return self.__listaPlanes

    def actualizarPlanes(self):

        for iplan in range (len(self.__listaPlanes)):
            print("Codigo {}, modelo {}, version {}".format(self.__listaPlanes[iplan].getCodigo(),self.__listaPlanes[iplan].getModelo(), self.__listaPlanes[iplan].getVersion()))
            nuevovalor = float(input("Ingrese el nuevo valor: "))
            self.__listaPlanes[iplan].actualizarValor(nuevovalor)
            print("Valor actualizado ({})".format(self.__listaPlanes[iplan].getValor()))
        
    def valorDado(self, valor):
        for iplan in range (len(self.__listaPlanes)):
            if valor > self.__listaPlanes[iplan].getValor():
                print("Codigo del plan: {}, modelo: {}, version {}". format(self.__listaPlanes[iplan].getCodigo(), self.__listaPlanes[iplan].getModelo(), self.__listaPlanes[iplan].getVersion()))

    def montoParaLicitar(self):
        for iplan in range (len(self.__listaPlanes)):
            print("Vehiculo: {} Monto para licitar: {:.2f}".format(self.__listaPlanes[iplan].getModelo(), self.__listaPlanes[iplan].importeCuota()*self.__listaPlanes[iplan].getLicitacion()))

        
    def buscarPlan(self, codigo):
        iplan = 0
        while (iplan < len(self.__listaPlanes) and (codigo != self.__listaPlanes[iplan].getCodigo())):
            iplan +=1
        else:
            return iplan 

    def modificarCuotas(self, codigo):
        iplan = self.buscarPlan(codigo)
        lic = int(input("Ingrese la nueva cantidad de cuotas que se debe tener pagas para licitar: "))
        self.__listaPlanes[iplan].modificarLicitacion(lic)
        print("Se modifico la cantidad de cuotas para licitacion ({})". format(self.__listaPlanes[iplan].getLicitacion()))

    def mostrarLista(self):
        for iplan in range (len(self.__listaPlanes)):
            print("{}\t{}\t{}\t{}\t{}\t{}".format(self.__listaPlanes[iplan].getCodigo(),self.__listaPlanes[iplan].getModelo(),self.__listaPlanes[iplan].getVersion(),self.__listaPlanes[iplan].getValor(),self.__listaPlanes[iplan].getCuotas(),self.__listaPlanes[iplan].getLicitacion()))