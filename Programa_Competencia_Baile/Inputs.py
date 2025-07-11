def pedir_nombre():
    """
    Solicita el nombre de un participante y valida que tenga al menos 3 caracteres
    y contenga solo letras y espacios.
    """
    while True:
        nombre = input("Ingrese el nombre del participante: ").strip()
        if len(nombre) >= 3 and all(c.isalpha() or c.isspace() for c in nombre):
            return nombre
        print("❌ Nombre inválido. Intente nuevamente.")

def pedir_puntuacion(jurado_numero):
    """
    Solicita una puntuación entre 1 y 10 para un jurado específico.
    """
    while True:
        valor = input(f"Ingrese la puntuación del jurado {jurado_numero} (1-10): ")
        if valor.isdigit():
            valor = int(valor)
            if 1 <= valor <= 10:
                return valor
        print("⚠️ Puntuación inválida. Debe ser un número entre 1 y 10.")

def pedir_opcion_menu():
    """
    Solicita una opción del menú entre 0 y 14.
    """
    while True:
        opcion = input("Seleccione una opción (0-14): ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 14:
                return opcion
        print("❌ Opción inválida.")