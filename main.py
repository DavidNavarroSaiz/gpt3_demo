from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class UserInput(BaseModel):
    user_input: str

@app.post("/extract-information/")
async def extract_information(user_input: UserInput):
    # Set your OpenAI API key
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Create a conversation using ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts information."},
            {"role": "user", "content": f"Extract the following information in JSON format:\nName, Location, Address, Age, Areas of interest, Goals.\nIf any data is missing, set it as None.\n\n{user_input.user_input}"}
        ]
    )

    # Extract the assistant's reply from the response
    chatgpt_output = response['choices'][0]['message']['content']
    return {"assistant_reply": chatgpt_output}
