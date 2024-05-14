from aiogram import types
from aiogram.dispatcher.filters.builtin import Text

from aiogram.dispatcher import FSMContext   
from states.states import States , BackButtonStates

from loader import dp , db , bot 


from keyboards.default import simpleKeyboards
from keyboards.default.categorykeyboards import categoryKeyboard
from keyboards.default.subcategorysKeyboard import SubCategoryKeyboard
from keyboards.default.LessonKeyboards import LessonKeyboards
from keyboards.default.simpleKeyboards import StartLesson ,  dasturlashKeyboard , HomeKeyboards


@dp.message_handler(Text(contains="Menyu") , state="*")
async def MainMenuHandler(message: types.Message , state: FSMContext):
    await state.finish()
    await message.answer("Bosh bo'lim" , reply_markup=HomeKeyboards)

@dp.message_handler(Text("Bepul Darslar"))
async def startLesson(message: types.Message):
    print(message.reply_markup)
    await message.answer("Quyidagi bo'limlardan birini tanlang.", reply_markup=HomeKeyboards)


@dp.message_handler(Text('Grafik dizayn') , state='*')
async def grafikdizaynHandler(message: types.Message):

    await States.grafikDizayn.set()
    # keyboards = simpleKeyboards.grafikdizayn
    # keyboards.keyboard.append([simpleKeyboards.back_button])

    # keyboards.add(simpleKeyboards.back_button)
    await message.answer("Kursni tanlang" , reply_markup=simpleKeyboards.grafikdizayn)

@dp.message_handler(Text(contains="Orqaga") , state=States.grafikDizayn  )
async def fisrtLevelBackHandler(message: types.Message , state : FSMContext):
    await state.finish()
    await message.answer(message.text , reply_markup=HomeKeyboards)


@dp.message_handler(state=States.grafikDizayn)
async def GrakifdizaynlessonHandler(message : types.Message):
    lessons = db.select_lesson(category="Grafik dizayn"  , subcategory=message.text)
    
    if lessons != []:
        global subcategory
        subcategory = message.text
        keyboard = await LessonKeyboards(category="Grafik dizayn" , subcategory=message.text)
        await message.answer("Dars sonini tanlang" , reply_markup=keyboard)
    else:
        try:
            text = f""
            lesson = db.select_lesson(VideoId=message.text[0] , category="Grafik dizayn" , Subcategory=subcategory)
            text += f"{subcategory} Darslari | {message.text} | {lesson[0][3]} \n\n"
            text += f"Youtub — {lesson[0][4]} \n\n"
            text += f"Telegram — {lesson[0][5]} \n\n"
            print(lesson)
            await bot.send_video(message.from_user.id , video=lesson[0][2] , caption=text , )
        # await state.finish()
        except:
            pass






@dp.message_handler(Text("Dasturlash") , state="*")
async def startLesson(message: types.Message):

    await BackButtonStates.level1.set()
    await message.answer("Kursni tanlang", reply_markup=simpleKeyboards.dasturlashKeyboard)

@dp.message_handler(Text(contains="Orqaga"), state=BackButtonStates.level1)
async def dasturlashBackButtonHandler(message : types.Message ,  state : FSMContext):
    await state.finish()
    await message.answer(message.text , reply_markup=HomeKeyboards)


@dp.message_handler(Text("Front-end") ,state="*")
async def SubCategory(message : types.Message , state : FSMContext):
    await States.fronEnd.set()
    keyboard = await SubCategoryKeyboard(category="front-end")
    

    await message.answer("ko'rsni tanlang" , reply_markup=keyboard)


@dp.message_handler(Text("Back-end") , state="*")
async def SubCategory(message : types.Message , state : FSMContext):
    await States.backEnd.set()
    keyboard = await SubCategoryKeyboard(category="back-end")

    await message.answer("ko'rsni tanlang" , reply_markup=keyboard)

# @dp.message_handler(Text(contains="Orqaga") , state=States.fronEnd  )
# async def fisrtLevelBackHandler(message: types.Message):
#     await message.answer(message.text , reply_markup=HomeKeyboards)


# @dp.message_handler(Text(contains="Orqaga") , state=States.backEnd  )
# async def fisrtLevelBackHandler(message: types.Message):
#     await message.answer(message.text , reply_markup=HomeKeyboards)


# keyboardLessons = None
Islesson = bool()

@dp.message_handler(state=States.fronEnd)
async def lessonKeyboards(message: types.Message, state: FSMContext):
    global keyboardLessons
    global Islesson
    if message.text == "🔙 Orqaga" and Islesson == True :
        Islesson = False
        print(Islesson)
        keyboardFront = await SubCategoryKeyboard(category="front-end")
        await message.answer("Orqaga", reply_markup=keyboardFront)

    elif message.text == "🔙 Orqaga" :
        Islesson = False
        await state.finish()
        await BackButtonStates.level1.set()
        await message.answer("Orqaga", reply_markup=dasturlashKeyboard)

    else:
        lessons = db.select_lesson(category="front-end", subcategory=message.text)
        
        if lessons:
            Islesson = True
            global subcategory
            subcategory = message.text
            keyboardLessons = await LessonKeyboards(category="front-end", subcategory=message.text)
            await message.answer("Dars sonini tanlang", reply_markup=keyboardLessons)
        else:
            Islesson = True
            text = ""
            lesson = db.select_lesson(VideoId=message.text[0], category="front-end", Subcategory=subcategory)
            text += f"{subcategory} Darslari | {message.text} | {lesson[0][3]} \n\n"
            text += f"Youtube — {lesson[0][4]} \n\n"
            text += f"Telegram — {lesson[0][5]} \n\n"
            await bot.send_video(message.from_user.id, video=lesson[0][2], caption=text)


IslessonBackend  = bool()
@dp.message_handler(state=States.backEnd)
async def lessonKeyboards(message : types.Message , state : FSMContext):
    global keyboardLessons
    global IslessonBackend
    if message.text == "🔙 Orqaga" and IslessonBackend == True :
        IslessonBackend = False
        print(Islesson)
        keyboardFront = await SubCategoryKeyboard(category="back-end")
        await message.answer("Orqaga", reply_markup=keyboardFront)

    elif message.text == "🔙 Orqaga" :
        IslessonBackend = False
        await state.finish()
        await BackButtonStates.level1.set()
        await message.answer("Orqaga", reply_markup=dasturlashKeyboard)

    else:
        lessons = db.select_lesson(category="back-end", subcategory=message.text)
        
        if lessons:
            IslessonBackend = True
            global subcategory
            subcategory = message.text
            keyboardLessons = await LessonKeyboards(category="back-end", subcategory=message.text)
            await message.answer("Dars sonini tanlang", reply_markup=keyboardLessons)
        else:
            IslessonBackend = True
            text = ""
            lesson = db.select_lesson(VideoId=message.text[0], category="back-end", Subcategory=subcategory)
            text += f"{subcategory} Darslari | {message.text} | {lesson[0][3]} \n\n"
            text += f"Youtube — {lesson[0][4]} \n\n"
            text += f"Telegram — {lesson[0][5]} \n\n"
            await bot.send_video(message.from_user.id, video=lesson[0][2], caption=text)








# orqaga va bosh menu button handler



