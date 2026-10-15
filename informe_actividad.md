# Informe de la actividad: Implementación de pilas y colas en un consultorio odontológico

## 1. Introducción
Este trabajo simula la gestión de pacientes de un consultorio odontológico mediante dos estructuras de datos: una pila para identificar las citas urgentes de extracción dental y una cola para administrar la agenda diaria. Se emplean datos ficticios con fines académicos.

## 2. Objetivo general
Desarrollar dos programas en Python que apliquen correctamente las estructuras de datos pila y cola para organizar la atención de pacientes según los requisitos del consultorio.

## 3. Objetivos específicos
- Filtrar únicamente pacientes cuyo procedimiento sea extracción dental y cuya prioridad sea Urgente.
- Ordenar los pacientes elegibles por fecha y hora, desde la cita más próxima hasta la más lejana.
- Generar un informe que permita al personal identificar a quién llamar primero.
- Construir una cola a partir de la agenda diaria y atender a los pacientes en el orden establecido.
- Comprobar el comportamiento de ambas estructuras mediante ejemplos.

## 4. Desarrollo

### 4.1. Pila de extracciones urgentes
El programa `pila_urgencias.py` almacena datos ficticios de pacientes. Primero filtra los registros que cumplen simultáneamente las dos condiciones: procedimiento igual a “Extracción dental” y prioridad igual a “Urgente”. Después convierte fecha y hora en valores comparables y ordena los candidatos de manera ascendente.

Como una pila retira su último elemento agregado, el programa invierte la lista ordenada al construir la pila. Así, la cita más próxima queda en la cima. El informe recorre la pila desde la cima sin modificarla, y la operación `pop()` retira al siguiente paciente que debe ser llamado.

### 4.2. Cola de atención diaria
El programa `cola_atencion.py` utiliza `deque` de `collections`. Los pacientes se agregan al final con `append()` y se atienden desde el principio con `popleft()`. Este funcionamiento corresponde a FIFO (*First In, First Out*): el primero que entra es el primero que sale. La agenda de ejemplo ya está en el orden de atención definido por el consultorio.

## 5. Algoritmos en pseudocódigo

### Pila
1. Crear la lista de pacientes.
2. Seleccionar los pacientes cuyo procedimiento sea extracción dental y cuya prioridad sea Urgente.
3. Ordenar los seleccionados por fecha y hora ascendentes.
4. Invertir la lista para que el paciente más próximo quede en la cima de la pila.
5. Mostrar el informe desde la cima hacia abajo.
6. Cuando corresponda, retirar al siguiente paciente con `pop()`.

### Cola
1. Crear la agenda del día en el orden establecido.
2. Insertar cada paciente al final de la cola.
3. Mostrar la agenda.
4. Mientras la cola no esté vacía, retirar el primer paciente con `popleft()` y mostrar que será atendido.
5. Finalizar cuando no queden pacientes.

## 6. Pruebas y resultados esperados

### Prueba de la pila
Los registros de ejemplo que cumplen los filtros son:
- Laura Gómez — 2026-10-16, 08:00.
- Valentina Díaz — 2026-10-16, 10:00.
- Sofía Ramírez — 2026-10-17, 09:30.
- Andrés Pérez — 2026-10-18, 11:00.

No se incluye a Carlos Ruiz porque tiene una limpieza dental, aunque su prioridad sea urgente. Tampoco se incluye a María Torres porque su prioridad es normal, ni a Julián Castro porque su procedimiento es ortodoncia.

El informe debe mostrar a Laura Gómez primero, seguida de Valentina Díaz, Sofía Ramírez y Andrés Pérez. Después de llamar a Laura, la cima pasa a ser Valentina.

### Prueba de la cola
La cola atiende a los pacientes en este orden:
1. Laura Gómez — 08:00.
2. Carlos Ruiz — 08:30.
3. María Torres — 09:00.
4. Andrés Pérez — 09:30.
5. Sofía Ramírez — 10:00.

La cola termina vacía cuando todos los pacientes han sido retirados y atendidos.

## 7. Estructuras y operaciones utilizadas

| Estructura | Operación | Función |
|---|---|---|
| Pila | `append()` | Agregar un elemento a la cima |
| Pila | `pop()` | Retirar el elemento de la cima |
| Cola | `append()` | Agregar un paciente al final |
| Cola | `popleft()` | Retirar al paciente del frente |

## 8. Conclusiones
La pila permite construir un listado específico de pacientes con extracciones urgentes y presentar primero la cita más cercana. La cola permite respetar el orden de la agenda diaria mediante la política FIFO. Ambas estructuras cumplen propósitos distintos y se implementan con operaciones coherentes con su funcionamiento.

## 9. Consideración
Este es un prototipo académico, no un sistema clínico real. En una clínica se deben verificar los datos y la prioridad con personal sanitario, proteger la información personal y no sustituir el criterio clínico por el orden informático. Los datos incluidos son ficticios.
