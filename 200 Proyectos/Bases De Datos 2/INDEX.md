# Índice Zettelkasten: Bases de Datos II

Bienvenido a la red de notas atómicas de **Bases de Datos II**. Está estructurado para facilitar el aprendizaje no lineal y la referencia rápida.

> **Cómo usar este índice:** Lee las secciones en orden para un aprendizaje lineal, o salta entre notas siguiendo los enlaces al final de cada una para un aprendizaje exploratorio.

## 📂 01. Fundamentos NoSQL
*¿Qué es NoSQL y cuándo elegirlo?*
*   [Introducción a NoSQL](01-Fundamentos-NoSQL/NoSQL-Introduction.md) — Por qué existen, características principales
*   [Teorema CAP](01-Fundamentos-NoSQL/CAP-Theorem.md) — Consistencia vs Disponibilidad vs Particiones
*   [ACID vs BASE](01-Fundamentos-NoSQL/ACID-vs-BASE.md) — Dos modelos de garantías transaccionales
*   [Tipos de NoSQL](01-Fundamentos-NoSQL/NoSQL-Types-Overview.md) — Clave-Valor, Documental, Columnar, Grafos, Vectorial

## 📂 02. MongoDB — Fundamentos y Consultas
*Modelo documental, operaciones y rendimiento.*
*   [Modelo Documental](02-MongoDB/MongoDB-Model-Overview.md) — Documentos, colecciones, esquema flexible
*   [JSON vs BSON](02-MongoDB/JSON-vs-BSON.md) — Formatos internos y tipos especiales
*   [Jerarquía de Datos](02-MongoDB/MongoDB-Data-Hierarchy.md) — Cluster → DB → Collection → Document → Field
*   [Operaciones CRUD](02-MongoDB/MongoDB-CRUD-Basics.md) — insertOne, find, updateOne, deleteMany
*   [Operadores de Consulta](02-MongoDB/MongoDB-Query-Operators.md) — Comparación, lógicos, arrays
*   [Diseño de Esquemas](02-MongoDB/MongoDB-Schema-Design-Patterns.md) — Embedding vs Referencing
*   [Aggregation Framework](02-MongoDB/MongoDB-Aggregation-Framework.md) — Pipeline: match, group, sort, project
*   [Índices y Rendimiento](02-MongoDB/MongoDB-Indexes.md) — Tipos de índices, explain(), ESR rule

## 📂 03. MongoDB — Modelado Avanzado
*Patrones profesionales, antipatrones y monitoreo.*
*   [Patrones de Modelado](02-MongoDB/MongoDB-Advanced-Modeling.md) — Subset, Bucket, Extended Ref, Computed, Outlier
*   [Antipatrones Comunes](02-MongoDB/MongoDB-Antipatterns.md) — Sobre-normalización, arrays sin límite, índices innecesarios
*   [Monitoreo y Rendimiento](02-MongoDB/MongoDB-Monitoring.md) — explain(), serverStatus, optimización de pipelines

## 📂 04. MongoDB — Seguridad y Operaciones
*Preparar MongoDB para producción.*
*   [Seguridad: Autenticación y Autorización](02-MongoDB/MongoDB-Security.md) — SCRAM, usuarios, roles, mínimo privilegio
*   [Validación de Esquemas](02-MongoDB/MongoDB-Schema-Validation.md) — JSON Schema, strict/moderate, evolución
*   [Errores Comunes](02-MongoDB/MongoDB-Security-Errors.md) — Checklist pre-producción
*   [Backup y Recuperación](02-MongoDB/MongoDB-Backup-Recovery.md) — mongodump, mongorestore, estrategias
*   [Observabilidad y Auditoría](02-MongoDB/MongoDB-Observability.md) — db.stats(), logs, auditoría
*   [Buenas Prácticas Operativas](02-MongoDB/MongoDB-Best-Practices.md) — Resumen profesional

## 📝 Ejercicios Prácticos
*Ordenados por dificultad progresiva.*
1.  [Clasificación de Escenarios (SQL vs NoSQL)](Ejercicios/Ej-Clasificacion-Escenarios.md) — 🟢 Conceptual
2.  [CRUD y Modelado Documental](Ejercicios/Ej-MongoDB-CRUD-Modelado.md) — 🟢 Básico
3.  [Aggregation Framework](Ejercicios/Ej-Aggregation-Ventas.md) — 🟡 Intermedio
4.  [Índices, Transacciones y Monitoreo](Ejercicios/Ej-Indices-Transacciones-Monitoreo.md) — 🔴 Avanzado

---
*Última actualización: 2026-03-09*
