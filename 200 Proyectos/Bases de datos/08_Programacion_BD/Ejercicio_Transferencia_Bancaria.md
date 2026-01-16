---
tags: [exercise, practice, db-programming]
topic: [[Transacciones_Control]]
level: beginner
time_estimate: 10 min
---

# Ejercicio: Transferencia Bancaria Segura

## 📝 Escenario y Datos
> [!info] Reglas de la Transferencia (Proximidad)
> Mover fondos entre dos cuentas de la tabla `cuentas (id_cuenta, saldo)`.
> *   **Regla**: Si después de restar el dinero de la cuenta origen, el saldo es negativo, la operación debe ser cancelada íntegramente.

---

## 🚀 El Reto
Implementa el procedimiento `transferencia(origen, destino, monto)` garantizando la atomicidad.

---

## 💡 Solución (Andamiaje)
> [!success]- Mostrar Solución (Step-by-Step)
> ```sql
> CREATE PROCEDURE transferencia(IN c_origen INT, IN c_destino INT, IN monto DECIMAL)
> BEGIN
>     START TRANSACTION;
>     -- Paso 1: Restar de origen
>     UPDATE cuentas SET saldo = saldo - monto WHERE id_cuenta = c_origen;
>     -- Paso 2: Sumar a destino
>     UPDATE cuentas SET saldo = saldo + monto WHERE id_cuenta = c_destino;
>     
>     -- Paso 3: Validación de integridad
>     IF (SELECT saldo FROM cuentas WHERE id_cuenta = c_origen) < 0 THEN
>         ROLLBACK; -- Deshace todo el bloque
>     ELSE
>         COMMIT;   -- Confirma el movimiento
>     END IF;
> END;
> ```

