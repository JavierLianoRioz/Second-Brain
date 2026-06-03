import os
from typing import List, Optional, Union
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from llm_bridge import GeminiCLILLM

@CrewBase
class VaultCrew():
    """VaultCrew usando el puente de Gemini CLI"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        # Usamos nuestro puente personalizado que hereda el auth del CLI
        self.llm = GeminiCLILLM(model="gemini-1.5-flash")

    @agent
    def analista_repositorios(self) -> Agent:
        agent_config = self.agents_config['analista_repositorios'].copy()
        return Agent(
            role=agent_config['role'],
            goal=agent_config['goal'],
            backstory=agent_config['backstory'],
            llm=self.llm,
            verbose=True
        )

    @agent
    def arquitecto_conocimiento(self) -> Agent:
        agent_config = self.agents_config['arquitecto_conocimiento'].copy()
        return Agent(
            role=agent_config['role'],
            goal=agent_config['goal'],
            backstory=agent_config['backstory'],
            llm=self.llm,
            verbose=True
        )

    @agent
    def escritor_apuntes(self) -> Agent:
        agent_config = self.agents_config['escritor_apuntes'].copy()
        return Agent(
            role=agent_config['role'],
            goal=agent_config['goal'],
            backstory=agent_config['backstory'],
            llm=self.llm,
            verbose=True
        )

    @agent
    def revisor_calidad(self) -> Agent:
        agent_config = self.agents_config['revisor_calidad'].copy()
        return Agent(
            role=agent_config['role'],
            goal=agent_config['goal'],
            backstory=agent_config['backstory'],
            llm=self.llm,
            verbose=True
        )

    @task
    def extraccion_datos_task(self) -> Task:
        return Task(
            config=self.tasks_config['extraccion_datos_task'],
        )

    @task
    def mapeo_conceptual_task(self) -> Task:
        return Task(
            config=self.tasks_config['mapeo_conceptual_task'],
        )

    @task
    def escribir_nota_task(self) -> Task:
        return Task(
            config=self.tasks_config['escribir_nota_task'],
        )

    @task
    def revisar_nota_task(self) -> Task:
        return Task(
            config=self.tasks_config['revisar_nota_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the VaultCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
