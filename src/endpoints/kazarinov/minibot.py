
## \file /src/endpoints/kazarinov/minibot.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
```rst
.. module:: src.endpoints.kazarinov.minibot 
```

Минибот для обслуживания запросов на создание прайслиста для Казаринова
========================================================================


[Документация](https://github.com/hypo69/hypotez/blob/master/docs/ru/src/endpoints/kazarinov/minibot.py.md)
"""

import telebot
import os
import datetime
import random
from pathlib import Path
import asyncio
import time


import header
from header import __root__
from src import gs
from src.logger import logger
from src.llm.gemini import GoogleGenerativeAi
from src.endpoints.kazarinov.scenarios.scenario import fetch_target_urls_onetab, Scenario
from src.utils.url import is_url
from src.utils.printer import pprint as print
from src import USE_ENV


# --- config.py -----------------
@dataclass
class Config:
    
    ENDPOINT:str = 'kazarinov'
    MODE:str = 'PRODUCTION' # <- Определяет режим разработчика. Если MODE=='PRODUCTION' будет запущен kazarionaov бот, иначе тестбот
    #MODE:str = 'DEV'
    BOT_TOKEN:str

    if MODE=='PRODUCTION':
        BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN') if USE_ENV else gs.credentials.telegram.hypo69_kazarinov_bot
    else:
        BOT_TOKEN = os.getenv('TEST_BOT_TOKEN') if USE_ENV else gs.credentials.telegram.hypo69_test_bot

    CHANNEL_ID = '@onela'
    PHOTO_DIR = Path(__root__ / 'endpoints' / 'kazarinov' / 'assets')
    COMMAND_INFO = 'This is a simple bot. Use /help to see commands.'
    UNKNOWN_COMMAND_MESSAGE = 'Unknown command. Use /help to see available commands.'
    START_MESSAGE = "Howdy, how are you doing?"
    HELP_MESSAGE = """
    Here are the available commands:
    /start - Starts the bot.
    /help - Shows this help message.
    /info - Shows information about the bot.
    /time - Shows the current time.
    /photo - Sends a random photo.
    """
    WINDOW_MODE = 'normal'

    if USE_ENV:
        from dotenv import load_dotenv
        load_dotenv()
    
# --- config.py end -----------------



class BotHandler:
    """Исполнитель команд, полученных ботом."""

    base_dir: Path = __root__ / 'src' / 'endpoints' / 'kazarinov'

    def __init__(self):
        """Инициализация обработчика событий телеграм-бота."""
        self.questions_list = ['Я не понял?', 'Объясни пожалуйста']
        self.model = GoogleGenerativeAi(os.getenv('GEMINI_API') if USE_ENV else gs.credentials.gemini.kazarinov)

    def handle_message(self, bot:telebot, message:'message'):
        """Обработка текстовых сообщений."""
        text = message.text
        if text == '?':
            self._send_user_flowchart(bot, message.chat.id)
        elif is_url(text):
            self._handle_url(bot, message)
        elif text in ('--next', '-next', '__next', '-n', '-q'):
            self._handle_next_command(bot, message)
        else:
            try:
                answer = self.model.chat(text)
                bot.send_message(message.chat.id, answer)
            except Exception as ex:
                logger.error(f"Error during model interaction: {ex}")
                bot.send_message(message.chat.id, "Произошла ошибка при обработке сообщения.")



    def _send_user_flowchart(self, bot, chat_id):
        """Отправка схемы user_flowchart."""
        photo_path = self.base_dir / 'assets' / 'user_flowchart.png'
        try:
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id, photo)
        except FileNotFoundError:
            logger.error(f"File not found: {photo_path}")
            bot.send_message(chat_id, "Схема не найдена.")

    def _handle_url(self, bot, message:'message'):
        """Обработка URL, присланного пользователем."""
        url = message.text
        if not url.startswith(('https://one-tab.com', 'https://www.one-tab.com')):
            bot.send_message(message.chat.id, 'Мне на вход нужен URL `https://one-tab.com` Проверь, что ты мне посылаешь')
            return

        # Parsing https//one-tab.com/XXXXXXXXX 
        try:
           price, mexiron_name, urls = fetch_target_urls_onetab(url)
           bot.send_message(message.chat.id, f'Получил мехирон {mexiron_name} - {price} шек')
        except Exception as ex:
            logger.error(f"Error fetching URLs from OneTab: ",ex)
            bot.send_message(message.chat.id, "Произошла ошибка при получении данных из OneTab.")
            return
        if not urls:
            bot.send_message(message.chat.id, 'Некорректные данные. Не получил список URL комплектующих')
            return

        try:
            self.scenario = Scenario(window_mode = Config.WINDOW_MODE)
            asyncio.run(
                self.scenario.run_scenario_async(
                mexiron_name = mexiron_name,
                urls = list(urls), 
                price = price,
                bot = bot,
                chat_id = message.chat.id,))

        

        except Exception as ex:
            logger.error(f"Error during scenario execution:", ex)
            bot.send_message(message.chat.id, f"Произошла ошибка при выполнении сценария. {ex}")



    def _handle_next_command(self, bot, message):
        """Обработка команды '--next' и её аналогов."""
        try:
            question = random.choice(self.questions_list)
            answer = self.model.ask(question)
            bot.send_message(message.chat.id, question)
            bot.send_message(message.chat.id, answer)
        except Exception as ex:
            logger.error(f'Ошибка чтения вопросов: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при чтении вопросов.')


    def help_command(self, bot, message):
        """Обработка команды /help."""
        bot.send_message(
            message.chat.id,
            'Available commands:\n'
            '/start - Start the bot\n'
            '/help - Show this help message\n'
            '/sendpdf - Send a PDF file'
        )


    def send_pdf(self, bot, message, pdf_file):
        """Обработка команды /sendpdf для отправки PDF."""
        try:
            with open(pdf_file, 'rb') as pdf_file_obj:
                bot.send_document(message.chat.id, document=pdf_file_obj)
        except Exception as ex:
            logger.error(f'Ошибка при отправке PDF-файла: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при отправке PDF-файла. Попробуй ещё раз.')

    def handle_voice(self, bot, message):
        """Обработка голосовых сообщений."""
        try:
            file_info = bot.get_file(message.voice.file_id)
            file = bot.download_file(file_info.file_path)
            file_path = gs.path.temp / f'{message.voice.file_id}.ogg'
            with open(file_path, 'wb') as f:
                f.write(file)
            transcribed_text = self._transcribe_voice(file_path)
            bot.send_message(message.chat.id, f'Распознанный текст: {transcribed_text}')
        except Exception as ex:
            logger.error(f'Ошибка при обработке голосового сообщения: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при обработке голосового сообщения. Попробуй ещё раз.')


    def _transcribe_voice(self, file_path):
        """Транскрибирование голосового сообщения (заглушка)."""
        return 'Распознавание голоса ещё не реализовано.'


    def handle_document(self, bot, message):
        """Обработка полученных документов."""
        try:
            file_info = bot.get_file(message.document.file_id)
            file = bot.download_file(file_info.file_path)
            tmp_file_path = gs.path.temp / message.document.file_name
            with open(tmp_file_path, 'wb') as f:
                f.write(file)
            bot.send_message(message.chat.id, f'Файл сохранен в {tmp_file_path}')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при обработке документа: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при обработке документа. Попробуй ещё раз.')
            return False




# --- bot.py ---
config = Config()
handler = BotHandler()
bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def command_start(message):
    logger.info(f"User {message.from_user.username} send /start command")
    bot.send_message(message.chat.id, config.START_MESSAGE)

@bot.message_handler(commands=['help'])
def command_help(message):
    logger.info(f"User {message.from_user.username} send /help command")
    handler.help_command(bot, message)

@bot.message_handler(commands=['info'])
def command_info(message):
    logger.info(f"User {message.from_user.username} send /info command")
    bot.send_message(message.chat.id, config.COMMAND_INFO)

@bot.message_handler(commands=['time'])
def command_time(message):
    logger.info(f"User {message.from_user.username} send /time command")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"Current time: {current_time}")

@bot.message_handler(commands=['photo'])
def command_photo(message):
    logger.info(f"User {message.from_user.username} send /photo command")
    try:
        photo_files = os.listdir(config.PHOTO_DIR)
        if photo_files:
            random_photo = random.choice(photo_files)
            photo_path = os.path.join(config.PHOTO_DIR, random_photo)
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, "No photos in the folder.")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Photo directory not found.")

@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    logger.info(f"User {message.from_user.username} send voice message")
    handler.handle_voice(bot, message)

@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    logger.info(f'User {message.from_user.username} send document message')
    handler.handle_document(bot, message)

@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f'User {message.from_user.username} sent message: {message.text}')
    handler.handle_message(bot, message )

@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    logger.info(f'User {message.from_user.username} send unknown command: {message.text}')
    bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)

# def main():

#     try:
#         logger.info(f'Starting bot in {Config.MODE} mode')
#         bot.polling(none_stop=True)
        
#     except Exception as ex:
#         logger.error(f'Error during bot polling: ', ex, False)
#         ...
#         try:
#             bot.stop_bot()
#         except Exception as ex:
#             logger.error(f'Ошибка останова бота:', ex, False)
#         logger.debug('Повторный запуск через 10 сек')
#         time.sleep(10)
#         main()

def run_bot() -> None:
    """
    Запускает polling-бота в бесконечном цикле с автоматическим восстановлением при ошибках.

    При возникновении исключений выполняется остановка бота и повторный запуск через 10 секунд.

    Raises:
        Exception: Повторно пробрасывается при фатальной ошибке, если бот не может быть запущен.
    """
    try:
        logger.info(f'Starting bot in {Config.MODE} mode')
        bot.infinity_polling()
        

    except Exception as ex:
        logger.error('Error during bot polling', ex, exc_info=True)

        try:
            bot.stop_bot()
        except Exception as ex:
            logger.error('Ошибка останова бота', ex, exc_info=True)

        logger.debug('Повторный запуск через 10 секунд')
        time.sleep(10)
        run_bot()

if __name__ == '__main__':
    run_bot()
   