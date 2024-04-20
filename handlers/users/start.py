
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from uuid import uuid4
from loader import dp , db

from keyboards.default.simpleKeyboards import StartLesson


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    uuid = uuid4()
    
    db.add_subcategory(id=f"{str(uuid)}1" , name="Html" , category="front-end")
    # db.add_subcategory(id=str(uuid) , name="Css" , category="dasturlash")
    # db.add_lesson(id=str(uuid) ,videoId="testvideoid", CountOfLesson="test1",info="testlessoninfo",youtube="testyoutube",telegram="testtelegram", category="dasturlash" , subcategory="Html")    
    # db.add_category(id=str(uuid) , name="front-end")
    # db.add_category(id=f"1{str(uuid)}" , name="back-end")


    await message.answer(f"Salom, {message.from_user.full_name}!" , reply_markup=StartLesson)