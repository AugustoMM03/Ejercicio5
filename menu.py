class MenuOpciones:
    def __init__(self):
        self.__opcion = None

    def opciones(self,lista):
        while self.__opcion != 5:
            print("Menu de opciones: ")
            print("1)- Actualizar el valor del vehiculo de cada plan.")
            print("2)- Mostrar codigo del plan, modelo y version del vehiculo cuyo valor de la cuota sea inferior al valor dado.")
            print("3)- Mostrar el monto que se debe pagar para licitar vehiculo.")
            print("4)- Modificar la cantidad de cuotas que debe tener pagas para licitar un plan")
            print("5)- SALIR")            
            self.__opcion = int(input ("Seleccione una opcion: "))

            if self.__opcion == 1:
                lista.actualizarPlanes()

            elif self.__opcion == 2:
                valor = float(input("Ingrese un valor: "))
                lista.valorDado(valor)

            elif self.__opcion == 3:
                lista.montoParaLicitar()

            elif self.__opcion == 4:
                codigo = int(input("Ingrese un codigo de plan para modificar la licitacion: "))
                lista.modificarCuotas(codigo)
    