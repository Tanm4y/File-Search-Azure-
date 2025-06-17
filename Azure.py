import os
import base64
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "your endpoint")
deployment = os.getenv("DEPLOYMENT_NAME", "your model")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "YOUR KEY")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="yyyy-dd-mm-preview",
)


chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "hi"
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Hello! How can I assist you today?"
            }
        ]
    }
]

messages = chat_prompt

completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
) 