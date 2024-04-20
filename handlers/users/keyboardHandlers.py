from aiogram import types

from aiogram.dispatcher.filters.builtin import Text

from loader import dp

from keyboards.default.categorykeyboards import categoryKeyboard
from keyboards.default.subcategorysKeyboard import SubCategoryKeyboard
from keyboards.default.LessonKeyboards import LessonKeyboards


@dp.message_handler(Text("Bepul Darslar"))
async def startLesson(message : types.Message):
    await message.answer("Bepul Darslar" , reply_markup=categoryKeyboard)

@dp.message_handler(Text("Dasturlash"))
async def SubCategory(message : types.Message):
    keyboard = await SubCategoryKeyboard("dasturlash")
    await LessonKeyboards(category="dasturlash" , subcategory="Html")
    await message.answer("dasturlashni bo'limini tanlang" , reply_markup=keyboard)