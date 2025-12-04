# Primera Forma Normal (1FN)

## Regla
Una tabla está en **1FN** si:
1.  Todos los atributos son **atómicos** (indivisibles).
2.  No hay grupos repetitivos (columnas como `tel1`, `tel2`).

## Ejemplo Violación
| Cliente | Telefonos |
| :--- | :--- |
| Ana | 555-123, 555-999 |

## Solución
Separar en filas distintas o crear nueva tabla.

| Cliente | Telefono |
| :--- | :--- |
| Ana | 555-123 |
| Ana | 555-999 |

---
[[00_MOC_Normalizacion]]
