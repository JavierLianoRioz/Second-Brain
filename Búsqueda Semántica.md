# Búsqueda Semántica

Es un tipo de búsqueda que intenta comprender la **intención** del usuario y el **significado** de las palabras, en lugar de buscar coincidencias exactas de texto (como hace el típico `Control+F` o un `WHERE` en SQL).

Por ejemplo, si buscas "perro feliz" en un sistema tradicional, solo te devolverá textos que contengan exactamente esas palabras.
En un sistema con búsqueda semántica, te puede devolver un documento que hable de "un caniche alegre", porque el sistema "entiende" que los conceptos están relacionados.

Para lograr esto, la búsqueda semántica convierte las palabras en números (ver [[Embedding]]) y las ubica en un "mapa" (ver [[Espacio Vectorial]]) para comparar qué tan cerca están los conceptos entre sí.