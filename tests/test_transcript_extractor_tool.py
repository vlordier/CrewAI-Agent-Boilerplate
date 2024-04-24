from unittest.mock import patch

import pytest

from src.tools.transcript_extractor_tool import TranscriptExtractorTool

# Sample mocked response from YoutubeLoader
mocked_transcript_data = {
    "transcript": [
        {
            "text": "Hello, welcome to our YouTube channel.",
            "start": 0.0,
            "duration": 7.0,
        },
        {
            "text": "Today, we'll discuss AI strategies in enterprises.",
            "start": 7.0,
            "duration": 10.0,
        },
    ]
}


@pytest.fixture
def extractor_tool():
    return TranscriptExtractorTool()


@patch("src.tools.transcript_extractor_tool.YoutubeLoader")
def test_transcript_extraction(MockYoutubeLoader, extractor_tool):
    # Mocking the load method of YoutubeLoader to return our mocked_transcript_data
    MockYoutubeLoader.return_value.load.return_value = mocked_transcript_data

    # The expected transcript text combines the text from the mocked_transcript_data
    expected_transcript = "Hello, welcome to our YouTube channel.\nToday, we'll discuss AI strategies in enterprises."

    # The URL here is a placeholder; in practice, it should be a valid YouTube video URL.
    video_url = "https://www.youtube.com/watch?v=dummy"

    # Running the _run method of the TranscriptExtractorTool, which should utilize the mocked YoutubeLoader
    transcript = extractor_tool._run(video_url)

    # Asserting that the returned transcript matches our expected output
    assert (
        transcript == expected_transcript
    ), "The TranscriptExtractorTool did not return the expected transcript text."
