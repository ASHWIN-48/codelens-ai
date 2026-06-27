from langchain_core.messages import HumanMessage
from app.agents.llm import llm
from app.agents.state import AgentState
from app.agents.tools.search_codebase import search_codebase
from app.agents.tools.get_file_contents import get_file_contents
from app.agents.tools.get_function_definition import get_function_definition

tools = [search_codebase, get_file_contents, get_function_definition]
llm_with_tools = llm.bind_tools(tools)

def agent_node(state: AgentState):
    if not state["messages"]:
        messages = [HumanMessage(content=state["question"])]
    else:
        messages = state["messages"][-6:]

    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}