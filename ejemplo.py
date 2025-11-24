# ==========================================
# LA ECUACION
# xy''' - x^2 y''' - xy'' - x^2 y' + xy = xsen(x)
# y(0) = y''(0) = 1; y'(0) = y'''(0) = 1
#
# Segun deepseek, de manera analitica se separa
# en un sistema de ecuaciones diferenciales
# es un capitulo que el curso respectivo omitio
# pero es posible, y una vez hecho eso, de forma
# vectorial, con ayuda de numpy, se resuelve de
# la forma que ya conocemos
# ==========================================
def funcion_ejemplo(x, y):
    """esta funcion hay que quitarla"""
    return x + y

# ignorar lo siguiente, no se que hacer con esto
# ==========================================
# 2. LOS PARÁMETROS (inputs)
# ==========================================
# Condiciones Iniciales
x0 = 0.0      # Empezamos en x = 0
y0 = 1.0      # Sabemos que y(0) = 1

# Intervalo y pasos
xn = 1.0      # Queremos calcular hasta x = 1
n  = 10       # Lo haremos en 10 pasos

# Cálculo de h (Tamaño de paso)
# h = (Final - Inicial) / Pasos
h  = (xn - x0) / n  # Esto resultará en h = 0.1
