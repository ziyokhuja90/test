
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from uuid import uuid4
from loader import dp , db

from keyboards.default.simpleKeyboards import StartLesson


uuid = uuid4()
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    # db.add_subcategory(id=f"{str(uuid)}1" , name="Photoshop", category="Grafik dizayn")
    # db.add_subcategory(id=f"{str(uuid)}" , name="Illustrator", category="Grafik dizayn")
    # db.add_subcategory(id=f"{str(uuid)}3" , name="CoralDraw", category="")
    # db.add_subcategory(id=f"{str(uuid)}" , name="Python Django", category="back-end")
    # db.add_subcategory(id=str(uuid) , name="Css" , category="dasturlash")
    # db.add_lesson(id=str(uuid) ,videoId="testvideoid", CountOfLesson="test1",info="testlessoninfo",youtube="testyoutube",telegram="testtelegram", category="dasturlash" , subcategory="Html")    
    # db.add_category(id=str(uuid) , name="Front-end")
    # db.add_category(id=f"1{str(uuid)}" , name="Back-end")
    # db.delete_one_category(name="Grafik dizayn")
    # db.add_category(id=f"1{str(uuid)}" , name="Grafik dizayn")


    await message.answer(f"Salom, {message.from_user.full_name}!" , reply_markup=StartLesson)