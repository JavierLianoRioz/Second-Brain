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
- 🏢 **[Jerarquía y Modelo](02-MongoDB/01-Basics/MongoDB-Data-Hierarchy.md)** — Cluster → DB → Colección → Documento.
- 📂 **[Modelo Documental](02-MongoDB/01-Basics/MongoDB-Model-Overview.md)** — Ventajas y estructura del esquema flexible.
- 📦 **[JSON vs BSON](02-MongoDB/01-Basics/JSON-vs-BSON.md)** — Diferencias técnicas y tipos de datos.
- 📑 **[Operaciones CRUD](02-MongoDB/01-Basics/MongoDB-CRUD-Basics.md)** — Inserción, consulta, actualización y borrado.
- 🛠️ **[Operadores de Consulta](02-MongoDB/01-Basics/MongoDB-Query-Operators.md)** — Filtrado avanzado y manipulación de arreglos.

### ⚙️ Rendimiento y Modelado
- 🚀 **[Índices y Rendimiento](02-MongoDB/03-Performance/MongoDB-Indexes.md)** — Cómo acelerar consultas y la regla ESR.
- 🏗️ **[Diseño de Esquemas](02-MongoDB/02-Design/MongoDB-Schema-Design-Patterns.md)** — Embedding vs Referencing (Cuándo usar cada cual).
- 🧬 **[Patrones Avanzados](02-MongoDB/02-Design/MongoDB-Advanced-Modeling.md)** — Subset, Bucket y otros patrones industriales.
- 📊 **[Monitoreo y Observabilidad](02-MongoDB/03-Performance/MongoDB-Observability.md)** — Métricas clave de rendimiento y auditoría operativa.
- 🔎 **[Análisis de Consultas](02-MongoDB/03-Performance/MongoDB-Monitoring.md)** — El uso de `explain()` y optimización de pipelines.
- ⚠️ **[Antipatrones](02-MongoDB/02-Design/MongoDB-Antipatterns.md)** — Errores de diseño que destrozan el rendimiento.

### ⛓️ Agregación y Operaciones
- 🧪 **[Aggregation Framework](02-MongoDB/03-Performance/MongoDB-Aggregation-Framework.md)** — El motor de análisis (Match, Group, Project).
- 🛡️ **[Seguridad y Roles](02-MongoDB/04-Ops/MongoDB-Security.md)** — Autenticación, RBAC y protección de datos.
- 📋 **[Validación de Esquemas](02-MongoDB/04-Ops/MongoDB-Schema-Validation.md)** — Forzando estructura con JSON Schema.
- 🔋 **[Backup y Admin](02-MongoDB/04-Ops/MongoDB-Backup-Recovery.md)** — Estrategias de mantenimiento y recuperación.
- ✅ **[Buenas Prácticas](02-MongoDB/04-Ops/MongoDB-Best-Practices.md)** — Checklist operativa y de gobernanza de datos.
- 🚩 **[Errores de Seguridad](02-MongoDB/04-Ops/MongoDB-Security-Errors.md)** — Fallos comunes a evitar antes de producción.

---

## 🕸️ Bloque 3: Más allá de los Documentos (Próximamente)
*Temas avanzados del programa de la asignatura.*

- 🔗 **BD de Grafos (Neo4j)** — Modelado de relaciones complejas y lenguaje Cypher.
- 🎯 **BD Vectoriales** — Búsqueda semántica, embeddings e IA.
- 📈 **Optimización y Escalabilidad** — Sharding, replicación y casos reales.

---

## 🎓 ¡Preparación para el Examen!
*Recursos clave para aprobar el parcial práctico.*

- 🚀 **[Guía de Supervivencia: Examen Práctico](05-GUIA-PRACTICA-EXAMEN.md)** — **¡LEER PRIMERO!** Resumen de queries, escenarios comunes y errores frecuentes del examen.
- 📝 **[Ejercicios: Escenarios SQL vs NoSQL](Ejercicios/Ej-Clasificacion-Escenarios.md)** — Para las preguntas teóricas del principio.
- 🟢 **[Ejercicios: CRUD y Modelado](Ejercicios/Ej-MongoDB-CRUD-Modelado.md)** — Práctica básica de inserción y consulta.
- 🟡 **[Ejercicios: Aggregation Framework](Ejercicios/Ej-Aggregation-Ventas.md)** — Análisis de datos complejo (clavi para el examen).
- 🔴 **[Ejercicios: Optimización Total](Ejercicios/Ej-Indices-Transacciones-Monitoreo.md)** — Índices y el uso de `.explain()`.

---
*Última sincronización con el temario: 2026-03-14*

