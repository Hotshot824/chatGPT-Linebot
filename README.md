## chatGPT-Linebot

![](https://github.com/Hotshot824/chatGPT-Linebot/blob/main/docs/linebot-example.JPG?raw=true)

### Feature

- chatGPT on linebot 
- Run on docker-compose 
- Publish on docker hub
- Use python3 django
- Only the first response is processed each time

### Require

- Must know how to set up Line Bot
    - refence: [LINE Bot Tutorial]
- Get the OpenAi api [KEY] 

### Config  

config path on `src/token.json` 
- "OPENAI_API"
    - openai_api_key : You openAI key
    - model
    - max_token
    - temperature
- "LINE_CHANNEL_SECRET"
- "LINE_CHANNEL_ACCESS_TOKEN"

### Build from scratch

1. clone repository to the local
2. install docker and docker-compose
3. set token.json in src/token.json
4. in chatGPT-Linebot directory run `docker-compose up -d`
<<<<<<< HEAD
5. service on port 8000
=======
5. service on localhost:8000/chatGPT/callback
6. edit the Line Webhook URL 
>>>>>>> main

[LINE Bot Tutorial]: https://github.com/FawenYo/LINE_Bot_Tutorial
[key]: https://openai.com/api/