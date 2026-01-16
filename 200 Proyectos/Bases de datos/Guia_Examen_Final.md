---
tags: [guide, exam, databases]
status: refined
difficulty: hard
---

# 🎓 Guía de Supervivencia: Examen Final Bases de Datos

Basada en los "leaks" definitivos. El enfoque es **100% práctico** y de **completar código** (vienen a medias).

## 🚫 Lo que NO entra
- **Teoría Pura**: Zero definiciones, zero test.
- **División**: No hay operador de división en Álgebra Relacional.
- **Justificaciones**: No hay que explicar por qué, solo poner la respuesta correcta.

## 📊 Estructura del Examen (6 Ejercicios)

### 1. Diseño Conceptual (Completar)
Identificar relaciones y escribir el **orden correcto de cardinalidades**.
- [Relación ER](02_Diseño/Relacion_ER.md)

### 2. Álgebra Relacional ⭐ (VALE MUCHO)
Los Joins ya suelen venir hechos. Enfócate en: **UNIÓN, INTERSECCIÓN y DIFERENCIA**.
- [MOC Álgebra Relacional (Ejercicios)](06_Algebra_Relacional/00_MOC_Algebra_Relacional.md)

### 3. DML y Consultas
Sentencias `SELECT` usando: `HAVING`, `GROUP BY`, `ORDER BY`.
- [SELECT Básico](03_SQL/SELECT_Basico.md)

### 4. Normalización ⭐ (VALE MUCHO - El más largo)
Ejercicio de **completar** hasta la **4FN**.
- [MOC Normalización](04_Normalizacion/00_MOC_Normalizacion.md)

### 5. Transacciones
Viene el Stored Procedure ya escrito, hay que completar los comandos: `COMMIT`, `ROLLBACK`, `IF`.
- [Transacciones Control](08_Programacion_BD/Transacciones_Control.md)

### 6. Optimización (La más "rentable")
Es más conceptual. Argumentar qué campos desnormalizar y proponer mejoras.
- [Optimización de Consultas](07_Optimizacion/Query_Optimization.md)

---

## 💡 Tips de Optimización (Extraídos de Clase)

> [!TIP]
> **Reescribir Queries para Velocidad:**
> 1. **Mover condiciones**: Pasa condiciones que estén en el `WHERE` directamente al `JOIN`.
> 2. **Poner LIMITS**: Ejemplo típico de clase: `LIMIT 0, 50`.
> 3. **Desnormalización Estratégica**: Proponer campos para evitar **Joins Masivos** en tablas gigantes.
> 4. **Índices**: Proponer índices para las columnas que filtran los queries.

---
*¡Mucha suerte! Enfócate en practicar los "completar" y asegúrate los puntos de Álgebra y Normalización.*
