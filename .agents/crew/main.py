#!/usr/bin/env python
import sys
import datetime
from crew import VaultCrew

def run(tema, chat_history, fuente_datos=""):
    # Carga modular de definiciones, guías y memoria
    try:
        # Generar índice de la bóveda actual para evitar duplicados
        vault_files = [f for f in os.listdir('.') if f.endswith('.md')]
        vault_index = ", ".join(vault_files)

        with open('.agents/writing_style.md', 'r') as f:
            style_guide = f.read()
        with open('.agents/memory.md', 'r') as f:
            memory_content = f.read()
        with open('.agents/crew/agents/escritor/definition.md', 'r') as f:
            escritor_def = f.read()
        with open('.agents/crew/agents/revisor/definition.md', 'r') as f:
            revisor_def = f.read()
        with open('.agents/crew/agents/analista/definition.md', 'r') as f:
            analista_def = f.read()
        with open('.agents/crew/agents/arquitecto/definition.md', 'r') as f:
            arquitecto_def = f.read()
    except Exception as e:
        style_guide = ""
        memory_content = ""
        escritor_def = ""
        revisor_def = ""
        analista_def = ""
        arquitecto_def = ""
        vault_index = ""

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
    
    crew_instance = VaultCrew().crew()
    result = crew_instance.kickoff(inputs=inputs)
    
    # Extraer outputs individuales de las tareas en el orden definido en el crew
    # Según la lógica de CrewAI sequential, los resultados fluyen.
    # El output final suele ser el de la última tarea o del crew.
    # En nuestro caso, queremos capturar la nota (escritor) y el grafo (arquitecto).
    
    nota_generada = ""
    grafo_generado = ""
    feedback_revision = ""

    # Mapeo manual de resultados basado en el orden de tareas
    # 0: extraccion, 1: mapeo, 2: escritura, 3: revision
    try:
        grafo_generado = crew_instance.tasks[1].output.raw
        nota_generada = crew_instance.tasks[2].output.raw
        feedback_revision = crew_instance.tasks[3].output.raw.strip()
    except:
        nota_generada = result.raw
    
    # Motor de Automejora
    if feedback_revision and "PERFECTO" not in feedback_revision.upper():
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        if "[YYYY-MM-DD]" in feedback_revision:
            feedback_revision = feedback_revision.replace("[YYYY-MM-DD]", today)
            
        with open('.agents/memory.md', 'a') as f:
            f.write(f"\n{feedback_revision}")
            
    # Output estructurado para el orquestador
    print("---INICIO_GRAFO---")
    print(grafo_generado)
    print("---FIN_GRAFO---")
    print("---INICIO_NOTA---")
    print(nota_generada)
    print("---FIN_NOTA---")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Si hay un tercer argumento, se asume que es el contenido de los datos (fuente_datos)
        run(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "", sys.argv[3] if len(sys.argv) > 3 else "")
    else:
        print("Uso: python main.py '<tema>' '<chat_history>' '<fuente_datos>'")
