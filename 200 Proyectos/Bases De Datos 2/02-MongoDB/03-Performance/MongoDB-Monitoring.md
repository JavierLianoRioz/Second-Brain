# Observabilidad y Monitoreo en MongoDB

Un sistema sin observabilidad no es profesional. MongoDB permite monitoreo en tres niveles: **consulta**, **base de datos** y **cluster**.

### Nivel de Consulta — `explain()`
```javascript
db.cursos.find({ nivel: "avanzado" }).explain("executionStats")
```
Campos críticos a analizar:
*   `stage`: `IXSCAN` (usó índice) vs `COLLSCAN` (escaneo completo)
*   `totalDocsExamined` vs `nReturned` — si el primero es mucho mayor, el índice no es óptimo
*   `executionTimeMillis`

### Nivel de Base de Datos — `serverStatus()`
```javascript
db.serverStatus()
```
Métricas clave: `opcounters`, `connections`, `mem`, `wiredTiger.cache`. Un aumento constante en *cache eviction* indica presión de memoria.

### Nivel de Índices — Uso Real
```javascript
db.collection.getIndexes()
```
Lo importante es **identificar índices no usados**. Un índice no utilizado es **deuda técnica**.

### Monitoreo en Entornos Distribuidos (Sharding)
*   Balanceo de chunks y distribución por shard
*   Latencia y throughput por nodo
*   Una distribución desigual implica mala shard key

### Optimización de Pipelines de Aggregation
Regla principal: **reducir volumen lo antes posible**.
```javascript
// ❌ Incorrecto: agrupar antes de filtrar
[{ $group: ... }, { $match: ... }]

// ✅ Correcto: filtrar antes de agrupar
[{ $match: ... }, { $group: ... }]
```
Usar `$project` temprano para reducir memoria en `$group`. Para un análisis más profundo de la infraestructura, consulta la [Observabilidad Operativa](MongoDB-Observability.md).
