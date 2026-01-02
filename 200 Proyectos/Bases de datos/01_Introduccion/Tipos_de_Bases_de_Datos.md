# Tipos de Bases de Datos

Las bases de datos se pueden clasificar según diversos criterios:

## Por Uso
*   **Operacionales (OLTP)**: Optimizadas para transacciones diarias rápidas (ej. ventas, reservas).
*   **Analíticas (OLAP)**: Optimizadas para consultas complejas y análisis histórico (ej. Business Intelligence).

## Por Modelo de Datos
*   **Relacional**: Datos en tablas relacionadas. Estándar de la industria. Ver [[Modelo_Relacional_Conceptos]].
*   **NoSQL**:
    *   **Documental**: JSON/BSON (MongoDB).
    *   **Clave-Valor**: Alta velocidad (Redis).
    *   **Grafos**: Relaciones complejas (Neo4j).
    *   **Columnar**: Big Data (Cassandra).
*   **Jerárquico / Red**: Modelos legados.

## Por Ubicación
*   **Centralizadas**: Todo en un solo servidor.
*   **Distribuidas**: Datos repartidos en múltiples nodos (transparencia para el usuario).
*   **Cloud**: Alojadas y gestionadas por proveedores (AWS RDS, Azure SQL).

---
[[00_MOC_Introduccion]]
