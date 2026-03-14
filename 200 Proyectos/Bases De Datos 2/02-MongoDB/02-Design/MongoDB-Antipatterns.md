# Antipatrones Comunes en Diseño Documental

Entender los errores evita rediseños costosos. Estos son los antipatrones más frecuentes en MongoDB.

### 1. Sobre-normalización
Intentar replicar el modelo relacional: demasiadas colecciones pequeñas con dependencia constante de `$lookup`.
*   **Consecuencia:** Aumento de latencia, mayor consumo de CPU, complejidad innecesaria.

> [!WARNING]
> MongoDB no fue optimizado para joins intensivos como un RDBMS. Si cada consulta requiere 3 `$lookup`, el diseño probablemente es incorrecto.

### 2. Documentos sin Control de Crecimiento
Arrays que crecen sin límite dentro de un documento:
```javascript
{
  usuario: "Carlos",
  logs: [ ... 50000 registros ... ]
}
```
*   **Problemas:** Reubicación en disco, fragmentación, riesgo de alcanzar el límite de **16MB**, actualizaciones cada vez más costosas.
*   **Soluciones:** Bucket pattern, colección separada, TTL, particionamiento lógico.

### 3. Índices Innecesarios
Crear índices "por si acaso" en todos los campos tiene un costo real:
*   Cada `insert` actualiza **todos** los índices.
*   Escrituras más lentas, mayor uso de RAM y disco.
*   Rebalanceo más frecuente en sharding.

> [!IMPORTANT]
> Cada índice debe justificarse por una consulta real medida con `explain()`.

### 4. Uso Incorrecto de Shard Key
Elegir un campo monotónico como `{ fecha: 1 }` genera *hotspots* y baja escalabilidad real. Este error puede obligar a migraciones complejas.

### 5. Optimizar sin Medir
*   Agregar índices sin medir rendimiento previo.
*   Activar sharding sin análisis de carga.
*   **Optimización sin métricas es especulación.**

Para evitar estos problemas, es vital aplicar [Patrones de Modelado](MongoDB-Advanced-Modeling.md) adecuados y realizar un [Análisis de Rendimiento](../03-Performance/MongoDB-Indexes.md#análisis-de-rendimiento) constante de la aplicación.
