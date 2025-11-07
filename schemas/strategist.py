from google.genai import types


schema_get_strategist_response = types.FunctionDeclaration(
    name='get_strategist_response',
    description="Get the response from the strategist",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
                "query": types.Schema(
                    type=types.Type.STRING,
                    description="""The query to get the response from
                                the strategist""",
                ),
        }
    )
)
