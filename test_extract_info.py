from dotenv import load_dotenv
import os
from extract_info_user import extract_data
import json


def test_extract_data():
    load_dotenv()
    # Set your OpenAI API key
    api_key = os.environ["OPENAI_API_KEY"]
    user_input = "I'm John Smith, and I live at 123 Main St, New York. I'm 25 years old, and you can reach me at john@example.com. My goal with this program is to improve my coding skills."

    expected_result = {
        "Name": "John Smith",
        "Location": "New York",
        "Address": "123 Main St",
        "Age": 25,
        "Areas of interest": None,
        "Goals": "improve coding skills",
    }

    actual_result_json = extract_data(user_input, api_key)
    actual_result = json.loads(
        actual_result_json
    )  # Parse the JSON string into a dictionary
    # Convert the expected JSON string to a dictionary
    assert expected_result["Name"] == actual_result["Name"]
    assert expected_result["Location"] == actual_result["Location"]
    assert expected_result["Address"] == actual_result["Address"]
    assert expected_result["Age"] == actual_result["Age"]
    assert expected_result["Areas of interest"] == actual_result["Areas of interest"]
    assert expected_result["Goals"] == actual_result["Goals"]
