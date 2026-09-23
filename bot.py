import os
import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = int(os.environ.get("CHAT_ID"))

logging.basicConfig(level=logging.INFO)

PHRASES = [
    "⏰ Не будь ебалаем. Встань и сделай что-нибудь полезное.",
    "⏰ Эй, ебалай! Хватит скроллить. Займись делом.",
    "⏰ Напоминание: ебалаи не добиваются целей. Ты не ебалай.",
    "⏰ Час прошёл. Ты всё ещё ебалай или уже нет?",
    "⏰ Вставай, ебалай. Мир ждёт твоих свершений.",
    "⏰ Не будь ебалаем — попей воды, разомнись, поработай.",
    "⏰ Ты серьёзно хочешь остаться ебалаем? Действуй!",
    "⏰ Ебалай detected. Начинаю исправлять. Действуй, брат.",
    "⏰ Час бездействия = шаг к ебалайству. Остановись.",
    "⏰ Напоминаю: ебалаем быть невыгодно. Сделай что-то.",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Бот запущен. Каждый час буду напоминать, что ты не ебалай 😎"
    )

async def remind_loop(app):
    import random
    while True:
        try:
            await app.bot.send_message(
                chat_id=CHAT_ID,
                text=random.choice(PHRASES)
            )
        except Exception as e:
            logging.error(f"Ошибка отправки: {e}")
        await asyncio.sleep(3600)  # 3600 секунд = 1 час

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    asyncio.create_task(remind_loop(app))
    # Держим процесс живым
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
