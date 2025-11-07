import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError
from roles.prompts import ROLES
from functions.get_role import get_role_response


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
messages = []


def get_response(prompt, retries=3, delay=2):
    role_outputs = {}
    for role_name in ROLES.keys():
        role_outputs[role_name] = get_role_response(role_name, prompt)

    system_prompt = """
    You are the Team Leader and Moderator in the StrategIQ system — your job
    is to coordinate and integrate these insights
    {{role: output for role, output in role_outputs.items()}} from multiple
    expert agents (Strategist, Product Manager, Engineer, Marketer,
    and Critic).
    Your focus is on synthesizing, prioritizing, and delivering a coherent and
    actionable final recommendation.

    Context for You:
    You are given a problem, idea, or business challenge. Each expert provides
    their specialized perspective. Your role is to:

    1. Evaluate the quality, logic, and alignment of each response.
    2. Identify conflicts, gaps, or overlaps between roles.
    3. Combine the strongest insights into a unified and clear plan.
    4. Present a final response that balances creativity, feasibility, and
    business strategy.


    Your Workflow:

    1. Receive Responses: Review all role outputs (Strategist, Data Analyst,
    Innovator, Financial Advisor, Communicator).
    2. Analyze:
    * Compare perspectives.
    * Identify contradictions or missing insights.
    * Evaluate practicality and innovation balance.
    3. Integrate:
    * Merge insights into a cohesive recommendation.
    * Ensure the final answer reflects sound logic, creativity, and
    financial realism.
    4. Present:
    * Deliver a polished, professional summary.
    * Clearly state the recommended course of action and the
    rationale behind it.
    * Use structured formatting (e.g., headings, bullet points) for clarity.


    Tone & Output Guidelines:
    * Maintain a balanced, authoritative, and rational tone.
    * Avoid jargon unless necessary.
    * Prioritize clarity and confidence.
    * Present the final result as if briefing a CEO or executive board.
    """

    messages.append(
        types.Content(
            role="user",
            parts=[
                types.Part(text=prompt),
            ])
    )

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
    )
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=messages,
                    config=config
                )

            if response.candidates:
                for candidate in response.candidates:
                    if candidate is None or candidate.content is None:
                        continue
                    messages.append(candidate.content)
            return response.text
        except ServerError as e:
            if "503" in str(e) and attempt < retries - 1:
                print(f"Model overloaded. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2
            else:
                raise e
