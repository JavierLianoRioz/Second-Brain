# Tercera Forma Normal (3FN)

Una tabla está en **3FN** si cumple dos condiciones:

1.  Está en [[Segunda Forma Normal (2FN)]].
2.  No existen **[[Dependencia Transitiva|dependencias transitivas]]**.

### Problema que resuelve:
Elimina las dependencias transitivas, que ocurren cuando un atributo no clave depende de otro atributo no clave, en lugar de depender directamente de la [[Clave Primaria (PK)]].

Ejemplo: `PK → Atributo_A → Atributo_B`. Aquí, `Atributo_B` depende transitivamente de la `PK`.

### Ejemplo

**Tabla No Normalizada (PK: ID_Empleado)**

| ID_Empleado | Nombre | ID_Depto | Nombre_Depto |
|---|---|---|---|
| 1 | Ana | 10 | Ventas |

`Nombre_Depto` depende de `ID_Depto`, no de `ID_Empleado`.

**Solución**

*   **Empleado**: (ID_Empleado, Nombre, ID_Depto)
*   **Departamento**: (ID_Depto, Nombre_Depto)

---
**Relacionado:** [[Normalización]], [[Segunda Forma Normal (2FN)]], [[Dependencia Transitiva]]
