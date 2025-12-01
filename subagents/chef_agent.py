from google.adk.agents import Agent
from ..agent import MODEL
from google.genai import types
from google.adk.models.google_llm import Gemini
from . import chef_agent_prompt


retry_config=types.HttpRetryOptions(
        attempts=5,  # Maximum retry attempts
        exp_base=7,  # Delay multiplier
        initial_delay=1, # Initial delay before first retry (in seconds)
        http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
    )

chef_agent = Agent(
    model=Gemini(
            model=MODEL,
            retry_options=retry_config
        ),
    name="chef_agent",
    description=(
        "Design's a food menu based on the criteria of an individual"
    ),
    instruction=chef_agent_prompt.PROMPT,
    #before_model_callback=rate_limit_callback,
)