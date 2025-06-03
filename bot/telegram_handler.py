from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from core.orchestrator import answer_query

MAX_LEN = 4000            # запас чуть меньше 4096

def split_message(text: str, limit: int = MAX_LEN):
    """Разбивает длинный текст на части ≤ limit."""
    parts = []
    while text:
        parts.append(text[:limit])
        text = text[limit:]
    return parts

async def handle(update: Update, context):
    user_text = update.message.text
    reply = answer_query(user_text)

    # Если текст длинный — шлём по кускам
    for chunk in split_message(reply):
        await update.message.reply_text(chunk)

def launch_bot(token: str):
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    print("Бот запущен. Ожидание сообщений…")
    app.run_polling()
