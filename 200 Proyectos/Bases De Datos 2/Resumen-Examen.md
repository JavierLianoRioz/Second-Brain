# Resumen General - Examen Bases de Datos 2

---

## 🧠 1. Modelos de Bases de Datos (Teoría)

### SQL (Relacionales)
*   **¿Qué es?** Datos organizados en tablas rígidas con filas y columnas (esquema estricto). Usa relaciones entre tablas (*joins*). Garantizan propiedades ACID (consistencia estricta).
*   **¿Cuándo usar?** Sistemas transaccionales financieros (bancos), ERPs, o cuando los datos están muy estructurados y no cambian de forma.
*   **Ejemplos:** MySQL, PostgreSQL, Oracle.

### NoSQL (Tipos y Familias)
Las NoSQL nacen para **escalar horizontalmente**, manejar gigas/teras de datos y tener **esquemas flexibles** (sin tablas rígidas ni *joins* pesados). Tienen 5 sub-familias principales:

| Tipo NoSQL | ¿De qué se trata? | ¿Cuándo se utiliza? (Casos de uso) | Ejemplos |
| :--- | :--- | :--- | :--- |
| **Clave-Valor** | El más simple. Es un diccionario de variables en memoria. Clave única ➔ Valor. | Sesiones de usuarios en webs, **Caché** de acceso rápido, carritos de compra. | Redis, DynamoDB |
| **Documental** | Guarda JSON/BSON. Cada objeto es independiente y puede tener campos distintos. | Catálogos de productos, CMS, perfiles de usuario, desarrollo ágil y flexible. | **MongoDB**, CouchDB |
| **Columnares** | Guarda familias de columnas juntas en vez de filas enteras. Ideal para escaneos masivos. | Análisis masivo (Big Data), registros de logs, métricas temporales de servidores IoT. | Cassandra, HBase |
| **Grafos** | Guarda los datos como **Nodos** y sus **Relaciones** (aristas). | Redes sociales (amigos de amigos), motores de recomendación, rutas o mapas. | Neo4j, JanusGraph |
| **Vectoriales** | Guardan arrays de números (embeddings/vectores matemáticos de similitud). | Inteligencia Artificial, búsquedas semánticas y LLMs (ChatGPT). | Pinecone, Milvus |

---

## 📄 2. Cómo escribir un Documento Muestra (JSON / Documental)

En el examen un "documento" es simplemente un bloque JSON rodeado de llaves. 

```json
{
  "_id": ObjectId("507f191e810c19729de860ea"), // Opcional, lo genera solo
  "jugador": "midas",
  "nivel": 42,
  "premium": true,
  "inventario": ["espada", "escudo", "poción"], // Es un array
  "gremio": {                                   // Es un objeto anidado (subdocumento / Embedding)
    "nombre": "Dragones",
    "rango": "Oficial"
  }
}
```

---

## 💻 3. Lista de Comandos (Práctica MongoDB)
Sintaxis básica para operar: `db.coleccion.comando(...)`

### 🟢 CREATE (Insertar)
*   **Comandos:** `insertOne( doc )` o `insertMany( [doc1, doc2] )`
*   **Ejemplo examen (Insertar 1 Documento):**
```javascript
db.estudiantes.insertOne({
  nombre: "Sara",
  edad: 21,
  modulos: ["Bases de Datos", "Programación"]
})
```

### 🔵 READ (Buscar / Query)
*   **Comando:** `find( { filtro } )`
*   **Operadores TOP:** `$gt` (mayor), `$gte` (mayor o igual), `$lt` (menor), `$lte` (menor o igual), `$ne` (distinto), `$or`, `$and`, `$in` (dentro del array).
*   **Ejemplo examen:** *Busca estudiantes mayores de 20 años o que se llamen "Sara".*
```javascript
db.estudiantes.find({
  $or: [
    { edad: { $gt: 20 } },
    { nombre: "Sara" }
  ]
})
```

### 🟠 UPDATE (Actualizar)
*   **Comandos:** `updateOne( filtro, operacion )` o `updateMany( filtro, operacion )`
*   **Regla de oro:** ¡Siempre, *siempre*, debes poner **`$set`** u otro modificador! Si no lo pones, sobrescribes el documento por completo. `$inc` para sumar/restar números; `$push` para añadir a un array.
*   **Ejemplo examen:** *A Sara, súbele un año la edad y añádele el campo "graduada" en true.*
```javascript
db.estudiantes.updateOne(
  { nombre: "Sara" },                // 1. Filtro: ¿A quién cambiamos?
  { 
    $inc: { edad: 1 },               // 2a. Operación: Sube 1 a la edad
    $set: { graduada: true }         // 2b. Operación: Añade graduada a true
  }
)
```

### 🔴 DELETE (Borrar)
*   **Comandos:** `deleteOne( filtro )` o `deleteMany( filtro )`
*   **Ejemplo examen:** *Borrar todos los estudiantes menores de 18*
```javascript
db.estudiantes.deleteMany({ edad: { $lt: 18 } })
```

---

## ⚙️ 4. Agregaciones (`aggregate`)
Cuando `find` no es suficiente y te piden agrupar, sumar totales o relacionar datos. Es una "tubería" (pipeline) donde pones etapas en **orden secuencial dentro de un array**.

**Etapas VIP:** `$match` (filtra), `$group` (agrupa y calcula, el `_id` es obligatorio), `$sort` (ordena con 1 ó -1), `$lookup` (Left Join para unir colecciones).

*   **Ejemplo examen (Agrupar y sumar):** *Obtén ingresos totales separados por ciudad para pedidos completados, ordenados de mayor a menor.*
```javascript
db.pedidos.aggregate([
  { $match: { estado: "completado" } },           // 1º Pasamos el filtro
  { $group: { 
      _id: "$ciudad",                             // 2º Agrupamos por ciudad ($ obligatorio)
      ingresoTotal: { $sum: "$precio" }           // Sumamos el campo 'precio'
  }},
  { $sort: { ingresoTotal: -1 } }                 // 3º Ordenamos de mayor a menor
])
```

---

## ⚡ 5. Miscelánea 
*   **Índices (Optimización del Rendimiento):** Aseguran que la BD haga un `IXSCAN` en vez de un lento `COLLSCAN`.
    *   *Crear índice simple:* `db.coleccion.createIndex({ nombreDelCampo: 1 })`
    *   *Crear índice compuesto:* `db.coleccion.createIndex({ edad: 1, ciudad: 1 })`
    *   *Comprobar rendimiento:* `db.coleccion.find({ ... }).explain("executionStats")`

*   **Administración desde consola Linux (bash):**
    *   *Hacer un backup (exportación BSON):* `mongodump --db=universidad --out=carpeta_backup`
    *   *Restaurar backup:* `mongorestore --drop carpeta_backup`
