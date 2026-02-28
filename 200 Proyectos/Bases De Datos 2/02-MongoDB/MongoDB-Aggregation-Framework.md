# Aggregation Framework en MongoDB

El **Aggregation Framework** es el motor de procesamiento de datos de MongoDB. Funciona como una tubería o *pipeline* donde los documentos pasan por una serie de etapas de transformación.

### Concepto de Pipeline
Cada etapa recibe un conjunto de documentos, los procesa y pasa el resultado a la siguiente.

### Etapas Comunes
1.  `$match`: Filtra los documentos (similar al `query` de `find`).
2.  `$group`: Agrupa documentos por una clave y realiza cálculos (sum, avg, etc.).
3.  `$project`: Selecciona, renombra o añade campos.
4.  `$sort`: Ordena los resultados.
5.  `$limit` / `$skip`: Paginación.
6.  `$lookup`: Realiza un *left outer join* con otra colección.

### Ejemplo de Consulta
Calcular el total de ventas por categoría:
```javascript
db.ventas.aggregate([
  { $match: { estado: "completado" } },
  { $group: { _id: "$categoria", total: { $sum: "$importe" } } },
  { $sort: { total: -1 } }
])
```

---
**Enlaces Relacionados:**
*   [Operadores de Consulta](MongoDB-Query-Operators.md)
*   [Índices y Rendimiento](MongoDB-Indexes.md)
