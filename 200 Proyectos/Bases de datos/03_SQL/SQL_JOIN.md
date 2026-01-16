---
tags: [sql, join, database]
moc: [[00_MOC_SQL]]
status: refined
difficulty: intermediate
---

# SQL JOIN: Combinación de Tablas

---

## 🧠 Núcleo del Concepto

La cláusula **JOIN** permite vincular datos de múltiples tablas en una sola consulta basándose en una columna común (normalmente una clave foránea que referencia a una clave primaria).

*   **Relación Directa**: Es la implementación práctica de la [Join Algebra](../06_Algebra_Relacional/Join_Algebra.md) (⨝).
*   **Integridad**: Permite mantener los datos normalizados en tablas separadas sin perder la capacidad de ver la información completa.
*   **Eficiencia**: Un Join bien indexado es infinitamente más rápido que cruzar datos manualmente en el código de la aplicación.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] Tipos de Join
> 
> ```mermaid
> graph LR
>     subgraph "INNER JOIN (Intersección)"
>     A1((A)) --- B1((B))
>     A1 --- C1{COINCIDENCIAS} --- B1
>     style C1 fill:#f9f,stroke:#333
>     end
> 
>     subgraph "LEFT JOIN (Todo A + B)"
>     A2((A)) --- B2((B))
>     style A2 fill:#f9f,stroke:#333
>     style B2 fill:#fff,stroke:#333
>     end
> ```

---

## 🔗 Conexiones y Contexto

*   **Se basa en:** [Join Algebra](../06_Algebra_Relacional/Join_Algebra.md), [Clave Foranea](../02_Dise%C3%B1o/Clave_Foranea.md).
*   **Se relaciona con:** [SQL SELECT](SELECT_Basico.md), [Normalizacion Objetivos](../04_Normalizacion/Normalizacion_Objetivos.md).

---

## 💻 Ejemplos de Implementación

### 1. Inner Join (Parejas perfectas)
```sql
SELECT c.nombre, p.total
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id;
```

### 2. Left Join (Todos los de la izquierda)
```sql
-- Autores que pueden o no tener libros
SELECT A.nombre, L.titulo
FROM autores A
LEFT JOIN libros L ON A.id = L.autor_id;
```

---

> [!tip] Idea Fuerza (Cierre)
> ¿Quieres ver la foto completa? Haz un JOIN. El JOIN es el puente que une las islas de datos en tu base de datos.

---

## 📝 Ejercicios de Autoevaluación

1.  Obtener todos los libros y su autor (solo si tienen autor): → **INNER JOIN**.
2.  Listar todos los autores, aunque no tengan libros publicados: → **LEFT JOIN**.
3.  Buscar libros sin autor asignado: → `SELECT titulo FROM libros WHERE autor_id IS NULL;`
---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC SQL](00_MOC_SQL.md).
