---
materia: Bases de Datos 2
---

# MongoDB: Modelo Documental y Procesamiento Analítico

MongoDB sustituye la relación lógica por la **agrupación física**. Su propósito es reducir la latencia eliminando el coste de normalización y los *joins* costosos, permitiendo que los datos que se consumen juntos se almacenen en una única estructura (BSON).

---

## ¿Por qué agrupar en documentos?
La fragmentación del modelo relacional genera el "desajuste de impedancia" (fricción entre el objeto y la tabla). El modelo documental busca la **cohesión física**:

- **SQL**: Requiere múltiples uniones (*joins*) para reconstruir una entidad compleja repartida en tablas.
- **MongoDB**: Recupera la entidad completa (documento y sus embebidos) en un **solo acceso a disco**, eliminando la latencia de reconstrucción.

---

## ¿Cómo operamos sobre la estructura? (CRUD y Mutación)

La interacción no se realiza mediante texto plano, sino mediante **predicados estructurales** (objetos JSON).

### Filtrado y Proyección (`find`)
Buscamos documentos que encajen en un molde y controlamos la salida (1: mostrar, 0: ocultar).

```js
// Ejemplo Examen (Grupo A): Cursos 'avanzado' mostrando solo nombre y profesor
db.cursos.find(
  { nivel: "avanzado" },
  { nombre: 1, profesor: 1, _id: 0 }
)

// Ejemplo Examen (Grupo D): Libros de 'informatica' mostrando titulo y autor
db.libros.find(
  { categoria: "informatica" },
  { titulo: 1, autor: 1, _id: 0 }
)
```

### Modificadores Atómicos
Permiten editar campos sin reescribir el documento.
- **`$set`**: Modifica valor o crea el campo.
- **`$inc`**: Incremento numérico (ej: créditos, stock, edad).

```js
// Ejemplo Examen (Grupo C): Actualizar temperatura del sensor S500 a 25
db.sensores.updateOne(
  { sensor_id: "S500" },
  { $set: { temperatura: 25 } }
)

// Ejemplo Examen (Grupo B): Reducir stock del Tablet X a 35
db.productos.updateOne(
  { nombre: "Tablet X" },
  { $set: { stock: 35 } }
)
```

**Estrategia de Escritura (Upsert):** El uso de `{ upsert: true }` en actualizaciones permite que MongoDB cree el documento si el filtro no encuentra ninguna coincidencia. Esto es vital en procesos de sincronización o ingesta de datos donde no sabemos si el registro ya existe, evitando errores y simplificando la lógica de la aplicación.

**Atomicidad:** Las operaciones en MongoDB son atómicas a **nivel de documento único**. Esto significa que si actualizas varios campos en un solo documento, o insertas un documento con múltiples subdocumentos embebidos, la operación se completa totalmente o no se hace nada, garantizando la integridad sin necesidad de transacciones complejas.

---

## ¿Cómo procesamos datos derivados? (Aggregation Framework)

El *Pipeline* es una secuencia de **transformaciones funcionales**.

### Acumuladores de Examen
1.  **Contar/Sumar por grupo (Grupo A/D - Total Créditos/Libros)**:
    ```js
    // Total de créditos por cada nivel
    db.cursos.aggregate([
      { $group: { _id: "$nivel", totalCreditos: { $sum: "$creditos" } } }
    ])
    ```
2.  **Calcular Promedios (Grupo C - Temperatura)**:
    ```js
    // Temperatura promedio por zona
    db.sensores.aggregate([
      { $group: { _id: "$zona", avgTemp: { $avg: "$temperatura" } } }
    ])
    ```
3.  **Stock Total (Grupo B)**:
    ```js
    db.productos.aggregate([
      { $group: { _id: "$categoria", stockTotal: { $sum: "$stock" } } }
    ])
    ```

**Gestión de Memoria:** El Pipeline se ejecuta por defecto en RAM (límite de 100MB). Para procesamientos masivos que superen este umbral (típico en `$group` o `$sort` sin índices), se debe activar la opción `{ allowDiskUse: true }`, permitiendo que MongoDB use archivos temporales en disco, aunque con una penalización en la velocidad.

---

## ¿Incrustar o Referenciar? (Patrones de Modelado)

El diseño se rige por el compromiso entre **latencia** y **escalabilidad**.

### Estrategias Base
- **Embedding (Incrustación)**: Datos altamente relacionados y de crecimiento controlado. (Lectura atómica).
- **Referencing (Referencia)**: Relaciones dinámicas o N:M. (Evita el límite de 16MB).

### Patrones Avanzados
- **Subset Pattern**: Guarda solo los N elementos más recientes (ej. últimos 5 comentarios) en el documento principal y el resto en otra colección. Optimiza el working set.
- **Computed Pattern**: Almacena el resultado de un cálculo frecuente (ej. `total_ventas`) para evitar ejecutar agregaciones pesadas en cada lectura.
- **Bucket Pattern**: Agrupa registros de series temporales (IoT/Logs) en documentos por intervalos (hora/día) para reducir el número de documentos e índices.

---

## ¿Cómo validamos el rendimiento?

La eficiencia se analiza mediante el **plan de ejecución** (`.explain("executionStats")`).

```js
// Ejemplo Examen: Verificar uso de índices en consulta por zona
db.sensores.find({ zona: "planta" }).explain("executionStats")
```

### Índices y Estrategias
- **Simple (Grupo A/B/C/D)**: `db.cursos.createIndex({ nivel: 1 })` o `db.sensores.createIndex({ zona: 1 })`.
- **Compuesto (Patrón Examen)**: `db.libros.createIndex({ categoria: 1, anio: -1 })`. 
  - *Clave cognitiva:* El primer campo es para el **filtrado** (`$match`) y el segundo suele ser para el **ordenamiento** (`$sort`).

### Análisis de Rendimiento
```js
// Ejemplo Examen: Verificar si la consulta de 'planta' usa el índice zona
db.sensores.find({ zona: "planta" }).explain("executionStats")
```

- **IXSCAN (Index Scan)**: Uso de índices. Estado óptimo.
- **COLLSCAN (Collection Scan)**: Lectura total. Indica falta de índices.

### Métricas de Diagnóstico (Interpretación de Examen)
- **`totalKeysExamined` vs `totalDocsExamined`**: 
    - En un escenario ideal con índice perfecto, el ratio es **1:1**. 
    - Si `totalKeysExamined` es alto pero `totalDocsExamined` es bajo, el índice está filtrando bien pero podría ser más selectivo. 
    - Si `totalKeysExamined` es 0 y `totalDocsExamined` es alto, tienes un **COLLSCAN** (no se está usando ningún índice), lo cual es el error más grave de rendimiento en el examen.
- **`executionTimeMillis`**: Indica el tiempo real de ejecución. Vital para justificar la eficiencia de un índice compuesto frente a uno simple.

### Índices Especiales
- **TTL (Time To Live)**: Elimina documentos automáticamente tras N segundos (útil para sesiones/logs).
- **Sparse**: Solo indexa documentos que contienen el campo (ahorra espacio en esquemas heterogéneos).
- **Text**: Habilita búsqueda semántica básica.
- **Hashed**: Optimiza el reparto en **Sharding** para evitar *hotspots* de escritura.

---

## Escalabilidad: Sharding
Para volúmenes masivos, MongoDB distribuye datos mediante una **Shard Key**. Una buena clave debe tener **alta cardinalidad** (muchos valores distintos) y evitar el crecimiento monótono para no colapsar un único nodo.


## Referencias
1. [[Bases de datos 2]]
2. [[Cypher|Neo4j]] — Comparativa de modelos (Documental vs Grafos).
3. Documentación técnica: MongoDB Indices & Aggregation.

---
### 🎓 Preparación para el Examen
- [[Simulacro_Examen_MongoDB|Simulacro de Examen Práctico (37 variantes)]]
