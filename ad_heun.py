import math

#FORMULAS
#yi+1 = yi + hf(x,y) para i = 1,2,3,4,...
# yi+1 = yi + hy'
#xi= x0 +ih
def mostrarX(n,xArray):
    for i in range(n+1):
        print(f"x[{i}] = {xArray[i]}")

def mostrarY(n,yArray):
    for i in range(n+1):
        print(f"F[{i}] = {yArray[i]}")

def mostrarTodo(n,yArray,xArray):
    for i in range(n+1):
        print(f"{i}\t|\tx[{i}]\t|\t{xArray[i]}\t|\t{yArray[i]}")

def funcion(x,y):
    return 4*math.exp(0.8*x)-0.5*y

def ySigConGorrito(y,h,f):
    return y + h*f

def ySig(y,h,f,f2):
    return y+h*(f+f2)/2

def xSig(i,x0,h):
    return x0 + i*h

def resolver_heun(x0, y0, h, n, f):
    """
    Implementación del método de Heun.
    Retorna dos listas: xArray, yArray
    """
    xArray = []
    xArray.append(x0)
    yArrayGorrito = []
    yArrayGorrito.append(0)
    yArray = []
    yArray.append(y0)

    # Generar X
    for i in range(n):
        xArray.append(float(xSig(i+1,x0,h)))

    # Generar Y (Predictor-Corrector)
    for i in range(n):
        yArrayGorrito.append(ySigConGorrito(yArray[i],h,f(xArray[i],yArray[i])))
        yArray.append(ySig(yArray[i],h,f(xArray[i],yArray[i]),f(xArray[i+1],yArrayGorrito[i+1])))
        
    return xArray, yArray


def metodo_heun(f: callable = funcion):
    n = 0
    print("+++++++++++++++++ CONDICIONES INICIALES +++++++++++++++++")
    print("----------------- OBTENER DATOS -----------------")
    x0 = int(input("Ingrese x0: "))
    y0 = int(input("Ingrese y0: "))
    print("---------------------------------------------")
    limiteInf = float(input("Ingrese el valor de limite inferior del intervalor: "))
    limiteSup = float(input("Ingrese el valor de limite superior del intervalo: "))
    print("---------------------------------------------")
    print("¿Como desea definir el tamanio del paso?")
    print("Definir mediante intervalos\t-\t[1]")
    print("Definir tamanio del paso directamente\t-\t[2]")
    print("---------------------------------------------")
    res = int(input("Elija una opción [1/2]: "))
    if res == 1:
        print("----------------- INTERVALO -----------------")
        n = int(input("Ingrese el valor de n: "))
        h = (limiteSup - limiteInf) / n
    else:
        h = float(input("Ingrese el tamanio del paso h : "))
        n = int((limiteSup - limiteInf) / h)
    # ----------------------------------------------------------------------

    xArray, yArray = resolver_heun(x0, y0, h, n, f)

    mostrarX(n, xArray)
    print("---------------------------------------------")
    # --------------------------------------------------------------------

    mostrarY(n, yArray)
    print("--------------------------------------------------")
    print("----------------- MOSTRAR DATOS  -----------------")
    print("--------------------------------------------------")
    print("i\t|\tXi  \t|\t \t|\tYi")
    print("----------------------------------------------")
    mostrarTodo(n, yArray, xArray)
    print("--------------------------------------------------")
    # ----------------------------------------------------------------------


if __name__ == "__main__":
    metodo_heun()