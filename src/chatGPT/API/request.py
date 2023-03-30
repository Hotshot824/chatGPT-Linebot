import chatGPT.API.history as history
import json, os, requests

class chatRequest(history.chatHistory):
    def __init__(self, user_id):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        history.chatHistory.__init__(self, user_id)
        self.__get_config()
        self.__response = ""

    def __get_config(self):
        with open("../../config.json", "r") as f:
            config = json.load(f)['OPENAI_API']
        self.__openai_api_key = config['openai_api_key']
        self.__model = config['model']
        self.__max_token = config['max_token']
        self.__temperature = config['temperature']
        self.__timeout = config['timeout']

        with open("../../models.json", "r") as f:
            config = json.load(f)[self.__model]
        self.__url = config['url']
        self.__choices_response_process()

    def __choices_response_process(self):
        choices = {
            "text-davinci-003": self.__process_gpt3_response,
            "gpt-3.5-turbo": self.__process_gpt3_5_response
        }
        self.__process_response = choices[self.__model]

    def __construct_request_data(self, message: str) -> dict:
        if self.__model == "gpt-3.5-turbo":
            return {
                "messages": [{"role": "user", "content": message}],
                "model": self.__model,
                "max_tokens": self.__max_token,
                "temperature": self.__temperature,
            }
        elif self.__model == "text-davinci-003":
            return {
                "prompt": message,
                "model": self.__model,
                "max_tokens": self.__max_token,
                "temperature": self.__temperature,
            }

    def __process_gpt3_response(self, response: str):
        self.__response = response['choices'][0]['text'].lstrip()

    def __process_gpt3_5_response(self, response: str):
        self.__response = response['choices'][0]['message']["content"].lstrip()

    def Request(self, message: str):
        if message == "#clean":
            self._clean_messages()
            self.__response = "A conversation has been restarted!"
            return

        data = self.__construct_request_data(self._construct_messages(message))
        try:
            response = requests.post(
                self.__url,
                headers={
                    "Authorization": f"Bearer {self.__openai_api_key}",
                    "Content-Type": "application/json",
                },
                json=data,
                timeout=self.__timeout,  # Set timeout to 10 seconds
            ).json()
            
            self.__process_response(response)
            self._storage_messages(message, self.__response)

        except requests.exceptions.RequestException as e:
            self.__response = "Network Error: This request is time out!"

    def GetResponse(self) -> str:
        return self.__response
