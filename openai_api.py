import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_openai_response(message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, there was a problem processing your request."
