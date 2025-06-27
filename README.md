# Telegram Quiz Bot

This is a ready-to-deploy Telegram Quiz Bot with scheduled quizzes in Indian Standard Time.

## Setup

1. Rename `.env.example` to `.env`
2. Add your `TOKEN` and `CHAT_ID` in `.env`
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the bot:
   ```
   python main.py
   ```

## Deployment

You can deploy this bot on platforms like Railway.app, Heroku, or your own server.

## Scheduling

Quizzes are scheduled at:
- 9:30 AM IST
- 10:00 AM IST
- 1:00 PM IST
- 4:30 PM IST
- 8:00 PM IST

---

Developed by ChatGPT