from roles.critic import CRITIC_PROMPT
from utils.memory import AgentMemory
from utils.llm import call_gemini


memory = AgentMemory()


def get_critic_response(query):
    context = memory.get_context()
    prompt = f"""
                Previous context:\n
                {context}\n\n
                New query: {query}
            """
    reply = call_gemini(CRITIC_PROMPT, prompt)
    memory.add("user", query)
    memory.add("critic", reply)
    return reply
