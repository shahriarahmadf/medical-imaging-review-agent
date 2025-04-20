"""Module to save all prompt templates."""

def test_prompt_template():
    """Returns test prompt template."""
    template = """
    You are a helpful assistant. The user asks a question, and you respond with a detailed, helpful answer.
    User's question: {question}
    """
    return template