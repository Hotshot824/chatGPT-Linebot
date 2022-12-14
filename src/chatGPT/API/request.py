import openai, json, os

class chatGPT():
    def __init__(self):
        self.__config  = self.__get_config()
        openai.api_key = self.__config['openai_api_key']

    def __get_config(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        print(os.getcwd())
        with open("../../token.json") as f:
            return json.load(f)['OPENAI_API']

    def Request(self, message):
        response = openai.Completion.create(
        model=self.__config['model'],
        prompt=message,
        max_tokens=self.__config['max_token'],
        temperature=self.__config['temperature'],
        )
        return response['choices'][0]['text'].lstrip()
