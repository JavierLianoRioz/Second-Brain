---
tags: [concept, neuro-efficiency, db-design]
moc: "[00_MOC_Diseño](00_MOC_Diseño.md)"
status: refined
difficulty: hard
---

# Transformación: De ER a Relacional

---

## 🧠 Núcleo del Concepto
El paso del Diseño Conceptual al Lógico sigue un algoritmo determinista para asegurar que no se pierda semántica ni integridad en el proceso.

*   **Entidades a Tablas:** Cada entidad fuerte se convierte en una tabla; su identificador es la PK.
*   **Relaciones 1:1 y 1:N:** Se resuelven mediante la **propagación de clave** (la PK del lado "uno" viaja como FK al lado opuesto).
*   **Relaciones N:M:** Generan obligatoriamente una **Tabla Intermedia** cuyas FKs son las PKs de las entidades originales.

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Reglas Clave de Mapeo
> ```mermaid
> graph TD
>     ER_Entidad --> T_Tabla
>     ER_1_N --> T_FK[Propagar FK]
>     ER_N_M --> T_TableNew[Nueva Tabla Intermedia]
> ```

---

## 💡 Práctica de Recuperación
> [!success]- Reto: Aplica la Transformación
> **Caso Videoclub**: Un `Socio` alquila muchas `Peliculas`, pero una `Pelicula` solo puede ser alquilada por un `Socio` a la vez (1:N).
> 
> **Puntos a resolver:**
> 1. ¿A qué tabla le añades una Clave Foránea?
> 2. Si cambiamos a N:M (histórico de alquileres), ¿qué estructura surge?
> 
> **Soluciones**:
> 1. Añadir `id_socio` (FK) a la tabla `Pelicula`.
> 2. Crear una tabla `Alquiler` con {`id_socio`, `id_pelicula`} como PK/FKs.

---

> [!tip] Idea Fuerza (Cierre)
> La transformación no es creativa, es algorítmica: si el diagrama ER es correcto, el modelo relacional surge por sí solo.
