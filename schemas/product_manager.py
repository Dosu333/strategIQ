from google.genai import types


schema_get_product_manager_response = types.FunctionDeclaration(
    name='get_product_manager_response',
    description="Get response from the product manager",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "query": types.Schema(
                type=types.Type.STRING,
                description="""The query to get the response from the
                            product manager""",
            ),
        }
    )
)
