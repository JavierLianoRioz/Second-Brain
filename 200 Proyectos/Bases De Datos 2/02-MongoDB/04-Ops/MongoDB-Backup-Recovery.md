# Backup y Recuperación en MongoDB

Un respaldo (backup) es una copia controlada del estado de la base de datos en un momento determinado, que garantiza: recuperación de datos, preservación de estructura, reconstrucción de índices y un estado consistente.

### mongodump — Respaldo Lógico
```bash
# Respaldar todas las bases de datos
mongodump --uri="mongodb://admin:admin123@localhost:27018" --out=backup_universidad

# Respaldar solo una BD
mongodump --uri="mongodb://admin:admin123@localhost:27018" \
  --db universidad --out backup_universidad

# Respaldar una colección específica
mongodump --uri="mongodb://admin:admin123@localhost:27018" \
  --db universidad --collection cursos --out backup_cursos
```
Genera archivos `.bson` (datos) y `.metadata.json` (información estructural) por cada colección.

### mongorestore — Restauración
```bash
# Restaurar todo
mongorestore --drop \
  --uri="mongodb://admin:admin123@localhost:27017" \
  backup_universidad

# Restaurar una colección específica
mongorestore --uri="mongodb://admin:admin123@localhost:27018" \
  --nsInclude="universidad.cursos" \
  backup_universidad
```

### Estrategias de Respaldo en Producción

| Tipo de backup | Frecuencia       |
| -------------- | ---------------- |
| Completo       | Semanal          |
| Incremental    | Diario           |
| Snapshot       | Cada pocas horas |

Buenas prácticas:
*   Almacenar backups en **servidores diferentes**
*   **Probar regularmente** los procesos de restauración
*   Mantener copias offline o en almacenamiento frío
*   Automatizar mediante cron o pipelines

> [!CAUTION]
> Un backup que nunca se ha probado **no garantiza recuperación**.

Un proceso de respaldo sólido debe integrarse con una política de [Seguridad](MongoDB-Security.md) coherente y seguir las [Buenas Prácticas Operativas](MongoDB-Best-Practices.md) para garantizar la continuidad del negocio.
