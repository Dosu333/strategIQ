from roles.product_manager import PRODUCT_MANAGER_PROMPT
from utils.memory import AgentMemory
from utils.llm import call_gemini


memory = AgentMemory()


def get_product_manager_response(query):
    context = memory.get_context()
    prompt = f"""
                Previous context:\n
                {context}\n\n
                New query: {query}
            """
    reply = call_gemini(PRODUCT_MANAGER_PROMPT, prompt)
    memory.add("user", query)
    memory.add("product manager", reply)
    return reply
