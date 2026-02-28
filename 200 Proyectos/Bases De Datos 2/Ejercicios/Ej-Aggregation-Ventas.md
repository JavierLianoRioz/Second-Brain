# Ejercicio - Aggregation Framework

### Escenario: Análisis de Ventas
Se tiene una colección `pedidos` con documentos que contienen `producto`, `categoria`, `cantidad` y `precio_unitario`.

### 1. Enunciado
Genera un informe que muestre el total recaudado por cada categoría, pero solo para pedidos que superen las 10 unidades de producto. El resultado debe estar ordenado de mayor a menor recaudación.

### 2. Solución

```javascript
db.pedidos.aggregate([
  // Etapa 1: Filtrar por cantidad > 10
  { $match: { cantidad: { $gt: 10 } } },
  
  // Etapa 2: Calcular el importe de cada pedido y agrupar
  { 
    $group: { 
      _id: "$categoria", 
      recaudacion_total: { $sum: { $multiply: ["$cantidad", "$precio_unitario"] } } 
    } 
  },
  
  // Etapa 3: Ordenar por recaudación descendente
  { $sort: { recaudacion_total: -1 } }
])
```

### 3. Explicación de Etapas
*   `$match`: Actúa como un filtro inicial para reducir el volumen de datos a procesar.
*   `$group`: El `_id` define la clave de agrupación. Usamos `$sum` junto a `$multiply` para el cálculo acumulativo.
*   `$sort`: El valor `-1` indica orden descendente.

---
**Referenciado desde:**
*   [Aggregation Framework](../MongoDB-Aggregation-Framework.md)
