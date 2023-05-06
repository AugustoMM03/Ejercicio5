from menu import MenuOpciones
from manejadorPlanAhorro import ManejadorPlanAhorro as MPA
from clasePlanAhorro import PlanAhorro as PA

def test():
    controlador = MPA()
    controlador.cargarLista()
    print("SE CARGO EL ARCHIVO")
    menu = MenuOpciones()
    menu.opciones(controlador)

if __name__ == "__main__":

    test()

