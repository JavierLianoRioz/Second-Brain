# Segunda Forma Normal (2FN)

## Regla
Una tabla está en **2FN** si:
1.  Cumple con la [Primera_Forma_Normal_1FN](Primera_Forma_Normal_1FN.md).
2.  **No existen Dependencias Parciales**.

Esto significa que si una tabla tiene una **Clave Primaria Compuesta** (formada por varios campos), los atributos que no son clave deben depender de **toda** la clave, no solo de una parte.

> [!TIP]
> Si la Clave Primaria es un solo campo (ej. ID), la tabla ya está automáticamente en 2FN.

## Ejemplo: Detalles de Pedido

Imagina una tabla para guardar los productos de un pedido.
**Clave Primaria Compuesta**: `(ID_Pedido, ID_Producto)`

| ID_Pedido | ID_Producto | Cantidad | Nombre_Producto |
| :--- | :--- | :--- | :--- |
| 101 | A1 | 2 | **Laptop** |
| 101 | B2 | 1 | **Mouse** |
| 102 | A1 | 1 | **Laptop** |

### El Problema (Dependencia Parcial)
*   `Cantidad` depende de **ambos** (`ID_Pedido` + `ID_Producto`). (Necesito saber qué pedido y qué producto para saber la cantidad). ✅
*   `Nombre_Producto` ("Laptop") depende **solo** de `ID_Producto`. No importa el número de pedido, el producto A1 siempre se llamará "Laptop". ❌

Esto es una **Dependencia Parcial**: `Nombre_Producto` depende solo de una parte de la clave (`ID_Producto`).

### Solución
Separar los datos del producto en su propia tabla.

**Tabla 1: Detalles_Pedido** (Solo datos del pedido-producto)

| ID_Pedido | ID_Producto | Cantidad |
| :--- | :--- | :--- |
| 101 | A1 | 2 |
| 101 | B2 | 1 |

**Tabla 2: Productos** (Datos fijos del producto)

| ID_Producto | Nombre_Producto |
| :--- | :--- |
| A1 | Laptop |
| B2 | Mouse |

Ahora `Nombre_Producto` depende totalmente de la clave de su nueva tabla (`ID_Producto`).

---
[00_MOC_Normalizacion](00_MOC_Normalizacion.md)
