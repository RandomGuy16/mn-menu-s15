# ==========================================
# 1. LA FUNCIÓN (f)
# Ecuación: dy/dx = x + y
# ==========================================
def funcion_ejemplo(x, y):
    return x + y

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