# FAISS

**FAISS** (Facebook AI Similarity Search) es una librería diseñada para acelerar las bases de datos vectoriales.

Imagina que tienes millones de puntos en tu [[Espacio Vectorial]]. Si tuvieras que comparar tu búsqueda con cada uno de ellos uno por uno (lo que se llama búsqueda lineal), el sistema sería lentísimo.

El trabajo de un índice vectorial como FAISS es organizar inteligentemente ese espacio. Divide el mapa en distintas zonas o agrupaciones. Así, cuando buscas algo, FAISS primero identifica en qué "zona" cayó tu búsqueda y **solo compara con los puntos de ese barrio**, saltándose el resto.

> [!INFO] A tener en cuenta
> FAISS **no entiende el texto ni las palabras**. Solo sabe hacer operaciones matemáticas súper rápidas con listas de números para encontrar a los más cercanos. El encargado de entender el texto es el [[Embedding]].

---

## Matemática del Score de Similitud

FAISS (en su versión `IndexFlatL2`) devuelve distancias geométricas. Para un humano, es más intuitivo trabajar con un **Score de Similitud** acotado entre 0 y 1, donde 1 es identidad total.

### La Función de Transformación
Para convertir la distancia $d$ en un score $S$, aplicamos la siguiente lógica:
$$S = \frac{1}{1 + d}$$

**¿Por qué esta fórmula?**
1. Si la distancia es **0** (puntos idénticos), el score es **1**.
2. A medida que la distancia $d$ crece hacia el infinito, el score tiende a **0**.
3. Nunca obtendremos valores negativos ni resultados fuera del rango [0, 1].

---

## Ciclo de Vida Dinámico del Índice (Python)

El manejo de un índice en producción requiere controlar la entrada, salida y persistencia de los datos.

### 1. Inserción en Caliente
Podemos añadir nuevos vectores a un índice ya existente sin necesidad de reconstruirlo desde cero.
```python
# 'vectores' debe ser un array de NumPy tipo float32
index.add(vectores)
```

### 2. Eliminación y Sincronización
Eliminar datos es complejo porque FAISS usa IDs internos. Si usas `IndexFlatL2`, puedes eliminar por ID:
```python
# Requiere que el índice sea IDMap o soporte remoción
index.remove_ids(np.array([id_a_eliminar]))
```
> [!WARNING] Riesgo de Desfase
> Si eliminas un vector en FAISS, debes asegurarte de eliminarlo también de tu "traductor" externo (tu lista de textos). Si no, cuando FAISS te diga "el resultado es el ID 5", tú podrías mostrar el texto equivocado.

### 3. Persistencia en Disco
No queremos regenerar el índice cada vez que el programa arranca. Podemos serializar el "cerebro" del índice:
```python
import faiss

# Guardar
faiss.write_index(index, "mi_memoria.faiss")

# Recuperar
index_recuperado = faiss.read_index("mi_memoria.faiss")
```