# Ejercicio - Clasificación de Escenarios (SQL vs NoSQL)

### Enunciados

1.  **Universidad:** Gestión de matrículas y actas. Se requiere consistencia fuerte y transacciones seguras.
2.  **Tokens de Sesión:** Almacenamiento temporal de preferencias de usuario con acceso inmediato por ID.
3.  **Sensores Industriales:** Millones de registros diarios para análisis histórico y patrones globales.
4.  **Gestor de Contenidos (CMS):** Artículos con campos muy variables y cambios frecuentes de modelo.
5.  **Transferencias Bancarias:** Registro crítico donde no se puede perder dinero bajo ningún concepto.
6.  **Detección de Fraude en Redes:** Análisis de conexiones indirectas y caminos entre múltiples entidades.
7.  **Similitud Semántica:** Buscador que encuentra documentos por significado conceptual, no solo palabras clave.

### Respuestas y Justificación

| Escenario | Tecnología Recomendada | Justificación |
| :--- | :--- | :--- |
| **1. Universidad** | SQL (Relacional) | Relaciones estables, consistencia fuerte necesaria (ACID). |
| **2. Sesiones** | NoSQL (Clave-Valor) | Acceso ultrarrápido por ID, datos temporales, sin relaciones. |
| **3. Sensores** | NoSQL (Columnar) | Gran volumen, consultas analíticas (agregados) sobre series temporales. |
| **4. CMS** | NoSQL (Documental) | Flexibilidad de esquema, documentos autocontenidos. |
| **5. Banco** | SQL (Relacional) | Atomicidad crítica, consistencia inmediata obligatoria. |
| **6. Fraude** | NoSQL (Grafos) | El valor reside en el análisis de relaciones profundas. |
| **7. Buscador** | NoSQL (Vectorial) | Búsqueda por proximidad semántica (embeddings). |

---
**Referenciado desde:**
*   [Introducción a NoSQL](NoSQL-Introduction.md)
*   [Tipos de NoSQL](NoSQL-Types-Overview.md)
