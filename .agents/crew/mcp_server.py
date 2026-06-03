#!/usr/bin/env python3
import sys
import os
import datetime
from fastmcp import FastMCP
from crew import VaultCrew

# Cambiar al directorio donde se encuentran los archivos de configuración
# Esto es necesario porque CrewBase busca rutas relativas
os.chdir(os.path.dirname(os.path.abspath(__file__)))

mcp = FastMCP("Vault-Crew")

@mcp.tool()
def generar_apuntes_desde_repo(tema: str, chat_history: str = "", fuente_datos: str = "") -> str:
    """
    Activa el equipo de agentes (CrewAI) para escanear un repositorio, extraer información, 
    organizar un grafo de ideas y redactar apuntes técnicos siguiendo la guía de estilo.
    
    Args:
        tema: El tema central de los apuntes.
        chat_history: Contexto relevante de la conversación previa.
        fuente_datos: El contenido crudo o ruta del repositorio a escanear.
    """
    try:
        # Generar índice de la bóveda actual para evitar duplicados
        vault_files = [f for f in os.listdir('../../') if f.endswith('.md')]
        vault_index = ", ".join(vault_files)

        # Carga modular de definiciones, guías y memoria
        with open('../../writing_style.md', 'r') as f:
            style_guide = f.read()
        with open('../../memory.md', 'r') as f:
            memory_content = f.read()
        with open('agents/escritor/definition.md', 'r') as f:
            escritor_def = f.read()
        with open('agents/revisor/definition.md', 'r') as f:
            revisor_def = f.read()
        with open('agents/analista/definition.md', 'r') as f:
            analista_def = f.read()
        with open('agents/arquitecto/definition.md', 'r') as f:
            arquitecto_def = f.read()
    except Exception as e:
        return f"Error cargando archivos de configuración: {str(e)}"

    inputs = {
        'tema': tema,
        'chat_history': chat_history,
        'fuente_datos': fuente_datos,
        'vault_index': vault_index,
        'style_guide_content': style_guide,
        'memory_content': memory_content,
        'escritor_definition': escritor_def,
        'revisor_definition': revisor_def,
        'analista_definition': analista_def,
        'arquitecto_definition': arquitecto_def,
        'extractos': 'Procesado por el analista...',
        'grafo_ideas': 'Generado por el arquitecto...',
        'informacion_extraida': 'Extracción completada...'
    }
    
    try:
        crew_instance = VaultCrew().crew()
        result = crew_instance.kickoff(inputs=inputs)
        
        # Mapeo manual de resultados basado en el orden de tareas
        # 0: extraccion, 1: mapeo, 2: escritura, 3: revision
        grafo_generado = crew_instance.tasks[1].output.raw
        nota_generada = crew_instance.tasks[2].output.raw
        feedback_revision = crew_instance.tasks[3].output.raw.strip()
        
        # Motor de Automejora
        if feedback_revision and "PERFECTO" not in feedback_revision.upper():
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            if "[YYYY-MM-DD]" in feedback_revision:
                feedback_revision = feedback_revision.replace("[YYYY-MM-DD]", today)
                
            with open('../../memory.md', 'a') as f:
                f.write(f"\n{feedback_revision}")
        
        # Formatear la respuesta para el orquestador
        response = f"""# Resultado del Procesamiento

## Grafo de Ideas
{grafo_generado}

---

## Nota Generada
{nota_generada}
"""
        return response
    except Exception as e:
        return f"Error ejecutando el Crew: {str(e)}"

if __name__ == "__main__":
    mcp.run()
