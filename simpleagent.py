from dotenv import load_dotenv
import os

load_dotenv()  
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  #
from phi.agent import Agent
from phi.model.groq import Groq

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)
agent.print_response("give a 2 line poem about India")
if __name__ == "__main__":
    print("Script started")
