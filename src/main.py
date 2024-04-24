from crewai import Crew, Process, Task

from src.agents.blog_post_outline_creator_agent import BlogPostOutlineCreatorAgent
from src.agents.content_writer_agent import ContentWriterAgent
from src.agents.critique_agent import CritiqueAgent
from src.agents.data_analyst_agent import DataAnalystAgent
from src.agents.editor_agent import EditorAgent
from src.agents.publisher_agent import PublisherAgent
from src.agents.question_generator_agent import QuestionGeneratorAgent
from src.agents.research_enhancer_agent import ResearchEnhancerAgent
from src.agents.researcher_agent import ResearcherAgent
from src.agents.transcript_extractor_agent import TranscriptExtractorAgent
from src.tools.blog_outline_creator_tool import BlogOutlineCreatorTool
from src.tools.content_refinement_tool import ContentRefinementTool
from src.tools.key_point_extraction_tool import KeyPointExtractionTool
from src.tools.question_generator_tool import QuestionGeneratorTool
from src.tools.transcript_extractor_tool import TranscriptExtractorTool


def main():
    # Initialize agents with their respective tools
    researcher = ResearcherAgent(tools=[YoutubeSearchTool()])
    transcript_extractor = TranscriptExtractorAgent(tools=[TranscriptExtractorTool()])
    data_analyst = DataAnalystAgent(
        tools=[VectorDatabaseTool(), KeyPointExtractionTool()]
    )
    question_generator = QuestionGeneratorAgent(tools=[QuestionGeneratorTool()])
    blog_outline_creator = BlogPostOutlineCreatorAgent(tools=[BlogOutlineCreatorTool()])
    content_writer = ContentWriterAgent()
    critique = CritiqueAgent(tools=[ContentRefinementTool()])
    research_enhancer = ResearchEnhancerAgent(tools=[ContentRefinementTool()])
    editor = EditorAgent(tools=[ContentRefinementTool()])
    publisher = PublisherAgent()

    # Define tasks (for simplicity, using generic Task class and description only)
    tasks = [
        Task(description="Search YouTube for AI strategy topics", agent=researcher),
        Task(description="Extract transcripts from videos", agent=transcript_extractor),
        Task(
            description="Analyze transcripts and extract key points", agent=data_analyst
        ),
        Task(
            description="Generate questions from video content",
            agent=question_generator,
        ),
        Task(description="Create blog post outlines", agent=blog_outline_creator),
        Task(description="Write content for blog posts", agent=content_writer),
        Task(description="Critique blog posts", agent=critique),
        Task(
            description="Enhance blog content based on critiques",
            agent=research_enhancer,
        ),
        Task(description="Finalize and edit blog posts", agent=editor),
        Task(description="Publish blog posts", agent=publisher),
    ]

    # Assemble the crew and set the process flow
    crew = Crew(
        agents=[
            researcher,
            transcript_extractor,
            data_analyst,
            question_generator,
            blog_outline_creator,
            content_writer,
            critique,
            research_enhancer,
            editor,
            publisher,
        ],
        tasks=tasks,
        process=Process.sequential,
    )

    # Kick off the process
    crew.kickoff(inputs={"topic": "AI strategy in enterprise"})


if __name__ == "__main__":
    main()
