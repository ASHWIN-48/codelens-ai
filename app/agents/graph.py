from langgraph.graph import START, END, StateGraph
from app.agents.nodes.tools_node import tool_node
from app.agents.state import AgentState
from app.agents.nodes.agent_node import agent_node


def route_tools(state: AgentState):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tool"

    return END
graph_builder = StateGraph(AgentState)

graph_builder.add_node("agent",agent_node)
graph_builder.add_node("tool",tool_node)

graph_builder.add_edge(START,"agent")

graph_builder.add_conditional_edges("agent",route_tools)
graph_builder.add_edge("tool","agent")

graph = graph_builder.compile()