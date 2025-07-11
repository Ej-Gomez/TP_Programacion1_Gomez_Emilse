def calcular_promedio(p1, p2, p3):
    """
    Calcula el promedio de tres puntuaciones.
    """
    return (p1 + p2 + p3) / 3

def promedio_por_jurado(lista_participantes, jurado_index):
    """
    Calcula el promedio de puntuaciones que otorgó un jurado.
    """
    total = 0
    for participante in lista_participantes:
        total += participante[jurado_index]
    return total / len(lista_participantes)

def jurado_estricto_generoso(lista_participantes):
    """
    Determina qué jurado fue más estricto y cuál más generoso.
    """
    promedios = []
    for i in range(1, 4):
        prom = promedio_por_jurado(lista_participantes, i)
        promedios.append(prom)

    menor = promedios[0]
    mayor = promedios[0]
    for p in promedios:
        if p < menor:
            menor = p
        if p > mayor:
            mayor = p

    jurados_estrictos = []
    jurados_generosos = []

    for i in range(3):
        if promedios[i] == menor:
            jurados_estrictos.append(i + 1)
        if promedios[i] == mayor:
            jurados_generosos.append(i + 1)

    return jurados_estrictos, jurados_generosos

def participantes_con_promedio_igual(lista_participantes):
    """
    Verifica participantes con puntuaciones iguales en los tres jurados.
    """
    iguales = []
    for participante in lista_participantes:
        if participante[1] == participante[2] == participante[3]:
            iguales.append(participante)
    return iguales

def buscar_participante(lista_participantes, nombre):
    """
    Busca un participante por nombre.
    """
    for p in lista_participantes:
        if p[0].lower() == nombre.lower():
            return p
    return None

def top_3(lista_participantes):
    """
    Retorna los tres participantes con mayor promedio.
    """
    lista_promedios = []
    for participante in lista_participantes:
        promedio = calcular_promedio(participante[1], participante[2], participante[3])
        lista_promedios.append((participante, promedio))

    # Ordenar manualmente por promedio descendente
    for i in range(len(lista_promedios)):
        for j in range(i + 1, len(lista_promedios)):
            if lista_promedios[j][1] > lista_promedios[i][1]:
                lista_promedios[i], lista_promedios[j] = lista_promedios[j], lista_promedios[i]

    return [p[0] for p in lista_promedios[:3]]

def ordenar_alfabeticamente(lista_participantes):
    """
    Ordena los participantes alfabéticamente por nombre.
    """
    for i in range(len(lista_participantes)):
        for j in range(i + 1, len(lista_participantes)):
            if lista_participantes[j][0].lower() < lista_participantes[i][0].lower():
                lista_participantes[i], lista_participantes[j] = lista_participantes[j], lista_participantes[i]
    return lista_participantes