from google.genai import types


schema_get_critic_response = types.FunctionDeclaration(
    name='get_critic_response',
    description="Get response from the critic",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "query": types.Schema(
                type=types.Type.STRING,
                description="""The query to get the response from
                            the critic""",
            ),
        }
    )
)
