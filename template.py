from langchain.prompts import PromptTemplate

template = """
You are an expert {subject} tutor. Explain the following concept to a {level} student:

Concept: {concept}
"""

prompt = PromptTemplate(
    # input_variables=["chemistry", "byebyebye", "hello"],
    template=template
)

formatted_prompt = prompt.format(
    subject="chemistry",
    level="high school",
    concept="molecular structure"
)

print(formatted_prompt)