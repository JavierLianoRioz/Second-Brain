# Tercera Forma Normal (3FN)

La **Tercera Forma Normal (3FN)** se centra en eliminar las **Dependencias Transitivas**. Su lema informal es: *"Todos los atributos deben depender de la clave, de toda la clave y nada más que de la clave"*.

## Regla
Una tabla está en **3FN** si:
1.  Ya cumple con la [[Segunda_Forma_Normal_2FN]].
2.  **No existen Dependencias Transitivas**: Ningún atributo no clave debe depender de otro atributo que no sea la Clave Primaria.

### ¿Qué es una Dependencia Transitiva?
Ocurre cuando un atributo $Z$ depende de $Y$, y $Y$ depende de $X$ (la Clave Primaria).
$$ X \rightarrow Y \rightarrow Z $$
En este caso, $Z$ depende "transitivamente" de $X$ a través de $Y$.

---

## Ejemplo Práctico: Empleados y Departamentos

Imagina una tabla `EMPLEADOS` donde guardamos información del empleado y su departamento.
**Clave Primaria**: `ID_Empleado`.

### ❌ Tabla NO Normalizada (Violación de 3FN)

| ID_Empleado | Nombre | ID_Depto | Nombre_Depto | Ubicacion_Depto |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Juan | D1 | Ventas | Madrid |
| 2 | Ana | D1 | Ventas | Madrid |
| 3 | Pedro | D2 | IT | Barcelona |

**Problema:**
*   `ID_Empleado` determina `ID_Depto`.
*   `ID_Depto` determina `Nombre_Depto` y `Ubicacion_Depto`.
*   Por tanto, `Nombre_Depto` depende transitivamente de `ID_Empleado`.

**Anomalías:**
1.  **Redundancia**: Repetimos "Ventas" y "Madrid" para cada empleado de ese departamento.
2.  **Actualización**: Si el departamento de Ventas se muda a "Valencia", tenemos que actualizar todas las filas de sus empleados. Si olvidamos uno, la base de datos queda inconsistente.

---

### ✅ Solución (Aplicando 3FN)

Sacamos los atributos que dependen del atributo no clave (`ID_Depto`) a su propia tabla.

**Tabla 1: EMPLEADOS**
(Solo guardamos la referencia)

| ID_Empleado | Nombre | ID_Depto |
| :--- | :--- | :--- |
| 1 | Juan | D1 |
| 2 | Ana | D1 |
| 3 | Pedro | D2 |

**Tabla 2: DEPARTAMENTOS**
(Información única del departamento)

| ID_Depto | Nombre_Depto | Ubicacion_Depto |
| :--- | :--- | :--- |
| D1 | Ventas | Madrid |
| D2 | IT | Barcelona |

## Beneficios
*   **Cero Redundancia**: La información del departamento se guarda una sola vez.
*   **Consistencia**: Si cambiamos el nombre del departamento, cambia automáticamente para todos los empleados.

---
[[00_MOC_Normalizacion]]
