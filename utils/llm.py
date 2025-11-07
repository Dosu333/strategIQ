import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def call_gemini(system_prompt, user_input, retries=3, delay=2, tools=None):
    messages = [
            types.Content(role="user", parts=[types.Part(text=user_input)]),
        ]
    if not tools:
        config = types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    else:
        config = types.GenerateContentConfig(
            tools=[tools],
            system_instruction=system_prompt
        )

    while True:
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
                if response.function_calls:
                    from functions.agent import call_agent
                    for function_call_part in response.function_calls:
                        result = call_agent(function_call_part)
                        messages.append(result)
                    continue
                return response.text
            except ServerError as e:
                if "503" in str(e) and attempt < retries - 1:
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2
                else:
                    raise e
