import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ==============================
# Telegram Bot Setup
# ==============================

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to MeetContractBot!")

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

# ==============================
# Flask Web Server (for Render)
# ==============================

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ==============================
# Run Both Together
# ==============================

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    application.run_polling()
