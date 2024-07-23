from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Any, List, Optional
from langchain_ibm import WatsonxLLM
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models import ModelInference

apikey = "UQ2jF4FyhBND5S7Xc5ImfQOCRsikRFFJ6AtQe-80StGp"

# Parameters for model inference
parameters = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.1,
}

llama2_llm = WatsonxLLM(
    model_id=ModelTypes.LLAMA_2_70B_CHAT.value,
    url="https://jp-tok.ml.cloud.ibm.com",
    project_id = "da4c5444-528c-4452-b677-71ed875add4c",
    params=parameters,
    apikey  = apikey
)

llama3_70b_llm = WatsonxLLM(
    model_id='meta-llama/llama-3-70b-instruct',
    url="https://jp-tok.ml.cloud.ibm.com",
    project_id="da4c5444-528c-4452-b677-71ed875add4c",
    apikey  = apikey,
    params=parameters,
)

llama3_8b_llm = WatsonxLLM(
    model_id='meta-llama/llama-3-8b-instruct',
    url="https://jp-tok.ml.cloud.ibm.com",
    project_id = "da4c5444-528c-4452-b677-71ed875add4c",
    apikey  = apikey,
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
    return f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>{system_instructions.strip()}<|eot_id|><|start_header_id|>user<|end_header_id|>{user_prompt.strip()}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""



