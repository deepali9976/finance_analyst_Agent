
#os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  
import os
from dotenv import load_dotenv
load_dotenv()  
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
print("APIkey=",os.environ["OPENAI_API_KEY"])