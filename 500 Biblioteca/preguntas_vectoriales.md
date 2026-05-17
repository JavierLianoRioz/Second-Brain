# Banco de Ejercicios: Bases Vectoriales y FAISS

---

## Ejercicio 1 (Facil)
**Tipo:** `modify_dataset`

**Enunciado:** Agregue al vocabulario los textos 'tigre salvaje asiático' y 'león africano grande'. Luego ejecute una búsqueda usando la query 'felino'. Analice cómo cambian los resultados.

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción correcta de textos
- Reconstrucción válida del índice
- Uso correcto de búsqueda
- Interpretación semántica básica

---

## Ejercicio 2 (Facil)
**Tipo:** `analyze_results`

**Enunciado:** Ejecute búsquedas usando las queries 'vehículo rápido' y 'coche deportivo'. Compare los resultados obtenidos y explique cuál query parece más específica.

### SOLUCIÓN

**Criterios de Evaluación:**
- Ejecución correcta de búsquedas
- Comparación de rankings
- Interpretación contextual

---

## Ejercicio 3 (Facil)
**Tipo:** `modify_dataset`

**Enunciado:** Agregue al vocabulario los textos 'banco de inversión internacional' y 'banco para descansar'. Luego busque la palabra 'banco' y explique los casos de ambigüedad encontrados.

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción correcta
- Detección de ambigüedad
- Interpretación semántica

---

## Ejercicio 4 (Facil)
**Tipo:** `compare_queries`

**Enunciado:** Ejecute búsquedas usando 'pizza', 'pizza italiana' y 'pizza italiana tradicional'. Explique cómo cambia el ranking al agregar más contexto.

### SOLUCIÓN

**Criterios de Evaluación:**
- Comparación correcta
- Análisis contextual
- Interpretación del embedding

---

## Ejercicio 5 (Facil)
**Tipo:** `modify_function`

**Enunciado:** Modifique la función buscar() para que también devuelva el índice original del texto encontrado.

**Código Base:**
```python
resultados.append({'texto': base[i], 'distancia': distancia, 'score': score})
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Uso correcto del índice
- Modificación funcional
- Estructura válida del resultado

---

## Ejercicio 6 (Facil)
**Tipo:** `analyze_results`

**Enunciado:** Ejecute búsquedas usando la query 'animal'. Explique por qué algunos resultados parecen menos precisos.

### SOLUCIÓN

**Criterios de Evaluación:**
- Análisis de resultados
- Interpretación de ambigüedad
- Relación con contexto

---

## Ejercicio 7 (Facil)
**Tipo:** `modify_dataset`

**Enunciado:** Inserte en el vocabulario textos relacionados con astronomía y luego ejecute búsquedas sobre animales. Explique cómo afecta esto al sistema.

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción válida
- Análisis de contaminación semántica
- Interpretación del ranking

---

## Ejercicio 8 (Facil)
**Tipo:** `complete_function`

**Enunciado:** Complete la función calcular_score() usando la fórmula 1 / (1 + distancia).

**Código Base:**
```python
def calcular_score(distancia):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Implementación correcta
- Uso válido de distancia
- Retorno funcional

---

## Ejercicio 9 (Facil)
**Tipo:** `compare_queries`

**Enunciado:** Compare resultados entre las queries 'tecnología' y 'computadora portátil moderna'. Explique cuál produce resultados más específicos.

### SOLUCIÓN

**Criterios de Evaluación:**
- Comparación válida
- Interpretación contextual
- Relación entre especificidad y embedding

---

## Ejercicio 10 (Facil)
**Tipo:** `modify_dataset`

**Enunciado:** Agregue tres tipos distintos de comida al vocabulario y ejecute búsquedas usando la palabra 'comida'. Explique cómo aparecen agrupaciones semánticas.

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción correcta
- Uso válido de búsquedas
- Interpretación de similitud

---

## Ejercicio 11 (Facil)
**Tipo:** `analyze_results`

**Enunciado:** Ejecute búsquedas usando la query 'objeto'. Explique por qué el sistema devuelve resultados débiles o ambiguos.

### SOLUCIÓN

**Criterios de Evaluación:**
- Interpretación de baja especificidad
- Relación con embeddings
- Análisis contextual

---

## Ejercicio 12 (Facil)
**Tipo:** `modify_function`

**Enunciado:** Modifique la función buscar() para que imprima también la distancia encontrada por FAISS.

**Código Base:**
```python
resultados.append({'texto': base[i], 'score': score})
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Uso correcto de distancia
- Modificación funcional
- Resultado válido

---

## Ejercicio 13 (Facil)
**Tipo:** `compare_queries`

**Enunciado:** Compare búsquedas usando 'ratón' y 'ratón inalámbrico computadora'. Explique diferencias semánticas observadas.

### SOLUCIÓN

**Criterios de Evaluación:**
- Comparación correcta
- Análisis de ambigüedad
- Interpretación contextual

---

## Ejercicio 14 (Facil)
**Tipo:** `modify_dataset`

**Enunciado:** Agregue palabras relacionadas con deportes y luego busque 'vehículo rápido'. Analice si aparecen resultados inesperados.

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción correcta
- Análisis de contaminación
- Interpretación del ranking

---

## Ejercicio 15 (Facil)
**Tipo:** `complete_function`

**Enunciado:** Complete una función que reciba una query y ejecute embedding(query).

**Código Base:**
```python
def generar_query(query):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Uso correcto de embedding
- Implementación funcional
- Retorno válido

---

## Ejercicio 16 (Facil)
**Tipo:** `analyze_results`

**Enunciado:** Ejecute búsquedas usando 'galaxia' y explique por qué aparecen ciertos resultados cercanos aunque no sean exactos.

### SOLUCIÓN

**Criterios de Evaluación:**
- Interpretación geométrica
- Relación entre proximidad y significado
- Análisis semántico

---

## Ejercicio 17 (Facil)
**Tipo:** `modify_dataset`

**Enunciado:** Agregue textos relacionados con videojuegos y luego ejecute búsquedas usando 'tecnología'. Explique el comportamiento del sistema.

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción correcta
- Relación entre dominios
- Interpretación semántica

---

## Ejercicio 18 (Facil)
**Tipo:** `modify_function`

**Enunciado:** Modifique la función buscar_filtrado() para usar un umbral mínimo de 0.5.

**Código Base:**
```python
if r['score'] >= umbral:
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Uso correcto de umbral
- Filtrado válido
- Modificación funcional

---

## Ejercicio 19 (Facil)
**Tipo:** `compare_queries`

**Enunciado:** Compare resultados entre las queries 'felino' y 'felino salvaje africano'. Explique cómo cambia el contexto.

### SOLUCIÓN

**Criterios de Evaluación:**
- Comparación contextual
- Interpretación semántica
- Análisis de especificidad

---

## Ejercicio 20 (Facil)
**Tipo:** `analyze_results`

**Enunciado:** Ejecute búsquedas usando 'computadora'. Explique por qué algunos resultados tecnológicos tienen scores más altos que otros.

### SOLUCIÓN

**Criterios de Evaluación:**
- Interpretación de score
- Relación semántica
- Análisis del ranking

---

## Ejercicio 21 (Medio)
**Tipo:** `modify_function`

**Enunciado:** Modifique la función buscar() para que los resultados se devuelvan ordenados por score descendente.

**Código Base:**
```python
return resultados
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Ordenamiento correcto
- Uso válido de score
- No alterar búsqueda FAISS

---

## Ejercicio 22 (Medio)
**Tipo:** `extend_system`

**Enunciado:** Implemente una función que permita agregar nuevos textos al vocabulario y reconstruir automáticamente el índice FAISS.

**Código Base:**
```python
def agregar(self, texto):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción dinámica correcta
- Reconstrucción válida del índice
- Actualización funcional del sistema

---

## Ejercicio 23 (Medio)
**Tipo:** `analyze_results`

**Enunciado:** Ejecute búsquedas usando las queries 'automóvil', 'coche', 'vehículo' y 'carro'. Compare diferencias de ranking y similitud.

### SOLUCIÓN

**Criterios de Evaluación:**
- Comparación semántica
- Interpretación lingüística
- Análisis contextual

---

## Ejercicio 24 (Medio)
**Tipo:** `modify_function`

**Enunciado:** Modifique la función buscar_filtrado() para permitir que el usuario envíe el valor de k dinámicamente.

**Código Base:**
```python
def buscar_filtrado(query, base, index, umbral=0.3, k=5):
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Uso dinámico de k
- Filtrado funcional
- Modificación correcta de parámetros

---

## Ejercicio 25 (Medio)
**Tipo:** `compare_queries`

**Enunciado:** Compare resultados entre una query de una palabra y una frase larga relacionada. Explique cómo cambia el embedding.

### SOLUCIÓN

**Criterios de Evaluación:**
- Comparación contextual
- Interpretación de embeddings
- Relación entre contexto y ranking

---

## Ejercicio 26 (Medio)
**Tipo:** `extend_system`

**Enunciado:** Implemente una función que exporte los resultados de búsqueda a un diccionario JSON con texto, score y distancia.

**Código Base:**
```python
def exportar_resultados(resultados):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Exportación correcta
- Formato JSON válido
- Persistencia estructurada

---

## Ejercicio 27 (Medio)
**Tipo:** `analyze_results`

**Enunciado:** Inserte varios textos muy similares y analice cómo cambia el ranking cuando existen múltiples embeddings cercanos.

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción válida
- Interpretación de saturación semántica
- Análisis de ambigüedad

---

## Ejercicio 28 (Medio)
**Tipo:** `modify_dataset`

**Enunciado:** Agregue frases extremadamente largas al vocabulario y compare los resultados contra frases cortas.

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción válida
- Análisis contextual
- Interpretación de embeddings largos

---

## Ejercicio 29 (Medio)
**Tipo:** `modify_function`

**Enunciado:** Cambie la fórmula de score por una nueva función distinta a 1/(1+distancia) y compare resultados.

**Código Base:**
```python
score = 1 / (1 + distancia)
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Modificación funcional
- Comparación de comportamiento
- Interpretación matemática básica

---

## Ejercicio 30 (Medio)
**Tipo:** `compare_queries`

**Enunciado:** Compare búsquedas usando 'animal peligroso', 'felino peligroso' y 'felino salvaje africano peligroso'.

### SOLUCIÓN

**Criterios de Evaluación:**
- Comparación contextual
- Interpretación de especificidad
- Análisis semántico

---

## Ejercicio 31 (Medio)
**Tipo:** `extend_system`

**Enunciado:** Implemente una función que registre cada búsqueda junto con su timestamp y score máximo.

**Código Base:**
```python
def registrar_busqueda(query, score):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Logging correcto
- Persistencia funcional
- Uso válido de score

---

## Ejercicio 32 (Medio)
**Tipo:** `analyze_results`

**Enunciado:** Ejecute búsquedas con errores ortográficos intencionales y explique cómo responde el sistema.

### SOLUCIÓN

**Criterios de Evaluación:**
- Pruebas válidas
- Análisis de robustez
- Interpretación de limitaciones

---

## Ejercicio 33 (Medio)
**Tipo:** `modify_function`

**Enunciado:** Modifique la función buscar() para mostrar únicamente resultados cuyo score sea mayor a 0.4.

**Código Base:**
```python
for j, i in enumerate(indices[0]):
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Filtrado correcto
- Uso válido de score
- No romper la búsqueda

---

## Ejercicio 34 (Medio)
**Tipo:** `extend_system`

**Enunciado:** Implemente una función que permita buscar únicamente dentro de una categoría específica como animales o tecnología.

**Código Base:**
```python
def buscar_categoria(query, categoria):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Filtrado correcto por categoría
- Separación de dominios
- Implementación funcional

---

## Ejercicio 35 (Medio)
**Tipo:** `compare_queries`

**Enunciado:** Compare resultados usando IndexFlatL2 e IndexFlatIP. Explique diferencias observadas.

### SOLUCIÓN

**Criterios de Evaluación:**
- Cambio correcto de índice
- Comparación válida
- Interpretación geométrica

---

## Ejercicio 36 (Medio)
**Tipo:** `modify_dataset`

**Enunciado:** Agregue textos de múltiples dominios como política, cocina y videojuegos. Analice contaminación semántica.

### SOLUCIÓN

**Criterios de Evaluación:**
- Inserción válida
- Análisis de contaminación
- Interpretación contextual

---

## Ejercicio 37 (Medio)
**Tipo:** `extend_system`

**Enunciado:** Implemente una función que calcule similitud entre dos textos usando embeddings sin utilizar FAISS.

**Código Base:**
```python
def similitud(texto1, texto2):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Uso correcto de embeddings
- Cálculo válido de similitud
- Interpretación funcional

---

## Ejercicio 38 (Medio)
**Tipo:** `analyze_results`

**Enunciado:** Analice casos donde scores altos producen resultados incorrectos o inesperados.

### SOLUCIÓN

**Criterios de Evaluación:**
- Identificación de anomalías
- Interpretación geométrica
- Análisis de limitaciones

---

## Ejercicio 39 (Medio)
**Tipo:** `modify_function`

**Enunciado:** Modifique la función buscar() para devolver también la categoría del texto encontrado.

**Código Base:**
```python
resultados.append({'texto': base[i]})
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Integración correcta de categorías
- Modificación funcional
- Resultados estructurados

---

## Ejercicio 40 (Medio)
**Tipo:** `compare_queries`

**Enunciado:** Compare el comportamiento del sistema usando bases pequeñas especializadas frente a bases grandes mezcladas.

### SOLUCIÓN

**Criterios de Evaluación:**
- Comparación válida
- Análisis de especialización
- Interpretación de ruido semántico

---

## Ejercicio 41 (Dificil)
**Tipo:** `extend_system`

**Enunciado:** Implemente una función llamada buscar_multidominio() que permita recibir una query y retornar resultados agrupados por categoría ('animales', 'vehículos', 'tecnología'). El sistema debe filtrar resultados con score menor a 0.4.

**Código Base:**
```python
def buscar_multidominio(query):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Agrupación correcta por categoría
- Filtrado válido
- Uso correcto de score
- Estructura funcional

---

## Ejercicio 42 (Dificil)
**Tipo:** `extend_system`

**Enunciado:** Implemente persistencia completa del índice FAISS utilizando escritura y lectura desde disco.

**Código Base:**
```python
faiss.write_index(index, 'indice.faiss')
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Persistencia funcional
- Carga correcta del índice
- Reutilización válida del sistema

---

## Ejercicio 43 (Dificil)
**Tipo:** `modify_function`

**Enunciado:** Modifique el sistema para detectar posibles queries fuera de dominio utilizando score promedio mínimo.

**Código Base:**
```python
def detectar_fuera_dominio(query):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Uso correcto de score
- Detección funcional
- Interpretación de umbrales

---

## Ejercicio 44 (Dificil)
**Tipo:** `extend_system`

**Enunciado:** Implemente una función que elimine textos del vocabulario y reconstruya completamente el índice FAISS.

**Código Base:**
```python
def eliminar(texto):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Eliminación correcta
- Reconstrucción válida
- Consistencia del índice

---

## Ejercicio 45 (Dificil)
**Tipo:** `analyze_results`

**Enunciado:** Analice por qué dos textos semánticamente distintos pueden terminar geométricamente cercanos dentro del espacio vectorial.

### SOLUCIÓN

**Criterios de Evaluación:**
- Interpretación geométrica
- Comprensión de embeddings
- Análisis de limitaciones semánticas

---

## Ejercicio 46 (Dificil)
**Tipo:** `extend_system`

**Enunciado:** Construya un mini recomendador semántico que sugiera textos similares a partir del historial de búsquedas realizadas.

**Código Base:**
```python
historial = []
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Uso correcto de historial
- Recomendación funcional
- Aplicación de similitud semántica

---

## Ejercicio 47 (Dificil)
**Tipo:** `modify_function`

**Enunciado:** Modifique buscar_filtrado() para calcular dinámicamente el umbral usando el score promedio de los resultados.

**Código Base:**
```python
def buscar_filtrado(query, base, index, umbral=0.3, k=5):
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Cálculo dinámico correcto
- Uso válido de promedio
- Filtrado funcional

---

## Ejercicio 48 (Dificil)
**Tipo:** `extend_system`

**Enunciado:** Implemente una función que compare múltiples queries simultáneamente y devuelva los textos más relevantes para todas ellas.

**Código Base:**
```python
def comparar_queries(queries):
    # completar
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Procesamiento múltiple
- Agregación correcta
- Interpretación de relevancia

---

## Ejercicio 49 (Dificil)
**Tipo:** `analyze_results`

**Enunciado:** Compare el comportamiento del sistema usando textos extremadamente cortos frente a descripciones largas y detalladas.

### SOLUCIÓN

**Criterios de Evaluación:**
- Comparación contextual
- Interpretación de embeddings
- Análisis de recuperación semántica

---

## Ejercicio 50 (Dificil)
**Tipo:** `extend_system`

**Enunciado:** Construya un mini sistema semántico completo que incluya embeddings, índice FAISS, score, filtrado, logging y persistencia básica. Luego explique fortalezas, limitaciones y posibles usos empresariales.

**Código Base:**
```python
class BuscadorSemantico:
    # extender sistema
```

### SOLUCIÓN

**Criterios de Evaluación:**
- Integración completa
- Uso correcto de FAISS
- Persistencia funcional
- Logging válido
- Análisis crítico del sistema

---

