from src.api.external_services.llm.gpt_turbo35 import get_gpt_3_5_turbo
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from src.api.utils.prompt_templates import test_prompt_template

def get_response_from_user_input(user_input):
    """Takes user input and generates response for testing."""

    prompt_template = test_prompt_template()
    print(type(prompt_template))

    prompt = PromptTemplate(input_variables=["question"], template=prompt_template)

    llm = get_gpt_3_5_turbo()

    chain = prompt | llm

    response = chain.invoke({"question": user_input})

    return response

response = get_response_from_user_input("What are your opinions on modern women?")

print(response.content)