---
materia: Bases de Datos 2
---

# Cypher: Guía de Ejecución Avanzada

Manual técnico enfocado en la descomposición jerárquica de consultas de grafos, patrones de análisis de red y optimización en Neo4j.

---

## 1. Consultas de Caminos y Filtrado Colectivo

Permite validar condiciones sobre la totalidad de un trayecto (**Path**) sin desestructurarlo.

```cypher
// SINTAXIS: MATCH <camino> WHERE <predicado>(<variable> IN <coleccion> WHERE <condicion>) RETURN <camino>
// CAMINO:    p=(n:Etiqueta)-[:RELACION*1..N]->(m:Etiqueta)
// PREDICADO: ALL (Todos), ANY (Al menos uno), NONE (Ninguno), SINGLE (Exactamente uno)
// COLECCION: nodes(p) (Nodos del camino) o relationships(p) (Relaciones del camino)

// Ejemplo: Rutas de influencia donde TODAS las relaciones son posteriores a 2020
MATCH p=(u:Usuario)-[:SIGUE*1..5]->(influencer:Usuario)
WHERE ALL(r IN relationships(p) WHERE r.desde > 2020)
RETURN p
```

---

## 2. Segmentación y Manipulación de Paths

Uso de funciones de extracción y rangos para analizar partes específicas de una ruta.

```cypher
// SINTAXIS: RETURN <coleccion>[<inicio>..<fin>]
// NODOS:    nodes(p) -> Devuelve lista de nodos
// RANGO:    [1..-1]  -> Salta el primero (0) y excluye el último (-1)

// Ejemplo: Extraer solo los nodos intermedios de un viaje (saltando origen y destino)
MATCH p=(inicio:Ciudad)-[:VIAJE*3..]->(fin:Ciudad)
RETURN nodes(p)[1..-1] AS paradas_intermedias
```

---

## 3. Encadenamiento Analítico (`WITH`)

El comando `WITH` actúa como una barrera de procesamiento que permite realizar cálculos intermedios antes de seguir con la consulta.

```cypher
// SINTAXIS: MATCH <A> WITH <variables>, <agregacion> AS <alias> MATCH <B> RETURN <alias>
// AGREGACION: count(n), collect(n), sum(n.valor), avg(n.valor)
// PROPOSITO:  Pasar resultados de una etapa a otra o filtrar por agregados (WHERE tras WITH)

// Ejemplo: Encontrar personas con más de 2 amigos (Filtro por conteo)
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)
WITH p, count(a) AS total_amigos
WHERE total_amigos > 2
RETURN p.nombre, total_amigos
```

---

## 4. Reducción y Destilación de Listas (`reduce`)

Procesa los elementos de una lista para obtener un único valor escalar (ej. una suma total o una cadena concatenada).

```cypher
// SINTAXIS: reduce(<acumulador> = <inicio>, <var> IN <lista> | <expresion>)
// ACUMULADOR: Variable que guarda el resultado parcial (ej. s = 0)
// LISTA:       relationships(p) o cualquier array
// EXPRESION:   Operación de actualización (ej. s + var.propiedad)

// Ejemplo: Sumar el kilometraje total de todas las relaciones en un camino
MATCH p=(a:Ciudad)-[:RUTA*]->(b:Ciudad)
RETURN reduce(km_total = 0, r IN relationships(p) | km_total + r.km) AS distancia_total
```

---

## 5. Patrones de Alta Fidelidad (Análisis de Red)

| Operación | Descomposición Estructural (SINTAXIS) |
| :--- | :--- |
| **Nodos Obligatorios** | `MATCH p=(a)-[*]->(b) WITH collect(p) AS ps UNWIND ps AS p UNWIND nodes(p) AS n WITH n, count(n) AS c WHERE c = size(ps) ...` |
| **Identidad Estructural** | `MATCH (n)-[:R]->(t) WITH n, collect(id(t)) AS profile ORDER BY id(t) WITH profile, collect(n) AS clones WHERE size(clones) > 1 ...` |
| **Desduplicación O(1)** | `MATCH (a), (b) WHERE id(a) < id(b) AND (a)-[:R]-(b) ...` |

---

## 6. Modularidad en Neo4j 5.x

### Subconsultas Correlacionadas
```cypher
// SINTAXIS: MATCH <externo> CALL { WITH <externo> MATCH <interno> RETURN <valor> } RETURN <externo>, <valor>
```

### Gestión de Escritura Masiva
```cypher
// SINTAXIS: LOAD CSV ... CALL { <operacion_escritura> } IN TRANSACTIONS OF <N> ROWS
```

---

## Referencias Prácticas
- [[Bases de Grafos]]
- [[Bases de datos 2]]
