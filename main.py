import logging
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN") or "7623598682:AAGjQwnmzAPDrjbgQmKiyjU8z6-xKtH4QKU"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Добро пожаловать в QuibixBot! 🚀 Используйте /price, /chart, /signals")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=SUPERUSDT"
    response = requests.get(url).json()
    price = response.get("price", "N/A")
    await update.message.reply_text(f"🔹 Цена SUPER/USDT: {price} USDT")

async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chart_url = "https://www.tradingview.com/x/q1w2e3r4/"  # Временно
    await update.message.reply_photo(chart_url, caption="📊 График SUPER/USDT")

async def signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 Сигнал: LONG\n⏱ Таймфрейм: 1ч\n🎯 Тейкпрофит: +4.2%\n🛑 Стоплосс: -1.8%")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("chart", chart))
app.add_handler(CommandHandler("signals", signals))

if __name__ == "__main__":
    app.run_polling()
