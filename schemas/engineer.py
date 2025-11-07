from google.genai import types


schema_get_engineer_response = types.FunctionDeclaration(
    name='get_engineer_response',
    description="Get response from the engineer",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "query": types.Schema(
                type=types.Type.STRING,
                description="""The query to get the response from the
                            engineer""",
            ),
        }
    )
)
