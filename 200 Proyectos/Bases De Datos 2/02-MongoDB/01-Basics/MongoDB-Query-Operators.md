# Operadores de Consulta en MongoDB

Los operadores permiten realizar filtrados avanzados más allá de la igualdad simple.

### Operadores de Comparación
*   `$eq`: Igual a.
*   `$ne`: No igual a.
*   `$gt` / `$gte`: Mayor que / mayor o igual que.
*   `$lt` / `$lte`: Menor que / menor o igual que.
*   `$in`: El valor está en un arreglo dado.

```javascript
// Encuentra documentos donde el campo 'categoría' sea 'Electrónica' o 'Hogar'
db.productos.find({ categoria: { $in: ["Electrónica", "Hogar"] } })
```

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

##### Ejemplos de uso:
```javascript
db.productos.find({ tags: { $all: ["nuevo", "oferta"] } })

db.productos.find({
  stock: { $elemMatch: { almacen: "Norte", cantidad: { $gt: 10 } } }
})

db.productos.find({ comentarios: { $size: 3 } })
```

> [!NOTE]
> * **`$all`**: Útil cuando el orden no importa pero la presencia de todos los elementos sí.
> * **`$elemMatch`**: Necesario cuando se consulta un arreglo de objetos y se quiere que un mismo objeto cumpla varias condiciones (evita falsos positivos).
> * **`$size`**: Solo acepta valores numéricos exactos (no soporta rangos como `$gt`).

Estos operadores son fundamentales tanto en las [operaciones CRUD](MongoDB-CRUD-Basics.md) básicas como en la etapa `$match` del [Aggregation Framework](../03-Performance/MongoDB-Aggregation-Framework.md).
