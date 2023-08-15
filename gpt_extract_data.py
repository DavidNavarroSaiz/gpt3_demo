import openai
from dotenv import load_dotenv
import os

load_dotenv()
# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# User input sentence
user_input = "I'm John Smith, and I live at 123 Main St, New York. I'm 25 years old, and you can reach me at john@example.com. My goal with this program is to improve my coding skills."

# Create a conversation using ChatGPT
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that extracts information.",
        },
        {
            "role": "user",
            "content": f"Extract the following information in JSON format:\nName, Location, Address, Age, Areas of interest, Goals.\nIf any data is missing, set it as None.\n\n{user_input}",
        },
    ],
)

# Extract the assistant's reply from the response
chatgpt_output = response["choices"][0]["message"]["content"]
# Print the assistant's reply
print(chatgpt_output)
