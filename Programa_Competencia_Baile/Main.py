from Inputs import pedir_nombre, pedir_puntuacion, pedir_opcion_menu
from Funciones import (
    calcular_promedio,
    promedio_por_jurado,
    jurado_estricto_generoso,
    participantes_con_promedio_igual,
    buscar_participante,
    top_3,
    ordenar_alfabeticamente
)
import random

participantes = []  # Cada elemento: [nombre, jurado1, jurado2, jurado3]
participantes_cargados = False
puntuaciones_cargadas = False

while True:
    print("\n📋 MENÚ DE OPCIONES")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Participantes con promedio < 4")
    print("5. Participantes con promedio < 8")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Jurado más generoso")
    print("9. Participantes con puntuaciones iguales")
    print("10. Buscar participante por nombre")
    print("11. Top 3 participantes")
    print("12. Participantes ordenados alfabéticamente")
    print("13. Mostrar ganador")
    print("14. Desempatar ganador")
    print("0. Salir")

    opcion = pedir_opcion_menu()

    if opcion == 0:
        print("👋 ¡Gracias por usar el sistema! Adiós.")
        break

    if opcion == 1:
        participantes = []
        for _ in range(5):
            nombre = pedir_nombre()
            participantes.append([nombre])
        participantes_cargados = True
        print("✅ Participantes cargados.")

    elif opcion == 2:
        if not participantes_cargados:
            print("❗ Primero debe cargar los participantes.")
        else:
            for i in range(5):
                p1 = pedir_puntuacion(1)
                p2 = pedir_puntuacion(2)
                p3 = pedir_puntuacion(3)
                participantes[i].extend([p1, p2, p3])
            puntuaciones_cargadas = True
            print("✅ Puntuaciones cargadas.")

    elif not participantes_cargados or not puntuaciones_cargadas:
        print("⚠️ Debe cargar participantes y puntuaciones antes de acceder a esta opción.")

    elif opcion == 3:
        for p in participantes:
            promedio = calcular_promedio(p[1], p[2], p[3])
            print(f"{p[0]} → J1: {p[1]} | J2: {p[2]} | J3: {p[3]} | Promedio: {round(promedio, 2)}")

    elif opcion == 4:
        hay_menor = False
        for p in participantes:
            promedio = calcular_promedio(p[1], p[2], p[3])
            if promedio < 4:
                print(f"{p[0]} → Promedio: {round(promedio, 2)}")
                hay_menor = True
        if not hay_menor:
            print("🚫 Ningún participante tiene promedio menor a 4.")

    elif opcion == 5:
        hay_menor = False
        for p in participantes:
            promedio = calcular_promedio(p[1], p[2], p[3])
            if promedio < 8:
                print(f"{p[0]} → Promedio: {round(promedio, 2)}")
                hay_menor = True
        if not hay_menor:
            print("🚫 Todos los participantes tienen promedio mayor o igual a 8.")

    elif opcion == 6:
        for i in range(1, 4):
            prom = promedio_por_jurado(participantes, i)
            print(f"🎯 Promedio del Jurado {i}: {round(prom, 2)}")

    elif opcion == 7:
        estrictos, _ = jurado_estricto_generoso(participantes)
        print(f"🔒 Jurado más estricto(s): {', '.join(str(j) for j in estrictos)}")

    elif opcion == 8:
        _, generosos = jurado_estricto_generoso(participantes)
        print(f"🎁 Jurado más generoso(s): {', '.join(str(j) for j in generosos)}")

    elif opcion == 9:
        iguales = participantes_con_promedio_igual(participantes)
        if iguales:
            for p in iguales:
                print(f"{p[0]} → Puntos iguales: {p[1]}")
        else:
            print("🚫 No hay participantes con puntuaciones iguales entre los jurados.")

    elif opcion == 10:
        nombre = input("🔍 Ingrese nombre a buscar: ")
        resultado = buscar_participante(participantes, nombre)
        if resultado:
            prom = calcular_promedio(resultado[1], resultado[2], resultado[3])
            print(f"{resultado[0]} → J1: {resultado[1]}, J2: {resultado[2]}, J3: {resultado[3]}, Promedio: {round(prom,2)}")
        else:
            print("❌ Participante no encontrado.")

    elif opcion == 11:
        top = top_3(participantes)
        print("🏅 TOP 3:")
        for p in top:
            promedio = calcular_promedio(p[1], p[2], p[3])
            print(f"{p[0]} → Promedio: {round(promedio, 2)}")

    elif opcion == 12:
        ordenados = ordenar_alfabeticamente(participantes[:])  # copia manual
        for p in ordenados:
            promedio = calcular_promedio(p[1], p[2], p[3])
            print(f"{p[0]} → Promedio: {round(promedio, 2)}")

    elif opcion == 13:
        top = top_3(participantes)
        mayor_prom = calcular_promedio(top[0][1], top[0][2], top[0][3])
        ganadores = []
        for p in participantes:
            if calcular_promedio(p[1], p[2], p[3]) == mayor_prom:
                ganadores.append(p)
        if len(ganadores) == 1:
            print(f"🏆 Ganador: {ganadores[0][0]}")
        else:
            print(f"🔔 Hay {len(ganadores)} participantes con puntaje máximo. Se requiere desempate.")

    elif opcion == 14:
        top = top_3(participantes)
        mayor_prom = calcular_promedio(top[0][1], top[0][2], top[0][3])
        empatados = []
        for p in participantes:
            if calcular_promedio(p[1], p[2], p[3]) == mayor_prom:
                empatados.append(p)
        if len(empatados) == 1:
            print(f"🎉 No hay empate. Ganador ya definido: {empatados[0][0]}")
        else:
            elegido = random.choice(empatados)
            print(f"⚡ Desempate resuelto. Ganador aleatorio: {elegido[0]}")
