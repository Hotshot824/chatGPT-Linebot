## chatGPT-Linebot

![](https://github.com/Hotshot824/chatGPT-Linebot/blob/main/docs/linebot-example.JPG?raw=true)

### Feature

- `chatGPT` on Line Bot 
- Runs on `docker-compose` 
- Published on `Docker Hub`
- Uses `Python3 Django` with `SQLite`
- Only the first response is processed each time

### Requirements

- Knowledge of setting up a `Line Bot`
    - Reference: [LINE Bot Tutorial]
- Obtain an `OpenAI` API [KEY]
- Using `ngrok` to build tunnel.

### Configuration  

**Linebot** config path is located at `src/config.json`
```json
{
    "OPENAI_API": {
        "openai_api_key": "ENTER YOUR OPENAPI KEY",
        "model": "gpt-3.5-turbo",
        "max_token": 1024,
        "temperature": 0.8,
        "timeout": 30
    },
    "LINE_CHANNEL_SECRET": "YOUR LINE SECRET",
    "LINE_CHANNEL_ACCESS_TOKEN": "YOUR LINE ACCESS TOKEN"
}
``` 
- "OPENAI_API" detal can watch [Open AI Chat] 
    - `openai_api_key`: Your OpenAI key
    - `model`
    - `max_token`
    - `temperature`
    - `timeout`: Timeout for each request
- "LINE_CHANNEL_SECRET"
- "LINE_CHANNEL_ACCESS_TOKEN"
All history session storage in `src/history.json`.

**Ngrok** config at init/ngrok/ngrok.yml

```yml
# Enter you ngrok authtoken
authtoken: INPUT AUTHTOKEN
```

### Build from Scratch

1. Clone the repository locally
2. Install Docker and Docker Compose
3. Set `config.json` in `src/config.json` and `ngrok.yml` in `init/ngrok/ngrok.yml`
4. In `chatGPT-Linebot` directory, run `docker-compose up -d`
5. Linebot will be listening at `localhost:8000/chatGPT/callback`
6. Can use `curl -s ngrok:4040/api/tunnels | jq -r '.tunnels[0].public_url' | awk '{print "Linebot Listening at " $0 "/chatGPT/callback"}'`
to get the ngrok tunnel address, or look at `docker compose up` output.
7. Edit the Line Webhook URL

### Client use

1. Can have a continuous conversation.
2. When you want to end a session, enter `#clean` to clean the history session.

[LINE Bot Tutorial]: https://github.com/FawenYo/LINE_Bot_Tutorial
[key]: https://openai.com/api/
[Open AI Chat]: https://platform.openai.com/docs/api-reference/chat/create