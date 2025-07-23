import os
from dotenv import load_dotenv
load_dotenv()  

from phi.agent import Agent
import phi
import phi.api
from phi.playground import Playground, serve_playground_app
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat


phi.api=os.getenv("PHI_API_KEY") 

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

app=Playground(agents=[finance_agent,search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)