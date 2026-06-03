#!/usr/bin/env python
import sys
import datetime
from crew import VaultCrew

def run(tema, chat_history):
    # Carga modular de definiciones, guías y memoria
    try:
        with open('.agents/writing_style.md', 'r') as f:
            style_guide = f.read()
        with open('.agents/memory.md', 'r') as f:
            memory_content = f.read()
        with open('.agents/crew/agents/escritor/definition.md', 'r') as f:
            escritor_def = f.read()
        with open('.agents/crew/agents/revisor/definition.md', 'r') as f:
            revisor_def = f.read()
    except Exception as e:
        style_guide = ""
        memory_content = ""
        escritor_def = ""
        revisor_def = ""

    inputs = {
        'tema': tema,
        'chat_history': chat_history,
        'style_guide_content': style_guide,
        'memory_content': memory_content,
        'escritor_definition': escritor_def,
        'revisor_definition': revisor_def
    }
    
    crew_instance = VaultCrew().crew()
    result = crew_instance.kickoff(inputs=inputs)
    
    # Extraer outputs individuales de las tareas
    # CrewAI expone las tareas en el orden en que se ejecutaron
    nota_generada = crew_instance.tasks[0].output.raw
    feedback_revision = crew_instance.tasks[1].output.raw.strip()
    
    # Motor de Automejora
    if feedback_revision and "PERFECTO" not in feedback_revision.upper():
        # Reemplazar el placeholder de fecha si es necesario
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        if "[YYYY-MM-DD]" in feedback_revision:
            feedback_revision = feedback_revision.replace("[YYYY-MM-DD]", today)
            
        with open('.agents/memory.md', 'a') as f:
            f.write(f"\n{feedback_revision}")
            
    # El output final del script es SOLO la nota.
    # El CLI (Gemini) leerá esto por stdout y lo guardará en el vault.
    print("---INICIO_NOTA---")
    print(nota_generada)
    print("---FIN_NOTA---")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")
    else:
        print("Uso: python main.py '<tema>' '<chat_history>'")
