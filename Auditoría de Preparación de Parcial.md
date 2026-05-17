# Auditoría de Preparación de Parcial

Esta nota registra la capacidad de los apuntes actuales para resolver el banco de ejercicios.

## Bloque A: Neo4j Cypher (100 Ejercicios)

| ID | Estado | Observación / Falta |
|---|---|---|
| 1-4 | ✅ | Cubierto por Cypher básico (MATCH, RETURN, LIMIT). |
| 5 | ✅ | Agregación implícita count(). |
| 6-8 | ✅ | MATCH múltiple, WHERE, ORDER BY. |
| 9 | ✅ | Cubierto por Cypher básico y avanzado (WITH). |
| 10 | ✅ | Longitud variable `*1..2`. |
| 11 | ✅ | MATCH de caminos. |
| 12-13 | ✅ | Función `length()`. |
| 14 | ✅ | OPTIONAL MATCH y IS NULL. |
| 15 | ✅ | Patrón de puente. |
| 16-23 | ✅ | Cubierto (id, DISTINCT, filtros). |
| 24-25 | ❌ | **Falta:** Explicación explícita de funciones de agregación matemáticas como `sum()`. |
| 26-30 | ✅ | Cubierto por Cypher avanzado (nodes, relationships). |
| 31-39 | ✅ | Cubierto. |
| 40 | ✅ | Predicado `ALL`. |
| 41-54 | ✅ | Cubierto. |
| 55 | ❌ | **Falta:** Explicación de la cláusula `UNWIND`. |
| 56-57 | ❌ | **Falta:** Función `size()` para listas y `collect()`. |
| 58-60 | ✅ | Cubierto por División Relacional en avanzado. |
| 61-62 | ❌ | **Falta:** `UNWIND` (repetido). |
| 63-90 | ✅ | Cubierto por lógica de avanzado (id, with, collect). |
| 91 | ❌ | **Falta:** Cálculo de medias con `avg()` o lógica manual más simple. |
| 92-100 | ✅ | Cubierto. |

---

## Bloque B: Vectoriales y FAISS (50 Ejercicios)

| ID | Estado | Observación / Falta |
|---|---|---|
| 1-4 | ✅ | Teoría de inserción, ambigüedad y contexto. |
| 5 | ❌ | **Falta:** Ejemplo de código de cómo acceder al índice `i` en un bucle de resultados. |
| 6-7 | ✅ | Fenómenos del espacio vectorial. |
| 8 | ✅ | Matemática del Score. |
| 9-11 | ✅ | Teoría de especificidad. |
| 12 | ❌ | **Falta:** Mostrar explícitamente cómo FAISS devuelve la matriz de `distancias`. |
| 13-17 | ✅ | Cubierto (ambigüedad, contaminación). |
| 18 | ✅ | Filtrado por umbral (Práctica). |
| 19-20 | ✅ | Teoría. |
| 21 | ❌ | **Falta:** Código para `sorted(resultados, key=...)` en Python. |
| 22 | ✅ | Ciclo de vida (Inserción caliente). |
| 23-33 | ✅ | Cubierto. |
| 34-36 | ✅ | Estrategias de filtrado (Metadata). |
| 37 | ❌ | **Falta:** Cómo calcular similitud sin FAISS (producto escalar o similar). |
| 38-41 | ✅ | Cubierto. |
| 42 | ✅ | Persistencia. |
| 43 | ❌ | **Falta:** Lógica de detección de "Out of Domain" por promedio de scores. |
| 44-50 | ✅ | Cubierto (eliminación, sistemas completos). |

---

## Resumen de Vacíos a Rellenar

1. **Cypher:**
   - Funciones de agregación: `sum()`, `avg()`, `min()`, `max()`.
   - Manipulación de listas: `size()`, `collect()`, `UNWIND`.
2. **Vectoriales:**
   - Python: Manipulación de resultados (ordenar diccionarios por score).
   - Python: Acceso a la matriz de distancias de FAISS.
   - Teoría/Práctica: Detección de fuera de dominio (Out of Domain).
   - Similitud manual (Cosina/Punto Escalar) sin librerías de índices.
