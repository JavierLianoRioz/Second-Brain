# Tercera Forma Normal (3FN)

## Regla
Una tabla está en **3FN** si:
1.  Cumple con [[Segunda_Forma_Normal_2FN]].
2.  No existen **Dependencias Transitivas**. Ningún atributo no clave debe depender de otro atributo no clave.

## Ejemplo Violación
Tabla `Empleados (ID, Nombre, CodigoPostal, Ciudad)`.
`CodigoPostal -> Ciudad`.
La ciudad depende del CP, no directamente del ID del empleado.

## Solución
Separar:
1.  `Ciudades (CodigoPostal, Ciudad)`
2.  `Empleados (ID, Nombre, CodigoPostal)`

---
[[00_MOC_Normalizacion]]
