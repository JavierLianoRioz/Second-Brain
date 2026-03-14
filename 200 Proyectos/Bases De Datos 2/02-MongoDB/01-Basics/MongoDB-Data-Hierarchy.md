# Jerarquía de Datos en MongoDB

Aunque MongoDB es flexible, entender la jerarquía lógica es vital para el diseño eficiente de aplicaciones.

### Estructura de Granularidad

1.  **Cluster:** Instancia o conjunto de instancias de MongoDB (servidores).
2.  **Database (Base de Datos):** Contenedor de nivel superior para colecciones.
3.  **Collection (Colección):** Grupo de documentos. Equivale a una tabla.
4.  **Document (Documento):** Registro individual. Equivale a una fila. Almacenado como BSON.
5.  **Field (Campo):** Par clave-valor dentro de un documento.

### Límites Físicos
*   **Tamaño del Documento:** Máximo de 16MB. Superar este límite es uno de los [Antipatrones](../02-Design/MongoDB-Antipatterns.md#2-documentos-sin-control-de-crecimiento) más comunes. Para archivos más grandes, se usa GridFS.
*   **Anidamiento:** Máximo de 100 niveles de profundidad para subdocumentos.

Esta estructura favorece el [Diseño de Esquemas](../02-Design/MongoDB-Schema-Design-Patterns.md) basado en la autocontención de datos según el [Modelo Documental](MongoDB-Model-Overview.md).
