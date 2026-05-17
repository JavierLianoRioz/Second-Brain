import json
import os

grafos_json = {
    "metadata": {
      "descripcion": "Banco de 100 ejercicios Neo4j Cypher (unificado)",
      "nota": "Pegar aquí los bloques 1–100 generados previamente"
    },
    "ejercicios": [
      {
        "id": 1,
        "tipo": "write_query",
        "nivel": "facil",
        "enunciado": "Obtén todas las personas que trabajan en alguna empresa y muestra el nombre de la persona y de la empresa.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN p.nombre, e.nombre",
          "validacion": {
            "tipo": "resultado",
            "expected": [
              ["Ana","TechCorp"],
              ["Luis","TechCorp"],
              ["Marta","DataSoft"],
              ["Carlos","DataSoft"]
            ],
            "wildcard": true
          }
        }
      },
      {
        "id": 2,
        "tipo": "write_query",
        "nivel": "facil",
        "enunciado": "Lista todas las personas que viven en Madrid.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad {nombre:'Madrid'}) RETURN p.nombre",
          "validacion": {
            "tipo": "resultado",
            "expected": ["Ana","Luis","Elena"],
            "wildcard": true
          }
        }
      },
      {
        "id": 3,
        "tipo": "fix_query",
        "nivel": "facil",
        "enunciado": "Corrige la consulta para devolver correctamente nombres de personas.",
        "query_base": "MATCH (p:Persona) RETURN nombre",
        "respuesta": {
          "query": "MATCH (p:Persona) RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["MATCH","RETURN"],
            "wildcard": true
          }
        }
      },
      {
        "id": 4,
        "tipo": "modify_query",
        "nivel": "facil",
        "enunciado": "Modifica la consulta para limitar a 2 resultados.",
        "query_base": "MATCH (p:Persona) RETURN p.nombre",
        "respuesta": {
          "query": "MATCH (p:Persona) RETURN p.nombre LIMIT 2",
          "validacion": {
            "tipo": "estructura",
            "expected": ["LIMIT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 5,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén las empresas junto con el número de empleados.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p)",
          "validacion": {
            "tipo": "resultado",
            "expected": [
              ["TechCorp",2],
              ["DataSoft",2]
            ],
            "wildcard": true
          }
        }
      },
      {
        "id": 6,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra personas que participan en proyectos y trabajan en empresa.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa), (p)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre",
          "validacion": {
            "tipo": "resultado",
            "expected": ["Ana","Luis","Marta"],
            "wildcard": true
          }
        }
      },
      {
        "id": 7,
        "tipo": "fix_query",
        "nivel": "medio",
        "enunciado": "Corrige la consulta para usar WHERE correctamente.",
        "query_base": "MATCH (p:Persona) WHERE nombre='Ana' RETURN p",
        "respuesta": {
          "query": "MATCH (p:Persona) WHERE p.nombre='Ana' RETURN p",
          "validacion": {
            "tipo": "estructura",
            "expected": ["WHERE"],
            "wildcard": true
          }
        }
      },
      {
        "id": 8,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para ordenar por nombre.",
        "query_base": "MATCH (p:Persona) RETURN p.nombre",
        "respuesta": {
          "query": "MATCH (p:Persona) RETURN p.nombre ORDER BY p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["ORDER BY"],
            "wildcard": true
          }
        }
      },
      {
        "id": 9,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra personas con al menos 2 amigos.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) WITH p, count(a) as amigos WHERE amigos >= 2 RETURN p.nombre, amigos",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 10,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra caminos de longitud hasta 2 entre personas.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*1..2]->(b:Persona) RETURN p",
          "validacion": {
            "tipo": "estructura",
            "expected": ["*1..2"],
            "wildcard": true
          }
        }
      },
      {
        "id": 11,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas conectadas a proyectos a través de amigos.",
        "respuesta": {
          "query": "MATCH (a:Persona)-[:AMIGO_DE]->(b:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN a.nombre, pr.nombre",
          "validacion": {
            "tipo": "resultado",
            "expected": [
              ["Ana","Apollo"],
              ["Luis","Zeus"]
            ],
            "wildcard": true
          }
        }
      },
      {
        "id": 12,
        "tipo": "fix_query",
        "nivel": "dificil",
        "enunciado": "Corrige la consulta para usar length correctamente.",
        "query_base": "MATCH p=(a)-[:AMIGO_DE*]->(b) RETURN length",
        "respuesta": {
          "query": "MATCH p=(a)-[:AMIGO_DE*]->(b) RETURN length(p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["length"],
            "wildcard": true
          }
        }
      },
      {
        "id": 13,
        "tipo": "modify_query",
        "nivel": "dificil",
        "enunciado": "Modifica la consulta para devolver solo la longitud del path.",
        "query_base": "MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN p",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN length(p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["length"],
            "wildcard": true
          }
        }
      },
      {
        "id": 14,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra personas que no participan en proyectos.",
        "respuesta": {
          "query": "MATCH (p:Persona) OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr) WHERE pr IS NULL RETURN p.nombre",
          "validacion": {
            "tipo": "resultado",
            "expected": ["Carlos","Elena"],
            "wildcard": true
          }
        }
      },
      {
        "id": 15,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que actúan como puente en relaciones de amistad.",
        "respuesta": {
          "query": "MATCH (a:Persona)-[:AMIGO_DE]->(b:Persona)-[:AMIGO_DE]->(c:Persona) RETURN b, count(*)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 16,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén todas las personas junto con la ciudad en la que viven.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN p.nombre, c.nombre",
          "validacion": {
            "tipo": "resultado",
            "expected": [
              ["Ana","Madrid"],
              ["Luis","Madrid"],
              ["Elena","Madrid"],
              ["Marta","Barcelona"],
              ["Carlos","Barcelona"]
            ],
            "wildcard": true
          }
        }
      },
      {
        "id": 17,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Cuenta cuántas personas viven en cada ciudad.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre, count(p)",
          "validacion": {
            "tipo": "resultado",
            "expected": [
              ["Madrid",3],
              ["Barcelona",2]
            ],
            "wildcard": true
          }
        }
      },
      {
        "id": 18,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para devolver solo las ciudades con más de 2 personas.",
        "query_base": "MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre, count(p)",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) WITH c, count(p) as total WHERE total > 2 RETURN c.nombre, total",
          "validacion": {
            "tipo": "estructura",
            "expected": ["WITH","WHERE"],
            "wildcard": true
          }
        }
      },
      {
        "id": 19,
        "tipo": "fix_query",
        "nivel": "medio",
        "enunciado": "Corrige la consulta para que agrupe correctamente.",
        "query_base": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN p.nombre, count(e)",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 20,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén personas junto con el número de tecnologías que usan.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN p.nombre, count(t)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 21,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra personas que usan la tecnología Neo4j.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia {nombre:'Neo4j'}) RETURN p.nombre",
          "validacion": {
            "tipo": "resultado",
            "expected": ["Ana","Marta"],
            "wildcard": true
          }
        }
      },
      {
        "id": 22,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra personas que trabajan en la misma empresa.",
        "respuesta": {
          "query": "MATCH (p1:Persona)-[:TRABAJA_EN]->(e:Empresa)<-[:TRABAJA_EN]-(p2:Persona) WHERE p1 <> p2 RETURN p1.nombre, p2.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["<>"],
            "wildcard": true
          }
        }
      },
      {
        "id": 23,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para evitar duplicados en pares de personas.",
        "query_base": "MATCH (p1:Persona)-[:TRABAJA_EN]->(e)<-[:TRABAJA_EN]-(p2:Persona) RETURN p1.nombre, p2.nombre",
        "respuesta": {
          "query": "MATCH (p1:Persona)-[:TRABAJA_EN]->(e)<-[:TRABAJA_EN]-(p2:Persona) WHERE id(p1) < id(p2) RETURN p1.nombre, p2.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["id"],
            "wildcard": true
          }
        }
      },
      {
        "id": 24,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén proyectos junto con el total de horas invertidas por personas.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[r:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, sum(r.horas)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["sum"],
            "wildcard": true
          }
        }
      },
      {
        "id": 25,
        "tipo": "fix_query",
        "nivel": "medio",
        "enunciado": "Corrige la consulta para usar propiedades de relación.",
        "query_base": "MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN pr.nombre, sum(horas)",
        "respuesta": {
          "query": "MATCH (p)-[r:PARTICIPA_EN]->(pr) RETURN pr.nombre, sum(r.horas)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["r.horas"],
            "wildcard": true
          }
        }
      },
      {
        "id": 26,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas conectadas por cadenas de amistad de hasta longitud 3.",
        "respuesta": {
          "query": "MATCH (a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN a.nombre, b.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["*1..3"],
            "wildcard": true
          }
        }
      },
      {
        "id": 27,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Devuelve los paths de amistad junto con su longitud.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN p, length(p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["length"],
            "wildcard": true
          }
        }
      },
      {
        "id": 28,
        "tipo": "modify_query",
        "nivel": "dificil",
        "enunciado": "Modifica la consulta para devolver solo paths de longitud mayor a 1.",
        "query_base": "MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN p",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) WHERE length(p) > 1 RETURN p",
          "validacion": {
            "tipo": "estructura",
            "expected": ["length"],
            "wildcard": true
          }
        }
      },
      {
        "id": 29,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Obtén los nodos intermedios en paths de amistad.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*2..3]->(b:Persona) RETURN nodes(p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["nodes"],
            "wildcard": true
          }
        }
      },
      {
        "id": 30,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Obtén las relaciones de un path.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN relationships(p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["relationships"],
            "wildcard": true
          }
        }
      },
      {
        "id": 31,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén personas junto con la universidad en la que estudiaron.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:ESTUDIO_EN]->(u:Universidad) RETURN p.nombre, u.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["ESTUDIO_EN"],
            "wildcard": true
          }
        }
      },
      {
        "id": 32,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra universidades con más de un estudiante.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:ESTUDIO_EN]->(u:Universidad) WITH u, count(p) as total WHERE total > 1 RETURN u.nombre, total",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 33,
        "tipo": "fix_query",
        "nivel": "medio",
        "enunciado": "Corrige la consulta para usar WITH correctamente.",
        "query_base": "MATCH (p:Persona) WITH p MATCH (p)-[:VIVE_EN]->(c) RETURN c",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:VIVE_EN]->(c) RETURN c",
          "validacion": {
            "tipo": "estructura",
            "expected": ["MATCH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 34,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para devolver solo ciudades únicas.",
        "query_base": "MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN DISTINCT c.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 35,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que trabajan con alguien que usa Neo4j.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia {nombre:'Neo4j'}) RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["TRABAJA_CON"],
            "wildcard": true
          }
        }
      },
      {
        "id": 36,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que viven en una ciudad distinta a la de sus amigos.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona),(p)-[:VIVE_EN]->(c1),(a)-[:VIVE_EN]->(c2) WHERE c1 <> c2 RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["<>"],
            "wildcard": true
          }
        }
      },
      {
        "id": 37,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que gestionan proyectos en los que no participan.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:GESTIONA]->(pr:Proyecto) WHERE NOT (p)-[:PARTICIPA_EN]->(pr) RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["NOT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 38,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén personas junto con el número de amigos.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 39,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para mostrar solo personas con más de un amigo.",
        "query_base": "MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) RETURN p.nombre, count(a)",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) WITH p, count(a) as total WHERE total > 1 RETURN p.nombre, total",
          "validacion": {
            "tipo": "estructura",
            "expected": ["WITH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 40,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra caminos entre personas donde todas las relaciones tienen propiedad since > 2018.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*]->(b:Persona) WHERE ALL(r IN relationships(p) WHERE r.since > 2018) RETURN p",
          "validacion": {
            "tipo": "estructura",
            "expected": ["ALL"],
            "wildcard": true
          }
        }
      },
      {
        "id": 41,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén personas junto con el número de proyectos en los que participan.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre, count(pr)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 42,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para incluir también personas sin proyectos.",
        "query_base": "MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre, count(pr)",
        "respuesta": {
          "query": "MATCH (p:Persona) OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN p.nombre, count(pr)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["OPTIONAL MATCH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 43,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra personas que participan en más de un proyecto.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) WITH p, count(pr) as total WHERE total > 1 RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["WITH","WHERE"],
            "wildcard": true
          }
        }
      },
      {
        "id": 44,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén proyectos junto con el número de personas distintas que participan en ellos.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(DISTINCT p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 45,
        "tipo": "fix_query",
        "nivel": "medio",
        "enunciado": "Corrige la consulta para evitar duplicados en el conteo.",
        "query_base": "MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p)",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(DISTINCT p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 46,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que trabajan en empresas donde al menos uno de sus compañeros usa Neo4j.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa)<-[:TRABAJA_EN]-(o:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia {nombre:'Neo4j'}) RETURN DISTINCT p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 47,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que tienen amigos que trabajan en una empresa distinta a la suya.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e1:Empresa),(p)-[:AMIGO_DE]->(a:Persona)-[:TRABAJA_EN]->(e2:Empresa) WHERE e1 <> e2 RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["<>"],
            "wildcard": true
          }
        }
      },
      {
        "id": 48,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra pares de personas que viven en la misma ciudad y trabajan juntas.",
        "respuesta": {
          "query": "MATCH (p1:Persona)-[:TRABAJA_CON]->(p2:Persona),(p1)-[:VIVE_EN]->(c),(p2)-[:VIVE_EN]->(c) RETURN p1.nombre, p2.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["VIVE_EN"],
            "wildcard": true
          }
        }
      },
      {
        "id": 49,
        "tipo": "modify_query",
        "nivel": "dificil",
        "enunciado": "Modifica la consulta para evitar pares duplicados.",
        "query_base": "MATCH (p1:Persona)-[:TRABAJA_CON]->(p2:Persona) RETURN p1.nombre, p2.nombre",
        "respuesta": {
          "query": "MATCH (p1:Persona)-[:TRABAJA_CON]->(p2:Persona) WHERE id(p1) < id(p2) RETURN p1.nombre, p2.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["id"],
            "wildcard": true
          }
        }
      },
      {
        "id": 50,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que están conectadas por amistad a alguien que participa en más de un proyecto.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) WITH a, count(pr) as total, p WHERE total > 1 RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["WITH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 51,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que usan exactamente una tecnología.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) WITH p, count(t) as total WHERE total = 1 RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 52,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que no tienen amigos.",
        "respuesta": {
          "query": "MATCH (p:Persona) WHERE NOT (p)-[:AMIGO_DE]->() RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["NOT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 53,
        "tipo": "fix_query",
        "nivel": "dificil",
        "enunciado": "Corrige la consulta para usar OPTIONAL MATCH correctamente.",
        "query_base": "MATCH (p:Persona) MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN p, pr",
        "respuesta": {
          "query": "MATCH (p:Persona) OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN p, pr",
          "validacion": {
            "tipo": "estructura",
            "expected": ["OPTIONAL MATCH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 54,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra caminos de amistad donde todos los nodos intermedios viven en la misma ciudad.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*2..3]->(b:Persona) WHERE ALL(n IN nodes(p)[1..-1] WHERE (n)-[:VIVE_EN]->(:Ciudad)) RETURN p",
          "validacion": {
            "tipo": "estructura",
            "expected": ["ALL"],
            "wildcard": true
          }
        }
      },
      {
        "id": 55,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que aparecen en más de un path de amistad.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) UNWIND nodes(p) as n WITH n, count(*) as total WHERE total > 1 RETURN n, total",
          "validacion": {
            "tipo": "estructura",
            "expected": ["UNWIND"],
            "wildcard": true
          }
        }
      },
      {
        "id": 56,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén personas junto con todas las tecnologías que usan.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN p.nombre, collect(t.nombre)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["collect"],
            "wildcard": true
          }
        }
      },
      {
        "id": 57,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para devolver solo personas que usan más de una tecnología.",
        "query_base": "MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN p.nombre, collect(t.nombre)",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) WITH p, collect(t) as techs WHERE size(techs) > 1 RETURN p.nombre, techs",
          "validacion": {
            "tipo": "estructura",
            "expected": ["size"],
            "wildcard": true
          }
        }
      },
      {
        "id": 58,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra tecnologías usadas por personas que trabajan en TechCorp.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(:Empresa {nombre:'TechCorp'}),(p)-[:USA_TECNOLOGIA]->(t:Tecnologia) RETURN DISTINCT t.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 59,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que trabajan en todas las empresas presentes en el grafo.",
        "respuesta": {
          "query": "MATCH (e:Empresa) WITH count(e) as total MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) WITH p, count(DISTINCT e) as c, total WHERE c = total RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["WITH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 60,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que comparten todas sus tecnologías con al menos otra persona.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:USA_TECNOLOGIA]->(t:Tecnologia) WITH p, collect(t) as techs MATCH (o:Persona)-[:USA_TECNOLOGIA]->(t2:Tecnologia) WITH p, techs, o, collect(t2) as techs2 WHERE techs = techs2 AND p <> o RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["collect"],
            "wildcard": true
          }
        }
      },
      {
        "id": 61,
        "tipo": "fix_query",
        "nivel": "dificil",
        "enunciado": "Corrige la consulta para usar correctamente UNWIND.",
        "query_base": "MATCH p=(a)-[:AMIGO_DE*]->(b) RETURN UNWIND nodes(p)",
        "respuesta": {
          "query": "MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n",
          "validacion": {
            "tipo": "estructura",
            "expected": ["UNWIND"],
            "wildcard": true
          }
        }
      },
      {
        "id": 62,
        "tipo": "modify_query",
        "nivel": "dificil",
        "enunciado": "Modifica la consulta para contar cuántas veces aparece cada nodo en paths.",
        "query_base": "MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n",
        "respuesta": {
          "query": "MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n, count(*)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 63,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que están conectadas a todas las demás mediante algún path.",
        "respuesta": {
          "query": "MATCH (p:Persona) MATCH (p)-[:AMIGO_DE*]->(o:Persona) WITH p, count(DISTINCT o) as total MATCH (x:Persona) WITH p, total, count(x) as all WHERE total = all - 1 RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 64,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que conectan diferentes ciudades a través de amistad.",
        "respuesta": {
          "query": "MATCH (a:Persona)-[:AMIGO_DE]->(b:Persona)-[:AMIGO_DE]->(c:Persona),(a)-[:VIVE_EN]->(c1),(c)-[:VIVE_EN]->(c2) WHERE c1 <> c2 RETURN b.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["<>"],
            "wildcard": true
          }
        }
      },
      {
        "id": 65,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra el nodo más frecuente en paths de amistad.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*]->(b:Persona) UNWIND nodes(p) as n RETURN n, count(*) as total ORDER BY total DESC LIMIT 1",
          "validacion": {
            "tipo": "estructura",
            "expected": ["ORDER BY","LIMIT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 66,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén todas las personas junto con la empresa en la que trabajan y la ciudad en la que viven.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa),(p)-[:VIVE_EN]->(c:Ciudad) RETURN p.nombre, e.nombre, c.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["MATCH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 67,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Cuenta cuántas personas trabajan en cada empresa y viven en Madrid.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa),(p)-[:VIVE_EN]->(:Ciudad {nombre:'Madrid'}) RETURN e.nombre, count(p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 68,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para ordenar los resultados por número de empleados descendente.",
        "query_base": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p)",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e:Empresa) RETURN e.nombre, count(p) as total ORDER BY total DESC",
          "validacion": {
            "tipo": "estructura",
            "expected": ["ORDER BY"],
            "wildcard": true
          }
        }
      },
      {
        "id": 69,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén personas que viven en la misma ciudad que sus compañeros de trabajo.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona),(p)-[:VIVE_EN]->(c),(o)-[:VIVE_EN]->(c) RETURN DISTINCT p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 70,
        "tipo": "fix_query",
        "nivel": "medio",
        "enunciado": "Corrige la consulta para usar correctamente ORDER BY.",
        "query_base": "MATCH (p:Persona) RETURN p.nombre ORDER p.nombre",
        "respuesta": {
          "query": "MATCH (p:Persona) RETURN p.nombre ORDER BY p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["ORDER BY"],
            "wildcard": true
          }
        }
      },
      {
        "id": 71,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra proyectos gestionados por personas que trabajan en DataSoft.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(:Empresa {nombre:'DataSoft'}),(p)-[:GESTIONA]->(pr:Proyecto) RETURN pr.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["GESTIONA"],
            "wildcard": true
          }
        }
      },
      {
        "id": 72,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén personas junto con el número de amigos y el número de proyectos en los que participan.",
        "respuesta": {
          "query": "MATCH (p:Persona) OPTIONAL MATCH (p)-[:AMIGO_DE]->(a) WITH p, count(a) as amigos OPTIONAL MATCH (p)-[:PARTICIPA_EN]->(pr) RETURN p.nombre, amigos, count(pr)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["WITH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 73,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para mostrar solo personas con al menos un amigo.",
        "query_base": "MATCH (p:Persona)-[:AMIGO_DE]->(a) RETURN p.nombre, count(a)",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a) WITH p, count(a) as total WHERE total > 0 RETURN p.nombre, total",
          "validacion": {
            "tipo": "estructura",
            "expected": ["WHERE"],
            "wildcard": true
          }
        }
      },
      {
        "id": 74,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas cuyos amigos participan en proyectos distintos a los suyos.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:PARTICIPA_EN]->(pr1),(p)-[:AMIGO_DE]->(a:Persona)-[:PARTICIPA_EN]->(pr2) WHERE pr1 <> pr2 RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["<>"],
            "wildcard": true
          }
        }
      },
      {
        "id": 75,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que trabajan con alguien que vive en otra ciudad.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona),(p)-[:VIVE_EN]->(c1),(o)-[:VIVE_EN]->(c2) WHERE c1 <> c2 RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["<>"],
            "wildcard": true
          }
        }
      },
      {
        "id": 76,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que comparten al menos una tecnología.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona) MATCH (p)-[:USA_TECNOLOGIA]->(t:Tecnologia),(a)-[:USA_TECNOLOGIA]->(t) RETURN DISTINCT p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 77,
        "tipo": "fix_query",
        "nivel": "dificil",
        "enunciado": "Corrige la consulta para aplicar correctamente múltiples MATCH.",
        "query_base": "MATCH (p:Persona)-[:TRABAJA_EN]->(e) MATCH (p)-[:VIVE_EN]->(c) RETURN p,e,c",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e),(p)-[:VIVE_EN]->(c) RETURN p,e,c",
          "validacion": {
            "tipo": "estructura",
            "expected": ["MATCH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 78,
        "tipo": "modify_query",
        "nivel": "dificil",
        "enunciado": "Modifica la consulta para devolver solo nombres únicos de personas.",
        "query_base": "MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona) RETURN p.nombre",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_CON]->(o:Persona) RETURN DISTINCT p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 79,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén personas junto con el número total de relaciones que tienen.",
        "respuesta": {
          "query": "MATCH (p:Persona)--() RETURN p.nombre, count(*)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["--"],
            "wildcard": true
          }
        }
      },
      {
        "id": 80,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra personas conectadas a al menos un proyecto a través de cualquier relación.",
        "respuesta": {
          "query": "MATCH (p:Persona)-->(:Proyecto) RETURN DISTINCT p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["--"],
            "wildcard": true
          }
        }
      },
      {
        "id": 81,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que están a distancia exactamente 2 en la red de amistad.",
        "respuesta": {
          "query": "MATCH (a:Persona)-[:AMIGO_DE*2..2]->(b:Persona) RETURN a.nombre, b.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["*2..2"],
            "wildcard": true
          }
        }
      },
      {
        "id": 82,
        "tipo": "modify_query",
        "nivel": "dificil",
        "enunciado": "Modifica la consulta para excluir relaciones directas.",
        "query_base": "MATCH (a:Persona)-[:AMIGO_DE*1..2]->(b:Persona) RETURN a,b",
        "respuesta": {
          "query": "MATCH (a:Persona)-[:AMIGO_DE*2..2]->(b:Persona) RETURN a,b",
          "validacion": {
            "tipo": "estructura",
            "expected": ["*2..2"],
            "wildcard": true
          }
        }
      },
      {
        "id": 83,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra ciudades donde viven personas que trabajan en TechCorp.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(:Empresa {nombre:'TechCorp'}),(p)-[:VIVE_EN]->(c:Ciudad) RETURN DISTINCT c.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 84,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén universidades junto con el número de personas que estudiaron en ellas.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:ESTUDIO_EN]->(u:Universidad) RETURN u.nombre, count(p)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 85,
        "tipo": "fix_query",
        "nivel": "medio",
        "enunciado": "Corrige la consulta para usar DISTINCT correctamente.",
        "query_base": "MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN c.nombre",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN DISTINCT c.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 86,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas cuyos amigos viven todos en la misma ciudad.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona),(a)-[:VIVE_EN]->(c:Ciudad) WITH p, collect(DISTINCT c) as ciudades WHERE size(ciudades)=1 RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["collect","size"],
            "wildcard": true
          }
        }
      },
      {
        "id": 87,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que trabajan en empresas donde todos los empleados viven en la misma ciudad.",
        "respuesta": {
          "query": "MATCH (e:Empresa)<-[:TRABAJA_EN]-(p:Persona),(p)-[:VIVE_EN]->(c:Ciudad) WITH e, collect(DISTINCT c) as ciudades WHERE size(ciudades)=1 MATCH (e)<-[:TRABAJA_EN]-(p2:Persona) RETURN p2.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["collect","size"],
            "wildcard": true
          }
        }
      },
      {
        "id": 88,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que tienen al menos un amigo en cada ciudad.",
        "respuesta": {
          "query": "MATCH (c:Ciudad) WITH collect(c) as ciudades MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:VIVE_EN]->(c2:Ciudad) WITH p, collect(DISTINCT c2) as ciudades2, ciudades WHERE ciudades2 = ciudades RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["collect"],
            "wildcard": true
          }
        }
      },
      {
        "id": 90,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que están conectadas por amistad a alguien que trabaja en todas las empresas.",
        "respuesta": {
          "query": "MATCH (e:Empresa) WITH count(e) as total MATCH (a:Persona)-[:TRABAJA_EN]->(e:Empresa) WITH a, count(DISTINCT e) as c, total WHERE c = total MATCH (p:Persona)-[:AMIGO_DE]->(a) RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["WITH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 91,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que tienen más amigos que la media.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a) WITH p, count(a) as total WITH collect(total) as totales, p, total WITH p, total, reduce(s=0, x IN totales | s + x) / size(totales) as media WHERE total > media RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["avg"],
            "wildcard": true
          }
        }
      },
      {
        "id": 92,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que están conectadas con otras mediante más de un camino distinto.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) WITH a,b,count(p) as total WHERE total > 1 RETURN a.nombre, b.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["count"],
            "wildcard": true
          }
        }
      },
      {
        "id": 93,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas cuyos amigos trabajan en todas las empresas.",
        "respuesta": {
          "query": "MATCH (e:Empresa) WITH collect(e) as empresas MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:TRABAJA_EN]->(e2:Empresa) WITH p, collect(DISTINCT e2) as empresas2, empresas WHERE empresas2 = empresas RETURN p.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["collect"],
            "wildcard": true
          }
        }
      },
      {
        "id": 94,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que están en todos los caminos entre dos nodos específicos.",
        "respuesta": {
          "query": "MATCH p=(a:Persona {nombre:'Ana'})-[:AMIGO_DE*]->(b:Persona {nombre:'Carlos'}) UNWIND nodes(p) as n RETURN n, count(*) as total ORDER BY total DESC",
          "validacion": {
            "tipo": "estructura",
            "expected": ["UNWIND"],
            "wildcard": true
          }
        }
      },
      {
        "id": 95,
        "tipo": "modify_query",
        "nivel": "dificil",
        "enunciado": "Modifica la consulta para devolver solo los nodos más frecuentes.",
        "query_base": "MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n, count(*)",
        "respuesta": {
          "query": "MATCH p=(a)-[:AMIGO_DE*]->(b) UNWIND nodes(p) as n RETURN n, count(*) as total ORDER BY total DESC LIMIT 1",
          "validacion": {
            "tipo": "estructura",
            "expected": ["LIMIT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 96,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Obtén personas junto con todas las ciudades en las que tienen amigos.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:AMIGO_DE]->(a:Persona)-[:VIVE_EN]->(c:Ciudad) RETURN p.nombre, collect(DISTINCT c.nombre)",
          "validacion": {
            "tipo": "estructura",
            "expected": ["collect"],
            "wildcard": true
          }
        }
      },
      {
        "id": 97,
        "tipo": "write_query",
        "nivel": "medio",
        "enunciado": "Encuentra empresas donde trabajan personas que usan Python.",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:USA_TECNOLOGIA]->(:Tecnologia {nombre:'Python'}),(p)-[:TRABAJA_EN]->(e:Empresa) RETURN DISTINCT e.nombre",
          "validacion": {
            "tipo": "estructura",
            "expected": ["DISTINCT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 98,
        "tipo": "fix_query",
        "nivel": "medio",
        "enunciado": "Corrige la consulta para usar correctamente múltiples relaciones.",
        "query_base": "MATCH (p:Persona)-[:TRABAJA_EN]->(e)-[:VIVE_EN]->(c) RETURN p,e,c",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:TRABAJA_EN]->(e),(p)-[:VIVE_EN]->(c) RETURN p,e,c",
          "validacion": {
            "tipo": "estructura",
            "expected": ["MATCH"],
            "wildcard": true
          }
        }
      },
      {
        "id": 99,
        "tipo": "modify_query",
        "nivel": "medio",
        "enunciado": "Modifica la consulta para devolver solo los 2 proyectos con más participantes.",
        "query_base": "MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p)",
        "respuesta": {
          "query": "MATCH (p:Persona)-[:PARTICIPA_EN]->(pr:Proyecto) RETURN pr.nombre, count(p) as total ORDER BY total DESC LIMIT 2",
          "validacion": {
            "tipo": "estructura",
            "expected": ["LIMIT"],
            "wildcard": true
          }
        }
      },
      {
        "id": 100,
        "tipo": "write_query",
        "nivel": "dificil",
        "enunciado": "Encuentra personas que maximizan el número de conexiones indirectas en la red de amistad.",
        "respuesta": {
          "query": "MATCH p=(a:Persona)-[:AMIGO_DE*1..3]->(b:Persona) RETURN a.nombre, count(DISTINCT b) as total ORDER BY total DESC LIMIT 1",
          "validacion": {
            "tipo": "estructura",
            "expected": ["ORDER BY","LIMIT"],
            "wildcard": true
          }
        }
      }  
    ]
}

vector_json = {
  "ejercicios": [
    {
      "id": 1,
      "tipo": "modify_dataset",
      "nivel": "facil",
      "enunciado": "Agregue al vocabulario los textos 'tigre salvaje asiático' y 'león africano grande'. Luego ejecute una búsqueda usando la query 'felino'. Analice cómo cambian los resultados.",
      "respuesta": {
        "criterios": [
          "Inserción correcta de textos",
          "Reconstrucción válida del índice",
          "Uso correcto de búsqueda",
          "Interpretación semántica básica"
        ]
      }
    },
    {
      "id": 2,
      "tipo": "analyze_results",
      "nivel": "facil",
      "enunciado": "Ejecute búsquedas usando las queries 'vehículo rápido' y 'coche deportivo'. Compare los resultados obtenidos y explique cuál query parece más específica.",
      "respuesta": {
        "criterios": [
          "Ejecución correcta de búsquedas",
          "Comparación de rankings",
          "Interpretación contextual"
        ]
      }
    },
    {
      "id": 3,
      "tipo": "modify_dataset",
      "nivel": "facil",
      "enunciado": "Agregue al vocabulario los textos 'banco de inversión internacional' y 'banco para descansar'. Luego busque la palabra 'banco' y explique los casos de ambigüedad encontrados.",
      "respuesta": {
        "criterios": [
          "Inserción correcta",
          "Detección de ambigüedad",
          "Interpretación semántica"
        ]
      }
    },
    {
      "id": 4,
      "tipo": "compare_queries",
      "nivel": "facil",
      "enunciado": "Ejecute búsquedas usando 'pizza', 'pizza italiana' y 'pizza italiana tradicional'. Explique cómo cambia el ranking al agregar más contexto.",
      "respuesta": {
        "criterios": [
          "Comparación correcta",
          "Análisis contextual",
          "Interpretación del embedding"
        ]
      }
    },
    {
      "id": 5,
      "tipo": "modify_function",
      "nivel": "facil",
      "enunciado": "Modifique la función buscar() para que también devuelva el índice original del texto encontrado.",
      "codigo_base": "resultados.append({'texto': base[i], 'distancia': distancia, 'score': score})",
      "respuesta": {
        "criterios": [
          "Uso correcto del índice",
          "Modificación funcional",
          "Estructura válida del resultado"
        ]
      }
    },
    {
      "id": 6,
      "tipo": "analyze_results",
      "nivel": "facil",
      "enunciado": "Ejecute búsquedas usando la query 'animal'. Explique por qué algunos resultados parecen menos precisos.",
      "respuesta": {
        "criterios": [
          "Análisis de resultados",
          "Interpretación de ambigüedad",
          "Relación con contexto"
        ]
      }
    },
    {
      "id": 7,
      "tipo": "modify_dataset",
      "nivel": "facil",
      "enunciado": "Inserte en el vocabulario textos relacionados con astronomía y luego ejecute búsquedas sobre animales. Explique cómo afecta esto al sistema.",
      "respuesta": {
        "criterios": [
          "Inserción válida",
          "Análisis de contaminación semántica",
          "Interpretación del ranking"
        ]
      }
    },
    {
      "id": 8,
      "tipo": "complete_function",
      "nivel": "facil",
      "enunciado": "Complete la función calcular_score() usando la fórmula 1 / (1 + distancia).",
      "codigo_base": "def calcular_score(distancia):\n    # completar",
      "respuesta": {
        "criterios": [
          "Implementación correcta",
          "Uso válido de distancia",
          "Retorno funcional"
        ]
      }
    },
    {
      "id": 9,
      "tipo": "compare_queries",
      "nivel": "facil",
      "enunciado": "Compare resultados entre las queries 'tecnología' y 'computadora portátil moderna'. Explique cuál produce resultados más específicos.",
      "respuesta": {
        "criterios": [
          "Comparación válida",
          "Interpretación contextual",
          "Relación entre especificidad y embedding"
        ]
      }
    },
    {
      "id": 10,
      "tipo": "modify_dataset",
      "nivel": "facil",
      "enunciado": "Agregue tres tipos distintos de comida al vocabulario y ejecute búsquedas usando la palabra 'comida'. Explique cómo aparecen agrupaciones semánticas.",
      "respuesta": {
        "criterios": [
          "Inserción correcta",
          "Uso válido de búsquedas",
          "Interpretación de similitud"
        ]
      }
    },
    {
      "id": 11,
      "tipo": "analyze_results",
      "nivel": "facil",
      "enunciado": "Ejecute búsquedas usando la query 'objeto'. Explique por qué el sistema devuelve resultados débiles o ambiguos.",
      "respuesta": {
        "criterios": [
          "Interpretación de baja especificidad",
          "Relación con embeddings",
          "Análisis contextual"
        ]
      }
    },
    {
      "id": 12,
      "tipo": "modify_function",
      "nivel": "facil",
      "enunciado": "Modifique la función buscar() para que imprima también la distancia encontrada por FAISS.",
      "codigo_base": "resultados.append({'texto': base[i], 'score': score})",
      "respuesta": {
        "criterios": [
          "Uso correcto de distancia",
          "Modificación funcional",
          "Resultado válido"
        ]
      }
    },
    {
      "id": 13,
      "tipo": "compare_queries",
      "nivel": "facil",
      "enunciado": "Compare búsquedas usando 'ratón' y 'ratón inalámbrico computadora'. Explique diferencias semánticas observadas.",
      "respuesta": {
        "criterios": [
          "Comparación correcta",
          "Análisis de ambigüedad",
          "Interpretación contextual"
        ]
      }
    },
    {
      "id": 14,
      "tipo": "modify_dataset",
      "nivel": "facil",
      "enunciado": "Agregue palabras relacionadas con deportes y luego busque 'vehículo rápido'. Analice si aparecen resultados inesperados.",
      "respuesta": {
        "criterios": [
          "Inserción correcta",
          "Análisis de contaminación",
          "Interpretación del ranking"
        ]
      }
    },
    {
      "id": 15,
      "tipo": "complete_function",
      "nivel": "facil",
      "enunciado": "Complete una función que reciba una query y ejecute embedding(query).",
      "codigo_base": "def generar_query(query):\n    # completar",
      "respuesta": {
        "criterios": [
          "Uso correcto de embedding",
          "Implementación funcional",
          "Retorno válido"
        ]
      }
    },
    {
      "id": 16,
      "tipo": "analyze_results",
      "nivel": "facil",
      "enunciado": "Ejecute búsquedas usando 'galaxia' y explique por qué aparecen ciertos resultados cercanos aunque no sean exactos.",
      "respuesta": {
        "criterios": [
          "Interpretación geométrica",
          "Relación entre proximidad y significado",
          "Análisis semántico"
        ]
      }
    },
    {
      "id": 17,
      "tipo": "modify_dataset",
      "nivel": "facil",
      "enunciado": "Agregue textos relacionados con videojuegos y luego ejecute búsquedas usando 'tecnología'. Explique el comportamiento del sistema.",
      "respuesta": {
        "criterios": [
          "Inserción correcta",
          "Relación entre dominios",
          "Interpretación semántica"
        ]
      }
    },
    {
      "id": 18,
      "tipo": "modify_function",
      "nivel": "facil",
      "enunciado": "Modifique la función buscar_filtrado() para usar un umbral mínimo de 0.5.",
      "codigo_base": "if r['score'] >= umbral:",
      "respuesta": {
        "criterios": [
          "Uso correcto de umbral",
          "Filtrado válido",
          "Modificación funcional"
        ]
      }
    },
    {
      "id": 19,
      "tipo": "compare_queries",
      "nivel": "facil",
      "enunciado": "Compare resultados entre las queries 'felino' y 'felino salvaje africano'. Explique cómo cambia el contexto.",
      "respuesta": {
        "criterios": [
          "Comparación contextual",
          "Interpretación semántica",
          "Análisis de especificidad"
        ]
      }
    },
    {
      "id": 20,
      "tipo": "analyze_results",
      "nivel": "facil",
      "enunciado": "Ejecute búsquedas usando 'computadora'. Explique por qué algunos resultados tecnológicos tienen scores más altos que otros.",
      "respuesta": {
        "criterios": [
          "Interpretación de score",
          "Relación semántica",
          "Análisis del ranking"
        ]
      }
    },
    {
      "id": 21,
      "tipo": "modify_function",
      "nivel": "medio",
      "enunciado": "Modifique la función buscar() para que los resultados se devuelvan ordenados por score descendente.",
      "codigo_base": "return resultados",
      "respuesta": {
        "criterios": [
          "Ordenamiento correcto",
          "Uso válido de score",
          "No alterar búsqueda FAISS"
        ]
      }
    },
    {
      "id": 22,
      "tipo": "extend_system",
      "nivel": "medio",
      "enunciado": "Implemente una función que permita agregar nuevos textos al vocabulario y reconstruir automáticamente el índice FAISS.",
      "codigo_base": "def agregar(self, texto):\n    # completar",
      "respuesta": {
        "criterios": [
          "Inserción dinámica correcta",
          "Reconstrucción válida del índice",
          "Actualización funcional del sistema"
        ]
      }
    },
    {
      "id": 23,
      "tipo": "analyze_results",
      "nivel": "medio",
      "enunciado": "Ejecute búsquedas usando las queries 'automóvil', 'coche', 'vehículo' y 'carro'. Compare diferencias de ranking y similitud.",
      "respuesta": {
        "criterios": [
          "Comparación semántica",
          "Interpretación lingüística",
          "Análisis contextual"
        ]
      }
    },
    {
      "id": 24,
      "tipo": "modify_function",
      "nivel": "medio",
      "enunciado": "Modifique la función buscar_filtrado() para permitir que el usuario envíe el valor de k dinámicamente.",
      "codigo_base": "def buscar_filtrado(query, base, index, umbral=0.3, k=5):",
      "respuesta": {
        "criterios": [
          "Uso dinámico de k",
          "Filtrado funcional",
          "Modificación correcta de parámetros"
        ]
      }
    },
    {
      "id": 25,
      "tipo": "compare_queries",
      "nivel": "medio",
      "enunciado": "Compare resultados entre una query de una palabra y una frase larga relacionada. Explique cómo cambia el embedding.",
      "respuesta": {
        "criterios": [
          "Comparación contextual",
          "Interpretación de embeddings",
          "Relación entre contexto y ranking"
        ]
      }
    },
    {
      "id": 26,
      "tipo": "extend_system",
      "nivel": "medio",
      "enunciado": "Implemente una función que exporte los resultados de búsqueda a un diccionario JSON con texto, score y distancia.",
      "codigo_base": "def exportar_resultados(resultados):\n    # completar",
      "respuesta": {
        "criterios": [
          "Exportación correcta",
          "Formato JSON válido",
          "Persistencia estructurada"
        ]
      }
    },
    {
      "id": 27,
      "tipo": "analyze_results",
      "nivel": "medio",
      "enunciado": "Inserte varios textos muy similares y analice cómo cambia el ranking cuando existen múltiples embeddings cercanos.",
      "respuesta": {
        "criterios": [
          "Inserción válida",
          "Interpretación de saturación semántica",
          "Análisis de ambigüedad"
        ]
      }
    },
    {
      "id": 28,
      "tipo": "modify_dataset",
      "nivel": "medio",
      "enunciado": "Agregue frases extremadamente largas al vocabulario y compare los resultados contra frases cortas.",
      "respuesta": {
        "criterios": [
          "Inserción válida",
          "Análisis contextual",
          "Interpretación de embeddings largos"
        ]
      }
    },
    {
      "id": 29,
      "tipo": "modify_function",
      "nivel": "medio",
      "enunciado": "Cambie la fórmula de score por una nueva función distinta a 1/(1+distancia) y compare resultados.",
      "codigo_base": "score = 1 / (1 + distancia)",
      "respuesta": {
        "criterios": [
          "Modificación funcional",
          "Comparación de comportamiento",
          "Interpretación matemática básica"
        ]
      }
    },
    {
      "id": 30,
      "tipo": "compare_queries",
      "nivel": "medio",
      "enunciado": "Compare búsquedas usando 'animal peligroso', 'felino peligroso' y 'felino salvaje africano peligroso'.",
      "respuesta": {
        "criterios": [
          "Comparación contextual",
          "Interpretación de especificidad",
          "Análisis semántico"
        ]
      }
    },
    {
      "id": 31,
      "tipo": "extend_system",
      "nivel": "medio",
      "enunciado": "Implemente una función que registre cada búsqueda junto con su timestamp y score máximo.",
      "codigo_base": "def registrar_busqueda(query, score):\n    # completar",
      "respuesta": {
        "criterios": [
          "Logging correcto",
          "Persistencia funcional",
          "Uso válido de score"
        ]
      }
    },
    {
      "id": 32,
      "tipo": "analyze_results",
      "nivel": "medio",
      "enunciado": "Ejecute búsquedas con errores ortográficos intencionales y explique cómo responde el sistema.",
      "respuesta": {
        "criterios": [
          "Pruebas válidas",
          "Análisis de robustez",
          "Interpretación de limitaciones"
        ]
      }
    },
    {
      "id": 33,
      "tipo": "modify_function",
      "nivel": "medio",
      "enunciado": "Modifique la función buscar() para mostrar únicamente resultados cuyo score sea mayor a 0.4.",
      "codigo_base": "for j, i in enumerate(indices[0]):",
      "respuesta": {
        "criterios": [
          "Filtrado correcto",
          "Uso válido de score",
          "No romper la búsqueda"
        ]
      }
    },
    {
      "id": 34,
      "tipo": "extend_system",
      "nivel": "medio",
      "enunciado": "Implemente una función que permita buscar únicamente dentro de una categoría específica como animales o tecnología.",
      "codigo_base": "def buscar_categoria(query, categoria):\n    # completar",
      "respuesta": {
        "criterios": [
          "Filtrado correcto por categoría",
          "Separación de dominios",
          "Implementación funcional"
        ]
      }
    },
    {
      "id": 35,
      "tipo": "compare_queries",
      "nivel": "medio",
      "enunciado": "Compare resultados usando IndexFlatL2 e IndexFlatIP. Explique diferencias observadas.",
      "respuesta": {
        "criterios": [
          "Cambio correcto de índice",
          "Comparación válida",
          "Interpretación geométrica"
        ]
      }
    },
    {
      "id": 36,
      "tipo": "modify_dataset",
      "nivel": "medio",
      "enunciado": "Agregue textos de múltiples dominios como política, cocina y videojuegos. Analice contaminación semántica.",
      "respuesta": {
        "criterios": [
          "Inserción válida",
          "Análisis de contaminación",
          "Interpretación contextual"
        ]
      }
    },
    {
      "id": 37,
      "tipo": "extend_system",
      "nivel": "medio",
      "enunciado": "Implemente una función que calcule similitud entre dos textos usando embeddings sin utilizar FAISS.",
      "codigo_base": "def similitud(texto1, texto2):\n    # completar",
      "respuesta": {
        "criterios": [
          "Uso correcto de embeddings",
          "Cálculo válido de similitud",
          "Interpretación funcional"
        ]
      }
    },
    {
      "id": 38,
      "tipo": "analyze_results",
      "nivel": "medio",
      "enunciado": "Analice casos donde scores altos producen resultados incorrectos o inesperados.",
      "respuesta": {
        "criterios": [
          "Identificación de anomalías",
          "Interpretación geométrica",
          "Análisis de limitaciones"
        ]
      }
    },
    {
      "id": 39,
      "tipo": "modify_function",
      "nivel": "medio",
      "enunciado": "Modifique la función buscar() para devolver también la categoría del texto encontrado.",
      "codigo_base": "resultados.append({'texto': base[i]})",
      "respuesta": {
        "criterios": [
          "Integración correcta de categorías",
          "Modificación funcional",
          "Resultados estructurados"
        ]
      }
    },
    {
      "id": 40,
      "tipo": "compare_queries",
      "nivel": "medio",
      "enunciado": "Compare el comportamiento del sistema usando bases pequeñas especializadas frente a bases grandes mezcladas.",
      "respuesta": {
        "criterios": [
          "Comparación válida",
          "Análisis de especialización",
          "Interpretación de ruido semántico"
        ]
      }
    },
    {
      "id": 41,
      "tipo": "extend_system",
      "nivel": "dificil",
      "enunciado": "Implemente una función llamada buscar_multidominio() que permita recibir una query y retornar resultados agrupados por categoría ('animales', 'vehículos', 'tecnología'). El sistema debe filtrar resultados con score menor a 0.4.",
      "codigo_base": "def buscar_multidominio(query):\n    # completar",
      "respuesta": {
        "criterios": [
          "Agrupación correcta por categoría",
          "Filtrado válido",
          "Uso correcto de score",
          "Estructura funcional"
        ]
      }
    },
    {
      "id": 42,
      "tipo": "extend_system",
      "nivel": "dificil",
      "enunciado": "Implemente persistencia completa del índice FAISS utilizando escritura y lectura desde disco.",
      "codigo_base": "faiss.write_index(index, 'indice.faiss')",
      "respuesta": {
        "criterios": [
          "Persistencia funcional",
          "Carga correcta del índice",
          "Reutilización válida del sistema"
        ]
      }
    },
    {
      "id": 43,
      "tipo": "modify_function",
      "nivel": "dificil",
      "enunciado": "Modifique el sistema para detectar posibles queries fuera de dominio utilizando score promedio mínimo.",
      "codigo_base": "def detectar_fuera_dominio(query):\n    # completar",
      "respuesta": {
        "criterios": [
          "Uso correcto de score",
          "Detección funcional",
          "Interpretación de umbrales"
        ]
      }
    },
    {
      "id": 44,
      "tipo": "extend_system",
      "nivel": "dificil",
      "enunciado": "Implemente una función que elimine textos del vocabulario y reconstruya completamente el índice FAISS.",
      "codigo_base": "def eliminar(texto):\n    # completar",
      "respuesta": {
        "criterios": [
          "Eliminación correcta",
          "Reconstrucción válida",
          "Consistencia del índice"
        ]
      }
    },
    {
      "id": 45,
      "tipo": "analyze_results",
      "nivel": "dificil",
      "enunciado": "Analice por qué dos textos semánticamente distintos pueden terminar geométricamente cercanos dentro del espacio vectorial.",
      "respuesta": {
        "criterios": [
          "Interpretación geométrica",
          "Comprensión de embeddings",
          "Análisis de limitaciones semánticas"
        ]
      }
    },
    {
      "id": 46,
      "tipo": "extend_system",
      "nivel": "dificil",
      "enunciado": "Construya un mini recomendador semántico que sugiera textos similares a partir del historial de búsquedas realizadas.",
      "codigo_base": "historial = []",
      "respuesta": {
        "criterios": [
          "Uso correcto de historial",
          "Recomendación funcional",
          "Aplicación de similitud semántica"
        ]
      }
    },
    {
      "id": 47,
      "tipo": "modify_function",
      "nivel": "dificil",
      "enunciado": "Modifique buscar_filtrado() para calcular dinámicamente el umbral usando el score promedio de los resultados.",
      "codigo_base": "def buscar_filtrado(query, base, index, umbral=0.3, k=5):",
      "respuesta": {
        "criterios": [
          "Cálculo dinámico correcto",
          "Uso válido de promedio",
          "Filtrado funcional"
        ]
      }
    },
    {
      "id": 48,
      "tipo": "extend_system",
      "nivel": "dificil",
      "enunciado": "Implemente una función que compare múltiples queries simultáneamente y devuelva los textos más relevantes para todas ellas.",
      "codigo_base": "def comparar_queries(queries):\n    # completar",
      "respuesta": {
        "criterios": [
          "Procesamiento múltiple",
          "Agregación correcta",
          "Interpretación de relevancia"
        ]
      }
    },
    {
      "id": 49,
      "tipo": "analyze_results",
      "nivel": "dificil",
      "enunciado": "Compare el comportamiento del sistema usando textos extremadamente cortos frente a descripciones largas y detalladas.",
      "respuesta": {
        "criterios": [
          "Comparación contextual",
          "Interpretación de embeddings",
          "Análisis de recuperación semántica"
        ]
      }
    },
    {
      "id": 50,
      "tipo": "extend_system",
      "nivel": "dificil",
      "enunciado": "Construya un mini sistema semántico completo que incluya embeddings, índice FAISS, score, filtrado, logging y persistencia básica. Luego explique fortalezas, limitaciones y posibles usos empresariales.",
      "codigo_base": "class BuscadorSemantico:\n    # extender sistema",
      "respuesta": {
        "criterios": [
          "Integración completa",
          "Uso correcto de FAISS",
          "Persistencia funcional",
          "Logging válido",
          "Análisis crítico del sistema"
        ]
      }
    }
  ]
}

def parse_grafos(data, filepath):
    md = "# Banco de Ejercicios: Neo4j Cypher\n\n"
    if "metadata" in data:
        for k, v in data["metadata"].items():
            md += f"* **{k.capitalize()}:** {v}\n"
    md += "\n---\n\n"

    for ej in data.get("ejercicios", []):
        md += f"## Ejercicio {ej.get('id')} ({ej.get('nivel', '').capitalize()})\n"
        md += f"**Tipo:** `{ej.get('tipo')}`\n\n"
        md += f"**Enunciado:** {ej.get('enunciado')}\n\n"
        
        if "query_base" in ej:
            md += "**Query Base:**\n```cypher\n" + ej["query_base"] + "\n```\n\n"
            
        md += "### SOLUCIÓN\n\n"
        
        resp = ej.get("respuesta", {})
        if "query" in resp:
            md += "**Query:**\n```cypher\n" + resp["query"] + "\n```\n\n"
        
        val = resp.get("validacion", {})
        if val:
            md += "**Validación:**\n"
            md += f"- Tipo: `{val.get('tipo')}`\n"
            if "expected" in val:
                md += f"- Esperado: `{val.get('expected')}`\n"
            if "wildcard" in val:
                md += f"- Wildcard: `{val.get('wildcard')}`\n"
        
        md += "\n---\n\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)

def parse_vectoriales(data, filepath):
    md = "# Banco de Ejercicios: Bases Vectoriales y FAISS\n\n---\n\n"

    for ej in data.get("ejercicios", []):
        md += f"## Ejercicio {ej.get('id')} ({ej.get('nivel', '').capitalize()})\n"
        md += f"**Tipo:** `{ej.get('tipo')}`\n\n"
        md += f"**Enunciado:** {ej.get('enunciado')}\n\n"
        
        if "codigo_base" in ej:
            md += "**Código Base:**\n```python\n" + ej["codigo_base"] + "\n```\n\n"
            
        md += "### SOLUCIÓN / CRITERIOS\n\n"
        
        resp = ej.get("respuesta", {})
        criterios = resp.get("criterios", [])
        if criterios:
            md += "**Criterios de Evaluación:**\n"
            for c in criterios:
                md += f"- {c}\n"
        
        md += "\n---\n\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)

grafos_path = r"C:\Users\symid\Documents\Second Brain\500 Biblioteca\preguntas_grafos.md"
vector_path = r"C:\Users\symid\Documents\Second Brain\500 Biblioteca\preguntas_vectoriales.md"

parse_grafos(grafos_json, grafos_path)
parse_vectoriales(vector_json, vector_path)
print("Parsed files in typical markdown format.")
