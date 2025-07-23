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

search_agent=Agent(
    name="Web Search Agent",
    role="search the web according to need",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    instructions=["always cite sources"],
    markdown=True

)

finance_agent = Agent(
    name="finance agent",
    role="give details about the stock",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls=True,
    instructions=["use tables to display data in a neat manner."],
    markdown=True,
)

multiagent=Agent(
    team=[search_agent,finance_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=["always cite sources","use tables to display data in a neat manner."],
    show_tool_calls=True,
    markdown=True,
)
multiagent.print_response("summarize analyst reccomendation and share latest news for NVDA")