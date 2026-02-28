# Modelado Avanzado: Patrones en MongoDB

Más allá del simple *Embedding* o *Referencing*, existen patrones de diseño específicos para resolver problemas comunes de rendimiento y estructura.

### 1. Patrón Outlier (Casos Excepcionales)
Se usa cuando la mayoría de los documentos tienen pocos hijos, pero unos pocos tienen miles (ej. un libro con millones de reseñas).
*   **Solución:** Los datos excesivos se mueven a una colección aparte o a un documento "desbordado".

### 2. Patrón Computed (Cálculos Previos)
En lugar de calcular un total cada vez que se lee (especialmente en Aggregation), el resultado se guarda en el documento.
*   **Solución:** Mantener un campo `total_compras` que se actualiza con cada nueva compra.

### 3. Patrón Extended Reference (Referencia Extendida)
Para evitar `$lookup` constantes, se copian los campos más usados del documento referenciado al documento principal.
*   **Solución:** Si un pedido referencia a un cliente, guardar también el `nombre_cliente` dentro del pedido.

---
**Enlaces Relacionados:**
*   [Diseño de Esquemas](MongoDB-Schema-Design-Patterns.md)
*   [Índices y Rendimiento](MongoDB-Indexes.md)
