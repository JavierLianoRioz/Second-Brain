# Memoria a Largo Plazo (Long-term Memory)

Este archivo almacena información estructural, reglas internas y aprendizajes que deben persistir a través de diferentes sesiones y tareas en este Second Brain.

## 1. Estructura de la Bóveda (Vault Structure)
- **Raíz:** Notas conceptuales y de aprendizaje (ej. Ingeniería de Software).
- **.agents/**: Guías de estilo, protocolos operativos y archivos de memoria del sistema.
- **500 Biblioteca/**: Copias locales de recursos externos (repositorios clonados, PDFs).

## 2. Organización Interna del Agente
- **Filosofía:** Red conceptual orgánica, sin jerarquías rígidas.
- **Estilo:** Narrativo académico, títulos en pregunta, estructura Claroscuro.
- **Metadatos:** Uso exclusivo de `materia`. Prohibido `tags` y `autor`.

## 4. Estado de la Infraestructura
- **Sistema de Agentes:** CrewAI configurado y operativo en `.agents/crew/`.
- **Modo de Aprendizaje:** Activo. El sistema evoluciona mediante auto-correcciones en la sección de "Aprendizajes y Optimización".

## 3. Aprendizajes y Optimización
- [2026-05-30] Transición exitosa de pies de página a listas numeradas para mejor visibilidad en Read View.
- [2026-05-30] Implementación de la raya (—) como estándar para incisos discursivos.
- [2026-06-02] **[AUTO-CORRECCIÓN DE SESGO]:** Erradicación de la "adjetivación pedagógica" y metáforas poéticas. Transición a una arquitectura de "Fricción Cero": priorizar la trazabilidad genética de los conceptos, concisión extrema y eliminación de ruido para minimizar la carga cognitiva.
- [2026-06-03] **[CONTENIDO]:** Se reconoce que la bóveda contiene material personal (videos, diario) además de apuntes académicos. El metadato `materia` solo debe aplicarse a notas de estudio, no a archivos personales o de gestión.

---
*Este documento se actualiza tras cada hito relevante para mejorar el desempeño futuro.*

- [AUTO-CORRECCIÓN] Eliminar los backticks (\`) alrededor de los Wikilinks. Has generado enlaces conceptuales envueltos en formato de código (ej. \`[[Ingeniería de Software]]\`), lo cual interfiere con la lectura natural y el renderizado nativo en Obsidian. Los enlaces deben escribirse de forma limpia en el texto: [[Ingeniería de Software]]. Los backticks deben reservarse exclusivamente para nombres de propiedades, variables o comandos, tal y como indica la regla de código in-line.