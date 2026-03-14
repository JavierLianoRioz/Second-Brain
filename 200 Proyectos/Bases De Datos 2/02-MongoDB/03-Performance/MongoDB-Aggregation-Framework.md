# Aggregation Framework en MongoDB

El **Aggregation Framework** es el motor de procesamiento de datos de MongoDB. Funciona como una tubería o *pipeline* donde los documentos pasan por una serie de etapas de transformación.

### Concepto de Pipeline
Cada etapa recibe un conjunto de documentos, los procesa y pasa el resultado a la siguiente.

### Etapas Comunes

*   **`$match`**: Filtra los documentos.
*   **`$group`**: Agrupa y realiza cálculos.
*   **`$project`**: Modifica la estructura de salida.
*   **`$sort`**: Ordena los resultados.
*   **`$limit` / `$skip`**: Paginación y limitación de resultados.
*   **`$lookup`**: Cruza datos con otras colecciones (Joins).
*   **`$unwind`**: Descompone arreglos para procesar sus elementos individualmente.

##### Ejemplos de uso:

**1. Agrupación y Cálculos ($group):**
Calcular el total de ventas por categoría para pedidos completados.
```javascript
db.ventas.aggregate([
  { $match: { estado: "completado" } },
  { $group: { _id: "$categoria", total: { $sum: "$importe" } } },
  { $sort: { total: -1 } }
])
```

**2. Transformación de campos ($project):**
Mostrar solo el nombre en mayúsculas y calcular un precio con IVA.
```javascript
db.productos.aggregate([
  { $project: { 
      nombre: { $toUpper: "$nombre" }, 
      precioIVA: { $multiply: ["$precio", 1.21] },
      _id: 0 
  } }
])
```

**3. Cruce de colecciones ($lookup):**
Unir la colección de `pedidos` con la de `clientes` usando el ID del cliente.
```javascript
db.pedidos.aggregate([
  { $lookup: {
      from: "clientes",
      localField: "cliente_id",
      foreignField: "_id",
      as: "datos_cliente"
  } }
])
```

**4. Descomposición de arreglos ($unwind):**
Útil para contar cuántas veces aparece cada elemento de un arreglo en toda la colección.
```javascript
db.productos.aggregate([
  { $unwind: "$tags" }, // 1. Crea un documento por cada elemento del arreglo
  { $group: { _id: "$tags", cantidad: { $sum: 1 } } } // 2. Cuenta las ocurrencias
])
```

> [!TIP]
> El orden de las etapas importa: filtrar con `$match` al principio del pipeline reduce drásticamente la carga de trabajo para las etapas posteriores. Para asegurar que el pipeline sea óptimo, verifica que las primeras etapas aprovechen los [Índices](MongoDB-Indexes.md) y consulta el [Análisis de Rendimiento](MongoDB-Indexes.md#análisis-de-rendimiento).
