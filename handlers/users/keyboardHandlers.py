from aiogram import types

from aiogram.dispatcher.filters.builtin import Text

from aiogram.dispatcher import FSMContext   
from states.states import States


from loader import dp , db , bot 

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

@dp.message_handler(Text("back-end"))
async def SubCategory(message : types.Message , state : FSMContext):
    await States.backEnd.set()
    keyboard = await SubCategoryKeyboard(category="back-end")
    await message.answer("ko'rsni tanlang" , reply_markup=keyboard)





@dp.message_handler(state=States.fronEnd)
async def lessonKeyboards(message : types.Message , state : FSMContext):
    lessons = db.select_lesson(category="front-end"  , subcategory=message.text)
    
    if lessons != []:
        global subcategory
        subcategory = message.text
        keyboard = await LessonKeyboards(category="front-end" , subcategory=message.text)
        await message.answer("Dars sonini tanlang" , reply_markup=keyboard)
    else:
        text = f""
        lesson = db.select_lesson(VideoId=message.text[0] , category="front-end" , Subcategory=subcategory)
        text += f"{subcategory} Darslari | {message.text} | {lesson[0][3]}" 
        print(lesson)
        await bot.send_video(message.from_user.id , video=lesson[0][2] , caption=text  )
        # await state.finish()


    # keyboards = await SubCategoryKeyboard(category="front-end")


@dp.message_handler(state=States.backEnd)
async def lessonKeyboards(message : types.Message):
    lessons = db.select_lesson(category="back-end"  , subcategory=message.text)
    
    if lessons != []:
        global subcategory
        subcategory = message.text
        keyboard = await LessonKeyboards(category="back-end" , subcategory=message.text)
        await message.answer("Dars sonini tanlang" , reply_markup=keyboard)

    else:
        text = f"it wooooooooooooooooooooooooooooooooooooooooooooooooooooooooooorks"
        lesson = db.select_lesson(VideoId=message.text[0] , category="back-end" , Subcategory=subcategory)
        print(lesson)
        # print("-----------------------------")
        # print(len(lesson))
        # print(lesson[0][2])
        await bot.send_video(message.from_user.id , video=lesson[0][2] , caption=text  )
