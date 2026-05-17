# Cypher

El lenguaje de programación de Neo4j.
## Creación e Inserción
### CREATE
El comando de `CREATE` se utiliza tanto para crear nodos como relaciones de maneras distintas.
Este comando no entiende de duplicados, por lo que si insertas la misma información dos veces no le importará.

Sintaxis: `CREATE` + _lo que vamos a crear_
#### Nodos
Los nodos se crean de la siguiente manera:

`CREATE (flag:type { property: info, … })`
Se descompone de la siguiente manera:
- **flag:type**: 
	- **flag**: el nombre temporal que le damos en el entorno de esa ejecución. **¡OJO!** puede estar vacía.
	- **type**: el tipo de nodo _Ej.: ":Persona"_
- **{  property: info, …}**: Define las propiedades.
	- **property**: el nombre de la propiedad _Ej.: nombre_
	- **info**: el valor de esa propiedad
#### Relaciones
En cuanto a relaciones tenemos una sintaxis parecida.

`CREATE (flag1:type_node) -[flag2:type]-> (flag3:type_node)`
Se descompone en 2 partes esenciales:
- Los nodos `(flag:type_node)` que siguen el formato anteriormente visto.
- La relación `-[flag:type]->` que al igual que antes el flag y el tipo funcionan exactamente igual, el flag puede ser vacío. Y tiene ese formato de `-[]->` ("flecha con caja").
_Ej.:_ `CREATE (a:Persona) -[r:AMIGO_DE]-> (b:Persona)`

Sin contexto se ve mal, pero mira este trozo de código:

```cypher
MATCH (a:Persona {nombre: "Carlos"})
MATCH (b:Persona {nombre: "Luis"})
CREATE (a)-[:AMIGO_DE]->(b)
```

Aquí se entiende perfectamente la intención de que Carlos sea amigo de Luis.
### MERGE
Merge viene a solucionar el problema que dijimos antes de: _Este comando no entiende de duplicados, por lo que si insertas la misma información dos veces no le importará_ en la sección de [[#CREATE|CREATE]].

¿Por qué? Pues porque MERGE nos permite **editar** un nodo ya existente, y si _no existe_, **lo crea**.

```cypher
CREATE (a:Persona {nombre: "Alex"})
```

```cypher
MERGE (a:Persona {nombre: "Alex"})
SET a.edad = 29
RETURN a
```

De esta manera hemos editado el nodo sin duplicarlo.
_Si no hubieramos corrido el CREATE primero, hubieramos creado el nodo con el MERGE_

> [!NOTE] Esto también es aplicable a las relaciones. Utilizaremos MERGE para no repetirlas.
## Consultas básicas
### MATCH
Consulta que nos permite seleccionar de la base de datos los nodos que tengan las características que le pedimos.
```cypher
MATCH (a: Persona {nombre: "Alex"})
```
### RETURN
Método para devolver los datos calculados.
```cypher
RETURN a
```
## Control de consultas
### DISTINCT
Este comando se utiliza para limpiar los resultados y evitar duplicados. Si un mismo nodo o valor se repite a través de distintos caminos en el grafo, DISTINCT asegura que solo aparezca una vez.

```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad)
RETURN DISTINCT c.nombre
```

De esta manera, aunque haya 100 personas viviendo en "Madrid", la ciudad solo aparecerá una vez en el resultado.
### ORDER BY
Nos permite ordenar los resultados calculados antes de devolverlos. Es excelente para hacer rankings o ver qué nodos tienen más conexiones.

```cypher
MATCH (p:Persona) 
RETURN p.nombre 
ORDER BY p.nombre
```

_Si quieres que sea descendente, solo tienes que añadir_ `DESC` _al final._
### GROUP BY
**¡OJO!** En Cypher **no se escribe** **GROUP BY** explícitamente como haríamos en SQL.

En Neo4j la agrupación es **implícita**. Cuando en tu `RETURN` combinas una propiedad (como el nombre) con una función de agregación (como `count()`), el sistema automáticamente agrupa por esa propiedad.

```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) 
RETURN e.nombre, count(p)
```

Aquí el sistema agrupará por el nombre de la empresa y contará cuántas personas apuntan a ese nodo.
### LIMIT
Como su nombre indica, corta y limita la cantidad de resultados que nos devuelve la consulta. En bases de datos de grafos grandes, no poner límites puede generar resultados enormes. Es ideal si lo combinamos con `ORDER BY` para sacar, por ejemplo, un "Top 3".

```cypher
MATCH (p:Persona) 
RETURN p.nombre 
LIMIT 3
```
## Clausulas Avanzadas
### WITH
`WITH` actúa como un **paso intermedio** en tu consulta. Te permite transformar datos, agruparlos o contarlos, y pasar ese resultado a la siguiente etapa de tu código para seguir trabajando o filtrando.

```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)
WITH p, count(a) as total_amigos
WHERE total_amigos >= 2
RETURN p.nombre, total_amigos
```

En este ejemplo, primero contamos los amigos, usamos `WITH` para pasar ese número y la persona a la siguiente etapa, y luego filtramos solo los que tengan 2 o más.

> [!IMPORTANT] 
> Solo las variables que declares explícitamente en el `WITH` sobreviven para el resto de la consulta. Si olvidas incluir una variable que necesitas después, el código fallará.
### Optional Match
Equivale a un `LEFT JOIN` de SQL. Sirve para incluir información que _podría_ estar ahí, pero que si no está, no queremos que nos rompa la consulta general.

Si el patrón se cumple, devuelve los datos. **Si no lo encuentra, devuelve** **null** en lugar de omitir al nodo principal.

```cypher
MATCH (p:Persona)
OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr:Proyecto)
RETURN p.nombre, pr.nombre
```

De esta forma garantizamos que la consulta nos devuelva a **todas** las personas. Las que no estén en ningún proyecto simplemente tendrán un `null` en la columna del proyecto, asegurando que no perdemos información valiosa por nodos "huérfanos".

## Recorridos (Paths) y Distancias

En Cypher no necesitamos hacer joins complejos para conectar datos profundos. Podemos recorrer múltiples niveles del grafo de forma nativa describiendo la ruta completa.
### Longitud Variable

Si queremos buscar conexiones indirectas (por ejemplo, amigos de amigos), podemos indicar cuántos saltos queremos dar usando `*min..max` dentro de la relación.

```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona)
RETURN p
```

Esto buscará caminos que tengan entre 1 y 3 saltos.

> [!WARNING] Cuidado con la explosión combinatoria
> Los grafos crecen muy rápido en profundidad. No poner límites en los saltos puede devolver una cantidad masiva de resultados y ralentizar la consulta.

### Medir la Distancia

Cuando guardas todo el recorrido en una variable de ruta (como la `p` en el ejemplo anterior), puedes utilizar funciones sobre ella. Por ejemplo, `length()` te dirá a cuántos saltos exactos está un nodo de otro.

```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) 
RETURN length(p)
```

## Dirección de las Relaciones

A diferencia de SQL, en Neo4j las relaciones son entidades con una dirección y un significado. Puedes jugar con la sintaxis de las flechas para buscar en distintos sentidos:

- `->` : **Dirección estricta.** Busca exactamente en el sentido en que se creó la relación.
- `<-` : **Dirección inversa.** Busca en el sentido contrario.
- `-` : **Ignora la dirección.** Útil para relaciones que conceptualmente son simétricas o bidireccionales.

```cypher
MATCH (a:Persona)-[:AMIGO_DE]-(b:Persona)
RETURN a.nombre, b.nombre
```

## Propiedades en las Relaciones

Las relaciones no son solo enlaces, son entidades de primer nivel que pueden contener sus propias propiedades (como la intensidad de una relación o la fecha de inicio).

> [!WARNING] Error típico
> Intentar filtrar por la propiedad de una relación sin haberle asignado un alias (flag). Esto hará que la consulta falle.

```cypher
// CORRECTO: Usamos 'r' para capturar la relación
MATCH (a:Persona)-[r:AMIGO_DE]->(b:Persona)
WHERE r.intensidad > 5
RETURN a.nombre, b.nombre
```

## Errores Comunes de Sintaxis

### Propiedad vs Variable

Un error muy frecuente al usar el `RETURN` es intentar devolver directamente el nombre de una propiedad sin hacer referencia al nodo.

```cypher
// INCORRECTO (Falla porque 'nombre' no es una variable)
MATCH (p:Persona) RETURN nombre 

// CORRECTO
MATCH (p:Persona) RETURN p.nombre
```

### Productos Cartesianos (Nodos sin relaciones)

Si separas dos patrones en un `MATCH` mediante una coma pero no describes la relación entre ellos, Cypher mezclará "todos con todos", generando combinaciones sin sentido. En los grafos, la relación es lo que da sentido a los datos.

```cypher
// INCORRECTO: Mezcla todas las personas con todas las empresas
MATCH (a:Persona), (b:Empresa) RETURN a, b

// CORRECTO: Los cruza usando un patrón de relación
MATCH (a:Persona)-[:TRABAJA_EN]->(b:Empresa) RETURN a, b
```

## Errores Comunes de Modelado (Anti-patrones)

A la hora de diseñar un grafo, es muy común caer en dos extremos que rompen la utilidad del modelo:

- **Error 1: Meter todo como propiedades:** Consiste en guardar datos que podrían ser entidades (como un "Proyecto") como simples atributos dentro de un nodo de Persona. El problema es que esto te devuelve a una base de datos plana: pierdes la capacidad de conectar entidades, no puedes recorrer el grafo y no puedes analizar relaciones complejas.
- **Error 2: Convertir todo en nodos:** El extremo opuesto es crear nodos para absolutamente cualquier dato (ej. hacer que la "Edad" o la "Fecha" sean nodos). Esto genera un grafo artificial y saturado, con demasiados nodos que carecen de significado real, dificultando las consultas.
## Refactorización y Calidad del Grafo

Un grafo no es estático; a medida que evoluciona o se analizan los datos, a menudo es necesario refactorizar su estructura para mantenerlo útil.

### Detectar Inconsistencias

El análisis de grafos permite hacer pruebas de calidad del modelo, revelando incoherencias en los datos. Por ejemplo, se puede detectar si una persona, a través de la red, está conectada participando en proyectos de empresas distintas a la empresa en la que trabaja directamente. Esto puede revelar inconsistencias en el modelo, o bien realidades del negocio como colaboraciones externas o movilidad laboral.

### Nodos Huérfanos y Relaciones Débiles

Al evaluar la salud del grafo, es importante detectar:

- **Nodos desconectados:** Entidades aisladas que no aportan a la estructura de la red.
- **Relaciones sin propiedades:** Conexiones que carecen de contexto o intensidad y que pueden resultar sospechosas o poco útiles según el dominio.

### Redundancia y Relaciones Derivadas

A veces, se pueden crear "relaciones derivadas" (crear una relación directa basada en un camino más largo) para simplificar consultas futuras. Sin embargo, esto añade duplicación de datos. Hay que analizar si dos caminos equivalentes significan lo mismo semánticamente; si no lo hacen (por ejemplo, participar en un proyecto no siempre implica trabajar en la empresa gestora), ambas estructuras deben conservarse.

### Calidad y Validación de Caminos (Paths)

Cuando analizamos recorridos, debemos tener en cuenta que un path puede existir en la base de datos, pero no ser relevante para el análisis.

### Cantidad vs. Calidad en los Caminos

No todos los caminos valen lo mismo. El análisis puede verse enturbiado por cientos de caminos débiles o irrelevantes. Es vital aplicar filtros que prioricen la calidad (relaciones "fuertes" o cortas) sobre la simple existencia de una ruta.

### Evitar Ciclos en el Recorrido

Un problema común al consultar es que el algoritmo pase varias veces por el mismo nodo creando bucles infinitos o redundantes. Es necesario definir rutas que eviten repetir nodos en el camino, garantizando así recorridos lógicos y limpios.
# **Referencias**
[Bases-De-Datos-2/Clases/Parcial2/3-Neo4J/2-cypher-basico at main · JavierLianoRioz/Bases-De-Datos-2 · GitHub](https://github.com/JavierLianoRioz/Bases-De-Datos-2/tree/main/Clases/Parcial2/3-Neo4J/2-cypher-basico)
[Cypher (query language) - Wikipedia](https://en.wikipedia.org/wiki/Cypher_(query_language)?useskin=vector)
[Neo4j - Wikipedia, la enciclopedia libre](https://es.wikipedia.org/wiki/Neo4j)