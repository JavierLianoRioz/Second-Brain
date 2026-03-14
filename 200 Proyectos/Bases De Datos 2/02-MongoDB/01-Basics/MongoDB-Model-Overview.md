# El Modelo Documental en MongoDB

MongoDB es una base de datos documental que almacena la información en unidades llamadas **documentos**, agrupados en **colecciones**.

### Conceptos Clave

*   **Documento:** Unidad básica de información (equivalente a una "fila" en SQL). Generalmente en formato BSON.
*   **Colección:** Agrupación de documentos (equivalente a una "tabla" en SQL).
*   **Esquema Flexible:** Los documentos de una misma colección no necesitan tener la misma estructura (*dynamic schema*).

### Estructura de un Documento
Un documento es un conjunto de pares campo-valor:

```json
{
  "_id": ObjectId("60a..."),
  "nombre": "Javier",
  "habilidades": ["NoSQL", "DevOps"],
  "direccion": {
    "ciudad": "Madrid",
    "pais": "España"
  }
}
```

### Ventajas del Modelo
1.  **Correspondencia Natural:** Los documentos se mapean casi directamente a objetos en lenguajes de programación.
2.  **Autocontención:** La información relacionada se suele almacenar junta, evitando *joins*.
3.  **Jerarquía:** Soporta arreglos y subdocumentos anidados, organizados en la [Jerarquía de Datos](MongoDB-Data-Hierarchy.md).

Toda manipulación de estos documentos se realiza mediante las [operaciones CRUD](MongoDB-CRUD-Basics.md) sobre la base del formato [JSON/BSON](JSON-vs-BSON.md).
