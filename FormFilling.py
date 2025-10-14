import asyncio
import os
import sys

from dotenv import load_dotenv

load_dotenv()

# Import the Google Gemini model class
from browser_use import Agent, ChatGoogle


async def main():
	# Initialize the Gemini model
	llm = ChatGoogle(model="gemini-2.5-flash")

	# Define a form filling task
	task = """
    Go to https://httpbin.org/forms/post and fill out the contact form with:
    - Customer name: Vedansh kadway
    - Telephone: 1234567890
    - Email: vedansh@gmail.com
    - Size: Medium
    - Topping: cheese
    - Delivery time: now
    - Comments: This is a test form submission
    
    Then submit the form and tell me what response you get.
    """

	# Create and run the agent
	agent = Agent(task=task, llm=llm)
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())