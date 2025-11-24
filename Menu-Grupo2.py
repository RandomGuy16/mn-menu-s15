from ad_euler import metodo_euler
from ad_rungekutta4 import metodo_rungekutta4
from ad_heun import metodo_heun
from ad_euler_mejorado import metodo_euler_mejorado
from ejemplo import funcion_ejemplo


def mostrar_menu(opciones):
    print("--------------------- MENU ---------------------")
    for clave in opciones:
        print(f"[{clave}] - {opciones[clave][0]}")
    print("-------------- ECUACIÓN A RESOLVER -------------")
    print("xy''' - x^2 y''' - xy'' - x^2 y' + xy = xsen(x)")
    print("y(0) = y''(0) = 1; y'(0) = y'''(0) = 1")
    print("-------------------------------------------------")


def leer_opcion(opciones):
    while (a := input('Elija el numero del metodo :  ')) not in opciones:
        print('Opcion incorrecta')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1](funcion_ejemplo)


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        if opcion == '0':
            break
        ejecutar_opcion(opcion, opciones)


def menu_principal():
    opciones = {
        '1' : ('Metodo 1: Euler', metodo_euler),
        '2' : ('Metodo 2: Heun', metodo_heun),
        '3' : ('Metodo 3: Runge Kutta de cuarto grado', metodo_rungekutta4),
        '4' : ('Metodo 4: Euler mejorado', metodo_euler_mejorado),
        '0' : ('Salir', )
    }
    generar_menu(opciones,'0')


if __name__ == "__main__":
    menu_principal()
