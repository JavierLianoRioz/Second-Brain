{
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