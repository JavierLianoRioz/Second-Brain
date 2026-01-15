# 🎓 Guía de Supervivencia: Examen Final Bases de Datos

Basada en los "leaks" del grupo de clase. El enfoque es **100% práctico**.

## 🚫 ¿Qué NO entra?
- **Teoría Pura**: No hay test ni preguntas de definiciones.
- **DDL**: Olvida `CREATE TABLE`, `ALTER TABLE`, etc. (No entra según la tutoría).

## 🎯 Temas Clave (Lo que SÍ entra)

### 1. Diseño y Relaciones (Lo más fácil)
Identificar entidades, establecer relaciones y sobre todo **Cardinalidades**.
- [Modelo Entidad-Relación](02_Diseño/Modelo_Relacional_Conceptos.md)
- [Relaciones ER](02_Diseño/Relacion_ER.md)

### 2. DML y Consultas (Casi seguro de "Completar")
Insertar, actualizar y sobre todo consultar con `JOIN`, `GROUP BY` y `HAVING`.
- [Consultas SELECT Básico](03_SQL/SELECT_Basico.md)
- [Uso de SQL JOIN](03_SQL/SQL_JOIN.md)
- [Agrupaciones y Filtros](03_SQL/SQL_GROUP_BY.md)

### 3. Transacciones (Seguro de "Completar")
Saber cuándo usar `COMMIT` o `ROLLBACK`.
- [Control de Transacciones](08_Programacion_BD/Transacciones_Control.md)
- [Propiedades ACID](05_Transacciones/Propiedades%20ACID.md)

### 4. Optimización e Índices
Entender el recorrido de izquierda a derecha.
- [Optimización de Consultas SQL](07_Optimizacion/Query_Optimization.md)
- [Índices Compuestos](07_Optimizacion/Indices_Compuestos.md) (Fundamental)

---

## 📝 Patrones para "Completar Código"

### Estructura de Transacción Típica
```sql
START TRANSACTION;
-- Operación (ej. UPDATE stock)
IF (condición_error) THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;
```

### Consultas con Agregación
```sql
SELECT columna, COUNT(*) 
FROM tabla1 
JOIN tabla2 ON tabla1.id = tabla2.fk 
WHERE condicion 
GROUP BY columna 
HAVING COUNT(*) > X;
```

---
*¡Mucha suerte! Dale caña a la práctica.*
