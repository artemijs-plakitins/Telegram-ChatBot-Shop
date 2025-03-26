## How to Obtain a Telegram Bot Token

1. Open Telegram and search for **"BotFather"**.
2. Start a chat with BotFather and send the command /newbot to create a new bot.
3. Follow the prompts to name your bot and choose a **unique username**.
4. Once created, BotFather will provide you with a **token** — this token is required for authentication and interaction with the **Telegram API.**

## Database

- This project requires a SQLite database URL. You need to create your own database file and provide the correct URL.<br>

## How to run

1. Create file **.env**<br>
2. Add const variables __TOKEN__ and **DB_URL**<br>
```TOKEN=...your token...```<br>
```DB_URL=...your DB URL...```<br>
3. Write in terminal:<br>
Linux / macOS : ```python3 main.py```<br>
Windows : ```python main.py```.
