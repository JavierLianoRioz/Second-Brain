# 🧠 Índice: Bases de Datos II (Zettelkasten)

Este índice organiza los conceptos de la asignatura siguiendo una progresión lógica, desde los fundamentos teóricos hasta la implementación práctica y bases de datos especializadas.

---

## 🏗️ Bloque 1: Fundamentos y NoSQL
*La base teórica necesaria antes de tocar ninguna base de datos.*

- 📝 **[Introducción a NoSQL](01-Fundamentos-NoSQL/NoSQL-Introduction.md)** — Por qué surgen y qué problemas resuelven.
- 📐 **[Teorema CAP](01-Fundamentos-NoSQL/CAP-Theorem.md)** — El equilibrio entre Consistencia, Disponibilidad y Particiones.
- ⚖️ **[ACID vs BASE](01-Fundamentos-NoSQL/ACID-vs-BASE.md)** — Garantías transaccionales en SQL vs NoSQL.
- 📂 **[Tipos de NoSQL](01-Fundamentos-NoSQL/NoSQL-Types-Overview.md)** — Panorama de Clave-Valor, Documental, Columnar y Grafos.

---

## 🍃 Bloque 2: MongoDB (Bases Documentales)
*Dominio del modelo documental y el ecosistema de MongoDB.*

### 🔍 Fundamentos y Consultas
- 🏢 **[Jerarquía y Modelo](02-MongoDB/MongoDB-Data-Hierarchy.md)** — Cluster → DB → Colección → Documento.
- 📦 **[JSON vs BSON](02-MongoDB/JSON-vs-BSON.md)** — Diferencias técnicas y tipos de datos.
- 📑 **[Operaciones CRUD](02-MongoDB/MongoDB-CRUD-Basics.md)** — Inserción, consulta, actualización y borrado.
- 🛠️ **[Operadores de Consulta](02-MongoDB/MongoDB-Query-Operators.md)** — Filtrado avanzado y manipulación de arreglos.

### ⚙️ Rendimiento y Modelado
- 🚀 **[Índices y Rendimiento](02-MongoDB/MongoDB-Indexes.md)** — Cómo acelerar consultas y la regla ESR.
- 🏗️ **[Diseño de Esquemas](02-MongoDB/MongoDB-Schema-Design-Patterns.md)** — Embedding vs Referencing (Cuándo usar cada cual).
- 🧬 **[Patrones Avanzados](02-MongoDB/MongoDB-Advanced-Modeling.md)** — Subset, Bucket y otros patrones industriales.
- ⚠️ **[Antipatrones](02-MongoDB/MongoDB-Antipatterns.md)** — Errores de diseño que destrozan el rendimiento.

### ⛓️ Agregación y Operaciones
- 🧪 **[Aggregation Framework](02-MongoDB/MongoDB-Aggregation-Framework.md)** — El motor de análisis (Match, Group, Project).
- 🛡️ **[Seguridad y Roles](02-MongoDB/MongoDB-Security.md)** — Autenticación, RBAC y protección de datos.
- 📋 **[Validación de Esquemas](02-MongoDB/MongoDB-Schema-Validation.md)** — Forzando estructura con JSON Schema.
- 🔋 **[Backup y Admin](02-MongoDB/MongoDB-Backup-Recovery.md)** — Estrategias de mantenimiento y recuperación.

---

## 🕸️ Bloque 3: Más allá de los Documentos (Próximamente)
*Temas avanzados del programa de la asignatura.*

- 🔗 **BD de Grafos (Neo4j)** — Modelado de relaciones complejas y lenguaje Cypher.
- 🎯 **BD Vectoriales** — Búsqueda semántica, embeddings e IA.
- 📈 **Optimización y Escalabilidad** — Sharding, replicación y casos reales.

---

## 🛠️ Laboratorio y Práctica
*Aplicación directa de los conceptos.*

1. 🟢 **[Clasificación de Escenarios](Ejercicios/Ej-Clasificacion-Escenarios.md)** — SQL vs NoSQL.
2. 🟢 **[Diseño y CRUD](Ejercicios/Ej-MongoDB-CRUD-Modelado.md)** — Primeros pasos en Mongo.
3. 🟡 **[Aggregation Ventas](Ejercicios/Ej-Aggregation-Ventas.md)** — Análisis de datos complejo.
4. 🔴 **[Optimización Total](Ejercicios/Ej-Indices-Transacciones-Monitoreo.md)** — Índices y transacciones avanzadas.

---
*Última sincronización con el temario: 2026-03-14*

