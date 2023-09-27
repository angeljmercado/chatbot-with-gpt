import openai
import sys
from decouple import config

api_key = config("key")

class Chatbot:
    """ Chatbot class to send request to the openai API """
    def __init__(self):
        openai.api_key = api_key
    
    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
            ).choices[0].text
        return response
