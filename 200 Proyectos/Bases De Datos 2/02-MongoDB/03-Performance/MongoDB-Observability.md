# Observabilidad y Auditoría Operativa en MongoDB

La **observabilidad** permite detectar problemas antes de que se conviertan en fallos críticos. La **auditoría** registra qué usuarios realizan operaciones dentro del sistema.

### Herramientas de Observabilidad
```javascript
db.stats()          // Información general de la BD
db.serverStatus()   // Métricas internas del servidor
db.currentOp()      // Operaciones en curso
db.collection.stats() // Estadísticas de una colección
```

`db.stats()` devuelve: colecciones, objetos, `avgObjSize`, `dataSize`, `storageSize` — permite estimar crecimiento y uso de almacenamiento.

`db.serverStatus()` proporciona: conexiones activas, operaciones por segundo, uso de memoria y actividad del motor de almacenamiento.

### Auditoría de Operaciones
MongoDB puede registrar:
*   Autenticación de usuarios
*   Creación/eliminación de colecciones
*   Modificaciones de documentos
*   Cambios en permisos

Permite responder: ¿quién eliminó una colección?, ¿qué usuario modificó datos?, ¿cuándo ocurrió un incidente?

> [!TIP]
> En entornos empresariales, las métricas suelen integrarse con **Prometheus** o **Grafana**, y los logs de auditoría con plataformas de análisis de seguridad.

La auditoría y el registro de incidentes son componentes clave de la [Seguridad](../04-Ops/MongoDB-Security.md) de la base de datos, permitiendo cumplir con las [Buenas Prácticas Operativas](../04-Ops/MongoDB-Best-Practices.md) y complementar el [Monitoreo de Rendimiento](MongoDB-Monitoring.md).
