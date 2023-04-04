import json
import os
import requests
from chatGPT.models import User, Chat


class chatHistory():
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__get_user()

    def __get_user(self):
        if not User.objects.filter(user=self.__user_id).exists():
            user = User.objects.create(
                user=self.__user_id
            )
            self.__user = user
        else:
            self.__user = User.objects.get(user=self.__user_id)

    def _construct_chat(self, message: str) -> str:
        related_chats = Chat.objects.filter(user=self.__user).order_by('date')
        history = ""
        for chat in related_chats:
            history += chat.question + "\n"
            history += chat.answer + "\n"
            
        return history + message

    def _storage_messages(self, message: str, response: str):
        Chat.objects.create(
            user=self.__user,
            question=message,
            answer=response
        )

    def _clean_messages(self):
        Chat.objects.filter(user=self.__user).delete()
