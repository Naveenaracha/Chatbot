import requests
import json

def get_answer(question):
    api_key = "AIzaSyCdZSZQK7_l5hwFqRy5dy2Vn2j5e_GGJnI"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f'''
                     This is the question of the user: {question}.This is embedded inside a chatbot in a website, answer it in 10-12
                     words and plz try to act like human and only give me the answer and nothing else.
                    '''}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            response_data = response.json()['candidates'][0]['content']['parts'][0]['text']
            
            
            return response_data
        
    except Exception as e:
        return f"Sorry, our servers seems to be a little busy currently."
