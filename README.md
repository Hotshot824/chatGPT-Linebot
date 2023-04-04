## chatGPT-Linebot

![](https://github.com/Hotshot824/chatGPT-Linebot/blob/main/docs/linebot-example.JPG?raw=true)

### Feature

- `chatGPT` on Line Bot 
- Runs on `docker-compose` 
- Published on `Docker Hub`
- Uses `Python3 Django` with `SQLite`
- Processes only the first response each time

### Requirements

- Knowledge of setting up a `Line Bot`
    - Reference: [LINE Bot Tutorial]
- Obtain an `OpenAI` API [KEY]

### Configuration  

Config path is located at `src/config.json` 
- "OPENAI_API"
    - `openai_api_key`: Your OpenAI key
    - `model`
    - `max_token`
    - `temperature`
    - `timeout`: Timeout for each request
- "LINE_CHANNEL_SECRET"
- "LINE_CHANNEL_ACCESS_TOKEN"
All history session storage in `src/history.json`.

### Build from Scratch

1. Clone the repository locally
2. Install Docker and Docker Compose
3. Set `config.json` in `src/config.json`
4. In `chatGPT-Linebot` directory, run `docker-compose up -d`
5. Service will be available on `localhost:8000/chatGPT/callback`
6. Edit the Line Webhook URL 

### How to use

1. Can have a continuous conversation.
2. When you want to end a session, enter `#clean` to clean the history session.

[LINE Bot Tutorial]: https://github.com/FawenYo/LINE_Bot_Tutorial
[key]: https://openai.com/api/