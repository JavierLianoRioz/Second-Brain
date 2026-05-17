# Cypher Avanzado

Este módulo cubre técnicas de manipulación de datos y optimización para resolver problemas complejos de grafos que van más allá de las consultas básicas.

## Predicados de Colecciones: `ALL`

El predicado `ALL` se utiliza para validar que **cada uno** de los elementos de una lista cumpla una condición específica. Internamente, Cypher utiliza un iterador que recorre la colección y detiene la evaluación (short-circuit) en cuanto encuentra el primer elemento que no cumple la condición.

### Por qué usarlo
Es vital cuando trabajamos con caminos (`Paths`) y necesitamos asegurar la calidad de **todas** las relaciones que lo componen, no solo de algunas.

```cypher
MATCH p=(u:Usuario)-[:SIGUE*1..5]->(influencer:Usuario)
WHERE ALL(r IN relationships(p) WHERE r.desde > 2020)
RETURN p
```
*Lógica:* Estamos filtrando rutas de influencia donde **todas** las conexiones se hayan entablado después del año 2020. Si una sola relación es de 2019, el camino entero se descarta.

---

## Manipulación Analítica de Paths

Un `Path` (p) no es un string ni un objeto plano; es una estructura compleja en memoria que contiene una secuencia alternada de nodos y relaciones.

### Extracción y Segmentación: `nodes()` y `relationships()`
Podemos descomponer el camino para analizar sus partes individualmente.

- `nodes(p)`: Devuelve una lista con todos los nodos del camino.
- `relationships(p)`: Devuelve una lista con todas las relaciones.

### Slicing de Arrays (Sintaxis de Rangos)
Podemos usar la sintaxis `[inicio..fin]` para ignorar partes del camino. Esto es extremadamente útil para analizar nodos intermedios.

```cypher
MATCH p=(inicio:Ciudad)-[:VIAJE*3..]->(fin:Ciudad)
// Extraemos solo los nodos intermedios (ignorando el primero y el último)
RETURN nodes(p)[1..-1] AS paradas_intermedias
```
*Nota:* El índice `1` salta el primer nodo, y `-1` indica el final de la lista de forma relativa, excluyendo el último nodo.

---

## Optimización y Desduplicación con `id()`

En consultas donde buscamos pares de nodos relacionados, es común que el motor nos devuelva el mismo par dos veces pero en orden inverso (espejo), como `(A, B)` y `(B, A)`.

### El truco del identificador interno
Cada nodo en Neo4j tiene un ID único interno accesible mediante `id(n)`. Comparar estos IDs es una operación de coste **O(1)** (acceso directo a memoria), lo que la hace mucho más eficiente que comparar strings de nombres o propiedades.

```cypher
MATCH (p1:Persona)-[:TRABAJA_EN]->(e:Empresa)<-[:TRABAJA_EN]-(p2:Persona)
WHERE id(p1) < id(p2)
RETURN p1.nombre, p2.nombre
```
*Lógica:* Al forzar que el ID de `p1` sea menor al de `p2`, garantizamos que cada pareja de compañeros de trabajo aparezca **exactamente una vez** en los resultados, eliminando permutaciones innecesarias.

---

## División Relacional y Coincidencias Totales

Este es uno de los problemas más difíciles en NoSQL: encontrar entidades que cumplan **todas** las relaciones de un conjunto (equivalente al "Double NOT EXISTS" de SQL).

### El Patrón de Doble Conteo con `WITH`
Para resolver esto, comparamos el tamaño de un conjunto de requisitos contra el tamaño de las coincidencias reales.

```cypher
// 1. Buscamos todas las empresas tecnológicas
MATCH (e:Empresa {tipo: "Tech"})
WITH count(e) AS total_empresas_tech, collect(e) AS empresas_tech

// 2. Buscamos personas que trabajan en esas empresas
MATCH (p:Persona)-[:TRABAJA_EN]->(target:Empresa)
WHERE target IN empresas_tech

// 3. Agrupamos por persona y contamos en cuántas de esas empresas está
WITH p, count(target) AS empresas_del_usuario, total_empresas_tech
WHERE empresas_del_usuario = total_empresas_tech
RETURN p.nombre
```

---

## Manipulación de Listas y Colecciones

Cypher permite trabajar con arrays de forma muy flexible mediante funciones específicas y cláusulas de expansión.

### 1. `collect()`: Agrupar en una lista
Transforma múltiples filas en una única lista. Es el paso previo habitual para realizar cálculos sobre conjuntos de datos.

```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia)
RETURN p.nombre, collect(t.nombre) AS lista_techs
```

### 2. `size()`: Contar elementos
Devuelve la cantidad de elementos que tiene una lista.

```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)
WITH p, collect(a) AS amigos
WHERE size(amigos) > 2
RETURN p.nombre, size(amigos)
```

### 3. `UNWIND`: Expandir una lista a filas
Es la operación inversa a `collect()`. Toma una lista y la descompone, creando una fila nueva por cada elemento. Es vital para procesar resultados de funciones como `nodes(p)`.

```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*]->(b:Persona)
UNWIND nodes(p) AS n
RETURN DISTINCT n.nombre
```
*Lógica:* Extraemos todos los nodos de un camino y usamos `UNWIND` para poder tratarlos como filas individuales y aplicarles un `DISTINCT`.

---

## Reducciones sobre Colecciones: `reduce()`

La función `reduce()` permite transformar una lista de valores en un único resultado escalar (un número, un booleano o un string) aplicando una operación acumulativa.

**Sintaxis:** `reduce(acumulador = valor_inicial, variable IN lista | expresion)`

### Ejemplo: Cálculo de "Peso Total" de un camino
Imagina que cada relación tiene una propiedad `distancia` y queremos sumar el total del recorrido.

```cypher
MATCH p=(a:Ciudad)-[:RUTA*]->(b:Ciudad)
RETURN reduce(total_km = 0, r IN relationships(p) | total_km + r.distancia) AS distancia_total
```
*Paso a paso:*
1. `total_km` empieza en 0.
2. Para cada relación `r` en el camino, toma el valor actual de `total_km` y le suma `r.distancia`.
3. El resultado final es la suma acumulada de todo el trayecto.