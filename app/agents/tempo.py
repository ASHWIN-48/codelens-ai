from langchain_core.messages import HumanMessage

from app.agents.llm import llm
from app.agents.tools.search_codebase import search_codebase

llm_with_tools = llm.bind_tools(
    [search_codebase]
)

messages = [
    HumanMessage(
        content="How authentication works?"
    )
]

response = llm_with_tools.invoke(
    messages
)

print(response)