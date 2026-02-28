# Diseño de Esquemas: Embedding vs Referencing

En MongoDB, la decisión fundamental de diseño es si los datos relacionados deben estar en el mismo documento (**Embedding**) o en documentos separados (**Referencing**).

### 1. Embedding (Embebido)
Almacena datos relacionados como subdocumentos o arreglos dentro del documento principal.
*   **Ventajas:** Lectura atómica (una sola consulta), sin *joins*, mayor rendimiento.
*   **Desventajas:** Límite de 16MB por documento, riesgo de duplicación de datos.
*   **Uso:** Relaciones 1:1 o 1:N donde "N" es pequeño y los datos no crecen indefinidamente.

### 2. Referencing (Referencia)
Almacena solo un identificador (`_id`) que apunta a un documento en otra colección. 
*   **Ventajas:** Evita duplicación, permite documentos más pequeños, mayor flexibilidad.
*   **Desventajas:** Requiere múltiples consultas o el uso de `$lookup` (*join* en tiempo de ejecución), menor rendimiento.
*   **Uso:** Relaciones N:M o 1:N donde "N" es muy grande (ej. seguidores de una celebridad).

> [!IMPORTANT]
> **Data that is accessed together should be stored together.** Esta es la regla de oro del modelado documental.

---
**Enlaces Relacionados:**
*   [Modelo Documental](MongoDB-Model-Overview.md)
*   [Jerarquía de Datos en MongoDB](MongoDB-Data-Hierarchy.md)
