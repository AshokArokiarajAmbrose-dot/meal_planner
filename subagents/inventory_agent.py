from google.adk.agents import Agent
from ..agent import MODEL
from google.genai import types
from google.adk.models.google_llm import Gemini
from . import inventory_prompt

retry_config=types.HttpRetryOptions(
        attempts=5,  # Maximum retry attempts
        exp_base=7,  # Delay multiplier
        initial_delay=1, # Initial delay before first retry (in seconds)
        http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
    )

inventory_agent = Agent(
    model=Gemini(
            model=MODEL,
            retry_options=retry_config
        ),
    name="inventory_agent",
    description=(
        "Checks the final meal plan and provides a list of groceries to be bought for each meal"
    ),
    instruction=inventory_prompt.PROMPT,
    #before_model_callback=rate_limit_callback,
)