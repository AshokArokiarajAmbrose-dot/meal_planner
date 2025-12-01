from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types

def mealplanner_after_agent_callback(callback_context: CallbackContext) -> types.Content:
    """
    This callback runs after the agent's main execution and can modify or replace the final response.
    """
    # Access the original content produced by the agent
    original_content = callback_context.current_content

    # You can modify the content, add additional information, or completely replace it.
    # For example, let's append a custom message.
    custom_message = "This message was added by the after_agent_callback."
    new_text = f"{original_content.parts[0].text}\n\n{custom_message}"

    # Return a new types.Content object with the modified content
    return types.Content(role="model", parts=[types.Part(text=new_text)])