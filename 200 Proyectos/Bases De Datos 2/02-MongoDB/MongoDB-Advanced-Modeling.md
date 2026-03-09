# Modelado Avanzado: Patrones en MongoDB

Más allá del simple *Embedding* o *Referencing*, existen patrones de diseño específicos para resolver problemas comunes de rendimiento y estructura. El modelado en MongoDB es una **decisión estratégica** basada en: frecuencia de lectura/escritura, atomicidad requerida, crecimiento esperado y patrón de consulta dominante.

> [!WARNING]
> El error más común es modelar por intuición estructural en lugar de modelar por **comportamiento de acceso**.

### 1. Patrón Subset (Acceso Frecuente)
Almacena solo una parte relevante de un conjunto grande dentro del documento principal. Ej: un usuario tiene 10,000 pedidos, pero se muestran los últimos 5.
```javascript
{
  _id: 1,
  nombre: "Carlos",
  ultimosPedidos: [
    { pedidoId: 201, total: 300 },
    { pedidoId: 202, total: 150 }
  ]
}
```
*   **Ventaja:** Reduce tamaño de documento, mejora lectura, evita `$lookup`.
*   **Riesgo:** Requiere sincronización manual con la colección completa.

### 2. Patrón Bucket (Series Temporales)
Agrupa datos que crecen continuamente (logs, sensores) en un solo documento en lugar de uno por registro:
```javascript
{
  sensorId: 1,
  fechaInicio: t1,
  valores: [20, 21, 22, 23]
}
```
*   **Ventaja:** Reduce documentos, carga en índices y sobrecarga de metadata (hasta 40–60% menos almacenamiento).
*   **Riesgo:** El tamaño del bucket no debe crecer indefinidamente.

### 3. Patrón Extended Reference (Referencia Extendida)
Copia los campos más usados del documento referenciado al documento principal para evitar `$lookup` constantes.
```javascript
pedido: {
  clienteId: ObjectId(...),
  nombreCliente: "Ana",
  ciudadCliente: "Madrid"
}
```
*   **Regla:** Duplicar datos cuando el costo de inconsistencia es menor que el costo de consulta repetitiva.

### 4. Patrón Computed (Cálculos Previos)
Para sistemas de alto tráfico, se pre-calculan agregaciones en lugar de recalcularlas constantemente:
```javascript
{
  cursoId: 10,
  promedioNotas: 4.3,
  totalInscripciones: 120
}
```
*   Clave en sistemas financieros y dashboards. Se actualiza cuando cambian los datos fuente.

### 5. Patrón Outlier (Casos Excepcionales)
Los datos excesivos se mueven a una colección aparte o a un documento "desbordado", ideal cuando la mayoría de documentos tienen pocos hijos pero unos pocos tienen miles.

---
**Enlaces Relacionados:**
*   [Antipatrones Comunes](MongoDB-Antipatterns.md)
*   [Diseño de Esquemas](MongoDB-Schema-Design-Patterns.md)
*   [Índices y Rendimiento](MongoDB-Indexes.md)
*   [Monitoreo y Observabilidad](MongoDB-Monitoring.md)
