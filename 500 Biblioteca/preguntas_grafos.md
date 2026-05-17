# Banco de Ejercicios: Neo4j Cypher

* **Descripcion:** Banco de 100 ejercicios Neo4j Cypher (unificado)
* **Nota:** Pegar aquí los bloques 1–100 generados previamente

---

## Ejercicio 1 (Facil)
**Tipo:** `write_query`

**Enunciado:** Obtén todas las personas que trabajan en alguna empresa y muestra el nombre de la persona y de la empresa.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN p.nombre, e.nombre
```

**Validación:**
- Tipo: `resultado`
- Expected: `[['Ana', 'TechCorp'], ['Luis', 'TechCorp'], ['Marta', 'DataSoft'], ['Carlos', 'DataSoft']]`
- Wildcard: `True`

---

## Ejercicio 2 (Facil)
**Tipo:** `write_query`

**Enunciado:** Lista todas las personas que viven en Madrid.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad {nombre:'Madrid'}) RETURN p.nombre
```

**Validación:**
- Tipo: `resultado`
- Expected: `['Ana', 'Luis', 'Elena']`
- Wildcard: `True`

---

## Ejercicio 3 (Facil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para devolver correctamente nombres de personas.

**Query Base:**
```cypher
MATCH (p:Persona) RETURN nombre
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['MATCH', 'RETURN']`
- Wildcard: `True`

---

## Ejercicio 4 (Facil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para limitar a 2 resultados.

**Query Base:**
```cypher
MATCH (p:Persona) RETURN p.nombre
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) RETURN p.nombre LIMIT 2
```

**Validación:**
- Tipo: `estructura`
- Expected: `['LIMIT']`
- Wildcard: `True`

---

## Ejercicio 5 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén las empresas junto con el número de empleados.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p)
```

**Validación:**
- Tipo: `resultado`
- Expected: `[['TechCorp', 2], ['DataSoft', 2]]`
- Wildcard: `True`

---

## Ejercicio 6 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que participan en proyectos y trabajan en empresa.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa), (p)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre
```

**Validación:**
- Tipo: `resultado`
- Expected: `['Ana', 'Luis', 'Marta']`
- Wildcard: `True`

---

## Ejercicio 7 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar WHERE correctamente.

**Query Base:**
```cypher
MATCH (p:Persona) WHERE nombre='Ana' RETURN p
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) WHERE p.nombre='Ana' RETURN p
```

**Validación:**
- Tipo: `estructura`
- Expected: `['WHERE']`
- Wildcard: `True`

---

## Ejercicio 8 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para ordenar por nombre.

**Query Base:**
```cypher
MATCH (p:Persona) RETURN p.nombre
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) RETURN p.nombre ORDER BY p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['ORDER BY']`
- Wildcard: `True`

---

## Ejercicio 9 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas con al menos 2 amigos.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) WITH p, count(a) as amigos WHERE amigos >= 2 RETURN p.nombre, amigos
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 10 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra caminos de longitud hasta 2 entre personas.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..2]->(b:Persona) RETURN p
```

**Validación:**
- Tipo: `estructura`
- Expected: `['*1..2']`
- Wildcard: `True`

---

## Ejercicio 11 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas conectadas a proyectos a través de amigos.

### SOLUCIÓN

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE]->(b:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN a.nombre, pr.nombre
```

**Validación:**
- Tipo: `resultado`
- Expected: `[['Ana', 'Apollo'], ['Luis', 'Zeus']]`
- Wildcard: `True`

---

## Ejercicio 12 (Dificil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar length correctamente.

**Query Base:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) RETURN length
```

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) RETURN length(p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['length']`
- Wildcard: `True`

---

## Ejercicio 13 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo la longitud del path.

**Query Base:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN p
```

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN length(p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['length']`
- Wildcard: `True`

---

## Ejercicio 14 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que no participan en proyectos.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr) WHERE pr IS NULL RETURN p.nombre
```

**Validación:**
- Tipo: `resultado`
- Expected: `['Carlos', 'Elena']`
- Wildcard: `True`

---

## Ejercicio 15 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que actúan como puente en relaciones de amistad.

### SOLUCIÓN

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE]->(b:Persona)-[:AMIGO_DE]->(c:Persona) RETURN b, count(*)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 16 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén todas las personas junto con la ciudad en la que viven.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN p.nombre, c.nombre
```

**Validación:**
- Tipo: `resultado`
- Expected: `[['Ana', 'Madrid'], ['Luis', 'Madrid'], ['Elena', 'Madrid'], ['Marta', 'Barcelona'], ['Carlos', 'Barcelona']]`
- Wildcard: `True`

---

## Ejercicio 17 (Medio)
**Tipo:** `write_query`

**Enunciado:** Cuenta cuántas personas viven en cada ciudad.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre, count(p)
```

**Validación:**
- Tipo: `resultado`
- Expected: `[['Madrid', 3], ['Barcelona', 2]]`
- Wildcard: `True`

---

## Ejercicio 18 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo las ciudades con más de 2 personas.

**Query Base:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre, count(p)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) WITH c, count(p) as total WHERE total > 2 RETURN c.nombre, total
```

**Validación:**
- Tipo: `estructura`
- Expected: `['WITH', 'WHERE']`
- Wildcard: `True`

---

## Ejercicio 19 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para que agrupe correctamente.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN p.nombre, count(e)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 20 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número de tecnologías que usan.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN p.nombre, count(t)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 21 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que usan la tecnología Neo4j.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia {nombre:'Neo4j'}) RETURN p.nombre
```

**Validación:**
- Tipo: `resultado`
- Expected: `['Ana', 'Marta']`
- Wildcard: `True`

---

## Ejercicio 22 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan en la misma empresa.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_EN]->(e:Empresa)<-[:TRABAJA_EN]-(p2:Persona) WHERE p1 <> p2 RETURN p1.nombre, p2.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['<>']`
- Wildcard: `True`

---

## Ejercicio 23 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para evitar duplicados en pares de personas.

**Query Base:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_EN]->(e)<-[:TRABAJA_EN]-(p2:Persona) RETURN p1.nombre, p2.nombre
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_EN]->(e)<-[:TRABAJA_EN]-(p2:Persona) WHERE id(p1) < id(p2) RETURN p1.nombre, p2.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['id']`
- Wildcard: `True`

---

## Ejercicio 24 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén proyectos junto con el total de horas invertidas por personas.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[r:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, sum(r.horas)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['sum']`
- Wildcard: `True`

---

## Ejercicio 25 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar propiedades de relación.

**Query Base:**
```cypher
MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN pr.nombre, sum(horas)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p)-[r:PARTICIPA_EN]->(pr) RETURN pr.nombre, sum(r.horas)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['r.horas']`
- Wildcard: `True`

---

## Ejercicio 26 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas conectadas por cadenas de amistad de hasta longitud 3.

### SOLUCIÓN

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN a.nombre, b.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['*1..3']`
- Wildcard: `True`

---

## Ejercicio 27 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Devuelve los paths de amistad junto con su longitud.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN p, length(p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['length']`
- Wildcard: `True`

---

## Ejercicio 28 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo paths de longitud mayor a 1.

**Query Base:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN p
```

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) WHERE length(p) > 1 RETURN p
```

**Validación:**
- Tipo: `estructura`
- Expected: `['length']`
- Wildcard: `True`

---

## Ejercicio 29 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Obtén los nodos intermedios en paths de amistad.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*2..3]->(b:Persona) RETURN nodes(p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['nodes']`
- Wildcard: `True`

---

## Ejercicio 30 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Obtén las relaciones de un path.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN relationships(p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['relationships']`
- Wildcard: `True`

---

## Ejercicio 31 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con la universidad en la que estudiaron.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:ESTUDIO_EN]->(u:Universidad) RETURN p.nombre, u.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['ESTUDIO_EN']`
- Wildcard: `True`

---

## Ejercicio 32 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra universidades con más de un estudiante.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:ESTUDIO_EN]->(u:Universidad) WITH u, count(p) as total WHERE total > 1 RETURN u.nombre, total
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 33 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar WITH correctamente.

**Query Base:**
```cypher
MATCH (p:Persona) WITH p MATCH (p)-[:VIVE_EN]->(c) RETURN c
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c) RETURN c
```

**Validación:**
- Tipo: `estructura`
- Expected: `['MATCH']`
- Wildcard: `True`

---

## Ejercicio 34 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo ciudades únicas.

**Query Base:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN DISTINCT c.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 35 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan con alguien que usa Neo4j.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia {nombre:'Neo4j'}) RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['TRABAJA_CON']`
- Wildcard: `True`

---

## Ejercicio 36 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que viven en una ciudad distinta a la de sus amigos.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona),(p)-[:VIVE_EN]->(c1),(a)-[:VIVE_EN]->(c2) WHERE c1 <> c2 RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['<>']`
- Wildcard: `True`

---

## Ejercicio 37 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que gestionan proyectos en los que no participan.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:GESTIONA]->(pr:Proyecto) WHERE NOT (p)-[:PARTICIPA_EN]->(pr) RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['NOT']`
- Wildcard: `True`

---

## Ejercicio 38 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número de amigos.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 39 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para mostrar solo personas con más de un amigo.

**Query Base:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) WITH p, count(a) as total WHERE total > 1 RETURN p.nombre, total
```

**Validación:**
- Tipo: `estructura`
- Expected: `['WITH']`
- Wildcard: `True`

---

## Ejercicio 40 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra caminos entre personas donde todas las relaciones tienen propiedad since > 2018.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*]->(b:Persona) WHERE ALL(r IN relationships(p) WHERE r.since > 2018) RETURN p
```

**Validación:**
- Tipo: `estructura`
- Expected: `['ALL']`
- Wildcard: `True`

---

## Ejercicio 41 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número de proyectos en los que participan.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre, count(pr)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 42 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para incluir también personas sin proyectos.

**Query Base:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre, count(pr)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre, count(pr)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['OPTIONAL MATCH']`
- Wildcard: `True`

---

## Ejercicio 43 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que participan en más de un proyecto.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) WITH p, count(pr) as total WHERE total > 1 RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['WITH', 'WHERE']`
- Wildcard: `True`

---

## Ejercicio 44 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén proyectos junto con el número de personas distintas que participan en ellos.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(DISTINCT p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 45 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para evitar duplicados en el conteo.

**Query Base:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(DISTINCT p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 46 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan en empresas donde al menos uno de sus compañeros usa Neo4j.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa)<-[:TRABAJA_EN]-(o:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia {nombre:'Neo4j'}) RETURN DISTINCT p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 47 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que tienen amigos que trabajan en una empresa distinta a la suya.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e1:Empresa),(p)-[:AMIGO_DE]->(a:Persona)-[:TRABAJA_EN]->(e2:Empresa) WHERE e1 <> e2 RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['<>']`
- Wildcard: `True`

---

## Ejercicio 48 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra pares de personas que viven en la misma ciudad y trabajan juntas.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_CON]->(p2:Persona),(p1)-[:VIVE_EN]->(c),(p2)-[:VIVE_EN]->(c) RETURN p1.nombre, p2.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['VIVE_EN']`
- Wildcard: `True`

---

## Ejercicio 49 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para evitar pares duplicados.

**Query Base:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_CON]->(p2:Persona) RETURN p1.nombre, p2.nombre
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_CON]->(p2:Persona) WHERE id(p1) < id(p2) RETURN p1.nombre, p2.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['id']`
- Wildcard: `True`

---

## Ejercicio 50 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están conectadas por amistad a alguien que participa en más de un proyecto.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) WITH a, count(pr) as total, p WHERE total > 1 RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['WITH']`
- Wildcard: `True`

---

## Ejercicio 51 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que usan exactamente una tecnología.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) WITH p, count(t) as total WHERE total = 1 RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 52 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que no tienen amigos.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) WHERE NOT (p)-[:AMIGO_DE]->() RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['NOT']`
- Wildcard: `True`

---

## Ejercicio 53 (Dificil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar OPTIONAL MATCH correctamente.

**Query Base:**
```cypher
MATCH (p:Persona) MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN p, pr
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN p, pr
```

**Validación:**
- Tipo: `estructura`
- Expected: `['OPTIONAL MATCH']`
- Wildcard: `True`

---

## Ejercicio 54 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra caminos de amistad donde todos los nodos intermedios viven en la misma ciudad.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*2..3]->(b:Persona) WHERE ALL(n IN nodes(p)[1..-1] WHERE (n)-[:VIVE_EN]->(:Ciudad)) RETURN p
```

**Validación:**
- Tipo: `estructura`
- Expected: `['ALL']`
- Wildcard: `True`

---

## Ejercicio 55 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que aparecen en más de un path de amistad.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) UNWIND nodes(p) as n WITH n, count(*) as total WHERE total > 1 RETURN n, total
```

**Validación:**
- Tipo: `estructura`
- Expected: `['UNWIND']`
- Wildcard: `True`

---

## Ejercicio 56 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con todas las tecnologías que usan.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN p.nombre, collect(t.nombre)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['collect']`
- Wildcard: `True`

---

## Ejercicio 57 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo personas que usan más de una tecnología.

**Query Base:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN p.nombre, collect(t.nombre)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) WITH p, collect(t) as techs WHERE size(techs) > 1 RETURN p.nombre, techs
```

**Validación:**
- Tipo: `estructura`
- Expected: `['size']`
- Wildcard: `True`

---

## Ejercicio 58 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra tecnologías usadas por personas que trabajan en TechCorp.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(:Empresa {nombre:'TechCorp'}),(p)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN DISTINCT t.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 59 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan en todas las empresas presentes en el grafo.

### SOLUCIÓN

**Query:**
```cypher
MATCH (e:Empresa) WITH count(e) as total MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) WITH p, count(DISTINCT e) as c, total WHERE c = total RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['WITH']`
- Wildcard: `True`

---

## Ejercicio 60 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que comparten todas sus tecnologías con al menos otra persona.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) WITH p, collect(t) as techs MATCH (o:Persona)-[:USA_TECNOLOGIA]->(t2:Tecnologia) WITH p, techs, o, collect(t2) as techs2 WHERE techs = techs2 AND p <> o RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['collect']`
- Wildcard: `True`

---

## Ejercicio 61 (Dificil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar correctamente UNWIND.

**Query Base:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) RETURN UNWIND nodes(p)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n
```

**Validación:**
- Tipo: `estructura`
- Expected: `['UNWIND']`
- Wildcard: `True`

---

## Ejercicio 62 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para contar cuántas veces aparece cada nodo en paths.

**Query Base:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n
```

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n, count(*)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 63 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están conectadas a todas las demás mediante algún path.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) MATCH (p)-[:AMIGO_DE*]->(o:Persona) WITH p, count(DISTINCT o) as total MATCH (x:Persona) WITH p, total, count(x) as all WHERE total = all - 1 RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 64 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que conectan diferentes ciudades a través de amistad.

### SOLUCIÓN

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE]->(b:Persona)-[:AMIGO_DE]->(c:Persona),(a)-[:VIVE_EN]->(c1),(c)-[:VIVE_EN]->(c2) WHERE c1 <> c2 RETURN b.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['<>']`
- Wildcard: `True`

---

## Ejercicio 65 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra el nodo más frecuente en paths de amistad.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*]->(b:Persona) UNWIND nodes(p) as n RETURN n, count(*) as total ORDER BY total DESC LIMIT 1
```

**Validación:**
- Tipo: `estructura`
- Expected: `['ORDER BY', 'LIMIT']`
- Wildcard: `True`

---

## Ejercicio 66 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén todas las personas junto con la empresa en la que trabajan y la ciudad en la que viven.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa),(p)-[:VIVE_EN]->(c:Ciudad) RETURN p.nombre, e.nombre, c.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['MATCH']`
- Wildcard: `True`

---

## Ejercicio 67 (Medio)
**Tipo:** `write_query`

**Enunciado:** Cuenta cuántas personas trabajan en cada empresa y viven en Madrid.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa),(p)-[:VIVE_EN]->(:Ciudad {nombre:'Madrid'}) RETURN e.nombre, count(p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 68 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para ordenar los resultados por número de empleados descendente.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p) as total ORDER BY total DESC
```

**Validación:**
- Tipo: `estructura`
- Expected: `['ORDER BY']`
- Wildcard: `True`

---

## Ejercicio 69 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas que viven en la misma ciudad que sus compañeros de trabajo.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona),(p)-[:VIVE_EN]->(c),(o)-[:VIVE_EN]->(c) RETURN DISTINCT p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 70 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar correctamente ORDER BY.

**Query Base:**
```cypher
MATCH (p:Persona) RETURN p.nombre ORDER p.nombre
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) RETURN p.nombre ORDER BY p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['ORDER BY']`
- Wildcard: `True`

---

## Ejercicio 71 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra proyectos gestionados por personas que trabajan en DataSoft.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(:Empresa {nombre:'DataSoft'}),(p)-[:GESTIONA]->(pr:Proyecto) RETURN pr.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['GESTIONA']`
- Wildcard: `True`

---

## Ejercicio 72 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número de amigos y el número de proyectos en los que participan.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona) OPTIONAL MATCH (p)-[:AMIGO_DE]->(a) WITH p, count(a) as amigos OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN p.nombre, amigos, count(pr)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['WITH']`
- Wildcard: `True`

---

## Ejercicio 73 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para mostrar solo personas con al menos un amigo.

**Query Base:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a) RETURN p.nombre, count(a)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a) WITH p, count(a) as total WHERE total > 0 RETURN p.nombre, total
```

**Validación:**
- Tipo: `estructura`
- Expected: `['WHERE']`
- Wildcard: `True`

---

## Ejercicio 74 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas cuyos amigos participan en proyectos distintos a los suyos.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr1),(p)-[:AMIGO_DE]->(a:Persona)-[:PARTICIPA_EN]->(pr2) WHERE pr1 <> pr2 RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['<>']`
- Wildcard: `True`

---

## Ejercicio 75 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan con alguien que vive en otra ciudad.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona),(p)-[:VIVE_EN]->(c1),(o)-[:VIVE_EN]->(c2) WHERE c1 <> c2 RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['<>']`
- Wildcard: `True`

---

## Ejercicio 76 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que comparten al menos una tecnología.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) MATCH (p)-[:USA_TECNOLOGIA]->(t:Tecnologia),(a)-[:USA_TECNOLOGIA]->(t) RETURN DISTINCT p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 77 (Dificil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para aplicar correctamente múltiples MATCH.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e) MATCH (p)-[:VIVE_EN]->(c) RETURN p,e,c
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e),(p)-[:VIVE_EN]->(c) RETURN p,e,c
```

**Validación:**
- Tipo: `estructura`
- Expected: `['MATCH']`
- Wildcard: `True`

---

## Ejercicio 78 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo nombres únicos de personas.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona) RETURN p.nombre
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona) RETURN DISTINCT p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 79 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número total de relaciones que tienen.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)--() RETURN p.nombre, count(*)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['--']`
- Wildcard: `True`

---

## Ejercicio 80 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas conectadas a al menos un proyecto a través de cualquier relación.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-->(:Proyecto) RETURN DISTINCT p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['--']`
- Wildcard: `True`

---

## Ejercicio 81 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están a distancia exactamente 2 en la red de amistad.

### SOLUCIÓN

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE*2..2]->(b:Persona) RETURN a.nombre, b.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['*2..2']`
- Wildcard: `True`

---

## Ejercicio 82 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para excluir relaciones directas.

**Query Base:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE*1..2]->(b:Persona) RETURN a,b
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE*2..2]->(b:Persona) RETURN a,b
```

**Validación:**
- Tipo: `estructura`
- Expected: `['*2..2']`
- Wildcard: `True`

---

## Ejercicio 83 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra ciudades donde viven personas que trabajan en TechCorp.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(:Empresa {nombre:'TechCorp'}),(p)-[:VIVE_EN]->(c:Ciudad) RETURN DISTINCT c.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 84 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén universidades junto con el número de personas que estudiaron en ellas.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:ESTUDIO_EN]->(u:Universidad) RETURN u.nombre, count(p)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 85 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar DISTINCT correctamente.

**Query Base:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN DISTINCT c.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 86 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas cuyos amigos viven todos en la misma ciudad.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona),(a)-[:VIVE_EN]->(c:Ciudad) WITH p, collect(DISTINCT c) as ciudades WHERE size(ciudades)=1 RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['collect', 'size']`
- Wildcard: `True`

---

## Ejercicio 87 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan en empresas donde todos los empleados viven en la misma ciudad.

### SOLUCIÓN

**Query:**
```cypher
MATCH (e:Empresa)<-[:TRABAJA_EN]-(p:Persona),(p)-[:VIVE_EN]->(c:Ciudad) WITH e, collect(DISTINCT c) as ciudades WHERE size(ciudades)=1 MATCH (e)<-[:TRABAJA_EN]-(p2:Persona) RETURN p2.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['collect', 'size']`
- Wildcard: `True`

---

## Ejercicio 88 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que tienen al menos un amigo en cada ciudad.

### SOLUCIÓN

**Query:**
```cypher
MATCH (c:Ciudad) WITH collect(c) as ciudades MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:VIVE_EN]->(c2:Ciudad) WITH p, collect(DISTINCT c2) as ciudades2, ciudades WHERE ciudades2 = ciudades RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['collect']`
- Wildcard: `True`

---

## Ejercicio 89 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para limitar a los 3 resultados con más amigos.

**Query Base:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a) as total ORDER BY total DESC LIMIT 3
```

**Validación:**
- Tipo: `estructura`
- Expected: `['LIMIT']`
- Wildcard: `True`

---

## Ejercicio 90 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están conectadas por amistad a alguien que trabaja en todas las empresas.

### SOLUCIÓN

**Query:**
```cypher
MATCH (e:Empresa) WITH count(e) as total MATCH (a:Persona)-[:TRABAJA_EN]->(e:Empresa) WITH a, count(DISTINCT e) as c, total WHERE c = total MATCH (p:Persona)-[:AMIGO_DE]->(a) RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['WITH']`
- Wildcard: `True`

---

## Ejercicio 91 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que tienen más amigos que la media.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a) WITH p, count(a) as total WITH collect(total) as totales, p, total WITH p, total, reduce(s=0, x IN totales | s + x) / size(totales) as media WHERE total > media RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['avg']`
- Wildcard: `True`

---

## Ejercicio 92 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están conectadas con otras mediante más de un camino distinto.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) WITH a,b,count(p) as total WHERE total > 1 RETURN a.nombre, b.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['count']`
- Wildcard: `True`

---

## Ejercicio 93 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas cuyos amigos trabajan en todas las empresas.

### SOLUCIÓN

**Query:**
```cypher
MATCH (e:Empresa) WITH collect(e) as empresas MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:TRABAJA_EN]->(e2:Empresa) WITH p, collect(DISTINCT e2) as empresas2, empresas WHERE empresas2 = empresas RETURN p.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['collect']`
- Wildcard: `True`

---

## Ejercicio 94 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están en todos los caminos entre dos nodos específicos.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona {nombre:'Ana'})-[:AMIGO_DE*]->(b:Persona {nombre:'Carlos'}) UNWIND nodes(p) as n RETURN n, count(*) as total ORDER BY total DESC
```

**Validación:**
- Tipo: `estructura`
- Expected: `['UNWIND']`
- Wildcard: `True`

---

## Ejercicio 95 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo los nodos más frecuentes.

**Query Base:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n, count(*)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n, count(*) as total ORDER BY total DESC LIMIT 1
```

**Validación:**
- Tipo: `estructura`
- Expected: `['LIMIT']`
- Wildcard: `True`

---

## Ejercicio 96 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con todas las ciudades en las que tienen amigos.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN p.nombre, collect(DISTINCT c.nombre)
```

**Validación:**
- Tipo: `estructura`
- Expected: `['collect']`
- Wildcard: `True`

---

## Ejercicio 97 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra empresas donde trabajan personas que usan Python.

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(:Tecnologia {nombre:'Python'}),(p)-[:TRABAJA_EN]->(e:Empresa) RETURN DISTINCT e.nombre
```

**Validación:**
- Tipo: `estructura`
- Expected: `['DISTINCT']`
- Wildcard: `True`

---

## Ejercicio 98 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar correctamente múltiples relaciones.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e)-[:VIVE_EN]->(c) RETURN p,e,c
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e),(p)-[:VIVE_EN]->(c) RETURN p,e,c
```

**Validación:**
- Tipo: `estructura`
- Expected: `['MATCH']`
- Wildcard: `True`

---

## Ejercicio 99 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo los 2 proyectos con más participantes.

**Query Base:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p)
```

### SOLUCIÓN

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p) as total ORDER BY total DESC LIMIT 2
```

**Validación:**
- Tipo: `estructura`
- Expected: `['LIMIT']`
- Wildcard: `True`

---

## Ejercicio 100 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que maximizan el número de conexiones indirectas en la red de amistad.

### SOLUCIÓN

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN a.nombre, count(DISTINCT b) as total ORDER BY total DESC LIMIT 1
```

**Validación:**
- Tipo: `estructura`
- Expected: `['ORDER BY', 'LIMIT']`
- Wildcard: `True`

---

