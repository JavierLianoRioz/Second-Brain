# Operaciones CRUD en MongoDB

El acrónimo **CRUD** representa las cuatro operaciones básicas de persistencia: *Create*, *Read*, *Update* y *Delete*.

### 1. Create (Creación)
*   `insertOne(doc)`: Inserta un único documento.
*   `insertMany([docs])`: Inserta una lista de documentos.

```javascript
db.usuarios.insertOne({ nombre: "Ana", edad: 25 })
```

### 2. Read (Lectura)
*   `find(query)`: Devuelve un cursor con los documentos que coinciden.
*   `findOne(query)`: Devuelve el primer documento que coincide.

```javascript
db.usuarios.find({ edad: { $gt: 18 } }) // $gt = Greater Than
```

### 3. Update (Actualización)
*   `updateOne(query, update)`: Actualiza el primer documento encontrado.
*   `updateMany(query, update)`: Actualiza todos los documentos que coincidan.

```javascript
db.usuarios.updateMany(
  { nombre: "Ana" },
  { $set: { ciudad: "Valencia" } } // $set evita sobrescribir todo el doc
)
```

### 4. Delete (Borrado)
*   `deleteOne(query)`: Borra el primero.
*   `deleteMany(query)`: Borra todos.

```javascript
db.usuarios.deleteMany({ edad: { $lt: 18 } })
```

---
**Enlaces Relacionados:**
*   [Operadores de Consulta](MongoDB-Query-Operators.md)
*   [Modelo Documental](MongoDB-Model-Overview.md)
