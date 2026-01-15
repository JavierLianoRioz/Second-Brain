# Ejercicio Práctico: Transacciones y ACID

## Escenario: Transferencia Bancaria con Comisión
Tenemos una tabla `CUENTAS` con la siguiente información inicial:

| ID_Cuenta | Titular | Saldo |
| :--- | :--- | :--- |
| 101 | Ana | 1000€ |
| 102 | Pedro | 500€ |
| 999 | Banco | 0€ |

**Regla de Negocio:** El saldo de una cuenta nunca puede ser negativo (`CHECK (Saldo >= 0)`).

## Código de la Transacción

Analiza la siguiente secuencia de operaciones SQL:

```sql
-- Paso 1: Inicio
BEGIN TRANSACTION;

-- Paso 2: Ana envía 600€ a Pedro
UPDATE CUENTAS SET Saldo = Saldo - 600 WHERE ID_Cuenta = 101;
UPDATE CUENTAS SET Saldo = Saldo + 600 WHERE ID_Cuenta = 102;

-- Paso 3: Punto de guardado
SAVEPOINT transferencia_ok;

-- Paso 4: Cobrar comisión de 10€ a Ana
UPDATE CUENTAS SET Saldo = Saldo - 10 WHERE ID_Cuenta = 101;

-- Paso 5: Cobrar comisión de 5€ a Pedro
UPDATE CUENTAS SET Saldo = Saldo - 5 WHERE ID_Cuenta = 102;

-- Paso 6: Simulación de Error
-- Imaginemos que aquí se intenta insertar un registro de log que falla
-- INSERT INTO LOGS ... (FALLA)

-- Paso 7: Decisión ante el error
ROLLBACK TO transferencia_ok;

-- Paso 8: Finalización
COMMIT;
```

## Preguntas

1.  Calcula el saldo de Ana paso a paso. ¿En qué momento (si ocurre) se violaría la restricción de saldo negativo?
2.  ¿Cuál es el estado final de las tres cuentas tras el `COMMIT`?
3.  ¿Qué propiedad **ACID** permite que el dinero no se "pierda" en el limbo durante el Paso 2?
4.  Si se fuera la luz justo antes del Paso 8 (`COMMIT`), ¿qué pasaría con los saldos?

---

## Solución Detallada

### 1. Traza paso a paso
*   **Inicio:** Ana=1000, Pedro=500.
*   **Paso 2 (Transferencia):**
    *   Ana: $1000 - 600 = 400$.
    *   Pedro: $500 + 600 = 1100$.
    *   *No se viola ninguna restricción.*
*   **Paso 3:** Se guarda el estado (Ana=400, Pedro=1100).
*   **Paso 4 (Comisión Ana):** Ana: $400 - 10 = 390$.
*   **Paso 5 (Comisión Pedro):** Pedro: $1100 - 5 = 1095$.
*   **Paso 7 (Rollback):** Se deshacen los cambios hechos **después** del `SAVEPOINT`.
    *   Se anulan las comisiones (Pasos 4 y 5).
    *   Volvemos al estado del Paso 3: Ana=400, Pedro=1100.

### 2. Estado Final
| ID_Cuenta | Titular | Saldo Final |
| :--- | :--- | :--- |
| 101 | Ana | **400€** |
| 102 | Pedro | **1100€** |
| 999 | Banco | **0€** |

### 3. Propiedad ACID
La **Atomicidad**. Esta propiedad asegura que las dos operaciones del Paso 2 (restar a Ana y sumar a Pedro) se traten como una unidad indivisible. Aunque son dos sentencias SQL, lógicamente son una sola operación atómica.

### 4. Fallo antes del COMMIT
Si falla la energía antes del `COMMIT`, entra en juego la **Atomicidad** y la **Durabilidad** (o falta de ella aún). El sistema realiza un **ROLLBACK automático** al reiniciarse.
*   **Resultado:** La transacción nunca existió para la base de datos.
*   **Saldos:** Ana=1000€, Pedro=500€. (Estado original).

---
[00_MOC_Transacciones](00_MOC_Transacciones.md)
