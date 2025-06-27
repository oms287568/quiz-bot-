import os
import logging
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, time, timedelta
import pytz

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)

# Example quiz list (simplified)
quizzes = [
    {"q": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Chennai"], "answer": 0},
    {"q": "Who is the President of USA?", "options": ["Biden", "Trump", "Obama"], "answer": 0},
    {"q": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": 1},
]

def send_quiz():
    quiz = quizzes.pop(0)
    quizzes.append(quiz)  # rotate
    question = quiz["q"]
    options = quiz["options"]
    text = f"Quiz Time!\n{question}\nOptions:\n"
    for i, option in enumerate(options):
        text += f"{i+1}. {option}\n"
    bot.send_message(chat_id=CHAT_ID, text=text)

def start(update, context):
    update.message.reply_text("Quiz Bot started!")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    scheduler = BackgroundScheduler(timezone=pytz.timezone('Asia/Kolkata'))

    # Schedule quiz every day at 9:30, 10:00, 13:00, 16:30, 20:00 IST
    times = [time(9,30), time(10,0), time(13,0), time(16,30), time(20,0)]
    for quiz_time in times:
        scheduler.add_job(send_quiz, 'cron', hour=quiz_time.hour, minute=quiz_time.minute)

    scheduler.start()
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()