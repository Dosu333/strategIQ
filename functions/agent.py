from google.genai import types
from agents.critic import get_critic_response
from agents.engineer import get_engineer_response
from agents.marketer import get_marketer_response
from agents.product_manager import get_product_manager_response
from agents.strategist import get_strategist_response


def call_agent(function_call_part, verbose=True):
    if verbose:
        print(f"""Calling function:
            {function_call_part.name}({function_call_part.args})""")
    else:
        print(f"Calling function: {function_call_part.name}")

    result = ""
    if function_call_part.name == "get_strategist_response":
        result = get_strategist_response(**function_call_part.args)
    elif function_call_part.name == "get_product_manager_response":
        result = get_product_manager_response(**function_call_part.args)
    elif function_call_part.name == "get_marketer_response":
        result = get_marketer_response(**function_call_part.args)
    elif function_call_part.name == "get_engineer_response":
        result = get_engineer_response(**function_call_part.args)
    elif function_call_part.name == "get_critic_response":
        result = get_critic_response(**function_call_part.args)
    else:
        result = {"status": "failure", "message": "Function not found"}

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={'result': result}
            )
        ]
    )
