from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])#обрабатывает команды
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, Добро пожаловать в магазин кроовок!')

@dp.message_handler()#обрабатывает неизвестные слова отвечая на них
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю.')

if __name__ == '__main__':
    executor.start_polling(dp)
