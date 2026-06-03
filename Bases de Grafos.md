---
materia: Bases de Datos 2
---

# Bases de Grafos: Persistencia Basada en Adyacencia

Las bases de datos de grafos resuelven la ineficiencia del modelo relacional ante la **profundidad de las conexiones**. Mientras que SQL escala exponencialmente el coste de consulta mediante uniones (*joins*), los grafos mantienen un coste constante al tratar las relaciones como estructuras físicas de acceso directo (adyacencia indexada).

---

## El Cambio de Paradigma: Del Filtro al Recorrido

En un modelo relacional, se filtran filas; en un grafo, se **recorren caminos**.

- **Relación como Ciudadano de Primera Clase**: Las conexiones tienen identidad, dirección y propiedades propias. No son claves foráneas, son punteros directos.
- **Navegación vs Búsqueda**: El valor no reside en el atributo del nodo, sino en la topología de la red (quién conoce a quién, a través de qué camino).

---

## Modelado Orientado a la Consulta

La regla de oro del diseño en grafos es la **especificidad del acceso**. No se modela para almacenar, sino para responder preguntas de negocio de alta conectividad.

### Decisión de Diseño: ¿Nodo o Propiedad?
- **Propiedad**: Datos informativos que no participan en la red de conexiones (ej. edad, nombre).
- **Nodo**: Entidades que actúan como puntos de convergencia o que requieren ser consultadas de forma independiente (ej. Proyectos, Empresas).

---

## Análisis Topológico y Redes

El análisis de grafos permite extraer información estructural que el modelo documental o relacional oculta:

1.  **Centralidad**: Identificación de nodos con mayor volumen de relaciones (*hubs*).
2.  **Intermediación (*Betweenness*)**: Nodos puente que conectan comunidades. Su eliminación fragmenta la red.
3.  **Distancia y Resiliencia**: La longitud del camino (*path*) define la fuerza del vínculo. Múltiples caminos entre dos nodos indican redundancia y estabilidad en la red.

---

## Referencias
1. [[Bases de datos 2]]
2. [[Cypher|Neo4j]] — Implementación práctica y lenguaje de consulta.
3. [[Bases Vectoriales]] — El siguiente paso hacia la similitud semántica.
