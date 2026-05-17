# Banco de Ejercicios: Neo4j Cypher

* **Descripcion:** Banco de 100 ejercicios Neo4j Cypher (unificado)
* **Nota:** Pegar aquí los bloques 1–100 generados previamente

---

## Ejercicio 1 (Facil)
**Tipo:** `write_query`

**Enunciado:** Obtén todas las personas que trabajan en alguna empresa y muestra el nombre de la persona y de la empresa.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN p.nombre, e.nombre
```
**Validación:**
- **Tipo:** `resultado`
- **Esperado:** `[['Ana', 'TechCorp'], ['Luis', 'TechCorp'], ['Marta', 'DataSoft'], ['Carlos', 'DataSoft']]`
- **Wildcard:** `True`

</details>

---

## Ejercicio 2 (Facil)
**Tipo:** `write_query`

**Enunciado:** Lista todas las personas que viven en Madrid.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad {nombre:'Madrid'}) RETURN p.nombre
```
**Validación:**
- **Tipo:** `resultado`
- **Esperado:** `['Ana', 'Luis', 'Elena']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 3 (Facil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para devolver correctamente nombres de personas.

**Query Base:**
```cypher
MATCH (p:Persona) RETURN nombre
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['MATCH', 'RETURN']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 4 (Facil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para limitar a 2 resultados.

**Query Base:**
```cypher
MATCH (p:Persona) RETURN p.nombre
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) RETURN p.nombre LIMIT 2
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['LIMIT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 5 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén las empresas junto con el número de empleados.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p)
```
**Validación:**
- **Tipo:** `resultado`
- **Esperado:** `[['TechCorp', 2], ['DataSoft', 2]]`
- **Wildcard:** `True`

</details>

---

## Ejercicio 6 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que participan en proyectos y trabajan en empresa.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa), (p)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre
```
**Validación:**
- **Tipo:** `resultado`
- **Esperado:** `['Ana', 'Luis', 'Marta']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 7 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar WHERE correctamente.

**Query Base:**
```cypher
MATCH (p:Persona) WHERE nombre='Ana' RETURN p
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) WHERE p.nombre='Ana' RETURN p
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['WHERE']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 8 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para ordenar por nombre.

**Query Base:**
```cypher
MATCH (p:Persona) RETURN p.nombre
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) RETURN p.nombre ORDER BY p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['ORDER BY']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 9 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas con al menos 2 amigos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) WITH p, count(a) as amigos WHERE amigos >= 2 RETURN p.nombre, amigos
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 10 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra caminos de longitud hasta 2 entre personas.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..2]->(b:Persona) RETURN p
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['*1..2']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 11 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas conectadas a proyectos a través de amigos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE]->(b:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN a.nombre, pr.nombre
```
**Validación:**
- **Tipo:** `resultado`
- **Esperado:** `[['Ana', 'Apollo'], ['Luis', 'Zeus']]`
- **Wildcard:** `True`

</details>

---

## Ejercicio 12 (Dificil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar length correctamente.

**Query Base:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) RETURN length
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) RETURN length(p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['length']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 13 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo la longitud del path.

**Query Base:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN p
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN length(p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['length']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 14 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que no participan en proyectos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr) WHERE pr IS NULL RETURN p.nombre
```
**Validación:**
- **Tipo:** `resultado`
- **Esperado:** `['Carlos', 'Elena']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 15 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que actúan como puente en relaciones de amistad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE]->(b:Persona)-[:AMIGO_DE]->(c:Persona) RETURN b, count(*)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 16 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén todas las personas junto con la ciudad en la que viven.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN p.nombre, c.nombre
```
**Validación:**
- **Tipo:** `resultado`
- **Esperado:** `[['Ana', 'Madrid'], ['Luis', 'Madrid'], ['Elena', 'Madrid'], ['Marta', 'Barcelona'], ['Carlos', 'Barcelona']]`
- **Wildcard:** `True`

</details>

---

## Ejercicio 17 (Medio)
**Tipo:** `write_query`

**Enunciado:** Cuenta cuántas personas viven en cada ciudad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre, count(p)
```
**Validación:**
- **Tipo:** `resultado`
- **Esperado:** `[['Madrid', 3], ['Barcelona', 2]]`
- **Wildcard:** `True`

</details>

---

## Ejercicio 18 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo las ciudades con más de 2 personas.

**Query Base:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre, count(p)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) WITH c, count(p) as total WHERE total > 2 RETURN c.nombre, total
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['WITH', 'WHERE']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 19 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para que agrupe correctamente.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN p.nombre, count(e)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 20 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número de tecnologías que usan.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN p.nombre, count(t)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 21 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que usan la tecnología Neo4j.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia {nombre:'Neo4j'}) RETURN p.nombre
```
**Validación:**
- **Tipo:** `resultado`
- **Esperado:** `['Ana', 'Marta']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 22 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan en la misma empresa.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_EN]->(e:Empresa)<-[:TRABAJA_EN]-(p2:Persona) WHERE p1 <> p2 RETURN p1.nombre, p2.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['<>']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 23 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para evitar duplicados en pares de personas.

**Query Base:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_EN]->(e)<-[:TRABAJA_EN]-(p2:Persona) RETURN p1.nombre, p2.nombre
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_EN]->(e)<-[:TRABAJA_EN]-(p2:Persona) WHERE id(p1) < id(p2) RETURN p1.nombre, p2.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['id']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 24 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén proyectos junto con el total de horas invertidas por personas.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[r:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, sum(r.horas)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['sum']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 25 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar propiedades de relación.

**Query Base:**
```cypher
MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN pr.nombre, sum(horas)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p)-[r:PARTICIPA_EN]->(pr) RETURN pr.nombre, sum(r.horas)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['r.horas']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 26 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas conectadas por cadenas de amistad de hasta longitud 3.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN a.nombre, b.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['*1..3']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 27 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Devuelve los paths de amistad junto con su longitud.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN p, length(p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['length']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 28 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo paths de longitud mayor a 1.

**Query Base:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN p
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) WHERE length(p) > 1 RETURN p
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['length']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 29 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Obtén los nodos intermedios en paths de amistad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*2..3]->(b:Persona) RETURN nodes(p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['nodes']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 30 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Obtén las relaciones de un path.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN relationships(p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['relationships']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 31 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con la universidad en la que estudiaron.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:ESTUDIO_EN]->(u:Universidad) RETURN p.nombre, u.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['ESTUDIO_EN']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 32 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra universidades con más de un estudiante.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:ESTUDIO_EN]->(u:Universidad) WITH u, count(p) as total WHERE total > 1 RETURN u.nombre, total
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 33 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar WITH correctamente.

**Query Base:**
```cypher
MATCH (p:Persona) WITH p MATCH (p)-[:VIVE_EN]->(c) RETURN c
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c) RETURN c
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['MATCH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 34 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo ciudades únicas.

**Query Base:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN DISTINCT c.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 35 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan con alguien que usa Neo4j.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia {nombre:'Neo4j'}) RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['TRABAJA_CON']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 36 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que viven en una ciudad distinta a la de sus amigos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona),(p)-[:VIVE_EN]->(c1),(a)-[:VIVE_EN]->(c2) WHERE c1 <> c2 RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['<>']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 37 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que gestionan proyectos en los que no participan.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:GESTIONA]->(pr:Proyecto) WHERE NOT (p)-[:PARTICIPA_EN]->(pr) RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['NOT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 38 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número de amigos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 39 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para mostrar solo personas con más de un amigo.

**Query Base:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) WITH p, count(a) as total WHERE total > 1 RETURN p.nombre, total
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['WITH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 40 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra caminos entre personas donde todas las relaciones tienen propiedad since > 2018.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*]->(b:Persona) WHERE ALL(r IN relationships(p) WHERE r.since > 2018) RETURN p
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['ALL']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 41 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número de proyectos en los que participan.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre, count(pr)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 42 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para incluir también personas sin proyectos.

**Query Base:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre, count(pr)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre, count(pr)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['OPTIONAL MATCH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 43 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que participan en más de un proyecto.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) WITH p, count(pr) as total WHERE total > 1 RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['WITH', 'WHERE']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 44 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén proyectos junto con el número de personas distintas que participan en ellos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(DISTINCT p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 45 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para evitar duplicados en el conteo.

**Query Base:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(DISTINCT p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 46 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan en empresas donde al menos uno de sus compañeros usa Neo4j.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa)<-[:TRABAJA_EN]-(o:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia {nombre:'Neo4j'}) RETURN DISTINCT p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 47 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que tienen amigos que trabajan en una empresa distinta a la suya.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e1:Empresa),(p)-[:AMIGO_DE]->(a:Persona)-[:TRABAJA_EN]->(e2:Empresa) WHERE e1 <> e2 RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['<>']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 48 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra pares de personas que viven en la misma ciudad y trabajan juntas.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_CON]->(p2:Persona),(p1)-[:VIVE_EN]->(c),(p2)-[:VIVE_EN]->(c) RETURN p1.nombre, p2.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['VIVE_EN']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 49 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para evitar pares duplicados.

**Query Base:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_CON]->(p2:Persona) RETURN p1.nombre, p2.nombre
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p1:Persona)-[:TRABAJA_CON]->(p2:Persona) WHERE id(p1) < id(p2) RETURN p1.nombre, p2.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['id']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 50 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están conectadas por amistad a alguien que participa en más de un proyecto.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) WITH a, count(pr) as total, p WHERE total > 1 RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['WITH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 51 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que usan exactamente una tecnología.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) WITH p, count(t) as total WHERE total = 1 RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 52 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que no tienen amigos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) WHERE NOT (p)-[:AMIGO_DE]->() RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['NOT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 53 (Dificil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar OPTIONAL MATCH correctamente.

**Query Base:**
```cypher
MATCH (p:Persona) MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN p, pr
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN p, pr
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['OPTIONAL MATCH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 54 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra caminos de amistad donde todos los nodos intermedios viven en la misma ciudad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*2..3]->(b:Persona) WHERE ALL(n IN nodes(p)[1..-1] WHERE (n)-[:VIVE_EN]->(:Ciudad)) RETURN p
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['ALL']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 55 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que aparecen en más de un path de amistad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) UNWIND nodes(p) as n WITH n, count(*) as total WHERE total > 1 RETURN n, total
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['UNWIND']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 56 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con todas las tecnologías que usan.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN p.nombre, collect(t.nombre)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['collect']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 57 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo personas que usan más de una tecnología.

**Query Base:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN p.nombre, collect(t.nombre)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) WITH p, collect(t) as techs WHERE size(techs) > 1 RETURN p.nombre, techs
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['size']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 58 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra tecnologías usadas por personas que trabajan en TechCorp.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(:Empresa {nombre:'TechCorp'}),(p)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN DISTINCT t.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 59 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan en todas las empresas presentes en el grafo.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (e:Empresa) WITH count(e) as total MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) WITH p, count(DISTINCT e) as c, total WHERE c = total RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['WITH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 60 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que comparten todas sus tecnologías con al menos otra persona.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) WITH p, collect(t) as techs MATCH (o:Persona)-[:USA_TECNOLOGIA]->(t2:Tecnologia) WITH p, techs, o, collect(t2) as techs2 WHERE techs = techs2 AND p <> o RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['collect']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 61 (Dificil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar correctamente UNWIND.

**Query Base:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) RETURN UNWIND nodes(p)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['UNWIND']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 62 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para contar cuántas veces aparece cada nodo en paths.

**Query Base:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n, count(*)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 63 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están conectadas a todas las demás mediante algún path.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) MATCH (p)-[:AMIGO_DE*]->(o:Persona) WITH p, count(DISTINCT o) as total MATCH (x:Persona) WITH p, total, count(x) as all WHERE total = all - 1 RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 64 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que conectan diferentes ciudades a través de amistad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE]->(b:Persona)-[:AMIGO_DE]->(c:Persona),(a)-[:VIVE_EN]->(c1),(c)-[:VIVE_EN]->(c2) WHERE c1 <> c2 RETURN b.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['<>']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 65 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra el nodo más frecuente en paths de amistad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*]->(b:Persona) UNWIND nodes(p) as n RETURN n, count(*) as total ORDER BY total DESC LIMIT 1
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['ORDER BY', 'LIMIT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 66 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén todas las personas junto con la empresa en la que trabajan y la ciudad en la que viven.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa),(p)-[:VIVE_EN]->(c:Ciudad) RETURN p.nombre, e.nombre, c.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['MATCH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 67 (Medio)
**Tipo:** `write_query`

**Enunciado:** Cuenta cuántas personas trabajan en cada empresa y viven en Madrid.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa),(p)-[:VIVE_EN]->(:Ciudad {nombre:'Madrid'}) RETURN e.nombre, count(p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 68 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para ordenar los resultados por número de empleados descendente.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p) as total ORDER BY total DESC
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['ORDER BY']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 69 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas que viven en la misma ciudad que sus compañeros de trabajo.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona),(p)-[:VIVE_EN]->(c),(o)-[:VIVE_EN]->(c) RETURN DISTINCT p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 70 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar correctamente ORDER BY.

**Query Base:**
```cypher
MATCH (p:Persona) RETURN p.nombre ORDER p.nombre
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) RETURN p.nombre ORDER BY p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['ORDER BY']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 71 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra proyectos gestionados por personas que trabajan en DataSoft.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(:Empresa {nombre:'DataSoft'}),(p)-[:GESTIONA]->(pr:Proyecto) RETURN pr.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['GESTIONA']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 72 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número de amigos y el número de proyectos en los que participan.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona) OPTIONAL MATCH (p)-[:AMIGO_DE]->(a) WITH p, count(a) as amigos OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN p.nombre, amigos, count(pr)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['WITH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 73 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para mostrar solo personas con al menos un amigo.

**Query Base:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a) RETURN p.nombre, count(a)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a) WITH p, count(a) as total WHERE total > 0 RETURN p.nombre, total
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['WHERE']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 74 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas cuyos amigos participan en proyectos distintos a los suyos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr1),(p)-[:AMIGO_DE]->(a:Persona)-[:PARTICIPA_EN]->(pr2) WHERE pr1 <> pr2 RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['<>']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 75 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan con alguien que vive en otra ciudad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona),(p)-[:VIVE_EN]->(c1),(o)-[:VIVE_EN]->(c2) WHERE c1 <> c2 RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['<>']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 76 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que comparten al menos una tecnología.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) MATCH (p)-[:USA_TECNOLOGIA]->(t:Tecnologia),(a)-[:USA_TECNOLOGIA]->(t) RETURN DISTINCT p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 77 (Dificil)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para aplicar correctamente múltiples MATCH.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e) MATCH (p)-[:VIVE_EN]->(c) RETURN p,e,c
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e),(p)-[:VIVE_EN]->(c) RETURN p,e,c
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['MATCH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 78 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo nombres únicos de personas.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona) RETURN p.nombre
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona) RETURN DISTINCT p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 79 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con el número total de relaciones que tienen.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)--() RETURN p.nombre, count(*)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['--']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 80 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas conectadas a al menos un proyecto a través de cualquier relación.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-->(:Proyecto) RETURN DISTINCT p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['--']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 81 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están a distancia exactamente 2 en la red de amistad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE*2..2]->(b:Persona) RETURN a.nombre, b.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['*2..2']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 82 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para excluir relaciones directas.

**Query Base:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE*1..2]->(b:Persona) RETURN a,b
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (a:Persona)-[:AMIGO_DE*2..2]->(b:Persona) RETURN a,b
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['*2..2']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 83 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra ciudades donde viven personas que trabajan en TechCorp.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(:Empresa {nombre:'TechCorp'}),(p)-[:VIVE_EN]->(c:Ciudad) RETURN DISTINCT c.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 84 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén universidades junto con el número de personas que estudiaron en ellas.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:ESTUDIO_EN]->(u:Universidad) RETURN u.nombre, count(p)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 85 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar DISTINCT correctamente.

**Query Base:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN DISTINCT c.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 86 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas cuyos amigos viven todos en la misma ciudad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona),(a)-[:VIVE_EN]->(c:Ciudad) WITH p, collect(DISTINCT c) as ciudades WHERE size(ciudades)=1 RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['collect', 'size']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 87 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que trabajan en empresas donde todos los empleados viven en la misma ciudad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (e:Empresa)<-[:TRABAJA_EN]-(p:Persona),(p)-[:VIVE_EN]->(c:Ciudad) WITH e, collect(DISTINCT c) as ciudades WHERE size(ciudades)=1 MATCH (e)<-[:TRABAJA_EN]-(p2:Persona) RETURN p2.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['collect', 'size']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 88 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que tienen al menos un amigo en cada ciudad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (c:Ciudad) WITH collect(c) as ciudades MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:VIVE_EN]->(c2:Ciudad) WITH p, collect(DISTINCT c2) as ciudades2, ciudades WHERE ciudades2 = ciudades RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['collect']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 89 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para limitar a los 3 resultados con más amigos.

**Query Base:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a) as total ORDER BY total DESC LIMIT 3
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['LIMIT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 90 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están conectadas por amistad a alguien que trabaja en todas las empresas.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (e:Empresa) WITH count(e) as total MATCH (a:Persona)-[:TRABAJA_EN]->(e:Empresa) WITH a, count(DISTINCT e) as c, total WHERE c = total MATCH (p:Persona)-[:AMIGO_DE]->(a) RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['WITH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 91 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que tienen más amigos que la media.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a) WITH p, count(a) as total WITH collect(total) as totales, p, total WITH p, total, reduce(s=0, x IN totales | s + x) / size(totales) as media WHERE total > media RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['avg']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 92 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están conectadas con otras mediante más de un camino distinto.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) WITH a,b,count(p) as total WHERE total > 1 RETURN a.nombre, b.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['count']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 93 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas cuyos amigos trabajan en todas las empresas.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (e:Empresa) WITH collect(e) as empresas MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:TRABAJA_EN]->(e2:Empresa) WITH p, collect(DISTINCT e2) as empresas2, empresas WHERE empresas2 = empresas RETURN p.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['collect']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 94 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que están en todos los caminos entre dos nodos específicos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona {nombre:'Ana'})-[:AMIGO_DE*]->(b:Persona {nombre:'Carlos'}) UNWIND nodes(p) as n RETURN n, count(*) as total ORDER BY total DESC
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['UNWIND']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 95 (Dificil)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo los nodos más frecuentes.

**Query Base:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n, count(*)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n, count(*) as total ORDER BY total DESC LIMIT 1
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['LIMIT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 96 (Medio)
**Tipo:** `write_query`

**Enunciado:** Obtén personas junto con todas las ciudades en las que tienen amigos.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN p.nombre, collect(DISTINCT c.nombre)
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['collect']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 97 (Medio)
**Tipo:** `write_query`

**Enunciado:** Encuentra empresas donde trabajan personas que usan Python.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:USA_TECNOLOGIA]->(:Tecnologia {nombre:'Python'}),(p)-[:TRABAJA_EN]->(e:Empresa) RETURN DISTINCT e.nombre
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['DISTINCT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 98 (Medio)
**Tipo:** `fix_query`

**Enunciado:** Corrige la consulta para usar correctamente múltiples relaciones.

**Query Base:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e)-[:VIVE_EN]->(c) RETURN p,e,c
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e),(p)-[:VIVE_EN]->(c) RETURN p,e,c
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['MATCH']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 99 (Medio)
**Tipo:** `modify_query`

**Enunciado:** Modifica la consulta para devolver solo los 2 proyectos con más participantes.

**Query Base:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p)
```

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p) as total ORDER BY total DESC LIMIT 2
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['LIMIT']`
- **Wildcard:** `True`

</details>

---

## Ejercicio 100 (Dificil)
**Tipo:** `write_query`

**Enunciado:** Encuentra personas que maximizan el número de conexiones indirectas en la red de amistad.

<details>
<summary><b>Respuesta Esperada</b></summary>

**Query:**
```cypher
MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN a.nombre, count(DISTINCT b) as total ORDER BY total DESC LIMIT 1
```
**Validación:**
- **Tipo:** `estructura`
- **Esperado:** `['ORDER BY', 'LIMIT']`
- **Wildcard:** `True`

</details>

---

