""" CrewBlog crew module """

import os
from pathlib import Path
from typing import Any, Dict

import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq


@CrewBase
class CrewBlogCrew:
    """CrewBlog crew

    Attributes:
            agents_config (str): Path to the agents configuration file
            tasks_config (str): Path to the tasks configuration file
            agents (Dict[str, Agent]): Dictionary of agents
            tasks (Dict[str, Task]): Dictionary of tasks
    """

    agents: Dict[str, Agent]
    tasks: Dict[str, Task]

    def __init__(
        self,
        agents_config_path: Path = Path("config/agents.yaml"),
        tasks_config_path: Path = Path("config/tasks.yaml"),
    ):
        """Initialize the CrewBlog crew

        Args:
            agents_config_path (str, optional): Path to the agents configuration file. Defaults to "config/agents.yaml".
            tasks_config_path (str, optional): Path to the tasks configuration file. Defaults to "config/tasks.yaml".

        Raises:
            ValueError: If the GROQ_API_KEY is not set in the .env file
            FileNotFoundError: If the agents or tasks configuration file does not exist
        """

        # get GROQ_API_KEY from .env
        groq_api_key = os.getenv("GROQ_API_KEY")
        if groq_api_key is None:
            raise ValueError("GROQ_API_KEY is not set in .env")

        groq_model_name = os.getenv("GROQ_MODEL_NAME")
        if groq_model_name is None:
            raise ValueError("GROQ_MODEL_NAME is not set in .env")

        # Define the model
        self.llm = ChatGroq(temperature=0, model_name=groq_model_name)

        # Define the paths
        current_file_path = Path(__file__).parent

        agents_config_path = current_file_path / agents_config_path
        agents_config_path = agents_config_path.resolve()

        if not agents_config_path.exists():
            raise FileNotFoundError(f"No such file: '{agents_config_path}'")

        self.agents_config_path = agents_config_path

        tasks_config_path = current_file_path / tasks_config_path
        tasks_config_path = tasks_config_path.resolve()

        if not tasks_config_path.exists():
            raise FileNotFoundError(f"No such file: '{tasks_config_path}'")

        self.tasks_config_path = tasks_config_path

        self.agents_config = self.load_agents_config()
        self.tasks_config = self.load_tasks_config()

    def load_agents_config(self) -> Dict[str, Agent]:
        """
        Load the agents configuration from a YAML file or similar

        Returns:
            Dict[str, Agent]: The agents configuration
        """
        with open(self.agents_config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        return config

    def load_tasks_config(self) -> Dict[str, Task]:
        """
        Load the tasks configuration from a YAML file or similar

        Returns:
            Dict[str, Task]: The tasks configuration
        """
        # Load the tasks configuration from a YAML file or similar
        with open(self.tasks_config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        return config

    @agent
    def researcher(self) -> Agent:
        """Creates a researcher agent

        Returns:
            Agent: The researcher agent with the specified configuration.
        """
        researcher_config: Dict[str, Any] = self.agents_config["researcher"]
        return Agent(
            config=researcher_config,
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
            llm=self.llm,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        """Creates a reporting analyst agent

        Returns:
            Agent: The reporting analyst agent with the specified configuration.
        """
        reporting_analyst_config: Dict[str, Any] = self.agents_config[
            "reporting_analyst"
        ]
        return Agent(
            config=reporting_analyst_config,
            verbose=True,
            llm=self.llm,
        )

    @task
    def research_task(self) -> Task:  # dead: disable
        """Creates a research task

        Returns:
            Task: The research task with the specified configuration and agent.
        """
        research_task_config: Dict[str, Any] = self.tasks_config["research_task"]
        return Task(config=research_task_config, agent=self.researcher())

    @task
    def reporting_task(self) -> Task:  # dead: disable
        """Creates a reporting task

        Returns:
            Task: The reporting task with the specified configuration and agent.
        """
        reporting_task_config: Dict[str, Any] = self.tasks_config["reporting_task"]
        return Task(
            config=reporting_task_config,
            agent=self.reporting_analyst(),
            output_file="report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewBlog crew

        Returns:
            Crew: The CrewBlog crew with the specified agents, tasks, and process.
        """
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
