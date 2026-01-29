---
tags: [exercise, practice, relational-algebra]
topic: "[Join_Algebra](Join_Algebra.md)"
level: intermediate
time_estimate: 10 min
---

# Ejercicio: AR Reunión (Join)

## 📝 Escenario y Datos
> [!info] Tablas Académicas (Proximidad)
> *   **Alumnos**: `DNI`, `Nombre`, `Edad`.
> *   **Matricula**: `DNI_A`, `Cod_C`.
> 
> Contexto: Queremos generar un listado que cruce la identidad de los alumnos con los códigos de los cursos en los que están inscritos de forma efectiva.

---

## 🚀 El Reto
Obtener el nombre de los alumnos y el código de los cursos en los que están matriculados.

---

## 💡 Solución (Andamiaje)
> [!success]- Mostrar Solución (Step-by-Step)
> ### Paso 1: Vincular tablas (Join)
> Utilizamos el operador $\bowtie$ para unir `Alumnos` y `Matricula`. Se asume que el cruce es por `DNI = DNI_A`.
> 
> ### Paso 2: Limitar columnas (Proyección)
> Proyectamos ($\pi$) solo los campos `Nombre` y `Cod_C`.
> 
> ---
> **Resultado Final:** 
> $$\pi\{Nombre, Cod\_C\}(Alumnos \bowtie Matricula)$$
