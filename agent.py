from google.adk.agents import Agent
from . import MODEL, root_agent_prompt
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types
from .subagents.chef_agent import chef_agent
from .subagents.inventory_agent import inventory_agent
from .subagents.nutrition_refiner_agent import nutrition_agent
from google.adk.models.google_llm import Gemini
from google.adk.sessions import InMemorySessionService
from google.adk.agents import SequentialAgent
from google.adk.agents import LoopAgent
from .utils.callbacks import mealplanner_after_agent_callback

retry_config=types.HttpRetryOptions(
        attempts=5,  # Maximum retry attempts
        exp_base=7,  # Delay multiplier
        initial_delay=1, # Initial delay before first retry (in seconds)
        http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
    )

session_service = InMemorySessionService()
looping_agent_meal_planner = LoopAgent(
    name="looping_agent_meal_planner",
    description="Executes a sequence of meal planning and then modification of the plan by nutrition ",
    sub_agents=[chef_agent, nutrition_agent],
     max_iterations=2 # Limit loops
)

sequential_agent_meal_planner = SequentialAgent(
    name="meal_planner_agent",
    description="Executes a sequence of meal planning and then modification of the plan by nutrition ",   
    sub_agents=[looping_agent_meal_planner, inventory_agent],
    #callback=mealplanner_after_agent_callback,
)

root_agent = sequential_agent_meal_planner
