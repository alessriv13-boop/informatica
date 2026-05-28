import operaciones_basicas as ob
import operaciones_cientificas as oc
import graficadora as graf
import historial as hist

# Diccionario de funciones predefinidas para evaluar/graficar (Requerimiento 3)
funciones_predefinidas = {
    "lineal": lambda x: 2 * x + 1,
    "cuadratica": lambda x: x * x,
    "cubica": lambda x: x * x * x
}

def menu_basicas():
    print("\n★------------ OPERACIONES BÁSICAS ------------★")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Potencia")
    sub_op = input("Seleccione: ")
    
    if sub_op in ['1', '2', '3', '4', '5']:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        if sub_op == '1':
            res = ob.sumar(a, b)
            desc = f"Suma: {a} + {b} = {res}"
        elif sub_op == '2':
            res = ob.restar(a, b)
            desc = f"Resta: {a} - {b} = {res}"
        elif sub_op == '3':
            res = ob.multiplicar(a, b)
            desc = f"Multiplicación: {a} * {b} = {res}"
        elif sub_op == '4':
            res = ob.dividir(a, b)
            desc = f"División: {a} / {b} = {res}"
        elif sub_op == '5':
            res = ob.potencia(a, int(b))
            desc = f"Potencia: {a} ^ {int(b)} = {res}"
            
        print(f"Resultado: {res}")
        hist.registrar_operacion(desc)

def menu_cientificas():
    print("\n★----------- OPERACIONES CIENTÍFICAS -----------★")
    print("1. Factorial\n2. Raíz Cuadrada\n3. Exponencial (e^x)\n4. Seno\n5. Coseno\n6. Logaritmo Natural")
    sub_op = input("Seleccione: ")
    
    if sub_op == '1':
        n = int(input("Ingrese un entero: "))
        res = oc.factorial(n)
        hist.registrar_operacion(f"Factorial: {n}! = {res}")
        print(f"Resultado aproximado: {res}")
        
    elif sub_op == '2':
        x = float(input("Ingrese el número: "))
        res = oc.raiz_cuadrada(x)
        hist.registrar_operacion(f"Raíz Cuadrada de {x} = {res}")
        print(f"Resultado aproximado: {res}")
        
    elif sub_op == '3':
        x = float(input("Ingrese x para e^x: "))
        res = oc.exponencial(x)
        hist.registrar_operacion(f"Exponencial e^{x} = {res}")
        print(f"Resultado aproximado: {res}")
        
    elif sub_op in ['4', '5']: # Seno y Coseno
        print("\n¿En qué unidad está el ángulo?")
        print("1. Radianes")
        print("2. Grados")
        unidad = input("Seleccione (1 o 2): ")
        
        angulo = float(input("Ingrese el valor del ángulo: "))
        original_angulo = angulo
        unidad_texto = "rad"
        
        # Si eligió grados, hacemos la conversión interna antes de calcular
        if unidad == '2':
            angulo = oc.grados_a_radianes(angulo)
            unidad_texto = "°"
            
        if sub_op == '4':
            res = oc.seno(angulo)
            hist.registrar_operacion(f"Seno de {original_angulo}{unidad_texto} = {res}")
            print(f"Resultado aproximado: {res}")
        elif sub_op == '5':
            res = oc.coseno(angulo)
            hist.registrar_operacion(f"Coseno de {original_angulo}{unidad_texto} = {res}")
            print(f"Resultado aproximado: {res}")
            
    elif sub_op == '6':
        x = float(input("Ingrese el número (>0): "))
        res = oc.logaritmo_natural(x)
        hist.registrar_operacion(f"Logaritmo Natural de {x} = {res}")
        print(f"Resultado aproximado: {res}")
        
    else:
        print("Opción no válida.")

def seleccionar_funcion():
    print("\nFunciones disponibles:")
    for clave in funciones_predefinidas.keys():
        print(f"- {clave}")
    seleccion = input("Escriba el nombre de la función: ").lower()
    return funciones_predefinidas.get(seleccion, None)

def main():
    while True:
        print("\n★==----------== CALCULADORA CIENTÍFICA ==---------==★\n")
        print("1. Operaciones básicas")
        print("2. Operaciones científicas")
        print("3. Evaluar una función")
        print("4. Ver historial de operaciones")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menu_basicas()
        elif opcion == '2':
            menu_cientificas()
        elif opcion == '3':
            f = seleccionar_funcion()
            if f:
                x = float(input("Ingrese el valor de X a evaluar: "))
                print(f"Resultado f({x}) = {f(x)}")
                hist.registrar_operacion(f"Evaluación de función en X={x}: Resultado = {f(x)}")
            else:
                print("Función no encontrada.")
        elif opcion == '4':
            hist.mostrar_historial()
        elif opcion == '5':
            print("¡Gracias por usar la calculadora! Fin del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

