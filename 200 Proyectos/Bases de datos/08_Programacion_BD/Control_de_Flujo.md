# Variables y Control de Flujo

La programación en bases de datos permite el uso de lógica procedimental similar a los lenguajes de programación tradicionales.

## Variables

### Locales
Se declaran dentro de un bloque `BEGIN ... END` y desaparecen al finalizar.
```sql
DECLARE nombre_variable TIPO [DEFAULT valor];
SET nombre_variable = valor;
-- O asignar desde una consulta
SELECT columna INTO nombre_variable FROM tabla WHERE ...;
```

### De Usuario
Persisten durante la sesión actual (prefijadas con `@`).
```sql
SET @mi_variable = 10;
```

## Estructuras de Control

### Condicionales (IF)
```sql
IF condicion THEN
    -- acciones
ELSEIF otra_condicion THEN
    -- acciones
ELSE
    -- acciones
END IF;
```

### Bucles (WHILE)
```sql
WHILE condicion DO
    -- acciones
    -- IMPORTANTE: Asegurar que la condición cambie para evitar bucles infinitos
END WHILE;
```

---
- **Relacionado**: [Sintaxis de Stored Procedures](Stored_Procedures_Sintaxis.md)
- **Ejemplo**: Ver [Script de Poblado](Ejemplos_Programacion.md#poblado-masivo-de-datos)
