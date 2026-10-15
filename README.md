# Actividad: Pilas y colas en un consultorio odontológico

## Archivos
- `pila_urgencias.py`: filtra extracciones dentales con prioridad Urgente, ordena por fecha y hora, genera el informe y permite llamar al siguiente paciente.
- `cola_atencion.py`: crea la agenda diaria y atiende a los pacientes en el orden FIFO.
- `informe_actividad.md`: explicación académica, algoritmo, pruebas y conclusiones.

## Requisitos
Python 3.9 o superior. No requiere instalar librerías externas.

## Ejecución
Desde una terminal, dentro de esta carpeta:

```bash
python pila_urgencias.py
python cola_atencion.py
```

Los nombres, fechas y horas son datos ficticios de ejemplo. Se pueden reemplazar por datos de prueba propios, evitando publicar información personal real de pacientes.

## Nota sobre la pila
La lista de Python se usa como pila: `append` agrega y `pop` retira la cima. Para que el siguiente paciente llamado sea el de fecha más cercana, los candidatos se ordenan cronológicamente y se invierten al construir la pila. El informe muestra la cima primero. Esto conserva el comportamiento LIFO de la estructura.
