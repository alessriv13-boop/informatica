import operaciones_basicas as ob

PI = 3.141592653589793
PI_2 = 6.283185307179586

def grados_a_radianes(grados):
    #Convierte un ángulo de grados a radianes
    return grados * (PI / 180.0)

def factorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, int(n) + 1):
        resultado = resultado * i
    return resultado

def raiz_cuadrada(x, toleracia=0.00001):
    # Método de Newton-Raphson para aproximar raíces
    if x < 0:
        return "Error: Raíz de número negativo"
    if x == 0:
        return 0.0
    estimacion = x / 2.0
    while True:
        mejor_estimacion = 0.5 * (estimacion + x / estimacion)
        # Verificamos si la diferencia es menor a la tolerancia
        diferencia = mejor_estimacion - estimacion

        # Si el resultado es negativo, lo convertimos en positivo
        if diferencia < 0:
            diferencia = diferencia * -1
        
        # Ahora que es seguro que es positivo, comparamos con la tolerancia
        if diferencia < toleracia:
            return mejor_estimacion
        estimacion = mejor_estimacion

def exponencial(x, terminos=50):
    # Serie de Taylor: e^x = suma( x^n / n! )
    resultado = 0.0
    for n in range(terminos):
        num = ob.potencia(x, n)
        den = factorial(n)
        resultado = resultado + num / den
    return resultado

def seno(x, terminos=20):
    # Serie de Taylor para el Seno
    resultado = 0.0
    for n in range(terminos):
        signo = 1 if n % 2 == 0 else -1
        exponente = 2 * n + 1
        num = ob.potencia(x, exponente)
        den = factorial(exponente)
        resultado = resultado + signo * (num / den)
    return resultado

def coseno(x, terminos=20):
    # Serie de Taylor para el Coseno
    resultado = 0.0
    for n in range(terminos):
        signo = 1 if n % 2 == 0 else -1
        exponente = 2 * n
        num = ob.potencia(x, exponente)
        den = factorial(exponente)
        resultado = resultado + signo * (num / den)
    return resultado

def logaritmo_natural(x, terminos=100):
    # Serie de Taylor para ln(x) alrededor de 1 (para x > 0)
    if x <= 0:
        return "Error: Logaritmo indefinido para valores <= 0"
    y = (x - 1) / (x + 1)
    resultado = 0.0
    for n in range(terminos):
        exponente = 2 * n + 1
        resultado += (1 / exponente) * ob.potencia(y, exponente)
    return 2 * resultado
