---
tags: [concept, neuro-efficiency, db-programming]
moc: [[00_MOC_Programacion_BD]]
status: refactored
difficulty: intermediate
---

# Control de Transacciones

---

## 🧠 Núcleo del Concepto
Una **Transacción** es una unidad de trabajo indivisible que garantiza que un conjunto de operaciones se ejecute por completo o no se ejecute en absoluto (ACID).

*   **Atomicidad:** "Todo o nada". El `COMMIT` confirma, el `ROLLBACK` deshace.
*   **Puntos de Guardado:** `SAVEPOINT` permite retrocesos parciales sin invalidar toda la transacción.
*   **Aislamiento y Bloqueo:** El uso de `FOR UPDATE` previene interferencias de otros procesos en las filas que estamos procesando.

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Ciclo de Vida de una Transacción
> ```mermaid
> stateDiagram-v2
>     [*] --> START_TRANSACTION
>     START_TRANSACTION --> Operations
>     Operations --> Validation: ¿Todo OK?
>     Validation --> COMMIT: Sí
>     Validation --> ROLLBACK: Fallo / Error
>     COMMIT --> [*]
>     ROLLBACK --> [*]
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [[Ejemplos_Programacion]] (patrones de diseño transaccional) y [[Propiedades_ACID]] (fundamento teórico).
*   **Diferencia clave con:** Operaciones Atómicas Individuales. Una transacción agrupa múltiples operaciones que dependen lógicamente entre sí.

---

## 💡 Práctica de Recuperación
> [!success]- Reto: Transferencia Segura
> **Escenario**: Restar 50€ de `cuenta_1` y sumarlos a `cuenta_2`. Si `cuenta_1` queda en negativo (< 0), cancelar todo.
> 
> **Código a completar**:
> ```sql
> __________ TRANSACTION;
> UPDATE cuentas SET saldo = saldo - 50 WHERE id = 1;
> UPDATE cuentas SET saldo = saldo + 50 WHERE id = 2;
> IF (SELECT saldo FROM cuentas WHERE id = 1) < 0 THEN
>     __________;
> ELSE
>     __________;
> END IF;
> ```
> 
> **Solución**: 1. `START`, 2. `ROLLBACK`, 3. `COMMIT`.

---

> [!tip] Idea Fuerza (Cierre)
> Las transacciones no son solo sobre "guardar datos", son sobre garantizar la verdad absoluta del sistema ante cualquier error.
