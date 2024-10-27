import requests
import os
import json

MODEL_GPT_4O="gpt-4o-2024-08-06"
MODEL_O1_MINI="o1-mini"
MODEL_HAIKU="claude-3-haiku-20240307"

def load_dotenv():
    if os.environ.get("__is_ai_loaded__") == "true":
        return
    if not os.path.exists(".env"):
        print(".env file not found, skipping")
        return

    with open(".env") as f:
        for line in f:
            key, value = line.strip().split("=")
            key = key.strip()
            # value also strip quotes if any
            value = value.strip().strip("\"'")
            os.environ[key] = value
            def mask(s):
                if len(s) > 4:
                    return s[:2] + "*"*(len(s)-4) + s[-2:]
                else:
                    return s
            # print(f"Loaded {key}={mask(value)} from .env")
            os.environ["__is_ai_loaded__"] = "true"

def query(prompt, user_message, model=MODEL_O1_MINI, json_mode=True):
    # Step 1: Load the environment variables
    load_dotenv()

    # Step 2: Prepare the API request payload
    payload = {
        "model": model,
        "max_tokens": 12800,
        "messages": [
            # {
            #     "role": "system",
            #     "content": prompt
            # },
            {
                "role": "user",
                "content": "SYSTEM: " + prompt + "\nUSER: " + user_message
            }
        ]
    }
    if json_mode:
        payload["response_format"] = {"type": "json_object"}

    # Step 3: Send the request to the API
    token = os.environ.get('TOKEN')
    endpoint = os.environ.get('ENDPOINT')
    response = requests.post(endpoint, json=payload,
                             headers={'Authorization': 'Bearer ' + token})
    if response.status_code!= 200:
        raise ValueError("Failed to get AI response" + response.text)

    # Step 4: Parse the response
    response_data = response.json()
    if not 'choices' in response_data:
        raise ValueError("Failed to get AI response choices" + response.text)

    ai_resp = response_data['choices'][0]['message']['content']

    if not json_mode:
        return ai_resp

    # remove code fence ```json and ``` if exists
    if ai_resp.startswith("```json") and ai_resp.endswith("```"):
        ai_resp = ai_resp[len("```json"):-len("```")]
    
    # remove all code before {
    ai_resp = "{" + ai_resp.split("{", 1)[-1]

    # Step 5: Attempt to parse the AI response as JSON
    try:
        return json.loads(ai_resp)
    except :
        print("Failed to decode AI response as JSON")
        print(ai_resp)
        raise ValueError("Failed to decode AI response as JSON")
