# Índices Compuestos

Un índice compuesto (o multinivel) es un índice que se construye sobre dos o más columnas de una misma tabla.

## Regla de Izquierda a Derecha

MySQL recorre los índices compuestos estrictamente de izquierda a derecha. Para que un índice sea efectivo:
1. Las columnas buscadas con `=` deben aparecer primero.
2. El índice se puede usar hasta que se encuentra una columna con una condición de **rango** (`> < BETWEEN LIKE 'x%'`).
3. Después de un rango, las columnas posteriores del índice ya no pueden usarse para filtrar ni para ordenar.

## El Caso Ideal (Perfect Match)
Para una consulta con:
- Filtros exactos (`=`) en varias columnas.
- Un filtro de rango o un `ORDER BY` al final.

**Ejemplo**:
```sql
INDEX (pais, tipo_usuario, fecha_pedido)
```
Funciona perfectamente para:
```sql
WHERE pais = 'ES' AND tipo_usuario = 'Premium' ORDER BY fecha_pedido DESC
```

## Errores Comunes
- **Saltarse el primer campo**: Si el índice empieza por `pais` y buscas solo por `tipo_usuario`, el índice es "invisible" para el optimizador.
- **Rango prematuro**: Poner una columna de rango al principio del índice inhabilita el resto de las columnas para filtrado eficiente.

---
- **Relacionado**: [Query Optimization](Query_Optimization.md), [[03_SQL/Constraints_SQL]]
