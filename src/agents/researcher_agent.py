# from crewai import Agent
# from crewai_tools import YoutubeVideoSearchTool

# class ResearcherAgent(Agent):
#     def __init__(self, tools=[]):
#         super().__init__(
#             role='Researcher',
#             goal='Search YouTube for videos on AI strategy in enterprise that are over 15 minutes long.',
#             tools=tools if tools else [YoutubeVideoSearchTool()],
#             verbose=True,
#             memory=True,
#             backstory=(
#                 "As a pioneer in the field of AI strategy, you're always on the lookout for the latest trends, "
#                 "insights, and breakthroughs. Your mission is to scour YouTube for valuable content that sheds light "
#                 "on how enterprises are leveraging AI to drive their strategy forward."
#             ),
#             allow_delegation=True
#         )

#     def perform_task(self, task_description):
#         # Utilize the YoutubeVideoSearchTool to search for videos.
#         # Here, you'll need to pass appropriate parameters to the tool based on your search criteria.
#         print(f"Performing task: {task_description}")
#         search_results = self.tools[0].search("AI strategy in enterprise", min_length=900)  # Example usage
#         return search_results


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
        self.tools[0](query=query)

    def perform_targeted_search(self, video_url):
        # Targeted search within a specific video's content
        self.tools[0](youtube_video_url=video_url)
