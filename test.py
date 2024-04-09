import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6773333833:AAFsaNhdm_8RvFxcmXoPx0tJ7jH0zGlo1rQ")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Приветики!😊'),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Нажимай уже UwU") 
    await message.answer('😁Приветствую тебя!😁', reply_markup=keyboard)    

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())