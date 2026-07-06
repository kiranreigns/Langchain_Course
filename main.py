from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

tavily = TavilyClient()

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
  return tavily.search(query=query)

llm = ChatOpenAI(model='gpt-5')
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
 result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for Software Engineer in Bangalore")})
 print(result)

if __name__ == "__main__":
  main()