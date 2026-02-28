# Ejercicio - Modelado Documental y CRUD

### Escenario: Plataforma de Cursos Online
Se desea modelar una base de datos para cursos que contienen lecciones, y usuarios que se inscriben en ellos.

### 1. Diseño del Esquema
Propón un esquema donde los cursos tengan sus lecciones (id, título, duración) embebidas.

```javascript
// Documento de Ejemplo para Colección 'cursos'
{
  "_id": ObjectId("..."),
  "titulo": "Programación con MongoDB",
  "instructor": "Dra. NoSQL",
  "lecciones": [
    { "id": 1, "titulo": "Intro", "segundos": 600 },
    { "id": 2, "titulo": "CRUD", "segundos": 1200 }
  ]
}
```

### 2. Consultas Prácticas

**A. Insertar un nuevo curso:**
```javascript
db.cursos.insertOne({
  titulo: "Arquitectura de Software",
  instructor: "Ing. SOLID",
  lecciones: []
})
```

**B. Buscar cursos con lecciones de más de 15 minutos (900s):**
```javascript
db.cursos.find({ "lecciones.segundos": { $gt: 900 } })
```

**C. Añadir una lección a un curso existente:**
```javascript
db.cursos.updateOne(
  { titulo: "Arquitectura de Software" },
  { $push: { lecciones: { id: 1, titulo: "Patrones", segundos: 1800 } } }
)
```

**D. Contar cuántos cursos tiene el instructor "Dra. NoSQL":**
```javascript
db.cursos.countDocuments({ instructor: "Dra. NoSQL" })
```

---
**Referenciado desde:**
*   [Modelo Documental](../MongoDB-Model-Overview.md)
*   [CRUD en MongoDB](../MongoDB-CRUD-Basics.md)
*   [Diseño de Esquemas](../MongoDB-Schema-Design-Patterns.md)
