# Validación de Esquemas con JSON Schema

MongoDB permite definir reglas de validación mediante **JSON Schema**, una capa de control estructural sobre los documentos que combate la inconsistencia de la flexibilidad documental.

### Creación con Validación
```javascript
db.createCollection("cursos", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["nombre", "nivel", "creditos"],
      properties: {
        nombre: { bsonType: "string", description: "Debe ser texto" },
        nivel: { enum: ["basico", "intermedio", "avanzado"] },
        creditos: { bsonType: "int", minimum: 1, maximum: 10 }
      }
    }
  }
})
```
Si insertamos `nivel: "experto"`, MongoDB **rechaza** la operación.

### Modos de Validación: `strict` vs `moderate`
*   **strict:** Rechaza cualquier documento que no cumpla el esquema (inserciones y actualizaciones).
*   **moderate:** Solo valida documentos nuevos o modificados; los antiguos permanecen intactos.

```javascript
db.runCommand({ collMod: "cursos", validationLevel: "strict" })
```

| Escenario                      | Nivel recomendado     |
| ------------------------------ | --------------------- |
| Proyecto nuevo                 | strict                |
| Migración de sistema existente | moderate              |
| Datos históricos heterogéneos  | moderate inicialmente |

### Evolución Controlada del Esquema
Estrategia profesional para evolucionar esquemas:
1. Definir la nueva versión del esquema
2. Actualizar la validación de la colección
3. Migrar documentos antiguos
4. Activar validación estricta

```javascript
// Migrar documentos antiguos sin el campo "creditos"
db.cursos.updateMany(
  { creditos: { $exists: false } },
  { $set: { creditos: 3 } }
)
```

> [!IMPORTANT]
> No confiar solo en la validación de la aplicación. La validación a nivel de BD es una **segunda línea de defensa**.

La validación estructural es el complemento necesario al [Diseño de Esquemas](../02-Design/MongoDB-Schema-Design-Patterns.md) para prevenir la corrupción de datos y fortalecer la [Seguridad](MongoDB-Security.md) de la aplicación.
