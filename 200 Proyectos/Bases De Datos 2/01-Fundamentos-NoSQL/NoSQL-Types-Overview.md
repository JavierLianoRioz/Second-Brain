# Tipos de Bases de Datos NoSQL

Las bases de datos NoSQL no son una única tecnología, sino un conjunto de familias diseñadas para problemas específicos.

### 1. Clave-Valor (Key-Value)
Es el modelo más simple. Almacena pares de claves únicas y valores asociados.
*   **Uso:** Sesiones, caché, carritos de compra.
*   **Ejemplos:** Redis, DynamoDB.

### 2. Documentales (Document)
Almacenan datos en documentos (JSON, BSON, XML). Cada documento es autocontenido y puede tener estructura variable.
*   **Uso:** CMS, catálogos de productos, aplicaciones web.
*   **Ejemplos:** MongoDB, CouchDB.

### 3. Columnares (Wide-Column)
Organizan los datos en familias de columnas en lugar de filas. Optimizadas para lecturas analíticas masivas.
*   **Uso:** Big Data, análisis de logs, series temporales.
*   **Ejemplos:** Cassandra, HBase.

### 4. Grafos (Graph)
Representan los datos como nodos y relaciones (aristas). Ideales para analizar conexiones complejas.
*   **Uso:** Redes sociales, recomendadores, detección de fraude.
*   **Ejemplos:** Neo4j, JanusGraph.

### 5. Vectoriales (Vector)
Almacenan representaciones matemáticas de datos (embeddings). Permiten búsquedas por similitud semántica.
*   **Uso:** IA, búsqueda de imágenes, LLMs.
*   **Ejemplos:** Pinecone, Milvus.

---
**Enlaces Relacionados:**
*   [Introducción a NoSQL](NoSQL-Introduction.md)
*   [Modelo Documental](./MongoDB-Model-Overview.md)
*   [Ejercicio - Clasificación](./Ejercicios/Ej-Clasificacion-Escenarios.md)
