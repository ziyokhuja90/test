from aiogram import types

from aiogram.dispatcher.filters.builtin import Text

from aiogram.dispatcher import FSMContext   
from states.states import States


from loader import dp

from keyboards.default.categorykeyboards import categoryKeyboard
from keyboards.default.subcategorysKeyboard import SubCategoryKeyboard
from keyboards.default.LessonKeyboards import LessonKeyboards


@dp.message_handler(Text("Bepul Darslar"))
async def startLesson(message: types.Message):

    await message.answer("Darslar bo'limini tanlang", reply_markup=categoryKeyboard)


@dp.message_handler(Text("front-end"))
async def SubCategory(message : types.Message , state : FSMContext):
    await States.fronEnd.set()
    keyboard = await SubCategoryKeyboard(category="front-end")
    await message.answer("ko'rsni tanlang" , reply_markup=keyboard)


@dp.message_handler(state=States.fronEnd)
async def lessonKeyboards(message : types.Message):
    # keyboards = await SubCategoryKeyboard(category="front-end")
    keyboard = await LessonKeyboards(category="front-end" , subcategory=message.text)
    await message.answer("Dars sonini tanlang" , reply_markup=keyboard)


