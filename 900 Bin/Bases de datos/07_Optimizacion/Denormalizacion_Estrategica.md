# Denormalización Estratégica

La denormalización consiste en introducir redundancia de forma controlada para mejorar el rendimiento de consultas de lectura en sistemas con volúmenes masivos de datos.

## El Problema del JOIN Masivo
En tablas con millones de registros, un JOIN indexado puede ser lento no por falta de índices, sino porque ocurre demasiadas veces (salto repetido entre páginas de datos en disco).

## Cuándo Denormalizar
- Tablas con millones de filas.
- Consultas críticas (listados frecuentes) que requieren columnas de otra tabla.
- Columnas que son **estables** (cambian poco) y se usan frecuentemente en filtros o visualización.

## Implementación
1. **Copiar columna**: Añadir la columna de la tabla "padre" a la tabla "hijo".
2. **Índice**: Crear un índice que incluya la nueva columna para evitar el JOIN completamente.
3. **Sincronización**: Mantener la consistencia mediante:
    - **Triggers**: Para actualizar automáticamente el hijo cuando el padre cambia.
    - **Lógica de Aplicación**: Manejar la duplicidad en el código de backend.

## Costes y Riesgos
- **Duplicación de datos**: Mayor uso de almacenamiento.
- **Update Anomalies**: Riesgo de inconsistencia si la sincronización falla.
- **Escrituras más lentas**: Las actualizaciones en el padre ahora disparan actualizaciones en los hijos.

---
- **Relacionado**: [Modelo Relacional Conceptos](../02_Diseño/Modelo_Relacional_Conceptos.md), [Query Optimization](Query_Optimization.md)
