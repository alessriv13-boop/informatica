def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    if b or a == 0:
        return 0
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(base, exponente):
    # Soporta exponentes enteros positivos
    resultado = 1
    for _ in range(int(exponente)):
        resultado = resultado * base
    return resultado
