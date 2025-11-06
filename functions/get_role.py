import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError
from roles.prompts import ROLES

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
messages = []


def get_role_response(role_name, prompt, retries=3, delay=2):
    system_prompt = ROLES[role_name]['system_prompt']

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
