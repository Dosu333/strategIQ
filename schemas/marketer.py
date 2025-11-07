from google.genai import types


schema_get_marketer_response = types.FunctionDeclaration(
    name='get_marketer_response',
    description="Get response from the marketer",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "query": types.Schema(
                type=types.Type.STRING,
                description="""The query to get the response from the
                            marketer""",
            ),
        }
    )
)
