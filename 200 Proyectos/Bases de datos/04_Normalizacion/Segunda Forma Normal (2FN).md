# Segunda Forma Normal (2FN)

Una tabla está en **2FN** si cumple dos condiciones:

1.  Está en [[Primera Forma Normal (1FN)]].
2.  Todos sus atributos no clave tienen una **[[Dependencia Funcional]] completa** de la [[Clave Primaria (PK)]] completa.

### Problema que resuelve:
Elimina las **dependencias parciales**. Esto solo es relevante para tablas con claves primarias compuestas (formadas por más de una columna). Una dependencia parcial ocurre cuando un atributo no clave depende solo de una parte de la clave primaria compuesta.

### Ejemplo

**Tabla No Normalizada (PK: ID_Pedido, ID_Producto)**

| ID_Pedido | ID_Producto | Cantidad | Nombre_Producto |
|---|---|---|---|
| 1 | 100 | 2 | Laptop |

Aquí `Nombre_Producto` depende solo de `ID_Producto` (parte de la clave), no del pedido.

**Solución (Tablas separadas)**

*   **Detalle_Pedido**: (ID_Pedido, ID_Producto, Cantidad)
*   **Producto**: (ID_Producto, Nombre_Producto)

---
**Relacionado:** [[Normalización]], [[Primera Forma Normal (1FN)]], [[Tercera Forma Normal (3FN)]]
