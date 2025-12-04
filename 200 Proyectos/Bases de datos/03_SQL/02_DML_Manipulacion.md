# SQL: Lenguaje de Manipulación de Datos (DML)

El **DML (Data Manipulation Language)** permite gestionar los datos almacenados: insertar, modificar y borrar.

## 1. INSERT (Insertar)

Añade nuevas filas a una tabla.

### Inserción simple
Especificando columnas (recomendado).

```sql
INSERT INTO cliente (id_cliente, nombre, ciudad)
VALUES (1, 'Ana Pérez', 'Madrid');
```

### Inserción múltiple
Varios registros en una sola sentencia.

```sql
INSERT INTO producto (nombre, precio) VALUES 
('Teclado', 25.50),
('Ratón', 15.00),
('Monitor', 150.00);
```

---

## 2. UPDATE (Actualizar)

Modifica datos existentes.

> [!IMPORTANT]
> Siempre usa `WHERE`. Si lo olvidas, **actualizarás todas las filas** de la tabla.

```sql
-- Subir el precio un 10% a los productos de Electrónica
UPDATE producto
SET precio = precio * 1.10
WHERE categoria = 'Electrónica';

-- Modificar varios campos
UPDATE cliente
SET telefono = '555-1234', ciudad = 'Barcelona'
WHERE id_cliente = 1;
```

---

## 3. DELETE (Borrar)

Elimina filas de una tabla.

> [!CAUTION]
> Al igual que con UPDATE, si olvidas el `WHERE`, **borrarás todos los datos** de la tabla.

```sql
-- Borrar un cliente específico
DELETE FROM cliente
WHERE id_cliente = 1;

-- Borrar pedidos antiguos
DELETE FROM pedido
WHERE fecha < '2023-01-01';
```

### Diferencia con TRUNCATE
*   `DELETE`: Borra fila a fila, registra en log, permite `WHERE`. Es más lento.
*   `TRUNCATE TABLE`: Reinicia la tabla completa. Es DDL, muy rápido, no permite `WHERE` y no se puede deshacer en algunos motores.
