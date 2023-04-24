from menu import MenuOpciones
from manejadorPlanAhorro import ManejadorPlanAhorro as MPA

def test():
    controlador = MPA()
    controlador.cargarLista()
    print("SE CARGO EL ARCHIVO")
    menu = MenuOpciones()
    menu.opciones(controlador)

if __name__ == "__main__":

    test()