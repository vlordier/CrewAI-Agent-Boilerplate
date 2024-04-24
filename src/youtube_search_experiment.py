from crewai_tools import YoutubeVideoSearchTool

# Initialize the YoutubeVideoSearchTool
youtube_search = YoutubeVideoSearchTool()

# Define your search query and parameters
query = "AI strategy in enterprise"
min_duration = 15 * 60  # Minimum duration in seconds (15 minutes)

# Execute the search
# Note: The actual method to specify the query and filter by duration might differ,
# as the specific API for YoutubeVideoSearchTool is not detailed here.
# This is a conceptual example to illustrate the approach.
results = youtube_search.search(query=query, min_duration=min_duration)

# Process and print the results
for video in results:
    print(f"Video Title: {video['title']}, URL: {video['url']}")
