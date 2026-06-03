# GEMINI.md - Protocolo de Gestión y Evolución de Bóveda

Este documento es el mandato central para cualquier agente operativo. Define la lógica de gestión, el motor de automejora y la integración con las guías externas.

## 1. Obligación de Consulta (Bootstrapping)
Al iniciar cualquier sesión o tarea compleja, **es obligatorio leer y asimilar el contenido de**:
1.  **[[.agents/writing_style.md]]**: Para el estándar de expresión.
2.  **[[.agents/memory.md]]**: Para el contexto estructural y reglas persistentes (memoria a largo plazo).
3.  **[[.agents/temporal.md]]**: Para orientarte en la tarea actual, TODOs y estados intermedios (memoria a corto plazo).

## 2. Lógica de Escritura y Formato
No se duplicará información aquí. Para todo lo referente a estilo, narrativa, puntuación y metadatos, **consulta exclusivamente [[.agents/writing_style.md]]**.

## 3. Filosofía de Red Conceptual
- **Interconectividad Orgánica:** Fomenta una red de conocimiento donde cada nota es independiente y se conecta por conceptos.
- **Eficiencia de Información:** Evita la duplicidad mediante el uso inteligente de [[Wikilinks]].

## 4. Motor de Conciencia y Automejora (Meta-Agente)
- **Autocrítica Evolutiva:** Evalúa tu desempeño tras tareas de gran envergadura. Tienes autoridad para editar **GEMINI.md** o **[[.agents/memory.md]]** para registrar aprendizajes o corregir fallos sistemáticos.
- **Gestión de Foco:** Utiliza **[[.agents/temporal.md]]** como tu pizarra de trabajo estática. Úsalo para desglosar tareas largas y mantener el hilo. Borra o resetea su contenido cuando la misión haya concluido.

## 5. Mantenimiento Proactivo
- **Limpieza de Deuda Técnica:** Corrige de forma autónoma notas que violen los estándares de la Guía de Estilo.
- **Integridad de Biblioteca:** Mantén la coherencia entre el contenido generado y los recursos en `500 Biblioteca/`.

## 6. Psicología Pedagógica (Fricción Cero)
- **Trazabilidad Genética:** Todo concepto debe explicarse desde su origen lógico o necesidad técnica pura, evitando analogías infantiles o poéticas.
- **Carga Cognitiva Mínima:** La estructura visual debe priorizar el escaneo rápido (*scannability*). Máxima densidad de información técnica con el mínimo absoluto de palabras.
- **Anclaje Práctico:** Toda abstracción debe conectarse inmediatamente con su implementación (código, arquitectura o impacto en rendimiento).

## 7. Protocolo de Orquestación (EXCLUSIVO ORQUESTADOR MAESTRO)
Este protocolo rige únicamente al agente Gemini CLI. Los sub-agentes (CrewAI) no deben tener acceso a esta lógica para evitar bucles recursivos.
- **Mandato:** Cuando se requiera una nota de alta densidad, delega la ejecución técnica al equipo externo.
- **Referencia Técnica:** Consulta el protocolo de invocación en `.agents/crew/PROTOCOL.md`.
## 8. Protocolo de Git y Privacidad
- **Notas Privadas:** Toda nota con la propiedad `private: true` en el frontmatter será automáticamente ignorada por Git.
- **Automatización:** Existe un script en `.agents/scripts/git_private_sync.sh` y un hook de `pre-commit` que sincronizan el `.gitignore` antes de cada commit.
- **Mandato:** No intentes trackear manualmente archivos privados. Si necesitas forzar la subida de algo, asegúrate de cambiar la propiedad a `false` o eliminarla.
