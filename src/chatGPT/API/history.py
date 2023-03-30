import json
import os
import requests


class chatHistory():
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__history = {}
        self.__get_history()

    def __get_history(self):
        with open("../../history.json", "r") as f:
            history = json.load(f)
        if self.__user_id in history:
            self.__history = history[self.__user_id]
        else:
            history[self.__user_id] = {"chat": ""}
            self.__history = history[self.__user_id]

    def __storage_histroy(self):
        with open("../../history.json", "r") as f:
            history = json.load(f)
        history[self.__user_id] = self.__history
        with open("../../history.json", "w") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)

    def _construct_messages(self, message: str) -> str:
        return self.__history['chat'] + message

    def _storage_messages(self, message: str, response: str):
        self.__history['chat'] += message
        self.__history['chat'] += response
        self.__storage_histroy()

    def _clean_messages(self):
        self.__history['chat'] = ""
        self.__storage_histroy()
