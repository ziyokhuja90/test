from loader import dp , db , bot
from aiogram.types import Message

from aiogram import types

from aiogram.dispatcher import FSMContext   

from states.add_lesson_states import Add_Lesson_State

from uuid import uuid4

from keyboards.default.categorykeyboards import categoryKeyboard
from keyboards.default.subcategorysKeyboard import SubCategoryKeyboard




@dp.message_handler(commands=["addLesson"])
async def AddLesson(message : Message , state : FSMContext):

    await Add_Lesson_State.password.set()
    await message.answer("Assaolmu alayekum yangi dars qo'shishlik uchun parolni kiritishingiz kerak bo'ladi \nParolni kiriting")


@dp.message_handler(state=Add_Lesson_State.password)
async def AddLessonVideoId(message:Message ,state : FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
    
    if data['password'] == "1234":
        await message.answer("Parollingiz to'gri \nDarsdi videosini tashlashingiz mumkin")
        await Add_Lesson_State.next()
    else:
        await message.answer("parol noto'g'ri")

@dp.message_handler(content_types=types.ContentTypes.VIDEO , state=Add_Lesson_State.videoId)
async def AddLessonNumberOfLesson(message:Message ,state : FSMContext):
    video_file_id = message.video.file_id

    async with state.proxy() as data:
        data['videoId'] = video_file_id
    
    await bot.send_message(chat_id=message.from_user.id , text="Video qabul qilindi \nDars sonini kiriting")
    await Add_Lesson_State.next()

@dp.message_handler(state=Add_Lesson_State.NumberOfLesson)
async def Addlessoninfo(message : Message , state : FSMContext):

    async with state.proxy() as data:
        data['NumberOfLesson'] = message.text
    

    await message.answer("Dars haqida ma'lumot kiriting")
    await Add_Lesson_State.next()

@dp.message_handler(state=Add_Lesson_State.info)
async def youtube(message : Message , state : FSMContext):

    async with state.proxy() as data:
        data['info'] = message.text
    

    await message.answer("Darsdi youtubedagi linkini joylang")
    await Add_Lesson_State.next()


@dp.message_handler(state=Add_Lesson_State.youtube)
async def Telegram(message : Message , state : FSMContext):

    async with state.proxy() as data:
        data['youtube'] = message.text
    

    await message.answer("Darsdi Telegramdagi linkini joylang")
    await Add_Lesson_State.next()

@dp.message_handler(state=Add_Lesson_State.telegram)
async def category(message : Message , state : FSMContext):

    async with state.proxy() as data:
        data['telegram'] = message.text
    

    await message.answer("categoryyani kiriting" , reply_markup=categoryKeyboard)
    await Add_Lesson_State.next()



@dp.message_handler(state=Add_Lesson_State.category)
async def subcategory(message : Message , state : FSMContext):

    async with state.proxy() as data:
        data['category'] = message.text
    
    keyboards  = await SubCategoryKeyboard(category=data["category"].lower())
    await message.answer("subcategoryyani kiriting" , reply_markup=keyboards)
    await Add_Lesson_State.next()


@dp.message_handler(state=Add_Lesson_State.subcategory)
async def SaveToDB(message : Message , state : FSMContext):

    async with state.proxy() as data:
        data['subcategory'] = message.text
    
    
    newLesson = db.add_lesson(
        id=str(uuid4()), 
        videoId=data["videoId"], 
        CountOfLesson=data["NumberOfLesson"],
        info=data["info"],
        youtube=data["youtube"],
        telegram=data["telegram"],
        category=data["category"],
        subcategory=data["subcategory"]
        
        )

    await message.answer("Yangi dars saqlandi")
    await state.finish()
