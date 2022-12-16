import openai, json, os, requests

class chatGPT():
    def __init__(self):
        self.__config  = self.__get_config()
        openai.api_key = self.__config['openai_api_key']

    def __get_config(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        print(os.getcwd())
        with open("../../config.json") as f:
            return json.load(f)['OPENAI_API']

    def Request(self, message):
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
            timeout=self.__config['timeout'],  # Set timeout to 5 seconds
        )
        response = response.json()
        return response['choices'][0]['text'].lstrip()