# Formas Normales Básicas (1FN, 2FN, 3FN)

Son las más importantes y suficientes para la mayoría de las bases de datos empresariales.

## 1. Primera Forma Normal (1FN)

**Regla**:
1.  Todos los atributos deben ser **atómicos** (indivisibles).
2.  No debe haber grupos repetitivos.

### Ejemplo: Violación de 1FN
Tabla `PEDIDO` con lista de productos en una celda.

| id_pedido | cliente | productos |
| :--- | :--- | :--- |
| 1 | Ana | TV, Lavadora |

### Solución 1FN
Separar en filas distintas (o crear tabla detalle).

| id_pedido | cliente | producto |
| :--- | :--- | :--- |
| 1 | Ana | TV |
| 1 | Ana | Lavadora |

---

## 2. Segunda Forma Normal (2FN)

**Regla**:
1.  Cumplir 1FN.
2.  **Eliminar Dependencias Parciales**: Todo atributo no clave debe depender de la **clave primaria completa**, no solo de una parte (si la PK es compuesta).

### Ejemplo: Violación de 2FN
Tabla `DETALLE_PEDIDO` con PK compuesta `(id_pedido, id_producto)`.

| id_pedido | id_producto | cliente (Dep. Parcial de id_pedido) | precio (Dep. Parcial de id_producto) | cantidad |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 10 | Ana | 800 | 1 |

*   `cliente` depende solo de `id_pedido`.
*   `precio` depende solo de `id_producto`.

### Solución 2FN
Dividir en tres tablas.
1.  `PEDIDO` (id_pedido, cliente)
2.  `PRODUCTO` (id_producto, precio)
3.  `DETALLE` (id_pedido, id_producto, cantidad)

---

## 3. Tercera Forma Normal (3FN)

**Regla**:
1.  Cumplir 2FN.
2.  **Eliminar Dependencias Transitivas**: Todo atributo no clave debe depender **directamente** de la PK, no de otro atributo no clave.

### Ejemplo: Violación de 3FN
Tabla `CLIENTE`.

| id_cliente | nombre | codigo_postal | ciudad (Dep. Transitiva) |
| :--- | :--- | :--- | :--- |
| 1 | Ana | 28001 | Madrid |

*   `ciudad` depende de `codigo_postal`, que a su vez depende de `id_cliente`.
*   Si cambiamos el CP de Madrid, tendríamos que actualizar todas las filas.

### Solución 3FN
Separar la dependencia transitiva.
1.  `CLIENTE` (id_cliente, nombre, codigo_postal)
2.  `CODIGO_POSTAL` (codigo_postal, ciudad)
