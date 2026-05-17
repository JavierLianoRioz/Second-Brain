# FAISS

**FAISS** (Facebook AI Similarity Search) es una librería diseñada para acelerar las bases de datos vectoriales.

Imagina que tienes millones de puntos en tu [[Espacio Vectorial]]. Si tuvieras que comparar tu búsqueda con cada uno de ellos uno por uno (lo que se llama búsqueda lineal), el sistema sería lentísimo.

El trabajo de un índice vectorial como FAISS es organizar inteligentemente ese espacio. Divide el mapa en distintas zonas o agrupaciones. Así, cuando buscas algo, FAISS primero identifica en qué "zona" cayó tu búsqueda y **solo compara con los puntos de ese barrio**, saltándose el resto.

> [!INFO] A tener en cuenta
> FAISS **no entiende el texto ni las palabras**. Solo sabe hacer operaciones matemáticas súper rápidas con listas de números para encontrar a los más cercanos. El encargado de entender el texto es el [[Embedding]].