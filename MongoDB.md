---
materia: Bases de Datos 2
---

# MongoDB: Guía Práctica de Ejecución

Manual técnico enfocado en la descomposición jerárquica de comandos y patrones de ejecución para MongoDB.

---

## 1. Consultas y Proyección (`find`)

Recupera documentos basados en un criterio y filtra las claves de salida.

```js
// SINTAXIS: db.coleccion.find(<filtro>, <proyeccion>)
// FILTRO:     { <campo>: <valor> } o { <campo>: { $operador: <valor> } }
// PROYECCION: { <campo>: 1 (mostrar) o 0 (ocultar) }

// Ejemplo: Mostrar solo nombre y profesor de cursos 'avanzado'
db.cursos.find(
  { nivel: "avanzado" },
  { nombre: 1, profesor: 1, _id: 0 }
)
```

---

## 2. Mutación Atómica (`updateOne`)

Modifica partes de un documento existente sin reescribirlo por completo.

```js
// SINTAXIS: db.coleccion.updateOne(<filtro>, <modificadores>, <opciones>)
// FILTRO:        { <campo>: <valor> }
// MODIFICADORES: { <$operador>: { <campo>: <nuevo_valor> } }
// OPCIONES:      { upsert: true } (Crea si no existe)

// Ejemplo: Incrementar créditos y crear si no existe
db.cursos.updateOne(
  { nombre: "Arquitectura" },
  { $inc: { creditos: 1 } },
  { upsert: true }
)
```

---

## 3. Aggregation Framework (Pipeline)

Procesamiento de datos mediante una secuencia de etapas jerárquicas contenidas en un array.

```js
// SINTAXIS: db.coleccion.aggregate(<array_de_pasos>)
// ARRAY:     Se divide normalmente en: [FILTRO, AGRUPAR, ORDENAR]
// FILTRO:    { $match: { <filtro_estilo_find> } }
// AGRUPAR:   { $group: { _id: "$<campo_grupo>", <alias>: { <$acumulador>: "$<campo_valor>" } } }
// ORDENAR:   { $sort:  { <alias>: 1 (ASC) o -1 (DESC) } }

// Ejemplo: Temperatura promedio por zona en sensores de 'planta'
db.sensores.aggregate([
  { $match: { zona: "planta" } },
  { $group: { _id: "$zona", avgTemp: { $avg: "$temperatura" } } }
])
```

---

## 4. Diagnóstico de Rendimiento (`explain`)

Herramienta para auditar la eficiencia de las consultas.

```js
// SINTAXIS: db.coleccion.find(<filtro>).explain("<modo>")
// MODO: "executionStats" (Para ver tiempos y uso de índices)

// Ejemplo: Diagnóstico de consulta por zona
db.sensores.find({ zona: "planta" }).explain("executionStats")
```

| Métrica | Diagnóstico | Significado |
| :--- | :--- | :--- |
| **`IXSCAN`** | **ÓPTIMO** | Uso de índice detectado. |
| **`COLLSCAN`** | **ERROR** | Lectura total de la colección (Faltan índices). |
| **`totalKeysExamined: 0`** | **ERROR** | Confirmación de que no se ha usado ningún índice. |

---

## 5. Patrones Avanzados (Cheat Sheet)

| Operación | Descomposición Estructural (SINTAXIS) |
| :--- | :--- |
| **Join ($lookup)** | `{ $lookup: { from: "<col>", localField: "a", foreignField: "b", as: "c" } }` |
| **Recursividad** | `{ $graphLookup: { from: "<col>", startWith: "$a", connectFromField: "a", ... } }` |
| **Índice Compuesto** | `db.coleccion.createIndex({ <campo1>: 1, <campo2>: -1 })` |

---

## Referencias Prácticas
- [[Simulacro_Examen_MongoDB|Simulacro de Examen Práctico]]
- [[Bases de datos 2]]
