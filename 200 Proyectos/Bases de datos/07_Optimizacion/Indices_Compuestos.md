---
tags: [optimization, indexes, database]
moc: [[Query_Optimization]]
status: refined
difficulty: intermediate
---

# Índices Compuestos

---

## 🧠 Núcleo del Concepto

Un **índice compuesto** es una estructura de datos que indexa múltiples columnas en una sola unidad lógica, optimizando consultas que filtran por varios campos simultáneamente.

*   **Regla de Izquierda a Derecha**: El optimizador solo puede usar "subconjuntos" del índice si se respetan las columnas desde la primera hacia la derecha (sin saltos).
*   **Selectividad y Orden**: Se debe colocar primero la columna con mayor capacidad de filtrado (más restrictiva) para reducir rápidamente el número de filas a procesar.
*   **Freno por Rango**: El uso de un rango (`<`, `>`, `LIKE`) en una columna "detiene" la capacidad del índice para filtrar columnas situadas a su derecha.

---

## 🧠 El Cerebro: El Optimizador de Consultas
La base de datos no usa los índices "por casualidad". Tiene un componente llamado **Optimizador de Consultas** que actúa como un bibliotecario experto.

1.  **Análisis del Patrón**: Cuando envías un `SELECT`, el optimizador analiza tu `WHERE`. Si ve `WHERE apellido = 'X'`, busca en su catálogo qué índices empiezan por `apellido`.
2.  **Cálculo de Coste**: El optimizador estima cuántas filas tendrá que leer. Si el índice le permite saltar directamente a 10 filas de entre 1.000.000, lo usará. Si estima que el índice no ahorra trabajo, lo ignorará (Full Table Scan).
3.  **Estadísticas**: La base de datos guarda "metadatos" sobre cuántos valores distintos hay en cada columna. Si sabe que `cliente_id` es muy variado, sabrá que el índice es muy útil.

---

## 💻 Implementación en Código

Para implementar un índice compuesto, la sintaxis en SQL sigue el estándar de creación de índices, pero listando las columnas en el orden deseado.

### 1. Creación del Índice
```sql
-- Sintaxis General
CREATE INDEX idx_usuario_nombre_edad 
ON usuarios (apellido, nombre, edad);
```

### 2. Ejemplo Práctico
Supongamos una tabla de pedidos donde buscamos frecuentemente por cliente y fecha.

```sql
-- Crear tabla
CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    cliente_id INT,
    fecha_pedido DATE,
    monto DECIMAL(10,2)
);

-- Implementar el índice compuesto
-- IMPORTANTE: El orden importa. Primero cliente_id para búsquedas exactas.
CREATE INDEX idx_cliente_fecha ON pedidos(cliente_id, fecha_pedido);
```

### 3. Verificación de Uso (`EXPLAIN`)
Para entender cómo el motor utiliza el código, usamos `EXPLAIN`:

```sql
-- USA EL ÍNDICE (Perfect Match)
EXPLAIN SELECT * FROM pedidos 
WHERE cliente_id = 50 
  AND fecha_pedido > '2023-01-01';

-- USA EL ÍNDICE PARCIALMENTE (Solo cliente_id)
EXPLAIN SELECT * FROM pedidos 
WHERE cliente_id = 50;

-- NO USA EL ÍNDICE (Se saltó cliente_id)
EXPLAIN SELECT * FROM pedidos 
WHERE fecha_pedido = '2023-10-10';
```

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] Modelo de Guía Telefónica
> Imagina el índice como una guía física ordenada jerárquicamente:
> 
> ```mermaid
> graph TD
>     A["Índice: (Apellido, Nombre)"]
>     A --> B["Apellidos (Nivel 1)"]
>     B --> B1["García"]
>     B --> B2["López"]
>     
>     B1 --> C1["Ana"]
>     B1 --> C2["Bernardo"]
>     
>     B2 --> D1["Alberto"]
>     B2 --> D2["Zulema"]
>     
>     style B fill:#f9f,stroke:#333
>     style C1 fill:#dfd,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto

*   **Se relaciona con:** [[Query_Optimization]], [[03_SQL/Constraints_SQL]].
*   **Diferencia clave con:** Un **Índice Simple** solo acelera búsquedas sobre una única columna; el compuesto permite resolver `WHERE` multi-columna sin cruzar múltiples índices.

---

> [!tip] Idea Fuerza (Cierre)
> Los índices compuestos funcionan como un juego de "muñecas rusas": no puedes llegar a la de dentro sin abrir la de fuera.

---

## 📝 Ejercicios de Autoevaluación

Dado el índice: `INDEX (apellido, nombre, edad)`

1.  `WHERE apellido = 'Ruiz' AND nombre = 'Ana'` → **Sí** (Usa las 2 primeras).
2.  `WHERE nombre = 'Ana'` → **No** (Se salta la jerarquía).
3.  `WHERE apellido = 'Ruiz' AND edad = 25` → **Parcial** (Usa `apellido`, ignora `edad` por el hueco en `nombre`).
4.  `WHERE apellido = 'Ruiz' AND nombre LIKE 'A%' AND edad = 25` → **Parcial** (Filtra por `apellido` y rango en `nombre`; `edad` no se usa para filtrar).
