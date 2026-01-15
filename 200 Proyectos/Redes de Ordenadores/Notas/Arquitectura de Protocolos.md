# Arquitectura de Protocolos

Una arquitectura de protocolos es el marco estructurado que permite la comunicación entre sistemas complejos mediante la división de tareas en capas.

## ¿Qué es un Protocolo?
Un conjunto de reglas que gobiernan el intercambio de datos. Sus componentes clave son:
- **Sintaxis**: El formato de los datos y los niveles de señal.
- **Semántica**: El significado de la información (ej. control de errores, información de control).
- **Temporización**: Coordinación de la velocidad y el orden de los datos.

## Concepto de Niveles (Layering)
La comunicación se divide en "capas" o niveles de abstracción:
- Cada capa $N$ ofrece servicios a la capa superior $N+1$.
- Cada capa $N$ utiliza los servicios de la capa inferior $N-1$.
- Esto permite cambiar la implementación de una capa sin afectar a las demás (independencia).

## Encapsulamiento y PDU
- **Encapsulamiento**: Al bajar por las capas, cada nivel añade su propia cabecera a los datos recibidos del nivel superior.
  - *Analogía*: Escribes una carta (Datos), la metes en un sobre con dirección (Cabecera de Red), y ese sobre se mete en un saco de correos con una ruta (Cabecera de Enlace).
- **Desencapsulamiento**: Proceso inverso al recibir los datos (abrir el saco, abrir el sobre, leer la carta).

---
**Relacionado**: [Modelo OSI](Modelo%20OSI.md), [Modelo TCP-IP](Modelo%20TCP-IP.md)
**Fuente**: [[12_Tema1.pdf]]
