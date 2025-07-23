import os
from dotenv import load_dotenv
load_dotenv()  
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  
print("loaded key",os.environ["GROQ_API_KEY"])

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo],
    show_tool_calls=True,
    instructions=["always cite sources"],
    markdown=True

)
agent.print_response("what is the usual trends of TSLA")