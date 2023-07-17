from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from django.contrib.sessions.backends.db import SessionStore
import chatGPT.API.request as API
import os

import logging
logger = logging.getLogger(__name__)

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# This global variable storage response status.
status = {}

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        logger.info('%s %s %s' % (request.META.get('REMOTE_ADDR'), request.method, request.path))
        logger.info('%s' % (request.META))
        
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                userid = event.source.user_id
                text = event.message.text

                if not userid in status:
                    status[userid] = False

                if status[userid]:
                    response = "Please wait for generating a response!"
                else:
                    status[userid] = True

                    try:
                        # Create chatGPT and send request.
                        chatGPT = API.chatRequest(userid)
                        chatGPT.Request(text)
                        response = chatGPT.GetResponse()
                        status[userid] = False

                        # Catch any error then recovery status.
                    except Exception as e:
                        status[userid] = False

                # Send response to linebot user.
                line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=response)
                )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()