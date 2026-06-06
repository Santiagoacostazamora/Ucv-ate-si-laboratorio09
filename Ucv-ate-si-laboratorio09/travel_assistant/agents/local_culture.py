from google.adk.agents import Agent

from travel_assistant.tools.culture_tools import get_local_culture_recommendations

local_culture_agent = Agent(
    name="local_culture_agent",
    model="gemini-2.0-flash",
    description="Recommends local food, customs and useful phrases for travelers.",
    instruction="""
You are a local culture travel advisor.

Include typical food, important local customs and useful phrases for travelers.

Rules:
1. Be respectful of local culture.
2. Avoid stereotypes.
3. Give practical recommendations.
4. Use the available tool when the destination is provided.
5. Answer in Spanish.
""",
    tools=[get_local_culture_recommendations],
)
