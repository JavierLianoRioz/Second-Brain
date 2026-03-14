# Ejercicio — Índices Avanzados, Transacciones y Monitoreo

> **🎯 Objetivo:** Entender cuándo usar cada tipo de índice, cómo funcionan las transacciones multi-documento y cómo diagnosticar rendimiento.

---

## 🗄️ Setup de datos

> Ejecuta estos bloques **una vez** en `mongosh` para crear los datos de prueba.

<details>
<summary>📦 Crear BD <code>academia</code> (cursos + estudiantes + inscripciones)</summary>

```javascript
use academia
db.cursos.drop()
db.estudiantes.drop()
db.inscripciones.drop()

const niveles = ["basico", "intermedio", "avanzado"]
const modalidades = ["online", "presencial", "hibrido"]

for (let i = 1; i <= 50; i++) {
  db.cursos.insertOne({
    nombre: "Curso " + i,
    nivel: niveles[i % 3],
    modalidad: modalidades[i % 3],
    creditos: (i % 5) + 1,
    fechaCreacion: new Date(2024, i % 12, (i % 28) + 1),
    ...(i % 3 === 0 && { fechaCertificacion: new Date(2025, i % 12, (i % 28) + 1) })
  })
}

for (let i = 1; i <= 60; i++) {
  db.estudiantes.insertOne({
    nombre: "Estudiante " + i,
    email: "estudiante" + i + "@correo.com",
    edad: 18 + (i % 10),
    ciudad: ["Madrid", "Bogota", "CDMX", "Buenos Aires"][i % 4],
    activo: i % 2 === 0,
    telefonoAlternativo: i % 5 === 0 ? "600000" + i : undefined
  })
}

for (let i = 1; i <= 100; i++) {
  db.inscripciones.insertOne({
    estudianteId: (i % 60) + 1,
    cursoId: (i % 50) + 1,
    fecha: new Date(2025, i % 12, (i % 28) + 1),
    estado: ["activa", "completada", "cancelada"][i % 3],
    nota: Math.floor(Math.random() * 5) + 1
  })
}
```
</details>

<details>
<summary>📦 Crear BD <code>tienda</code> (pedidos + ventas)</summary>

```javascript
use tienda
db.pedidos.drop()
db.ventas.drop()

for (let i = 1; i <= 100; i++) {
  db.pedidos.insertOne({
    clienteId: (i % 30) + 1,
    fecha: new Date(2026, i % 12, (i % 28) + 1),
    total: Math.floor(Math.random() * 1000) + 50,
    estado: ["pendiente", "enviado", "entregado"][i % 3],
    cliente: {
      nombre: "Cliente " + ((i % 30) + 1),
      ciudad: ["Madrid", "Lima", "CDMX", "Santiago"][i % 4]
    }
  })
}

for (let i = 1; i <= 80; i++) {
  db.ventas.insertOne({
    clienteId: (i % 25) + 1,
    producto: "Producto " + (i % 15),
    cantidad: (i % 5) + 1,
    total: Math.floor(Math.random() * 500) + 20,
    fecha: new Date(2026, i % 12, (i % 28) + 1)
  })
}
```
</details>

---

## Ejercicio 1 — Sparse Index

> **Concepto:** Un índice *sparse* solo indexa documentos que **tienen** el campo. Útil cuando muchos documentos no lo tienen.

### Pasos
```javascript
use academia

// 1. Crear índice NORMAL sobre un campo que no todos tienen
db.estudiantes.createIndex({ telefonoAlternativo: 1 })
db.estudiantes.getIndexes()

// 2. Ver cuántos documentos examina una consulta
db.estudiantes.find(
  { telefonoAlternativo: { $exists: true } }
).explain("executionStats")
// → Fíjate en totalDocsExamined y totalKeysExamined

// 3. Ahora reemplazar por índice SPARSE
db.estudiantes.dropIndex({ telefonoAlternativo: 1 })
db.estudiantes.createIndex({ telefonoAlternativo: 1 }, { sparse: true })

// 4. Repetir la misma consulta
db.estudiantes.find(
  { telefonoAlternativo: { $exists: true } }
).explain("executionStats")
```

### 🧠 ¿Qué observar?

| Métrica | Índice normal | Índice sparse |
|---------|--------------|---------------|
| `totalKeysExamined` | Todos los docs (60) | Solo los que tienen el campo (~12) |
| Tamaño del índice | Mayor | Menor |

> [!IMPORTANT]
> El índice sparse es más eficiente cuando **la mayoría de documentos no tiene el campo**. Si casi todos lo tienen, un índice normal es mejor.

---

## Ejercicio 2 — Hashed Index

> **Concepto:** Un índice *hashed* distribuye valores uniformemente (ideal para shard keys), pero **no soporta rangos**.

### Pasos
```javascript
use tienda

db.ventas.createIndex({ clienteId: "hashed" })

// ✅ Consulta exacta → USA el índice
db.ventas.find({ clienteId: 3 }).explain("executionStats")
// → stage: IXSCAN

// ❌ Consulta por rango → NO usa el índice
db.ventas.find({ clienteId: { $gt: 10 } }).explain("executionStats")
// → stage: COLLSCAN
```

### 🧠 ¿Por qué no sirve para rangos?
El hash transforma `clienteId: 3` → `hash_abc` y `clienteId: 4` → `hash_xyz`. Los hashes **no preservan orden**, así que MongoDB no puede recorrer un rango secuencialmente.

```
clienteId:  1  2  3  4  5         ← ordenados
hashed:    fA 3C B7 E2 1D         ← desordenados → no hay rango posible
```

---

## Ejercicio 3 — Elección de Shard Key (conceptual)

> **Concepto:** La shard key determina cómo se distribuyen los datos entre servidores. Una mala elección crea *hotspots*.

### Escenario
Sistema de pedidos con estas consultas:
- **90%** buscan por `clienteId`
- **10%** son reportes por `fecha`

### 🧠 Analiza estas opciones

| Shard key | Distribución | Problema potencial |
|-----------|-------------|-------------------|
| `{ fecha: 1 }` | Datos recientes en un solo shard | **Hotspot**: un shard recibe casi todo el tráfico |
| `{ clienteId: 1 }` | Buena distribución si hay muchos clientes | Reportes por fecha requieren broadcast a todos los shards |
| `{ clienteId: "hashed" }` | Distribución muy uniforme | No soporta rangos por `clienteId` |
| `{ clienteId: 1, fecha: 1 }` | ✅ Buena distribución + rangos por fecha dentro de cada cliente | Mejor opción para este caso |

> [!TIP]
> **Regla:** La shard key debe coincidir con el **patrón de consulta más frecuente** y tener **alta cardinalidad** (muchos valores distintos).

---

## Ejercicio 4 — Transacciones multi-documento

> **Concepto:** Las transacciones garantizan que varias operaciones se ejecuten como **todo o nada** (ACID), incluso sobre distintas colecciones.

### Paso 1 — Transacción exitosa
```javascript
use academia

session = db.getMongo().startSession()
dbTx = session.getDatabase("academia")
session.startTransaction()

try {
  dbTx.estudiantes.updateOne(
    { nombre: "Estudiante 1" },
    { $set: { activo: true } }
  )
  dbTx.cursos.insertOne({ nombre: "Curso Nuevo" })

  session.commitTransaction()
  print("✅ COMMIT EJECUTADO")
} catch(e) {
  session.abortTransaction()
  print("❌ ROLLBACK — " + e.message)
}
session.endSession()
```

### Paso 2 — Provocar un rollback
```javascript
// Crear un índice único en nombre de curso
db.cursos.createIndex({ nombre: 1 }, { unique: true })

// Ahora intentar insertar un curso duplicado dentro de una transacción
session = db.getMongo().startSession()
dbTx = session.getDatabase("academia")
session.startTransaction()

try {
  dbTx.estudiantes.updateOne(
    { nombre: "Estudiante 1" },
    { $set: { activo: false } }    // ← esto se haría...
  )
  dbTx.cursos.insertOne({ nombre: "Curso Nuevo" })  // ← ...pero esto FALLA (duplicado)

  session.commitTransaction()
  print("✅ COMMIT EJECUTADO")
} catch(e) {
  session.abortTransaction()
  print("❌ ROLLBACK — " + e.message)
}
session.endSession()
```

### 🧠 ¿Qué observar?
```javascript
// Verificar que el estudiante NO cambió (rollback revirtió todo)
db.estudiantes.findOne({ nombre: "Estudiante 1" })
// → activo: true (no false), porque el rollback deshizo la actualización
```

> [!IMPORTANT]
> Sin transacción, el `updateOne` se habría ejecutado aunque el `insertOne` fallara → datos **inconsistentes**. La transacción lo previene.

---

## Ejercicio 5 — Diagnóstico de rendimiento

> **Concepto:** `explain()` es tu herramienta principal para detectar consultas lentas.

### Paso 1 — Identificar COLLSCAN
```javascript
use academia

// Consulta SIN índice → COLLSCAN (escaneo completo)
db.cursos.find({ nivel: "avanzado" }).explain("executionStats")
```

### 🧠 Qué buscar en la salida

| Campo | Valor bueno | Valor malo |
|-------|------------|-----------|
| `winningPlan.stage` | `IXSCAN` | `COLLSCAN` |
| `totalDocsExamined` | ≈ nReturned | >> nReturned |
| `executionTimeMillis` | Bajo | Alto |

### Paso 2 — Crear índice y comparar
```javascript
// Crear índice
db.cursos.createIndex({ nivel: 1 })

// Repetir la misma consulta
db.cursos.find({ nivel: "avanzado" }).explain("executionStats")
// → Ahora debería mostrar IXSCAN y menos docs examinados
```

### Paso 3 — Estado del servidor
```javascript
db.serverStatus().opcounters  // ← operaciones de lectura/escritura
db.serverStatus().connections // ← conexiones activas
db.currentOp()               // ← operaciones en curso
```

> [!TIP]
> Si `totalDocsExamined` es mucho mayor que `nReturned`, el índice no es óptimo o falta un índice.

---

### 🧠 Resumen: ¿Cuándo usar cada índice?

| Tipo | Caso de uso | Soporta rangos |
|------|------------|----------------|
| **Normal** (`1`/`-1`) | Consultas generales | ✅ Sí |
| **Compound** | Consultas multi-campo | ✅ Sí |
| **Sparse** | Campo opcional en pocos docs | ✅ Sí |
| **Hashed** | Distribución uniforme / sharding | ❌ No |
| **TTL** | Datos con expiración (sesiones) | ✅ Sí |
| **Text** | Búsqueda full-text | N/A |

Este diseño avanzado previene [Antipatrones](../02-MongoDB/02-Design/MongoDB-Antipatterns.md) y asegura la escalabilidad mediante el uso correcto de [Índices](../02-MongoDB/03-Performance/MongoDB-Indexes.md) y el [Monitoreo](../02-MongoDB/03-Performance/MongoDB-Monitoring.md) constante de la infraestructura.
