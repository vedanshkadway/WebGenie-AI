from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    llm = ChatGoogle(model="gemini-2.5-flash")
    task = "Go to youtube.com and search for top 3 AI tools in 2025"
    agent = Agent(task=task, llm=llm)
    history = await agent.run()
    # Access useful information
    history.urls()                    # List of visited URLs
    history.screenshot_paths()        # List of screenshot paths  
    history.screenshots()             # List of screenshots as base64 strings
    history.action_names()            # Names of executed actions
    history.extracted_content()       # List of extracted content from all actions
    history.errors()                  # List of errors (with None for steps without errors)
    history.model_actions()           # All actions with their parameters
    history.model_outputs()           # All model outputs from history
    history.last_action()             # Last action in history

    # Analysis methods
    history.final_result()            # Get the final extracted content (last step)
    history.is_done()                 # Check if agent completed successfully
    history.is_successful()           # Check if agent completed successfully (returns None if not done)
    history.has_errors()              # Check if any errors occurred
    history.model_thoughts()          # Get the agent's reasoning process (AgentBrain objects)
    history.action_results()          # Get all ActionResult objects from history
    history.action_history()          # Get truncated action history with essential fields
    history.number_of_steps()         # Get the number of steps in the history
    history.total_duration_seconds()  # Get total duration of all steps in seconds

    # Structured output (when using output_model_schema)
    history.structured_output         # Property that returns parsed structured output

if __name__ == "__main__":
    asyncio.run(main())

