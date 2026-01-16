---
tags: [optimization, sql, performance]
moc: [[00_MOC_Optimizacion]]
status: refined
difficulty: intermediate
---

# Optimización de Consultas SQL

---

## 🧠 Núcleo del Concepto

La **optimización de consultas** es el proceso de ajustar las sentencias SQL para que se ejecuten de la manera más eficiente posible, minimizando el consumo de recursos (CPU, disco y memoria).

*   **Evitar Full Table Scans**: El objetivo es que la base de datos use índices en lugar de leer toda la tabla.
*   **Filtrado Temprano**: Reducir el volumen de datos con `WHERE` antes de realizar JOINs costosos.
*   **Sargability**: Escribir condiciones que el motor pueda procesar a través de índices (evitar funciones sobre las columnas indexadas).

---

## 🗺️ Herramientas de Diagnóstico

> [!abstract] El comando `EXPLAIN`
> Permite visualizar el "Plan de Ejecución" que el optimizador ha diseñado para tu consulta.
> 
> *   **type: ALL**: 🚨 ¡Peligro! Escaneo completo de tabla. Necesitas un índice.
> *   **rows**: Estimación de cuántas filas tendrá que examinar el motor.
> *   **key**: El índice que realmente se está utilizando.

---

## 🛠️ Estrategias Proactivas

1.  **Selección Mínima**: No usar `SELECT *`. Solicita solo las columnas necesarias.
2.  **Índices Inteligentes**: Implementación de [[Indices_Compuestos]] basados en los patrones de búsqueda.
3.  **Rediseño**: [Denormalizacion Estratégica](Denormalizacion_Estrategica.md) o uso de [Tablas Temporales](Tablas_Temporales.md) en casos de alta carga.

---

## 🔗 Conexiones y Contexto

*   **Se basa en:** [Algebra Relacional Concepto](../06_Algebra_Relacional/Algebra_Relacional_Concepto.md).
*   **Aplica técnicas como:** [Optimizacion Algebraica](Optimizacion_Algebraica.md) (Pushing Selections Down).

---

> [!tip] Idea Fuerza (Cierre)
> Optimizar no es hacer que la base de datos trabaje más rápido, sino hacer que tenga que trabajar menos.

---

## 🗺️ Mapa de Contenido
*   Volver al: [00 MOC Optimizacion](00_MOC_Optimizacion.md).
