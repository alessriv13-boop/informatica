historial_operaciones = []

def registrar_operacion(descripcion):
    historial_operaciones.append(descripcion)

def mostrar_historial():
    if not historial_operaciones:
        print("\nEl historial está vacío.")
    else:
        print("\n★----------- HISTORIAL DE OPERACIONES --------------★")
        contador = 1  # Empezamos a contar desde 1
        for op in historial_operaciones:
            print(f"{contador}. {op}")
            contador = contador + 1  # Le sumamos 1 para la siguiente vuelta
        print("---------------------★--★--★-------------------------")
