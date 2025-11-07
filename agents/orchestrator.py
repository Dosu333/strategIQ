from google.genai import types
from schemas.strategist import schema_get_strategist_response
from schemas.product_manager import schema_get_product_manager_response
from schemas.marketer import schema_get_marketer_response
from schemas.engineer import schema_get_engineer_response
from schemas.critic import schema_get_critic_response
from utils.memory import AgentMemory
from utils.llm import call_gemini

memory = AgentMemory()


def get_response(prompt, retries=3, delay=2):
    system_prompt = """
        You are the Team Leader and Moderator in the StrategIQ system.
        You may at any point call specialized agents (Strategist
        , Product Manager, Engineer, Marketer, Critic) whenever their input
        would help refine your response or resolve uncertainty.
        Continue doing so as needed throughout the conversation.

        1. Evaluate the quality, logic, and alignment of each response.
        2. Identify conflicts, gaps, or overlaps between roles.
        3. Combine the strongest insights into a unified and clear plan
        when necessary.


        Tone & Output Guidelines:
        * Maintain a balanced, authoritative, and rational tone.
        * Avoid jargon unless necessary.
        * Prioritize clarity and confidence.
    """

    context = memory.get_context()
    available_agents = types.Tool(
        function_declarations=[
            schema_get_strategist_response,
            schema_get_product_manager_response,
            schema_get_marketer_response,
            schema_get_engineer_response,
            schema_get_critic_response,
        ]
    )
    prompt = f"""
        Previous Context:\n
        {context}\n\n
        New query:\n
        {prompt}
    """
    reply = call_gemini(system_prompt, prompt, tools=available_agents)
    return reply
