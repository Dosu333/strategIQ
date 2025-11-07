from roles.engineer import ENGINEER_PROMPT
from utils.memory import AgentMemory
from utils.llm import call_gemini


memory = AgentMemory()


def get_engineer_response(query):
    context = memory.get_context()
    prompt = f"""
                Previous context:\n
                {context}\n\n
                New query: {query}
            """
    reply = call_gemini(ENGINEER_PROMPT, prompt)
    memory.add("user", query)
    memory.add("engineer", reply)
    return reply
