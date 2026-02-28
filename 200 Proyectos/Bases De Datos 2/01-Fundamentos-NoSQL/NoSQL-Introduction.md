# Introducción a NoSQL

Las bases de datos NoSQL (**Not Only SQL**) surgen como respuesta a las limitaciones de escalabilidad y flexibilidad del modelo relacional ante el crecimiento masivo de datos y la necesidad de esquemas dinámicos.

### ¿Por qué NoSQL?

El modelo relacional tradicional enfrenta dificultades en escenarios de:
*   **Gran volumen de datos:** Dificultad para escalar horizontalmente ([sharding](../../../001%20Areas/Sharding.md)).
*   **Velocidad:** Latencia en operaciones complejas con múltiples *joins*.
*   **Variedad:** Estructuras de datos que cambian frecuentemente o no son uniformes.

### Características Principales

1.  **Escalabilidad Horizontal:** Diseñadas para distribuirse en clústeres de servidores económicos.
2.  **Esquema Flexible:** No requieren una definición rígida previa (*schema-less*).
3.  **Sin Joins:** Priorizan la desnormalización para mejorar el rendimiento de lectura.
4.  **Propiedades BASE:** En contraste con ACID, buscan disponibilidad y consistencia eventual.

---
**Enlaces Relacionados:**
*   [Teorema CAP](CAP-Theorem.md)
*   [Modelo BASE](ACID-vs-BASE.md)
*   [Tipos de NoSQL](NoSQL-Types-Overview.md)
*   [Ejercicio - Clasificación](Ej-Clasificacion-Escenarios.md)
