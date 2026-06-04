# Guía de Estilo y Escritura (Source of Truth)

> [!IMPORTANT] Inmutabilidad
> Este documento es la base estética y estructural del repositorio. El agente **NO DEBE MODIFICAR** este archivo bajo ninguna circunstancia, salvo por petición o incentivo explícito del usuario.

Este documento define las reglas de formato, estructura y tono que deben seguir los agentes para generar contenido que se integre perfectamente en el Second Brain del usuario. El objetivo es que la información sea coherente, pedagógica y centrada en conexiones conceptuales narrativas.

## 1. Tono y Lenguaje
- **Idioma:** Siempre en **Español**.
- **Enfoque Pedagógico:** Escribe como si te estuvieras explicando el concepto a ti mismo o a un colega. Debe ser claro, directo y con un propósito práctico.
- **Mentalidad:** Prioriza el "por qué" (paradigma) junto con el "cómo" (sintaxis).
- **Metáforas de Progresión:** Se permite el uso de terminología como **early-game**, **mid-game** y **late-game** como organizador mental para situar conceptos en su fase de aplicación o madurez. Debe usarse como una herramienta de comparación pedagógica, no de forma esencial ni abusiva.
- **Expresiones Clave:**
    - **"¡OJO!"**: Para advertencias críticas o detalles que suelen olvidarse.
    - **"Se descompone de la siguiente manera:"**: Antes de explicar la sintaxis de un comando.
    - **"La regla de oro:"**: Para principios fundamentales de diseño o modelado.
    - **"Error típico"**: Para señalar fallos comunes en la práctica.

## 2. Estructura de las Notas
Cada nota es un mundo independiente que se interconecta con otros mediante conceptos, no mediante una jerarquía rígida.

1.  **Título Principal (#):** El nombre del concepto o tecnología. **¡OJO!** No utilices emojis en los títulos ni en los encabezados.
2.  **Enfoque Conceptual:** Evita crear "índices" o "MOCs" puros. Cada nota debe explicar el concepto de forma narrativa y profunda, utilizando enlaces naturales para saltar a otros conceptos relacionados.
3. Títulos Narrativos (##): Sustituye los encabezados genéricos (ej. "Teoría", "Práctica") por preguntas directas que guíen la narrativa y cuya respuesta sea el contenido del apartado. Esto mantiene al lector enganchado en el flujo de ideas y reduce la carga cognitiva.
4. Dinámica de Continuidad (Claroscuro): Para dar fluidez, utiliza una estructura de Problema -> Solución -> Nuevo Problema -> Nueva Solución.
5. El Método Esqueleto: Es obligatorio preceder los ejemplos complejos con un mapa visual simplificado.
   ```javascript
   // EL ESQUELETO: db.coleccion.metodo( {filtro}, {opciones} )
   ```
6. No Duplicidad: Nunca dupliques información.
7. Frontmatter (Metadatos): Todas las notas deben incluir metadatos en YAML. Materia es obligatorio.
8. Introducción: Una o dos frases breves que definan el tema.

## 3. Formato y Elementos Visuales
- **Signos de Puntuación:**
    - Usa la raya o guion largo (**—**) para realizar incisos o paréntesis que den continuidad al discurso dentro de una frase.
    - Usa los paréntesis (**( )**) para subtemas más aislados o aclaraciones técnicas breves que se alejan del flujo principal de la oración.
- **Emojis:** Están prohibidos en enunciados, títulos y encabezados para mantener una estética sobria y limpia.
- **Énfasis:** 
    - Usa **Negrita** para términos técnicos y conceptos clave.
    - Usa *Cursiva* para matices o aclaraciones breves.
    - **Prohibición de Resaltado:** El agente tiene completamente prohibido utilizar `====` para hacer highlight en markdown. Está completamente reservado para el editor humano para poder destacar manualmente por el usuario los temarios que le parecen más importantes. Nunca deberás eliminar y/o añadir highlights.
- **Código:**
    - **In-line:** Usa backticks (\` \`) para nombres de propiedades, variables o comandos.
    - **Bloques:** Usa bloques de código con el lenguaje especificado (ej. ` ```cypher `) y añade comentarios breves.
    - **Norma de Sintaxis (Método Esqueleto):** Es obligatorio preceder los ejemplos con un mapa visual simplificado del comando, evitando el exceso de corchetes y símbolos técnicos.
        1. **El Esqueleto:** Muestra la estructura base en una o dos líneas limpias.
        2. **La Leyenda:** Explica qué es cada pieza en lenguaje humano justo debajo.
        3. **Formato:**
           ```javascript
           // SINTAXIS: comando( [etapa1, etapa2] )
           //   ├─ etapa1: El filtro inicial ($match).
           //   └─ etapa2: La acción principal ($group).
           ```

- **Callouts (Obsidian):** Utilízalos con moderación para resaltar información crítica (NOTE, IMPORTANT, WARNING, INFO, TIP).
- **Matemáticas y Lógica:** Usa LaTeX ($$...$$ o $...$) para fórmulas y estructuras de lista para desglosar sintaxis.

## 4. Conectividad (Networking)
- **Wikilinks:** Usa `[[Nombre de la Nota]]` de forma extensiva. La relación entre notas debe nacer de la necesidad de expandir un concepto, creando una red de conocimiento orgánica.

---
*Este documento es la referencia para el modelado de información por parte de agentes.*
