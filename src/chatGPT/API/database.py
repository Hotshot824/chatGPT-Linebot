import json
import os
import requests
import tiktoken
from chatGPT.models import User, Chat


class chatDatabase():
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

    def _get_count(self) -> int:
        related_chats = Chat.objects.filter(user=self.__user)
        return related_chats.count()

    def __num_tokens_from_string(self, string: str, model: str) -> int:
        # Returns the number of tokens in a text string.
        encoding = tiktoken.encoding_for_model(model)
        num_tokens = len(encoding.encode(string))
        return num_tokens

    def _construct_chat(self, message: str, model: str, max_token: int=1024) -> str:
        # The order is from the early to the last.
        related_chats = Chat.objects.filter(user=self.__user).order_by('-date')

        # Organize past chat record into a string.
        history = ""
        for chat in related_chats:

            count = self.__num_tokens_from_string(history + chat.question + "\n" + chat.answer + "\n" + message, model)
            # Count greater than max toker, break for loop.
            if count < max_token:
                history += chat.question + "\n" + chat.answer + "\n"
            else:
                break

        # Add this time question.
        return history + message

    def _storage_messages(self, message: str, response: str):
        Chat.objects.create(
            user=self.__user,
            question=message,
            answer=response
        )

    def _clean_messages(self):
        Chat.objects.filter(user=self.__user).delete()
