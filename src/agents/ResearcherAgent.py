from crewai import Agent
from crewai_tools import YoutubeVideoSearchTool


class ResearcherAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Researcher",
            goal="Find YouTube videos on AI strategy in enterprises.",
            tools=[YoutubeVideoSearchTool()],
            verbose=True,
            memory=True,
            backstory="Searching YouTube for the latest in AI strategy.",
            allow_delegation=True,
        )

    def perform_general_search(self, query):
        # General search for content related to AI strategy across YouTube
        self.tools[0].search(query=query)

    def perform_targeted_search(self, video_url):
        # Targeted search within a specific video's content
        self.tools[0].search(youtube_video_url=video_url)
