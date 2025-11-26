# Dependencia Funcional

Una **dependencia funcional** es una [[Restricciones (Constraints) en SQL|restricción]] entre dos atributos o conjuntos de atributos en una base de datos. Es un concepto fundamental para la [[Normalización]].

Se dice que un atributo B tiene una dependencia funcional de un atributo A (denotado como **A → B**) si cada valor de A en la tabla está asociado con exactamente un valor de B.

En otras palabras, si conoces el valor de A, puedes determinar unívocamente el valor de B.

Ejemplo: `DNI → Nombre_Empleado`.

---
**Relacionado:** [[Normalización]], [[Segunda Forma Normal (2FN)]], [[Tercera Forma Normal (3FN)]]
