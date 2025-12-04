# Álgebra Relacional: Fundamentos

El **Álgebra Relacional** es un lenguaje de consulta procedimental que constituye la base teórica de SQL. Describe **cómo** obtener los datos paso a paso.

## Conceptos Clave
*   **Operandos**: Relaciones (tablas).
*   **Resultado**: Una nueva relación (tabla).
*   **Cerradura**: El resultado de una operación puede ser la entrada de otra.

---

## Operadores Fundamentales

Son 6 operadores primitivos con los que se puede expresar cualquier consulta relacional básica.

### 1. Selección ($\sigma$)
Filtra **filas** (tuplas) que cumplen una condición.
*   **Sintaxis**: $\sigma_{condición}(R)$
*   **SQL equivalente**: `WHERE`

**Ejemplo**: $\sigma_{DEPARTAMENTO='IT'}(EMPLEADO)$

| ID | NOMBRE | DEPARTAMENTO |
|----|--------|--------------|
| 1  | Ana    | IT           |
| 3  | Marta  | IT           |

### 2. Proyección ($\pi$)
Selecciona **columnas** (atributos) y elimina duplicados.
*   **Sintaxis**: $\pi_{columna1, columna2}(R)$
*   **SQL equivalente**: `SELECT DISTINCT`

**Ejemplo**: $\pi_{NOMBRE, SALARIO}(EMPLEADO)$

| NOMBRE | SALARIO |
|--------|---------|
| Ana    | 4000    |
| Luis   | 3200    |

### 3. Unión ($\cup$)
Combina tuplas de dos relaciones compatibles (mismas columnas).
*   **Sintaxis**: $R \cup S$
*   **SQL equivalente**: `UNION`

### 4. Diferencia ($-$)
Devuelve tuplas que están en R pero **no** en S.
*   **Sintaxis**: $R - S$
*   **SQL equivalente**: `EXCEPT` o `MINUS`

### 5. Producto Cartesiano ($\times$)
Combina todas las tuplas de R con todas las de S.
*   **Sintaxis**: $R \times S$
*   **Resultado**: Si R tiene $N$ filas y S tiene $M$, el resultado tiene $N \times M$ filas.

### 6. Renombramiento ($\rho$)
Cambia el nombre de una relación o sus atributos. Útil para auto-joins o desambiguar.
*   **Sintaxis**: $\rho_{NUEVO\_NOMBRE}(R)$
