**1.** Corrige la consulta para devolver correctamente nombres de personas.

```cypher
MATCH (p:Persona) RETURN nombre
```

---

**2.** Modifica la consulta para limitar a 2 resultados.

```cypher
MATCH (p:Persona) RETURN p.nombre
```

---

**3.** Obtén personas junto con todas las tecnologías que usan.

---

**4.** Corrige la consulta para evitar duplicados en el conteo.

```cypher
MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p)
```

---

**5.** Encuentra caminos entre personas donde todas las relaciones tienen propiedad since > 2018.