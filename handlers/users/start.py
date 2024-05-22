
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from uuid import uuid4
from loader import dp , db

from keyboards.default.simpleKeyboards import StartLesson


uuid = uuid4()
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
   
   

    await message.answer(f"Salom, {message.from_user.full_name}!" , reply_markup=StartLesson)