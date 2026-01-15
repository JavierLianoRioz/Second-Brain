# Optimización de Consultas SQL

La optimización de consultas es el proceso de ajustar las sentencias SQL para que se ejecuten de la manera más eficiente posible, minimizando el uso de CPU, disco y memoria.

## Principios Fundamentales

1. **Evitar Full Table Scans**: El objetivo principal es que el optimizador use índices para localizar las filas necesarias.
2. **Filtrado Temprano**: Aplicar cláusulas `WHERE` lo antes posible para reducir el volumen de datos que fluye a través de JOINs y agregaciones.
3. **Selección de Columnas**: No usar `SELECT *`. Solicitar solo las columnas estrictamente necesarias para reducir el ancho de banda y permitir el uso de **Covering Indexes**.
4. **Sargability**: Asegurarse de que las condiciones en el `WHERE` permitan el uso de índices. Evitar funciones en las columnas indexadas (ej. `WHERE YEAR(fecha) = 2024` rompe el índice).

## Herramientas de Análisis

- **EXPLAIN**: Permite ver el plan de ejecución de MySQL.
- **Señales de alerta en EXPLAIN**:
    - `type: ALL`: Escaneo completo de tabla.
    - `Extra: Using temporary`: Se necesitan tablas temporales para procesar la consulta.
    - `Extra: Using filesort`: Se requiere una fase de ordenamiento en disco/memoria.

## Estrategias Proactivas
- [Índices Compuestos](Indices_Compuestos.md)
- [Denormalización Estratégica](Denormalizacion_Estrategica.md)
- [Tablas Temporales y Resúmenes](Tablas_Temporales.md)

---
- **Fuente**: Clase 25 y 26 - Optimización
- **Relacionado**: [[03_SQL/00_MOC_SQL]], [[Modelo_Relacional_Conceptos]]
