---
materia: Bases de Datos 2
---

# Cypher: Lenguaje de Consulta de Grafos

Cypher es un lenguaje declarativo basado en la **correspondencia de patrones** (*pattern matching*). Su sintaxis ASCII-art visualiza los nodos `()` y las relaciones `[]` para describir recorridos de forma intuitiva pero técnicamente rigurosa.

---

## 1. Mutación de la Red

### Creación e Integridad (`CREATE` vs `MERGE`)
- **`CREATE`**: Inserta nuevos elementos sin verificar preexistencia. Riesgo de duplicidad.
- **`MERGE`**: Operación atómica de "Buscar o Crear". Garantiza la unicidad de nodos y relaciones.

```cypher
// Crea o actualiza la relación entre nodos existentes
MATCH (a:Persona {nombre: "Carlos"}), (b:Persona {nombre: "Luis"})
MERGE (a)-[r:AMIGO_DE]->(b)
SET r.desde = 2024
```

---

## 2. Consulta y Transformación

### Selección de Patrones (`MATCH`)
Define la estructura que debe localizar el motor.
- **Búsqueda Directa**: `MATCH (p:Persona {ciudad: "Madrid"})`
- **Opcionales (`OPTIONAL MATCH`)**: Equivalente al `LEFT JOIN`. Devuelve `null` si la relación no existe, evitando que el nodo principal desaparezca del resultado.

### Pasos Intermedios (`WITH`)
Actúa como una barrera de flujo. Permite realizar cálculos, filtrar y pasar solo las variables necesarias a la siguiente etapa de la consulta.
- **¡OJO!**: Las variables no declaradas en `WITH` se pierden para el resto de la ejecución.

---

## 3. Análisis de Caminos (*Paths*)

Cypher permite consultar la red en profundidad sin definir joins infinitos.

### Longitud Variable
Busca conexiones indirectas definiendo el rango de saltos:
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona)
RETURN p, length(p) AS distancia
```
- **Riesgo**: Los recorridos sin límite (*n) pueden causar una explosión combinatoria y colapsar la memoria.

---

## 4. Agregación Implícita

En Cypher no existe el `GROUP BY`. La agrupación es automática al combinar propiedades con funciones de agregación (`count`, `sum`, `avg`).

```cypher
MATCH (p:Persona)-[r:TRABAJA_EN]->(e:Empresa)
RETURN e.nombre, count(p) AS total_empleados
```

---

## Errores Críticos de Diseño (Antipatrones)

1.  **Saturación de Propiedades**: Meter como atributo lo que debería ser un nodo. Impide el recorrido del grafo.
2.  **Nodos Huérfanos**: Entidades sin relaciones que no aportan valor estructural.
3.  **Filtro sin Alias**: Intentar usar una propiedad de relación sin haberle asignado una variable (ej. `[r:TIPO]`).

---

## Referencias
1. [[Bases de Grafos]]
2. [[Cypher Avanzado]]
3. Documentación oficial de Neo4j (Cypher Manual).
