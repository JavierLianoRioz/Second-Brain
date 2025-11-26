# Dependencia Transitiva

Una **dependencia transitiva** es una [[Dependencia Funcional]] indirecta en una tabla, donde un atributo no clave depende de otro atributo no clave.

Se produce cuando tenemos una cadena de dependencias funcionales:
`A → B` y `B → C`. Si A es la [[Clave Primaria (PK)]] y B y C son atributos no clave, entonces `C` depende transitivamente de `A` a través de `B`.

La [[Tercera Forma Normal (3FN)]] se enfoca en eliminar este tipo de dependencias para reducir la redundancia de datos.

---
**Relacionado:** [[Tercera Forma Normal (3FN)]], [[Dependencia Funcional]]
