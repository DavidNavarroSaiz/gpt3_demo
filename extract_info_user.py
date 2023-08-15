import openai

# User input sentence
def extract_data(user_input,api_key):
    openai.api_key = api_key
    # Create a conversation using ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts information."},
            {"role": "user", "content": f"Extract the following information in JSON format:\nName, Location, Address, Age, Areas of interest, Goals.\nIf any data is missing, set it as None.\n\n{user_input}"}
        ]
    )

    # Extract the assistant's reply from the response
    chatgpt_output = response['choices'][0]['message']['content']
    # Print the assistant's reply
    return chatgpt_output
