import matplotlib.pyplot as plt
from tabulate import tabulate  # Si no tienes esto, puedes comentar las líneas que lo usan


# =============================================================================
# DEFINICIÓN DE LA FUNCIÓN
# =============================================================================
def funcion(x, y):
    """
    Aquí defines tu ecuación diferencial: dy/dx = f(x,y)
    Ejemplo actual: x^2 + y
    """
    return x ** 2 + y


# =============================================================================
# FUNCIONES DE VISUALIZACIÓN (Estilo Euler Mejorado)
# =============================================================================
def mostrarX(n, xArray):
    for i in range(n + 1):
        print(f"x[{i}] = {xArray[i]:.6f}")


def mostrarY(n, yArray):
    for i in range(n + 1):
        print(f"y[{i}] = {yArray[i]:.6f}")


def mostrarTodo(n, yArray, xArray):
    # Cabecera simple estilo consola
    print(f"{'i':<5} | {'xi':<12} | {'yi':<12}")
    print("-" * 35)
    for i in range(n + 1):
        print(f"{i:<5} | {xArray[i]:<12.6f} | {yArray[i]:<12.6f}")


# =============================================================================
# LÓGICA DEL MÉTODO RK4
# =============================================================================
def resolver_runge_kutta_4(x0, y0, h, n, f):
    """
    Acepta x0, y0, h, n y la función f.
    Retorna listas x_values, y_values y detalles para tablas.
    """
    x_values = [x0]
    y_values = [y0]
    detalles = []

    x = x0
    y = y0

    # Iteraciones
    for i in range(n):
        # Cálculo de las pendientes (k)
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        # Cálculo del siguiente punto
        y_next = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x + h

        # Guardar detalles para quien quiera ver los k1, k2...
        detalles.append({
            'i': i + 1, 'x': x, 'y': y,
            'k1': k1, 'k2': k2, 'k3': k3, 'k4': k4
        })

        # Actualizar variables
        x = x_next
        y = y_next
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values, detalles


def metodo_rungekutta4(f: callable = funcion):

    print("+++++++++++++++++ CONDICIONES INICIALES (RK4) +++++++++++++++++")
    print("----------------- OBTENER DATOS -----------------")

    # Inputs convertidos a float para mayor precisión
    x0 = float(input("Ingrese x0 (Condición inicial x): "))
    y0 = float(input("Ingrese y0 (Condición inicial y): "))
    n = int(input("Ingrese el valor de n (número de pasos): "))

    print("----------------- INTERVALO -----------------")
    limiteInf = float(input("Ingrese el valor de limite inferior del intervalo (usualmente x0): "))
    limiteSup = float(input("Ingrese el valor de limite superior del intervalo (xn): "))

    # Cálculo automático de h
    h = (limiteSup - limiteInf) / n
    print(f"\n[INFO] Tamaño de paso calculado: h = {h}")
    print("----------------------------------------------------------------------")

    # Llamada al método
    # Nota: Pasamos 'funcion' que definimos arriba
    xArray, yArray, detalles = resolver_runge_kutta_4(x0, y0, h, n, f)

    # Mostrar X
    print("\n--- Valores de X ---")
    mostrarX(n, xArray)
    print("---------------------------------------------")

    # Mostrar Y
    print("--- Valores de Y (Resultados) ---")
    mostrarY(n, yArray)
    print("--------------------------------------------------")

    # Mostrar Tabla Resumen
    print("----------------- TABLA FINAL  -----------------")
    mostrarTodo(n, yArray, xArray)
    print("--------------------------------------------------")

    # Opcional: Gráfica rápida si se desea
    graficar = input("\n¿Desea ver la gráfica? (s/n): ")
    if graficar.lower() == 's':
        plt.plot(xArray, yArray, 'bo-', label='RK4')
        plt.grid(True)
        plt.title(f"Aproximación RK4 (n={n}, h={h})")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    metodo_rungekutta4()
