#Inputs.py
import random

# Participantes con sus notas del jurado (3 notas por participante)
# Ejemplo: [("Ana", [8, 9, 10]), ("Luis", [7, 8, 9]), ...]
participantes = [
    ("Ana", [9, 9, 10]),
    ("Luis", [10, 8, 9]),
    ("Sofía", [9, 10, 9]),
    ("Carlos", [10, 10, 8])
]

# Función para calcular el promedio de notas (sin usar sum())
def calcular_promedio(notas):
    total = 0
    i = 0
    while i < len(notas):
        total = total + notas[i]
        i = i + 1
    return total / len(notas)

# Función para obtener el/la mejor participante
def obtener_ganador(lista_participantes):
    mejores = []
    mejor_promedio = 0
    i = 0

    while i < len(lista_participantes):
        nombre = lista_participantes[i][0]
        notas = lista_participantes[i][1]
        promedio = calcular_promedio(notas)

        if promedio > mejor_promedio:
            mejores = [[nombre, promedio]]
            mejor_promedio = promedio
        elif promedio == mejor_promedio:
            mejores += [[nombre, promedio]]
        i += 1

    if len(mejores) == 1:
        return mejores[0][0]
    else:
        return desempatar(mejores)

# Función para desempatar (elige al azar uno de los empatados)
def desempatar(lista_empatados):
    cantidad = 0
    for _ in lista_empatados:
        cantidad += 1
    indice_aleatorio = int(random.random() * cantidad)
    return lista_empatados[indice_aleatorio][0]

# Mostrar resultados
ganador = obtener_ganador(participantes)
print("El/la representante seleccionado/a es:", ganador)
