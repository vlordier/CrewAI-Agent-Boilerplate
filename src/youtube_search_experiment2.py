from crewai import Agent, Crew, Task
from crewai_tools import YoutubeVideoSearchTool

# Setting up the YouTube search tool
youtube_search_tool = YoutubeVideoSearchTool()

# Creating an agent for YouTube video searching
youtube_agent = Agent(
    role="Video Researcher",
    goal="Find relevant YouTube videos over 10 minutes on the topic: {topic}",
    tools=[youtube_search_tool],
    backstory="A diligent researcher focused on sourcing extensive video content for in-depth analysis.",
    verbose=True,
    memory=True,
    allow_delegation=True,
)

# Defining the YouTube search task
youtube_search_task = Task(
    description="Search for YouTube videos longer than 10 minutes on the topic: {topic}.",
    tools=[youtube_search_tool],
    agent=youtube_agent,
    expected_output="List of relevant YouTube video URLs.",
)

# Creating the crew
crew = Crew(agents=[youtube_agent], tasks=[youtube_search_task])


# Adjusting task input to dynamically include the topic in the search query
def execute_youtube_search(topic):
    youtube_agent.interpolate_inputs(
        {"topic": topic}
    )  # Ensuring the topic is interpolated into the agent's goal and task description
    result = crew.kickoff(
        inputs={"topic": topic}
    )  # The input now just needs to carry the topic
    return result


# Example usage
if __name__ == "__main__":
    topic = "AI advancements"
    videos = execute_youtube_search(topic)
    print(videos)
