import json, os, requests

class chatGPT():
    def __init__(self):
        self.__config  = self.__get_config()

    def __get_config(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        print(os.getcwd())
        with open("../../config.json") as f:
            return json.load(f)['OPENAI_API']

    def Request(self, message):
        try:
            response = requests.post(
                "https://api.openai.com/v1/completions",
                headers = {
                    "Authorization": f"Bearer {self.__config['openai_api_key']}",
                    "Content-Type": "application/json",
                },
                json={
                    "prompt": message,
                    "model": self.__config['model'],
                    "max_tokens": self.__config['max_token'],
                    "temperature": self.__config['temperature'],
                },
                timeout=30,  # Set timeout to 10 seconds
            )
            response = response.json()
            return response['choices'][0]['text'].lstrip()
        except requests.exceptions.RequestException as e:
            return "Network Error: This request is time out!"