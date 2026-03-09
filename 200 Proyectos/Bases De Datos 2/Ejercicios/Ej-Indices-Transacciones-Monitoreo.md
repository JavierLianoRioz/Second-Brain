# Ejercicios: Índices Avanzados, Transacciones y Monitoreo

Ejercicios prácticos para índices especializados, sharding, transacciones y monitoreo.

## Setup de Datos

### BD `academia`
```javascript
use academia
db.cursos.drop()
db.estudiantes.drop()
db.inscripciones.drop()

// Cursos
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

// Estudiantes
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

// Inscripciones
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

### BD `tienda`
```javascript
use tienda
db.pedidos.drop()
db.ventas.drop()
db.logs.drop()

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
```

---

## Ejercicio 1 — Sparse Index
Crear índice normal vs sparse sobre `telefonoAlternativo`. Comparar con `explain()`:
```javascript
use academia
db.usuarios.createIndex({ telefonoAlternativo: 1 })
// vs
db.usuarios.createIndex({ telefonoAlternativo: 1 }, { sparse: true })
```
**Pregunta:** ¿Cuántos documentos indexa cada uno? ¿Cuál es el tamaño?

## Ejercicio 2 — Hashed Index
```javascript
use tienda
db.ventas.createIndex({ clienteId: "hashed" })
db.ventas.find({ clienteId: 1003 }).explain("executionStats")   // ✅
db.ventas.find({ clienteId: { $gt: 1002 } }).explain("executionStats") // ❌
```
**Reflexión:** ¿Por qué el índice hashed no sirve para consultas por rango?

## Ejercicio 3 — Shard Key (Conceptual)
Sistema de pedidos: 90% consultas por `clienteId`, 10% reportes por fecha. ¿Cuál shard key elegirías y por qué?

## Ejercicio 4 — Transacciones
```javascript
session = db.getMongo().startSession()
dbTx = session.getDatabase("academia")
session.startTransaction()
try {
  dbTx.estudiantes.updateOne({ nombre: "Estudiante 1" }, { $set: { activo: true } })
  dbTx.cursos.insertOne({ nombre: "Curso 1000" })
  session.commitTransaction()
  print("COMMIT EJECUTADO")
} catch(e) {
  session.abortTransaction()
  print("ROLLBACK EJECUTADO")
}
session.endSession()
```
**Observar:** Crear `unique index` en `cursos.nombre` y repetir. ¿Qué pasa?

## Ejercicio 5 — Monitoreo
```javascript
use academia
db.cursos.find({ nivel: "avanzado" }).explain("executionStats")
db.cursos.find({ creditos: { $gt: 3 } }).explain("executionStats")
db.serverStatus()
db.currentOp()
```
**Identificar:** COLLSCAN, totalDocsExamined, executionTimeMillis.

---
**Enlaces Relacionados:**
*   [Índices y Rendimiento](MongoDB-Indexes.md)
*   [Monitoreo y Observabilidad](MongoDB-Monitoring.md)
*   [Modelado Avanzado](MongoDB-Advanced-Modeling.md)
