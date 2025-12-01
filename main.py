import uvicorn
from google.adk.web import WebApp
from agent import root_agent, session_service

# 1. Create an instance of the ADK WebApp.
#    This class is designed to create a web interface for your agent.
#    - 'agent': This is your main agent that will process user requests.
#    - 'session_service': This manages the memory and state of the conversation.
#    - 'title': This sets the title that appears in the browser tab.
app = WebApp(
    agent=root_agent,
    session_service=session_service,
    title="Meal Planner Agent",
)

# 2. Use a standard Python entry point.
#    This code will only run when you execute `python main.py`.
if __name__ == "__main__":
    # 3. Run the web application using uvicorn.
    #    uvicorn is a web server that runs your 'app'.
    uvicorn.run(
        "main:app",  # Tells uvicorn to look for the 'app' object in the 'main.py' file.
        host="127.0.0.1",  # Makes the server accessible on your local machine.
        port=8000,  # The port to access the UI from your browser.
        reload=True,  # The server will automatically restart if you change the code.
    )
