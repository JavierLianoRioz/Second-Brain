# Ejercicio — Aggregation Framework

> **🎯 Objetivo:** Dominar el concepto de pipeline y las etapas más usadas: `$match`, `$group`, `$sort`, `$project`.

## 📖 Escenario: Sistema de Ventas

Colección `pedidos` con esta estructura:
```javascript
{
  producto: "Laptop Pro",
  categoria: "electrónica",
  cantidad: 15,
  precio_unitario: 1200,
  estado: "completado",
  fecha: ISODate("2026-01-15")
}
```

---

## Ejercicio 1 — Total por categoría (guiado)

**Enunciado:** Calcular el total recaudado por categoría, solo para pedidos con más de 10 unidades. Ordenar de mayor a menor.

### 💡 Estrategia del pipeline

Piénsalo como una cadena de transformaciones:

```
Documentos → Filtrar (cantidad > 10) → Agrupar por categoría → Ordenar
```

> [!TIP]
> **Regla de oro:** Siempre `$match` antes de `$group`. Filtrar primero = menos documentos que procesar = más rápido.

### Solución
```javascript
db.pedidos.aggregate([
  // 1. Filtrar: solo pedidos con más de 10 unidades
  { $match: { cantidad: { $gt: 10 } } },

  // 2. Agrupar por categoría, sumando (cantidad × precio)
  { $group: {
      _id: "$categoria",
      recaudacion_total: { $sum: { $multiply: ["$cantidad", "$precio_unitario"] } }
  }},

  // 3. Ordenar: mayor recaudación primero
  { $sort: { recaudacion_total: -1 } }
])
```

### Desglose de cada etapa

| Etapa | ¿Qué hace? | Técnica clave |
|-------|------------|---------------|
| `$match` | Filtra documentos (como `find`) | Reduce volumen **temprano** |
| `$group` | Agrupa por `_id` y calcula acumulados | `$sum`, `$avg`, `$count`, `$multiply` |
| `$sort` | Ordena resultados | `-1` = descendente, `1` = ascendente |

---

## Ejercicio 2 — Promedio y conteo (practica tú)

**Enunciado:** Para pedidos **completados**, calcular por categoría:
- Cantidad promedio de productos por pedido
- Número total de pedidos

Ordenar por número de pedidos descendente.

<details>
<summary>💡 Ver pista</summary>

```javascript
db.pedidos.aggregate([
  { $match: { estado: "completado" } },
  { $group: {
      _id: "$categoria",
      promedio_cantidad: { $avg: "$cantidad" },
      total_pedidos: { $count: {} }
  }},
  { $sort: { total_pedidos: -1 } }
])
```
</details>

---

## Ejercicio 3 — Usar `$project` para limpiar salida

**Enunciado:** Del ejercicio 1, mejorar la salida para que muestre `categoria` en vez de `_id` y formatee el total como `total_EUR`.

<details>
<summary>💡 Ver pista</summary>

Añade un `$project` al final del pipeline:
```javascript
{ $project: {
    _id: 0,
    categoria: "$_id",
    total_EUR: { $concat: [{ $toString: "$recaudacion_total" }, " €"] }
}}
```
</details>

---

## Ejercicio 4 — Análisis temporal con `$lookup`

**Enunciado:** Si tienes una colección `clientes` vinculada por `clienteId`, ¿cómo obtendrías el nombre del cliente junto con el total de sus compras?

<details>
<summary>💡 Ver pista</summary>

```javascript
db.pedidos.aggregate([
  { $group: { _id: "$clienteId", total: { $sum: "$precio_unitario" } } },
  { $lookup: {
      from: "clientes",
      localField: "_id",
      foreignField: "_id",
      as: "info_cliente"
  }},
  { $unwind: "$info_cliente" },
  { $project: { nombre: "$info_cliente.nombre", total: 1 } }
])
```
</details>

---

### 🧠 Resumen mental del pipeline

```
$match   → Filtro (WHERE)
$group   → Agrupar + calcular (GROUP BY + SUM/AVG)
$sort    → Ordenar (ORDER BY)
$project → Seleccionar/renombrar campos (SELECT)
$lookup  → Join con otra colección (LEFT JOIN)
$unwind  → Descomponer array en documentos individuales
```

Este sistema de ventas se basa en el [Modelo Documental](../02-MongoDB/01-Basics/MongoDB-Model-Overview.md) y permite practicar tanto [operaciones CRUD](../02-MongoDB/01-Basics/MongoDB-CRUD-Basics.md) como filtros avanzados con los [Operadores de Consulta](../02-MongoDB/01-Basics/MongoDB-Query-Operators.md).
