# JSON vs BSON

MongoDB utiliza internamente **BSON** (*Binary JSON*) para el almacenamiento y la transmisión de datos, aunque el usuario interactúa principalmente con **JSON**.

### Comparativa

| Característica | JSON | BSON |
| :--- | :--- | :--- |
| **Formato** | Texto (Legible) | Binario (Eficiente) |
| **Velocidad** | Lento de parsear | Rápido de escanear y saltar campos |
| **Tipos de datos** | Básicos (Número, String, Booleano, Array, Objeto) | Extendidos (Long, Date, Decimal128, ObjectId, Binary) |
| **Espacio** | Generalmente mayor (como texto) | Optimizado para almacenamiento binario |

### Tipos Específicos de BSON
*   `ObjectId`: Identificador único de 12 bytes para cada documento.
*   `Date`: Almacena fechas como enteros de 64 bits (milisegundos desde Unix epoch).
*   `Binary Data`: Para almacenar archivos o datos binarios pequeños.

> [!TIP]
> Al realizar [operaciones CRUD](MongoDB-CRUD-Basics.md) en el shell de MongoDB, el formato que escribes es JSON (o EJSON), pero MongoDB lo convierte a BSON internamente para su procesamiento según el [Modelo Documental](MongoDB-Model-Overview.md).
