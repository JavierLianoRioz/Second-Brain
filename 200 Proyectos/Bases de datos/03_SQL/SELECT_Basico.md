---
tags: [sql, select, database]
moc: "[00_MOC_SQL](00_MOC_SQL.md)"
status: refined
difficulty: easy
---

# SELECT Básico

---

## 🧠 Núcleo del Concepto

El comando **SELECT** es la herramienta fundamental de SQL DML para recuperar y consultar datos almacenados en una base de datos relacional.

*   **Proyección de Datos**: Permite elegir qué columnas específicas queremos ver del conjunto total.
*   **Origen**: La cláusula `FROM` especifica la tabla o conjunto de tablas de donde extraeremos la información.
*   **Clausura**: El resultado de una consulta `SELECT` es siempre otra relación (tabla), permitiendo consultas anidadas.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] Estructura de la Consulta
>
> ```mermaid
> graph LR
>     S[SELECT] --> C[Columnas]
>     F[FROM] --> T[Tabla]
>     
>     style S fill:#f9f,stroke:#333
>     style F fill:#dfd,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto

*   **Base Teórica**: Este comando implementa las operaciones del [Algebra Relacional Concepto](../06_Algebra_Relacional/Algebra_Relacional_Concepto.md).
*   **Operaciones**: 
    *   La lista de columnas implementa la [Proyeccion Operador](../06_Algebra_Relacional/Proyeccion_Operador.md).
    *   La cláusula [SQL WHERE](SQL_WHERE.md) implementa la [Seleccion Operador](../06_Algebra_Relacional/Seleccion_Operador.md).

---

## 💻 Ejemplos de Implementación

### 1. Consulta Total
```sql
-- Recupera todas las columnas y filas
SELECT * FROM producto;
```

### 2. Proyección Específica
```sql
-- Filtra solo las columnas de interés
SELECT nombre, precio FROM producto;
```

---

> [!tip] Idea Fuerza (Cierre)
> Si la base de datos es una biblioteca, el `SELECT` es el bibliotecario que te trae exactamente el libro y la página que pediste.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC SQL](00_MOC_SQL.md).
