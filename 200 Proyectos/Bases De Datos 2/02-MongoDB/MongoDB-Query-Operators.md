# Operadores de Consulta en MongoDB

Los operadores permiten realizar filtrados avanzados más allá de la igualdad simple.

### Operadores de Comparación
*   `$eq`: Igual a.
*   `$ne`: No igual a.
*   `$gt` / `$gte`: Mayor que / mayor o igual que.
*   `$lt` / `$lte`: Menor que / menor o igual que.
*   `$in`: El valor está en un arreglo dado.

```javascript
db.productos.find({ precio: { $gte: 10, $lte: 50 } })
```

### Operadores Lógicos
*   `$and`: Todas las condiciones deben cumplirse.
*   `$or`: Al menos una condición debe cumplirse.
*   `$not`: Invierte el resultado de la condición.

```javascript
db.usuarios.find({
  $or: [ { edad: { $lt: 18 } }, { activo: false } ]
})
```

### Operadores de Arreglos
*   `$all`: El arreglo debe contener todos los elementos especificados.
*   `$elemMatch`: Al menos un elemento del arreglo cumple múltiples criterios.
*   `$size`: El arreglo tiene un tamaño específico.

---
**Enlaces Relacionados:**
*   [MongoDB CRUD](MongoDB-CRUD-Basics.md)
*   [Aggregation Framework](MongoDB-Aggregation-Framework.md)
