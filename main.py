#-*- coding: utf-8 -*-
#!/usr/bin/python3
import os
import re
import sys
import time
import random
import logging

from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types import ContentType, Message

"""
EGER_KUZMICH_BOT
5680340390:AAEybg4OLdEasPiqzHvIcdGUX92u3lz5HtQ
"""

DEBUG = 0
API_TOKEN = '5680340390:AAEybg4OLdEasPiqzHvIcdGUX92u3lz5HtQ'
bot_name = 'KUZMICH'

# Configure logging
logging.basicConfig(format="%(asctime)s %(filename)s %(name)s %(funcName)s %(levelname)s %(message)s", 
                    filename='log/messages', 
                    level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help', 'shit', 'crone']) # Реакция на событие - команда /start
async def command_start(message: types.Message): ##Создаем функцию реакции на сообщение
    await bot.send_message(message.from_user.id, "Привет! Я эхо-бот, отправь мне сообщение")  #отправляем сообщение

@dp.message_handler() #Принимает событие - сообщение от юзера
async def anymessage(message: types.Message): #Создаем функцию реакции на сообщение
  if "fuck" in message.text.lower():
    await bot.send_message(message.from.user.id, "Сам ты ФАК!!!")
  else:
    await bot.send_message(message.from_user.id, message.text) # отправляем сообщение

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
