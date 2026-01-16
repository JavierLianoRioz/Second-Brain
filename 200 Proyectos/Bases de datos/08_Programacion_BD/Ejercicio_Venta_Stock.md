---
tags: [exercise, practice, db-programming]
topic: "[Stored_Procedures_Sintaxis](Stored_Procedures_Sintaxis.md)"
level: intermediate
time_estimate: 15 min
---

# Ejercicio: Venta con Control de Stock

## 📝 Escenario y Datos
> [!info] Lógica de Negocio (Proximidad)
> Se requiere un script que procese una venta verificando el stock antes de descontarlo.
> *   **Tabla**: `productos (id_prod, nombre, stock)`.
> *   **Requisito 1**: Si hay stock suficiente, restar la cantidad y confirmar.
> *   **Requisito 2**: Si no hay suficiente, deshacer cualquier cambio.
> *   **Requisito 3**: Bloquear la fila durante la lectura para evitar condiciones de carrera.

---

## 🚀 El Reto
Escribe un Procedimiento Almacenado `realizar_venta(p_id, p_cant)` que implemente esta lógica de forma segura.

---

## 💡 Solución (Andamiaje)
> [!success]- Mostrar Solución (Procedimiento Transaccional)
> ```sql
> CREATE PROCEDURE realizar_venta(IN p_id_prod INT, IN p_cantidad INT)
> BEGIN
>     DECLARE v_stock INT;
>     START TRANSACTION;
>     
>     -- Bloqueo de fila para lectura segura
>     SELECT stock INTO v_stock FROM productos WHERE id_prod = p_id_prod FOR UPDATE;
>     
>     IF v_stock >= p_cantidad THEN
>         UPDATE productos SET stock = stock - p_cantidad WHERE id_prod = p_id_prod;
>         COMMIT;
>     ELSE
>         ROLLBACK;
>     END IF;
> END;
> ```

