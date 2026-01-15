# Tablas Temporales y Resúmenes

Cuando una consulta requiere cálculos complejos (agregaciones sobre millones de filas) que no pueden ser indexados directamente, la solución es cambiar el enfoque hacia un diseño orientado a la consulta.

## El Problema de las Consultas no Indexables
Ciertos cálculos como `SUM(unidades * precio)` o `COUNT(DISTINCT ide_pedido)` sobre grandes volúmenes no existen físicamente en la tabla y, por tanto, no pueden ser indexados. Estos generan en EXPLAIN señales de `Using temporary` y `Using filesort` sobre millones de registros.

## Tablas de Resumen Materializadas
En lugar de calcular en tiempo real para cada reporte, se crea una tabla física (materializada) que contiene los datos ya procesados.

### Ventajas
- **Dataset Reducido**: Una consulta sobre 8 millones de items puede convertirse en una tabla de resumen con solo unos pocos miles de filas (ej. ventas por país y día).
- **Sin JOINs**: La tabla resumen contiene toda la información necesaria.
- **Indexable**: Se pueden crear índices sobre las columnas ya calculadas.

## Flujo de Trabajo
1. **Poblado**: Se ejecuta una consulta pesada fuera de horas pico para llenar la tabla resumen.
2. **Consulta en Caliente**: Los usuarios consultan la tabla resumen de forma casi instantánea.
3. **Actualización**: Se programa un proceso (script o evento) para actualizar la tabla periódicamente (diario, por hora).

---
- **Relacionado**: [Optimización de Consultas SQL](Query_Optimization.md), [Denormalización Estratégica](Denormalizacion_Estrategica.md)
