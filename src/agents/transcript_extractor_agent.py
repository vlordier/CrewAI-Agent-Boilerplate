from crewai import Agent

# Assuming a custom tool for transcript extraction or an API integration
from src.tools.transcript_extractor_tool import TranscriptExtractorTool


class TranscriptExtractorAgent(Agent):
    def __init__(self, tools=[]):
        super().__init__(
            role="Transcript Extractor",
            goal="Extract transcripts from YouTube videos identified by the Researcher Agent.",
            tools=tools if tools else [TranscriptExtractorTool()],
            verbose=True,
            memory=True,
            backstory=(
                "With a keen eye for detail and a relentless pursuit of information, "
                "you delve into the depths of video content to extract valuable insights. "
                "Your mission is to capture the essence of each video through its transcript, "
                "providing a textual foundation for further analysis."
            ),
            allow_delegation=True,
        )

    def perform_task(self, video_ids):
        # Placeholder logic for transcript extraction
        # In a real scenario, you would interact with the TranscriptExtractorTool or API to get transcripts.
        print(f"Extracting transcripts for videos: {video_ids}")
        transcripts = {video_id: f"Transcript for {video_id}" for video_id in video_ids}
        return transcripts
