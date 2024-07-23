from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Any, List, Optional
from langchain_ibm import WatsonxLLM
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models import ModelInference
import os
import json

#Please contact me @+91 9179041912 for creds
apikey = "available on request"
project_id = "available on request"

# Parameters for model inference
parameters = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.1,
}

llama2_llm = WatsonxLLM(
    model_id=ModelTypes.LLAMA_2_70B_CHAT.value,
    url="https://jp-tok.ml.cloud.ibm.com",
    project_id=project_id,
    params=parameters,
    apikey=apikey
)

llama3_70b_llm = WatsonxLLM(
    model_id='meta-llama/llama-3-70b-instruct',
    url="https://jp-tok.ml.cloud.ibm.com",
    project_id=project_id,
    apikey=apikey,
    params=parameters,
)

llama3_8b_llm = WatsonxLLM(
    model_id='meta-llama/llama-3-8b-instruct',
    url="https://jp-tok.ml.cloud.ibm.com",
    project_id=project_id,
    apikey=apikey,
    params=parameters,
)

def prompt_llama2(system_prompt, user_prompt):
    formatted_prompt = format_llama2_prompt(system_prompt, user_prompt)
    response = llama2_llm.invoke(formatted_prompt)
    return response

def prompt_llama3_70b(system_prompt, user_prompt):
    formatted_prompt = format_llama3_prompt(system_prompt, user_prompt)
    response = llama3_70b_llm.invoke(formatted_prompt)
    return response

def prompt_llama3_8b(system_prompt, user_prompt):
    formatted_prompt = format_llama3_prompt(system_prompt, user_prompt)
    response = llama3_8b_llm.invoke(formatted_prompt)
    return response

class CallerMessage(BaseModel):
    summary: str = Field(description="summary of what the customer said")
    script: str = Field(description="what the customer support rep should say next from the script")
    sentiment: str = Field(description="A number from 0-100 indicating the sentiment of the message. 0 is negative, 50 is neutral, and 100 is positive")
    complete: str = Field(description="true if all the tasks are complete")
    notes: str = Field(description="any extra notes you want to provide the customer support rep")

def callerMessageTemplate():
    parser = JsonOutputParser(pydantic_object=CallerMessage)
    return parser.get_format_instructions()

def format_llama2_prompt(system_instructions, user_prompt):
    return f"""<s>[INST] <<SYS>>{system_instructions.strip()}<</SYS>>{user_prompt.strip()}[/INST]"""

def format_llama3_prompt(system_instructions, user_prompt):
    return f"""system{system_instructions.strip()}user{user_prompt.strip()}assistant"""

# Function to generate mail draft using LLM
def generate_mail_draft_llm(parsed_response):
    mail_template = f"""
    Dear Customer,
    Thank you for reaching out to us. Below is the summary of our interaction:
    Summary:
    {parsed_response['summary']}
    Script:
    {parsed_response['script']}
    Sentiment:
    The sentiment of your message was noted as {parsed_response['sentiment']}.
    Completion:
    {parsed_response['complete']}
    Notes:
    {parsed_response['notes']}
    Please let us know if you have any further questions or concerns.
    Best regards,
    Support Team
    """
    SYSTEM_MESSAGE = "You are an AI assistant. Please refine the following draft to make it a coherent and professional email:"
    response = prompt_llama3_70b(SYSTEM_MESSAGE, mail_template)

    try:
        refined_mail_draft = json.loads(response).get("text", "Could not generate mail draft.")
    except json.JSONDecodeError:
        refined_mail_draft = response

    return refined_mail_draft
