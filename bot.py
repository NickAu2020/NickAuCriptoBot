import os
import logging
from telegram import Bot
from telegram.ext import CommandHandler, Updater

# Получаем токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Настройка логгирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Обработчик команды /start
def start(update, context):
    update.message.reply_text("✅ Привет, Николай! Бот работает. Жду сигналы по стратегии Gainers!")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Команда /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
