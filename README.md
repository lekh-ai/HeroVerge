# HeroVerge

HeroVerge is a tool built for providing Gen-AI-based assistance to Support Engineers, maximizing productivity and managing extensive workloads.

## Features

- **Query Handling**: Takes user input as a query and returns responses from a pretrained LLM of the selective choice. Currently available models are: `llama3_70b`, `llama3_8b`, and `llama2`.
- **JSON Responses**: Returns JSON responses with 5 keys: `summary`, `script`, `sentiment`, `complete`, and `notes`. These responses can be configured at the backend to retain ticket data and provide a guide for further resolution.
- **Client Sharable Email**: Frames a client-sharable email to address the query and take forward the next steps. `LangChain` is used to create a chain out of the JSON responses and cook up an email-based response from the JSON created by the AI model.

  ## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-32236B?style=for-the-badge&logo=flask&logoColor=white)
![LLM](https://img.shields.io/badge/LLMs-llama3_70b,_llama3_8b,_llama2-67232A?style=for-the-badge&logo=alpaca&logoColor=white)
![IBM Watson](https://img.shields.io/badge/IBM_Watson-1F70C1?style=for-the-badge&logo=ibm&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-3498DB?style=for-the-badge&logo=langchain&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD500?style=for-the-badge&logo=hugging-face&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## Deployments

There are two deployments of this project across two Python frameworks:

### Flask Version
- Runs on a local server
- Supports robust designs and functionality using HTML, CSS, and JS

### Streamlit Version
- Deployed on Hugging Face
- [Streamlit Deployment Link](https://huggingface.co/spaces/lekhsisodiya/HeroVerge-streamlit)

Both versions have different UI and frontend configurations. Unlike Streamlit/Gradio, Flask supports HTML, CSS, and JS for more robust designs and functionality.

## UI Appearance

### Flask Version (localhost)
![Flask Version](https://github.com/lekh-ai/HeroVerge/blob/main/static/images/Flask%20UI.png)

### Streamlit Version (Hugging Face)
![Streamlit Version](static/images/Streamlit UI.png)

## Example Test Run Case

- **Query Used**: "Hi support, can you please help me fix my problems with your APIs?"
- **Model Selected**: `llama3_70b`

### API Response
```json
{
  "summary": "Customer is experiencing issues with the APIs",
  "script": "Can you please provide more details about the issues you're facing with our APIs?",
  "sentiment": 50,
  "complete": false,
  "notes": "Customer is experiencing unknown issues with the APIs, need more information to troubleshoot"
}
```



### Future Development
Ticketing System: Facilitate recording and tracking of issues and grant the LLM access to this data to generate insights.
Roles and Permissions: Allot admin and user roles so only admins can create insights from the ticketing database using credentials.

Contact
For more information or to get in touch, please email lekhsisdiya@gmail.com
