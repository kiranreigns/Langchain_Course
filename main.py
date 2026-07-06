from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

class Source(BaseModel):
  """ Schema for a source used by the agent """
  url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
  """ Schema for agent response with answers and sources """
  answer:str = Field(description="The agent's answer to the query")
  sources:List[Source] = Field(default_factory=list, description="The list of sources used to generate the answer")

tavily_search = TavilySearch()
llm = ChatOpenAI(model='gpt-5')
tools = [tavily_search]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
 result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for Software Engineer in Bangalore")})
 print(result)

if __name__ == "__main__":
  main()