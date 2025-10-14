import asyncio
import os
import sys

from dotenv import load_dotenv

load_dotenv()

# Import the Google Gemini model class
from browser_use import Agent, ChatGoogle


async def main():
	# Initialize the Gemini model
	llm = ChatGoogle(model="gemini-pro")

	# Define a data extraction task
	task = """
    Go to https://quotes.toscrape.com/ and extract the following information:
    - The first 5 quotes on the page
    - The author of each quote
    - The tags associated with each quote
    
    Present the information in a clear, structured format like:
    Quote 1: "[quote text]" - Author: [author name] - Tags: [tag1, tag2, ...]
    Quote 2: "[quote text]" - Author: [author name] - Tags: [tag1, tag2, ...]
    etc.
    """

	# Create and run the agent
	agent = Agent(task=task, llm=llm)
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())