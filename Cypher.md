---
materia: Bases de Datos 2
---

# Cypher: Guía Maestra de Grafos (Neo4j)

Manual unificado que cubre desde la navegación básica hasta el análisis avanzado de caminos y procesamiento de listas.

---

## ¿Cómo dibujamos y buscamos patrones? (`MATCH` y `CREATE`)

Cypher se basa en el "Arte ASCII" para representar los datos.

```cypher
// EL ESQUELETO: (nodo:Etiqueta {propiedad: "valor"})-[relacion:TIPO]->(objetivo)
//   ├─ ( ): Representa un Nodo.
//   ├─ [ ]: Representa una Relación.
//   └─ ->: Indica la dirección obligatoria.
```

### ¿Cómo creamos datos sin duplicar? (`MERGE`)
`MERGE` busca el patrón; si no existe, lo crea. Es la forma más segura de insertar.
```cypher
MATCH (p:Persona {nombre: "Ana"})
MERGE (p)-[:USA_TECNOLOGIA]->(:Tecnologia {nombre: "Neo4j"})
```

---

## ¿Cómo filtramos y transformamos resultados? (`WHERE` y `WITH`)

### El poder del `WITH` (La barrera de cálculo)
`WITH` permite hacer una pausa para calcular algo (como un `count`) y usar ese resultado en el resto de la consulta.
**¡OJO!** — `WITH` borra todas las variables que no menciones explícitamente.
```cypher
MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa)
WITH e, count(p) AS total
WHERE total > 5
RETURN e.nombre, total
```

---

## ¿Cómo navegamos por la red? (`Paths` y Longitud)

Para buscar conexiones indirectas (amigos de amigos) usamos el asterisco `*`.

```cypher
// SINTAXIS: -[:TIPO*min..max]->
//   └─ *1..3: Distancia de entre 1 y 3 saltos.

// Ejemplo: Amigos de mis amigos (distancia exacta 2)
MATCH (yo:Persona {nombre: "Ana"})-[:AMIGO_DE*2..2]->(conocido:Persona)
RETURN conocido.nombre
```

---

## ¿Cómo realizamos análisis avanzado sobre caminos?

Cuando guardamos un camino en una variable (`p = (...)`), podemos aplicar funciones Pro.

### Filtros sobre colecciones (`ALL`, `ANY`, `NONE`)
Verifica si los elementos de un camino cumplen una condición.
```cypher
MATCH p = (a:Persona)-[:AMIGO_DE*1..5]->(b:Persona)
WHERE ALL(r IN relationships(p) WHERE r.intensidad > 5)
RETURN p
```

### Manipulación de listas y `reduce`
- **`nodes(p)`**: Devuelve la lista de todos los nodos del camino.
- **`relationships(p)`**: Devuelve la lista de todas las relaciones.
- **`reduce`**: Compacta una lista en un valor único (como sumar distancias).
  ```cypher
  RETURN reduce(total = 0, r IN relationships(p) | total + r.horas) AS total_horas
  ```

---

## Checklist de Supervivencia en el Examen

| Problema | Solución Cypher |
| :--- | :--- |
| **Duplicados** | Usa `RETURN DISTINCT`. |
| **Pares Inversos** | Usa `WHERE id(a) < id(b)` para evitar ver (A-B) y (B-A). |
| **Relaciones Opcionales** | Usa `OPTIONAL MATCH` para no perder resultados si la relación no existe. |
| **Propiedades de Relación** | Asigna un alias: `-[r:REL]->` para acceder a `r.propiedad`. |

---

## Referencias
1. [[MongoDB]] — Guía de Documentos.
2. [[Simulacro_Examen_BD2]] — Práctica real.
3. [[Bases de datos 2]] — Índice de asignatura.
