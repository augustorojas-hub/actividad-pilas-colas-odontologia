"""
PROGRAMA 1: PILA DE PACIENTES PARA EXTRACCIONES URGENTES
Consultorio odontológico - Datos ficticios para fines académicos.

Reglas:
- Solo incluye procedimientos de extracción dental.
- Solo incluye prioridad "Urgente".
- Ordena por fecha de cita de la más cercana a la más lejana.
- La cima de la pila contiene la próxima cita.
"""

from datetime import datetime

pacientes = [
    {"id": 1, "nombre": "Laura Gómez", "procedimiento": "Extracción dental",
     "prioridad": "Urgente", "fecha": "2026-10-16", "hora": "08:00"},
    {"id": 2, "nombre": "Carlos Ruiz", "procedimiento": "Limpieza dental",
     "prioridad": "Urgente", "fecha": "2026-10-16", "hora": "09:00"},
    {"id": 3, "nombre": "María Torres", "procedimiento": "Extracción dental",
     "prioridad": "Normal", "fecha": "2026-10-17", "hora": "10:00"},
    {"id": 4, "nombre": "Andrés Pérez", "procedimiento": "Extracción dental",
     "prioridad": "Urgente", "fecha": "2026-10-18", "hora": "11:00"},
    {"id": 5, "nombre": "Sofía Ramírez", "procedimiento": "Extracción dental",
     "prioridad": "Urgente", "fecha": "2026-10-17", "hora": "09:30"},
    {"id": 6, "nombre": "Julián Castro", "procedimiento": "Ortodoncia",
     "prioridad": "Normal", "fecha": "2026-10-16", "hora": "11:30"},
    {"id": 7, "nombre": "Valentina Díaz", "procedimiento": "Extracción dental",
     "prioridad": "Urgente", "fecha": "2026-10-16", "hora": "10:00"},
]

def construir_pila(lista_pacientes):
    """Devuelve una lista usada como pila; el último elemento es la cima."""
    candidatos = [
        p for p in lista_pacientes
        if p["procedimiento"].strip().casefold() == "extracción dental".casefold()
        and p["prioridad"].strip().casefold() == "urgente"
    ]

    # Orden ascendente por fecha y hora: primero la cita más próxima.
    candidatos.sort(
        key=lambda p: datetime.strptime(
            f'{p["fecha"]} {p["hora"]}', "%Y-%m-%d %H:%M"
        )
    )

    # Una pila retira desde el final. Se invierte para que la cita más próxima
    # quede en la cima (final de la lista).
    pila = list(reversed(candidatos))
    return pila

def mostrar_informe(pila):
    print("=" * 72)
    print("INFORME DE PILA: EXTRACCIONES DENTALES URGENTES")
    print("La cima de la pila aparece primero en este informe.")
    print("=" * 72)

    if not pila:
        print("No hay pacientes que cumplan los criterios.")
        return

    # Mostrar desde la cima hacia abajo, sin modificar la pila.
    for posicion, paciente in enumerate(reversed(pila), start=1):
        print(
            f"{posicion}. {paciente['nombre']} | "
            f"Fecha: {paciente['fecha']} | Hora: {paciente['hora']} | "
            f"Procedimiento: {paciente['procedimiento']} | "
            f"Prioridad: {paciente['prioridad']}"
        )

def atender_siguiente(pila):
    """Retira de la pila al paciente de fecha más cercana."""
    if not pila:
        print("La pila está vacía. No hay pacientes pendientes.")
        return None

    paciente = pila.pop()
    print(
        f"Se llama a {paciente['nombre']} para su extracción dental "
        f"urgente ({paciente['fecha']} a las {paciente['hora']})."
    )
    return paciente

if __name__ == "__main__":
    pila_urgentes = construir_pila(pacientes)
    mostrar_informe(pila_urgentes)

    print("\n--- DEMOSTRACIÓN: LLAMAR AL PRÓXIMO PACIENTE ---")
    atender_siguiente(pila_urgentes)

    print("\n--- PILA ACTUALIZADA ---")
    mostrar_informe(pila_urgentes)
