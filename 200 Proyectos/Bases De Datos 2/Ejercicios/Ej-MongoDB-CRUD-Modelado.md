# Ejercicio — Modelado Documental y CRUD

> **🎯 Objetivo:** Practicar diseño de esquemas con embedding y las 4 operaciones CRUD.

## 📖 Escenario: Plataforma de Cursos Online

Una plataforma necesita gestionar **cursos** que contienen **lecciones**, y **usuarios** que se inscriben en ellos.

---

## Parte 1 — Diseño del Esquema

> [!NOTE]
> Antes de ver la solución, piensa: ¿las lecciones deberían estar **embebidas** o en una colección aparte? Pista: un curso tiene pocas lecciones y siempre se muestran juntas.

**Modelo propuesto** (embedding, porque las lecciones siempre se leen junto al curso):
```javascript
// Colección: cursos
{
  _id: ObjectId("..."),
  titulo: "Programación con MongoDB",
  instructor: "Dra. NoSQL",
  lecciones: [
    { id: 1, titulo: "Intro", segundos: 600 },
    { id: 2, titulo: "CRUD", segundos: 1200 }
  ]
}
```

**¿Por qué embedding?** Relación 1:N con N pequeño. Los datos se acceden juntos → regla de oro: *data that is accessed together should be stored together.*

---

## Parte 2 — Operaciones CRUD

### ➕ Create — Insertar un curso
```javascript
db.cursos.insertOne({
  titulo: "Arquitectura de Software",
  instructor: "Ing. SOLID",
  lecciones: []
})
```

### 🔍 Read — Buscar cursos con lecciones largas (>15 min)
```javascript
db.cursos.find({ "lecciones.segundos": { $gt: 900 } })
```
> `$gt: 900` porque 15 minutos = 900 segundos. La notación con punto (`lecciones.segundos`) accede dentro de subdocumentos embebidos.

### ✏️ Update — Añadir una lección a un curso existente
```javascript
db.cursos.updateOne(
  { titulo: "Arquitectura de Software" },
  { $push: { lecciones: { id: 1, titulo: "Patrones", segundos: 1800 } } }
)
```
> `$push` añade un elemento al final del array. Si usáramos `$set`, **sobrescribiríamos** todo el array.

### 📊 Read — Contar cursos de un instructor
```javascript
db.cursos.countDocuments({ instructor: "Dra. NoSQL" })
```

---

## Parte 3 — Practica tú mismo

Intenta resolver estos sin mirar la solución:

1. **Insertar** un curso llamado "Data Science" con 2 lecciones.
2. **Buscar** todos los cursos del instructor "Ing. SOLID".
3. **Actualizar** el título de la lección con `id: 1` del curso "Arquitectura de Software".
4. **Eliminar** todos los cursos que no tengan lecciones (`lecciones` vacío).

<details>
<summary>💡 Ver pistas</summary>

1. Usa `insertOne` con un array de objetos en `lecciones`.
2. Usa `find` con filtro por `instructor`.
3. Usa `updateOne` con filtro `{ titulo: ..., "lecciones.id": 1 }` y operador `$set` con notación `"lecciones.$.titulo"`.
4. Usa `deleteMany` con `{ lecciones: { $size: 0 } }`.

</details>

Este ejercicio práctico demuestra las ventajas del [Modelo Documental](../02-MongoDB/01-Basics/MongoDB-Model-Overview.md) y cómo las [operaciones CRUD](../02-MongoDB/01-Basics/MongoDB-CRUD-Basics.md) se adaptan naturalmente al [Diseño de Esquemas](../02-MongoDB/02-Design/MongoDB-Schema-Design-Patterns.md) flexible.
