from roles.marketer import MARKETER_PROMPT
from utils.memory import AgentMemory
from utils.llm import call_gemini


memory = AgentMemory()


def get_marketer_response(query):
    context = memory.get_context()
    prompt = f"""
                Previous context:\n
                {context}\n\n
                New query: {query}
            """
    reply = call_gemini(MARKETER_PROMPT, prompt)
    memory.add("user", query)
    memory.add("marketer", reply)
    return reply
