---
tags: [exercise, practice, relational-algebra]
topic: "[Interseccion_Operador](Interseccion_Operador.md)"
level: advanced
time_estimate: 15 min
---

# Ejercicio: AR Intersección

## 📝 Escenario y Datos
> [!info] Coincidencias de Cursos (Proximidad)
> Una tabla **Matricula** con campos `DNI_A` y `Cod_C`.
> 
> Contexto: Buscamos identificar a los alumnos "dual-track" que están cursando simultáneamente dos asignaturas específicas de alto rendimiento.

---

## 🚀 El Reto
Obtener los DNI de alumnos que están en el curso 'C1' y también en el 'C2'.

---

## 💡 Solución (Andamiaje)
> [!success]- Mostrar Solución (Step-by-Step)
> ### Paso 1: Aislar grupo C1
> Seleccionamos los alumnos con `Cod_C='C1'` y proyectamos sus DNIs.
> 
> ### Paso 2: Aislar grupo C2
> Seleccionamos los alumnos con `Cod_C='C2'` y proyectamos sus DNIs.
> 
> ### Paso 3: Encontrar la coincidencia
> Aplicamos el operador de intersección ($\cap$) entre ambos conjuntos.
> 
> ---
> **Resultado Final:** 
> $$\pi\{DNI\_A\}(\sigma\{Cod\_C='C1'\}(Matricula)) \cap \pi\{DNI\_A\}(\sigma\{Cod\_C='C2'\}(Matricula))$$
