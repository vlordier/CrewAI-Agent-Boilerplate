from crewai_tools import BaseTool
from langchain_community.document_loaders import YoutubeLoader


class TranscriptExtractorTool(BaseTool):
    name = "Transcript Extractor"
    description = (
        "Extracts transcripts from YouTube videos using LangChain's YoutubeLoader."
    )

    def _run(self, video_url: str) -> str:
        # Initialize the YoutubeLoader
        loader = YoutubeLoader()

        # Use the loader to fetch the transcript
        transcript_data = loader.load(video_url)

        # Process the transcript_data as needed, e.g., combine text segments into a single string
        transcript_text = "\n".join(
            segment["text"] for segment in transcript_data["transcript"]
        )

        return transcript_text
