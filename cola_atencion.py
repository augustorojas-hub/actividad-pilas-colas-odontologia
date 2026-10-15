"""
PROGRAMA 2: COLA DE ATENCIÓN DIARIA
Consultorio odontológico - Datos ficticios para fines académicos.

Regla:
- Se atiende en el orden de la agenda: primero en entrar, primero en salir (FIFO).
"""

from collections import deque

agenda = [
    {"hora": "08:00", "nombre": "Laura Gómez", "procedimiento": "Valoración"},
    {"hora": "08:30", "nombre": "Carlos Ruiz", "procedimiento": "Limpieza dental"},
    {"hora": "09:00", "nombre": "María Torres", "procedimiento": "Control odontológico"},
    {"hora": "09:30", "nombre": "Andrés Pérez", "procedimiento": "Extracción dental"},
    {"hora": "10:00", "nombre": "Sofía Ramírez", "procedimiento": "Restauración"},
]

def generar_cola(agenda_del_dia):
    """Construye una cola respetando el orden en que aparece la agenda."""
    cola = deque()
    for paciente in agenda_del_dia:
        cola.append(paciente)
    return cola

def mostrar_agenda(cola):
    print("=" * 65)
    print("AGENDA DIARIA DEL CONSULTORIO ODONTOLÓGICO")
    print("=" * 65)
    if not cola:
        print("No hay pacientes en la agenda.")
        return
    for numero, paciente in enumerate(cola, start=1):
        print(
            f"{numero}. {paciente['hora']} | {paciente['nombre']} | "
            f"{paciente['procedimiento']}"
        )

def atender_paciente(cola):
    """Atiende y retira al primer paciente de la cola."""
    if not cola:
        print("La cola está vacía. No hay pacientes pendientes.")
        return None

    paciente = cola.popleft()
    print(
        f"Atendiendo a las {paciente['hora']} a {paciente['nombre']}. "
        f"Procedimiento: {paciente['procedimiento']}."
    )
    return paciente

if __name__ == "__main__":
    cola_atencion = generar_cola(agenda)
    mostrar_agenda(cola_atencion)

    print("\n--- INICIO DE ATENCIÓN ---")
    while cola_atencion:
        atender_paciente(cola_atencion)

    print("\nTodos los pacientes de la agenda han sido atendidos.")
