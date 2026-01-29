---
tags: [exercise, practice, relational-algebra]
topic: "[Algebra_Relacional_Concepto](Algebra_Relacional_Concepto.md)"
level: beginner
time_estimate: 5 min
---

# Ejercicio: AR Selección y Proyección

## 📝 Escenario y Datos
> [!info] Tabla Alumnos (Proximidad)
> Se dispone de una tabla `Alumnos` con los campos: `DNI`, `Nombre`, `Apellido`, `Edad`.
> 
> Un párrafo de contexto: En el sistema académico actual, necesitamos identificar rápidamente a los alumnos que cumplen con la mayoría de edad legal para ciertos trámites administrativos.

---

## 🚀 El Reto
Obtener el nombre de todos los alumnos que tienen más de 20 años utilizando álgebra relacional.

---

## 💡 Solución (Andamiaje)
> [!success]- Mostrar Solución (Step-by-Step)
> ### Paso 1: Filtrado de filas (Selección)
> Aplicamos el operador $\sigma$ sobre la tabla `Alumnos` filtrando por `Edad > 20`.
> 
> ### Paso 2: Selección de columnas (Proyección)
> Aplicamos el operador $\pi$ sobre el resultado anterior para quedarnos solo con la columna `Nombre`.
> 
> ---
> **Resultado Final:** 
> $$\pi\{Nombre\}(\sigma\{Edad > 20\}(Alumnos))$$
