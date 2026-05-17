## Teoría

Las bases de datos de grafos no están diseñadas solo para guardar información y recuperarla bajo ciertas condiciones (como SQL o NoSQL). Están pensadas para representar conexiones de forma directa y natural .
### El Cambio de Paradigma: Relacional vs Grafos
En un modelo relacional, las bases de datos resuelven las conexiones usando joins. El problema es que a medida que aumenta la profundidad de las relaciones (ej. buscar los amigos de los amigos de los amigos), las consultas crecen drásticamente en complejidad y el sistema se vuelve ineficiente.

En los grafos ocurre un cambio fundamental:

- **Las relaciones son entidades de primer nivel**: Tienen dirección, significado y sus propias propiedades.
- **No filtras registros, recorres conexiones**: En lugar de hacer preguntas como "dame los usuarios con X condición", en grafos haces preguntas como "¿qué caminos existen entre estas dos entidades?" o "¿a qué nodos puedo llegar desde aquí?".

### Modelado de Grafos (Diseño)
El diseño de un grafo consiste en decidir qué representa cada entidad, qué relaciones existen y qué va en nodos vs qué va en relaciones.

La regla de oro del modelado es: **Modelas para consultar, no para almacenar**. No existe un único modelo correcto, todo depende de las preguntas de negocio que quieras responder.

#### ¿Nodos o Propiedades?
A veces surge la duda de si algo debe ser una propiedad o un nodo separado. Por ejemplo, al conectar Personas con Empresas y Proyectos.

- Si solo te importa saber en qué proyecto participa alguien de forma informativa, podría ser una propiedad en la relación.
- Si necesitas conectar a varias personas de distintas empresas al mismo proyecto y medir el impacto de ese proyecto, el proyecto debe extraerse como un nodo intermedio. Esto añade complejidad, pero da mucha más flexibilidad al modelo.

#### Refactorización e Inconsistencias
Un grafo no es estático. Con el tiempo y a medida que cambian las necesidades de la aplicación, es habitual encontrar nodos desconectados ("huérfanos") o redundancias que fuerzan a refactorizar el modelo. Por ejemplo:
- **Inconsistencias lógicas**: Si alguien participa en un proyecto asociado a una empresa pero el sistema indica que no tiene relación formal de trabajar en dicha empresa, el modelo enriquece el descubrimiento permitiendo revelar, mediante cruces (queries), esta disonancia o colaboración "en la sombra".
- **Relaciones Derivadas**: A veces se opta por añadir nuevos "atajos" en el modelo (ej. conectar a dos personas que trabajan en la misma empresa con `ES_COLEGA_DE`) para que las consultas concurrentes sean mucho más veloces, a expensas de tolerar un ligero nivel intencionado de redundancia estructural.
### Análisis de Redes y Descubrimiento
Un grafo no solo responde preguntas, permite descubrir cosas ocultas y analizar estructuras. Cuando las consultas devuelven Paths (Caminos), dejan de ser simples datos y se convierten en información de red.

#### Centralidad
Podemos medir la importancia de una entidad observando sus conexiones. Contar cuántas relaciones tiene cada nodo permite identificar a personas muy sociales, hubs geográficos, o entidades con gran influencia en la red.

#### Nodos Puente (Intermediarios)
Más allá de tener muchas conexiones, hay nodos clave porque aparecen mucho en medio de los recorridos (paths). Estos "nodos puente" actúan como intermediarios críticos; si los eliminas, distintas partes del grafo podrían quedar desconectadas.

#### Significado de la Distancia y Múltiples Caminos
La distancia entre entidades es información vital:

- **Distancia**: Una distancia corta implica una relación cercana o fuerte. Una distancia larga implica una conexión débil o indirecta.
- **Múltiples caminos**: Que existan múltiples rutas (paths) entre dos mismos nodos significa que hay redundancia en las conexiones. Esto aumenta la probabilidad de interacción y hace que la red sea más resiliente, ya que no dependen de un solo enlace

#### Interpretación Extendida de Redes
Añadido a la centralidad y los nodos puente, el análisis topológico del grafo nos permite descubrir:
- **Hubs Geográficos**: Al contar los recorridos que terminan en ciertas ciudades, podemos medir la intensidad de su presencia en la red y detectar zonas geográficas que actúan como grandes puntos de concentración o actividad.
- **Conexiones Ocultas entre Organizaciones**: Evaluando los "caminos fuertes" que cruzan a través de empleados o proyectos de distintas empresas, el grafo puede revelar colaboraciones indirectas, relaciones no oficiales u organizaciones que están operando juntas sin tener un vínculo directo registrad.
### ¿Cómo funciona?
En vez de hablar de **tablas**, hablamos de **entidades**.

Un grafo está compuesto por [[nodo|nodos]], [[relacion|relaciones]] y [[propiedad|propiedades]].
### ¿Qué casos de uso tienen?
Algunos ejemplos reales son:
- relaciones entre nodos como núcleo del programa (redes sociales)
- sistemas de conexiones indirectas (sistemas de recomendación)
- para búsqueda de patrones ocultos (detección de fraude)
- búsqueda de caminos óptimos (sistema de enrutamiento)
- relaciones de conceptos (grafos de conocimiento)
### Adicionalmente: ¿Cómo se usa?
Tenemos este setup que nos enseña como instalarlo: [Bases-De-Datos-2/Clases/Parcial2/3-Neo4J/1-teoria/5-neo4J.md at main · JavierLianoRioz/Bases-De-Datos-2 · GitHub](https://github.com/JavierLianoRioz/Bases-De-Datos-2/blob/main/Clases/Parcial2/3-Neo4J/1-teoria/5-neo4J.md) 

## Práctica

Nosotros lo que utilizaremos será Neo4j que utiliza como motor de código: [[Cypher]].