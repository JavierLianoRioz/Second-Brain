---
tags: [concept, neuro-efficiency, optimization]
moc: "[00_MOC_Optimizacion](00_MOC_Optimizacion.md)"
status: refined
difficulty: intermediate
---

# Tablas Temporales y Resúmenes

---

## 🧠 Núcleo del Concepto

Las **Tablas Temporales y Resúmenes** son estrategias de optimización que consisten en pre-calcular y materializar resultados de consultas costosas para evitar el procesamiento repetitivo de grandes volúmenes de datos.

*   **Poblamiento Pesado**: Se ejecuta una consulta compleja (ej. agregaciones sobre millones de filas) en horas de baja demanda.
*   **Consulta Ligera**: El usuario final consulta la tabla de resumen, obteniendo resultados de forma casi instantánea.
*   **Materialización**: A diferencia de una vista simple, los datos están físicamente escritos en disco, permitiendo su indexación directa.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] El Flujo de Materialización
>
> ```mermaid
> graph TD
>     D[(Big Data: 8M filas)] -- "Cálculo Programado" --> R[(Tabla Resumen: 10K filas)]
>     R -- "JOIN Indexable" --> U[Usuario / Reporte]
>     
>     style R fill:#dfd,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto

*   **Soluciona**: Problemas de agregaciones no indexables como `SUM(unidades * precio)`.
*   **Relacionado con**: [Query Optimization](Query_Optimization.md) y [Denormalización Estratégica](Denormalizacion_Estrategica.md).

---

## 💻 Flujo de Trabajo

1.  **Diagnóstico**: Detectar señales de `Using temporary` o `Using filesort` en el [Query_Optimization](Query_Optimization.md).
2.  **Mantenimiento**: Programar un proceso (script o evento) para actualizar la tabla periódicamente.

---

> [!tip] Idea Fuerza (Cierre)
> Las tablas resumen son el "caché de disco" de tu lógica de negocio: sacrifica sincronía inmediata por velocidad absoluta.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Optimización](00_MOC_Optimizacion.md).
