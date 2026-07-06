from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


@tool
def search(query: str) -> str:
  """
  Tool that searches over internet

  Args:
      query (str): The query to search for

  Returns:
      str: The search result
  """  
  print(f'searching for {query}')
  return "tokyo weather is sunny"

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
 result = agent.invoke({"messages": HumanMessage(content="What's weather like in Tokyo?")})
 print(result)

if __name__ == "__main__":
  main()