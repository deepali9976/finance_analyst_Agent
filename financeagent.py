from dotenv import load_dotenv
import os
import os
from dotenv import load_dotenv
load_dotenv()  
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  
print("loaded key",os.environ["OPENAI_API_KEY"])

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.model.openai import OpenAIChat
def get_company_symbol(company:str)->str:
    """use this particular function to get the symbol for a company 
    Args:
    company(str): The name of the company
    Returns:
    str: The symbol for the company
    """
    symbols={
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple":"AAPL",
        "Microsoft":"MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL"
    }
    return symbols.get(company,"Unknown")

agent = Agent(
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    #model=OpenAIChat(id="gpt-3.5-turbo"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True),get_company_symbol],
    show_tool_calls=True,
    markdown=True,
instructions=["use tables to display data in a neat manner.",
              "if you dont know the company symbol, use get_company_symbol,even if it is not"],
#debug_mode=True

)
agent.print_response("summarize and compare and analyst recommdations between TSLA and Phidata")

if __name__ == "__main__":
    print("Script started")
