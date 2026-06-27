from app.agents.graph import graph
from groq import BadRequestError

class AgentService:
    def run(self, task: str) -> str:
        try:
            result = graph.invoke({
                "question": task,
                "messages": []
            })
            last_message = result["messages"][-1]
            return last_message.content
        except BadRequestError as e:
            body = e.body or {}
            failed_gen = body.get("error", {}).get("failed_generation", "")
            if failed_gen:
                lines = failed_gen.split("\n")
                content_lines = [l for l in lines if not l.startswith("<function")]
                content = "\n".join(content_lines).strip()
                if len(content) > 50:
                    return content
            return "Request failed. Try a simpler query or smaller file."

agent_service = AgentService()