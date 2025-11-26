# Primera Forma Normal (1FN)

Una tabla está en **1FN** si cumple dos condiciones:

1.  La tabla tiene una [[Clave Primaria (PK)]].
2.  Todos sus atributos son **atómicos**, es decir, cada celda de la tabla contiene un único valor. No se permiten listas ni grupos de valores.

Es el primer paso obligatorio en el proceso de [[Normalización]].

### Problema que resuelve:
Elimina los **grupos repetitivos** y los **atributos multivaluados**.

### Ejemplo

**Tabla No Normalizada (No cumple 1FN)**

| Alumno | Cursos |
|---|---|
| Ana | SQL, Python |
| Luis | Java |

**Tabla en 1FN (Atómica)**

| Alumno | Curso |
|---|---|
| Ana | SQL |
| Ana | Python |
| Luis | Java |

---
**Relacionado:** [[Normalización]], [[Segunda Forma Normal (2FN)]]
