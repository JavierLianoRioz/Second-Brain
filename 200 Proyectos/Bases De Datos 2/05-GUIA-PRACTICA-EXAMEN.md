# 🎓 Guía de Supervivencia: Examen Práctico de MongoDB

Esta guía está diseñada para el examen práctico a ordenador. Sigue el formato de **Escenario → Query** que piden en clase.

---

## 💡 Reglas de Oro para el Examen
1.  **Sé Conciso en la Teoría**: Si preguntan por un tipo de base de datos, responde solo el nombre (ej: "Base de datos vectorial"), no escribas un párrafo.
2.  **Cuidado con los Nombres de Campos**: En `Aggregation`, si te piden "total de libros", el campo debe llamarse exactamente así o como especifique el enunciado (evita inventar nombres como `cantidad` si puedes usar el del enunciado).
3.  **Proyecciones**: Si te piden "solo el título", recuerda poner `_id: 0` si no quieres que aparezca el ID por defecto.
4.  **Explain**: Siempre usa `.explain("executionStats")` para que se vea el detalle del rendimiento (IXSCAN vs COLLSCAN).

---

## 📂 1. CRUD (Operaciones Básicas)

### Escenario: Insertar un nuevo libro
**Pregunta**: Inserta un libro con título "Guía Mongo", autor "Yo", año 2024 y categoría "Estudio".
```javascript
db.libros.insertOne({
  titulo: "Guía Mongo",
  autor: "Yo",
  anio: 2024,
  categoria: "Estudio"
})
```

### Escenario: Buscar con filtros
**Pregunta**: Encuentra todos los libros de la categoría "bases de datos".
```javascript
db.libros.find({ categoria: "bases de datos" })
```

### Escenario: Actualizar datos
**Pregunta**: Cambia el año del libro "Introduccion a NoSQL" a 2022.
```javascript
db.libros.updateOne(
  { titulo: "Introduccion a NoSQL" },
  { $set: { anio: 2022 } }
)
```

### Escenario: Proyección (Seleccionar campos)
**Pregunta**: Devuelve solo los títulos de todos los libros (sin el _id).
```javascript
db.libros.find({}, { titulo: 1, _id: 0 })
```

---

## 📊 2. Aggregation Framework (Análisis)

### Escenario: Contar por grupo
**Pregunta**: ¿Cuántos libros hay por cada categoría? (Llamar al resultado `total_libros`).
```javascript
db.libros.aggregate([
  { 
    $group: { 
      _id: "$categoria", 
      total_libros: { $sum: 1 } 
    } 
  }
])
```

### Escenario: Promedio de valores
**Pregunta**: ¿Cuál es el año promedio de publicación por categoría?
```javascript
db.libros.aggregate([
  { 
    $group: { 
      _id: "$categoria", 
      promedio_anio: { $avg: "$anio" } 
    } 
  }
])
```

---

## 🚀 3. Índices y Rendimiento

### Escenario: Crear Índice Simple
**Pregunta**: Crea un índice para mejorar las búsquedas por categoría.
```javascript
db.libros.createIndex({ categoria: 1 })
```

### Escenario: Crear Índice Compuesto
**Pregunta**: Crea un índice para búsquedas por categoría y año.
```javascript
db.libros.createIndex({ categoria: 1, anio: 1 })
```

### Escenario: Verificar Rendimiento
**Pregunta**: Comprueba si la consulta por categoría usa el índice.
```javascript
db.libros.find({ categoria: "bases de datos" }).explain("executionStats")
```
*   **Resultado esperado**: En `winningPlan`, debes ver `IXSCAN`. Si ves `COLLSCAN`, el índice no se está usando.

---

## 🧩 4. Conceptos (Teoría Rápida)

| Pregunta Típica | Respuesta Corta (Examen) |
| :--- | :--- |
| Busca por similitud semántica / vectores | **Base de datos vectorial** |
| Datos altamente relacionados / nodos | **Base de datos de grafos** (ej: Neo4j) |
| Escalamiento horizontal masivo / columnas | **Base de datos columnar** (ej: Cassandra) |
| Sencillez extrema / Caché / Sesiones | **Base de datos Clave-Valor** (ej: Redis) |
| ¿Qué estructura usa un índice en Mongo? | **B-Tree** |
| ¿Qué significa el 1 en `{ edad: 1 }`? | **Orden Ascendente** |

---
*Preparado para el Parcial 1 - ¡Mucha suerte!*
