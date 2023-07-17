import chatGPT.API.database as DB
import json
import os
import requests

class chatRequest(DB.chatDatabase):
    def __init__(self, user_id):
        DB.chatDatabase.__init__(self, user_id)
        self.__get_config()
        self.__response = ""

    def __get_config(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Set config.
        with open("../../config.json", "r") as f:
            config = json.load(f)['OPENAI_API']
        self.__openai_api_key = config['openai_api_key']
        self.__model = config['model']
        self.__max_token = config['max_token']
        self.__temperature = config['temperature']
        self.__timeout = config['timeout']

        # Set different model config.
        with open("../../models.json", "r") as f:
            config = json.load(f)[self.__model]
        self.__url = config['url']

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

    def __process_response(self, message: str, response: str):
        choices = {
            "text-davinci-003": self.__process_gpt3_response,
            "gpt-3.5-turbo": self.__process_gpt3_5_response
        }

        # Processed response then storage this time chat to database.
        choices[self.__model](response)
        self._storage_messages(message, self.__response)

    def __process_gpt3_response(self, response: str):
        self.__response = response['choices'][0]['text'].lstrip()

    def __process_gpt3_5_response(self, response: str):
        self.__response = response['choices'][0]['message']["content"].lstrip()

    def Request(self, message: str):
        if message == "#clean":
            self._clean_messages()
            self.__response = "A conversation has been restarted!"
            return

        # Get all history chats construct message, then construct request body.
        data = self.__construct_request_data(self._construct_chat(message, self.__model, self.__max_token))

        try:
            response = requests.post(
                self.__url,
                headers={
                    "Authorization": f"Bearer {self.__openai_api_key}",
                    "Content-Type": "application/json",
                },
                json=data,
                # Set request timeout.
                timeout=self.__timeout,
            ).json()

            if "error" in response:
                self.__response = response["error"]["message"]
            else:
                self.__process_response(message, response)

        except requests.exceptions.RequestException as e:
            self.__response = "Network error!"

    def GetResponse(self) -> str:
        return self.__response
