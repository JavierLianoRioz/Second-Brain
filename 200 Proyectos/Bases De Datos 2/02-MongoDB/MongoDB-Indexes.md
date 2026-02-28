# Índices y Rendimiento en MongoDB

Los índices mejoran drásticamente la velocidad de las consultas de lectura al evitar que MongoDB tenga que escanear cada documento de una colección (*Collection Scan*).

### Tipos de Índices
1.  **Single Field:** Índice sobre un solo campo.
2.  **Compound Index:** Índice sobre múltiples campos. El orden de los campos importa (*ESR rule*: Equality, Sort, Range).
3.  **Multikey Index:** Índice sobre un campo que contiene un arreglo.
4.  **Text Index:** Para búsquedas de texto completo.
5.  **TTL (Time To Live):** Borra documentos automáticamente tras un tiempo (útil para sesiones).

### Análisis de Consultas
Para verificar si una consulta está usando un índice, se utiliza el método `.explain()`:
```javascript
db.usuarios.find({ email: "test@example.com" }).explain("executionStats")
```

> [!WARNING]
> Los índices mejoran las lecturas pero penalizan las escrituras, ya que cada inserción o actualización requiere actualizar el índice. Úsalos con prudencia.

---
**Enlaces Relacionados:**
*   [CRUD en MongoDB](MongoDB-CRUD-Basics.md)
*   [Diseño de Esquemas](MongoDB-Schema-Design-Patterns.md)
