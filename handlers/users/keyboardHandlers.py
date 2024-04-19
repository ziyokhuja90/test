from aiogram import types

from aiogram.dispatcher.filters.builtin import Text

from loader import dp

from keyboards.default.categorykeyboards import categoryKeyboard


@dp.message_handler(Text("Bepul Darslar"))
async def startLesson(message : types.Message):
    await message.answer("Bepul Darslar" , reply_markup=categoryKeyboard)