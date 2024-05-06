""" This is an example of a custom tool that can be used in the agent. """

from crewai_tools import BaseTool


class MyCustomTool(BaseTool):  # dead: disable
    """My custom tool class.

    Attributes:
        name (str): Name of the tool.
        description (str): Description of the tool.
    """

    def __init__(self) -> None:
        """Initializes the custom tool class.

        Attributes:
            name (str): Name of the tool.
            description (str): Description of the tool.
        """
        self.name: str = "Name of my tool"
        self.description: str = (
            "Clear description for what this tool is useful for, you agent will need this information to use it."
        )

    def _run(self) -> str:  # dead: disable
        """This is the method that will be called when the tool is used in the agent.

        Returns:
            str: Output of the tool.
        """
        # Implementation goes here
        # The actual implementation should be here
        return "this is an example of a tool output, ignore it and move along."
