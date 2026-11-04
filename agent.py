from agno.agent import Agent

from agno.models.openai import OpenAIResponses
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv

load_dotenv()

def build_agent():
  return Agent(
    model=Groq(
        id="openai/gpt-oss-120b",
        retries=2,
        exponential_backoff=True
    ),
    fallback_models=[
        OpenAIResponses(id="gpt-4o-mini"),
        Gemini(id="gemini-3.8-flash")
    ],
    markdown=True,
    instructions="You are a halpful and expert travel agent.",
    add_datetime_to_context=True,
    tools=[DuckDuckGoTools()]
  )
agent=build_agent()
agent.print_response("What is the current situation in India?")