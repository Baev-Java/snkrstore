from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add("Каталог").add("Корзина").add("Контакты")


main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add("Каталог").add("Корзина").add("Контакты").add("Админ-панель")


admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add("Добавить товар").add("Удалить товар").add("Сделать рассылку")

@dp.message_handler(text="Админ-панель")
async def contacts(message: types.Message):
    if message.from_user.id == int(os.getenv("ADMIN_ID")):
        await message.answer(f'Вы вошли в админ панель', reply_markup=admin_panel)
    else:
        await message.reply('Я тебя не понимаю.')

@dp.message_handler(commands=['start'])#обрабатывает команды
async def cmd_start(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAMeZHcYRYRrbEw0MSoK9vwWco-15BYAAsYBAAIWQmsKSiPU9MnbeUcvBA")#отправка стикера
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в магазин кроовок!',
                         reply_markup=main)
    if message.from_user.id == int(os.getenv("ADMIN_ID")):
        await message.answer(f'Вы вошли как администратор!', reply_markup=main_admin)


@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')


@dp.message_handler(text="Контакты")
async def contacts(message: types.Message):
    await message.answer(f'Покупать товар у него: @Y_Baev')


@dp.message_handler(text="Корзина")
async def cart(message: types.Message):
    await message.answer(f'Корзина пуста!')


@dp.message_handler(text="Каталог")
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст!')


@dp.message_handler()#обрабатывает неизвестные слова отвечая на них
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю.')


if __name__ == '__main__':
    executor.start_polling(dp)
