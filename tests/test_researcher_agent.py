from unittest.mock import patch

import pytest

from src.agents.researcher_agent import ResearcherAgent


@pytest.fixture
def agent():
    return ResearcherAgent()


@patch("src.agents.researcher_agent.YoutubeVideoSearchTool")
def test_perform_general_search(MockYoutubeTool, agent):
    agent.perform_general_search("AI strategy in enterprises")
    MockYoutubeTool.assert_called_once()


@patch("src.agents.researcher_agent.YoutubeVideoSearchTool")
def test_perform_targeted_search(MockYoutubeTool, agent):
    video_url = "https://youtube.com/watch?v=example"
    agent.perform_targeted_search(video_url)
    MockYoutubeTool.assert_called_once_with(youtube_video_url=video_url)
