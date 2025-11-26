# Quinta Forma Normal (5FN)

Una tabla está en **Quinta Forma Normal (5FN)**, también conocida como **Forma Normal de Proyección-Unión (PJ/NF)**, si:

1.  Está en [[Cuarta Forma Normal (4FN)]].
2.  No puede descomponerse más sin perder información (no hay dependencias de unión no triviales).

La 5FN se aplica cuando una tabla con **tres o más atributos** puede ser descompuesta en relaciones más pequeñas, y la relación original puede reconstruirse mediante la unión de esas proyecciones, sin generar tuplas espurias. Se aborda cuando existen dependencias de unión.

### Ejemplo
Consideremos una tabla `PROVEEDOR_PRODUCTO_TIENDA` donde un proveedor suministra productos a tiendas específicas, pero no todos los proveedores venden a todas las tiendas ni todos los productos están en todas las tiendas.

**Tabla PROVEEDOR_PRODUCTO_TIENDA (no normalizada)**

| proveedor | producto | tienda  |
|-----------|----------|---------|
| A         | Tornillo | Madrid  |
| A         | Tornillo | Sevilla |
| A         | Tuerca   | Madrid  |
| B         | Tuerca   | Madrid  |

Aquí la información se puede reconstruir a partir de combinaciones de pares de atributos (proveedor-producto, producto-tienda, proveedor-tienda).

### Normalización a 5FN
Dividimos en tres relaciones más simples, cada una representando una dependencia independiente:

**PROVEEDOR_PRODUCTO**

| proveedor | producto |
|-----------|----------|
| A         | Tornillo |
| A         | Tuerca   |
| B         | Tuerca   |

**PRODUCTO_TIENDA**

| producto | tienda  |
|----------|---------|
| Tornillo | Madrid  |
| Tornillo | Sevilla |
| Tuerca   | Madrid  |

**PROVEEDOR_TIENDA**

| proveedor | tienda  |
|-----------|---------|
| A         | Madrid  |
| A         | Sevilla |
| B         | Madrid  |

La relación original se puede reconstruir mediante un JOIN de estas tres tablas, eliminando la redundancia sin perder información.

---
**Relacionado:** [[Normalización]], [[Cuarta Forma Normal (4FN)]], [[Tercera Forma Normal (3FN)]]
