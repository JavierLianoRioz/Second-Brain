import subprocess
from typing import Any, List, Optional, Mapping
from crewai.llms.base_llm import BaseLLM

class GeminiCLILLM(BaseLLM):
    """
    Un LLM personalizado que utiliza el comando 'gemini -p' 
    para realizar inferencia usando el auth del CLI.
    """
    
    llm_type: str = "gemini-cli-bridge"
    model: str = "gemini-1.5-flash"

    def call(
        self,
        messages: str | List[dict[str, Any]],
        tools: List[dict[str, Any]] | None = None,
        callbacks: List[Any] | None = None,
        available_functions: dict[str, Any] | None = None,
        from_task: Any | None = None,
        from_agent: Any | None = None,
        response_model: type | None = None,
    ) -> str:
        # Convertimos los mensajes a un solo string para el CLI
        prompt = ""
        if isinstance(messages, str):
            prompt = messages
        else:
            for m in messages:
                role = m.get("role", "user")
                content = m.get("content", "")
                prompt += f"{role}: {content}\n"
        
        if self.stop:
            prompt += f"\n\n[STOP SEQUENCE: {', '.join(self.stop)}]"
        
        try:
            print(f" > [DEBUG] Llamando a Gemini CLI...")
            # Ejecutamos el comando gemini en modo headless
            result = subprocess.run(
                ["gemini", "-y", "-p", prompt],
                capture_output=True,
                text=True,
                check=True
            )
            print(f" < [DEBUG] Respuesta recibida.")
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"Error al llamar a Gemini CLI: {e.stderr if e.stderr else e.stdout}"

    def to_config_dict(self) -> dict[str, Any]:
        config = super().to_config_dict()
        config.update({
            "model": self.model,
            "llm_type": self.llm_type
        })
        return config
