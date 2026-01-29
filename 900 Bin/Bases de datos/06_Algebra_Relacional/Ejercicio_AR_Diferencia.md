---
tags: [exercise, practice, relational-algebra]
topic: "[Diferencia_Operador](Diferencia_Operador.md)"
level: intermediate
time_estimate: 10 min
---

# Ejercicio: AR Diferencia

## 📝 Escenario y Datos
> [!info] Integridad de Matrícula (Proximidad)
> *   **Alumnos**: Contiene todos los estudiantes registrados.
> *   **Matricula**: Contiene los registros de matriculación (`DNI_A`, `Cod_C`).
> 
> Contexto: El departamento de administración necesita detectar qué alumnos están registrados en el sistema pero aún no se han matriculado en ninguna asignatura.

---

## 🚀 El Reto
Obtener los DNI de los alumnos que NO se han matriculado en ningún curso.

---

## 💡 Solución (Andamiaje)
> [!success]- Mostrar Solución (Step-by-Step)
> ### Paso 1: Obtener todos los candidatos
> Proyectamos los DNIs de la tabla `Alumnos`.
> 
> ### Paso 2: Obtener los ya matriculados
> Proyectamos los DNIs de la tabla `Matricula`.
> 
> ### Paso 3: Aplicar resta de conjuntos
> Restamos (-) el segundo conjunto al primero para encontrar la diferencia.
> 
> ---
> **Resultado Final:** 
> $$\pi\{DNI\}(Alumnos) - \pi\{DNI\_A\}(Matricula)$$
