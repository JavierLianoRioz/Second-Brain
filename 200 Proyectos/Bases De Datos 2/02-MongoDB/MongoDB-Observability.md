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

---
**Enlaces Relacionados:**
*   [Monitoreo y Rendimiento](MongoDB-Monitoring.md)
*   [Seguridad (Autenticación/Autorización)](MongoDB-Security.md)
*   [Buenas Prácticas Operativas](MongoDB-Best-Practices.md)
