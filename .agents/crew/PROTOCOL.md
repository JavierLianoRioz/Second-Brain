# Protocolo Técnico de Invocación CrewAI

> [!CAUTION] Uso Exclusivo del Orquestador Maestro (Gemini CLI)
> Este archivo contiene los comandos de shell necesarios para levantar el equipo de agentes. 
> NO debe ser pasado como contexto a los sub-agentes para evitar recursividad.

## Comando de Ejecución
```bash
source .agents/crew/.venv/bin/activate && python3 .agents/crew/main.py "{tema}" "{chat_history}" "{fuente_datos}"
```

## Lógica de Procesamiento
1. El script devuelve la nota entre delimitadores `---INICIO_NOTA---`.
2. El Orquestador extrae el bloque y lo guarda vía `write_file`.
3. El `revisor_calidad` dentro del script se encarga de actualizar `memory.md` de forma autónoma.
