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

### ### DELTA: Modularidad y Paralelismo en Neo4j 5.x

#### 1. Subconsultas Correlacionadas (`CALL { ... }`)
Permite anidar lógica de consulta donde cada fila del flujo principal dispara una subconsulta independiente. Es la base de la programación funcional en Cypher.
```cypher
MATCH (p:Persona)
CALL {
  WITH p
  MATCH (p)-[:TRABAJA_EN]->(e:Empresa)
  RETURN e.nombre AS empresa
  LIMIT 1
}
RETURN p.nombre, empresa
```

#### 2. Gestión de Escritura Masiva (`CALL ... IN TRANSACTIONS`)
Mecanismo de *batching* nativo para procesar millones de cambios (ej. cargas de CSV o refactorizaciones de nodos) sin saturar la memoria RAM.
```cypher
LOAD CSV FROM 'file:///datos.csv' AS row
CALL {
  CREATE (:Nodo {id: row[0]})
} IN TRANSACTIONS OF 1000 ROWS
```

#### 3. Ejecución Paralela (`CALL ... IN CONCURRENT TRANSACTIONS`)
Permite aprovechar todos los núcleos de la CPU ejecutando subconsultas en paralelo, reduciendo drásticamente el tiempo de ejecución en tareas de escritura pesada.

---

## Reducciones sobre Colecciones: `reduce()`

La función `reduce()` es un "destilador". Toma una lista con muchos valores y los procesa uno a uno para obtener un **único resultado final**. Es el equivalente funcional al `fold` o a un bucle `for` con un acumulador externo.

### Anatomía del acumulador
**Sintaxis:** `reduce(acumulador = valor_inicial, variable IN lista | expresion_de_actualizacion)`

1.  **`acumulador`**: La "caja" donde guardas el resultado parcial. Debes darle un nombre y un valor inicial (ej. `0` para sumas, `""` para textos).
2.  **`variable IN lista`**: Define cómo vas a llamar a cada elemento mientras recorres la lista.
3.  **`| expresion`**: La operación matemática o lógica que actualiza la "caja" en cada paso.

### Ejemplo visual: Sumar pesos de un Path
Si tenemos un camino con distancias `[10, 5, 20]`:

```cypher
MATCH p=(a:Ciudad)-[:RUTA*]->(b:Ciudad)
RETURN reduce(total = 0, r IN relationships(p) | total + r.km) AS km_totales
```

**Paso a paso interno:**
- **Inicio:** `total = 0`.
- **Vuelta 1:** `total = 0 + 10` → La caja ahora vale `10`.
- **Vuelta 2:** `total = 10 + 5` → La caja ahora vale `15`.
- **Vuelta 3:** `total = 15 + 20` → La caja ahora vale `35`.
- **Resultado:** `35`.

### Cuándo usarlo vs `sum()`
- Usa `sum()` para valores que están en **filas separadas** (agregación clásica).
- Usa `reduce()` para valores que ya están dentro de una **misma lista o Path** (como los que devuelven `nodes(p)` o `relationships(p)`). Es la única forma de "entrar" en una lista y operar con sus elementos sin usar `UNWIND`.

### Profundizando en `reduce()` (Explicación Extendida)
Para entender `reduce()` de forma más clara, imagínalo como una bola de nieve que va rodando por una colina (la colección). A medida que rueda por cada elemento, la bola (el acumulador) crece o cambia según una regla que tú defines, hasta llegar al final y entregarte el resultado compacto. 

No solo sirve para sumar números. Puedes usarlo para concatenar cadenas de texto o construir estructuras más complejas a partir de un `Path`. Por ejemplo, para construir una ruta separada por flechas:
```cypher
MATCH p=(inicio:Localidad)-[:CONECTA_CON*1..4]->(fin:Localidad)
RETURN reduce(ruta = inicio.nombre, n IN nodes(p)[1..] | ruta + " -> " + n.nombre) AS ruta_completa
```
*Lógica:* Partimos con el nombre del primer nodo. Luego recorremos el resto de nodos (`nodes(p)[1..]`) y, en cada paso, concatenamos al texto acumulado una flecha y el nombre del siguiente nodo.

---

## Más Predicados de Colecciones: `ANY`, `NONE` y `SINGLE`

Al igual que `ALL`, estos predicados nos permiten evaluar condiciones sobre colecciones y paths sin tener que desarmarlos con `UNWIND`.

### `ANY` (Al menos uno)
Devuelve verdadero si **uno o más** elementos de la lista cumplen la condición.
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona)
WHERE ANY(n IN nodes(p) WHERE n.nombre = "Luis")
RETURN p
```
*Uso:* Ideal para encontrar caminos que pasen forzosamente por un nodo específico (un "nodo puente").

### `NONE` (Ninguno)
Devuelve verdadero solo si **ningún** elemento de la lista cumple la condición.
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona)
WHERE NONE(n IN nodes(p) WHERE n.nombre = "Carlos")
RETURN p
```
*Uso:* Útil para excluir rutas donde intervienen actores que queremos evitar (filtrado de exclusión).

### `SINGLE` (Exactamente uno)
Devuelve verdadero si **uno y solo un** elemento cumple la condición. 
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto)
WITH p, collect(pr) as proyectos
WHERE SINGLE(x IN proyectos WHERE x.presupuesto > 100000)
RETURN p.nombre
```

### Prevención de Ciclos con `SINGLE` y `ALL`
Una combinación avanzada de estos predicados nos permite encontrar caminos simples (sin bucles donde un nodo se visite más de una vez).
```cypher
MATCH p=(a:Persona)-[r:AMIGO_DE*1..4]->(b:Persona)
WHERE ALL(n IN nodes(p) WHERE SINGLE(x IN nodes(p) WHERE x = n))
RETURN p
```

### ### DELTA: Modularidad y Paralelismo en Neo4j 5.x

#### 1. Subconsultas Correlacionadas (`CALL { ... }`)
Permite anidar lógica de consulta donde cada fila del flujo principal dispara una subconsulta independiente. Es la base de la programación funcional en Cypher.
```cypher
MATCH (p:Persona)
CALL {
  WITH p
  MATCH (p)-[:TRABAJA_EN]->(e:Empresa)
  RETURN e.nombre AS empresa
  LIMIT 1
}
RETURN p.nombre, empresa
```

#### 2. Gestión de Escritura Masiva (`CALL ... IN TRANSACTIONS`)
Mecanismo de *batching* nativo para procesar millones de cambios (ej. cargas de CSV o refactorizaciones de nodos) sin saturar la memoria RAM.
```cypher
LOAD CSV FROM 'file:///datos.csv' AS row
CALL {
  CREATE (:Nodo {id: row[0]})
} IN TRANSACTIONS OF 1000 ROWS
```

#### 3. Ejecución Paralela (`CALL ... IN CONCURRENT TRANSACTIONS`)
Permite aprovechar todos los núcleos de la CPU ejecutando subconsultas en paralelo, reduciendo drásticamente el tiempo de ejecución en tareas de escritura pesada.