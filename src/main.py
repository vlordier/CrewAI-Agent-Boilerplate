#!/usr/bin/env python
""" Main module for the crew blog crew """
import agentops

from crew import CrewBlogCrew

agentops.init(tags="crew_blog")


def run() -> None:
    """Run the crew"""

    inputs = {"topic": "AI LLMs"}
    CrewBlogCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
