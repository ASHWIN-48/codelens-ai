from langchain_core.messages import ToolMessage
from app.agents.state import AgentState
from app.agents.tools.search_codebase import search_codebase
from app.agents.tools.get_file_contents import get_file_contents
from app.agents.tools.get_function_definition import get_function_definition

tools_map = {
    "search_codebase": search_codebase,
    "get_file_contents": get_file_contents,
    "get_function_definition": get_function_definition
}


def tool_node(state: AgentState):
    last_message = state["messages"][-1]
    tool_messages = []

    for tool_call in last_message.tool_calls:
        tool = tools_map.get(tool_call["name"])
        if tool is None:
            result = f"Tool '{tool_call['name']}' not found"
        else:
            result = tool.invoke(tool_call["args"])

        tool_messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )
        )

    return {"messages": tool_messages}