import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot setup
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 MeetContractBot is online!")

# Telegram app
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

# Run bot in background thread
def run_bot():
    application.run_polling()

threading.Thread(target=run_bot, daemon=True).start()

# Flask app in main thread
app = Flask(__name__)

@app.route("/")
def home():
    return "MeetContractBot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
