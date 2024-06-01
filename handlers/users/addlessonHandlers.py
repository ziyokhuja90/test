from loader import dp , db , bot
from aiogram.types import Message

from aiogram import types

from aiogram.dispatcher import FSMContext   

from states.add_lesson_states import Add_Lesson_State

from uuid import uuid4

from keyboards.default.categorykeyboards import categoryKeyboard    
# from keyboards.default.subcategorysKeyboard import SubCategoryKeyboard
from keyboards.default.simpleKeyboards import StartLesson


Apps = {
    "dizayn":{
        "photoshop":{
            "P15":"BQACAgIAAxkBAAIHLGZVf6ELSrfk42seCN71RLMOZsYIAAIKDwACTZvYS9VhJ1iA6ngbNQQ",
            "P17":"BQACAgIAAxkBAAIHNGZVgbfX1D4mFi-wZtwddLOxce8UAAIQDwACTZvYS6F4zVdGVRPvNQQ",
            "P18":"BQACAgIAAxkBAAIHLmZVgOwAAWLnEZDVDXW-t21nkpu8RgACFA8AAk2b2EtaY4GhT6-ttjUE",
            "P19":"BQACAgIAAxkBAAIHOmZVrR35nYqdRKpF6u-wAmvY41jTAAIfDwACTZvYS8G-nCU95rDPNQQ",
            "P20":"BQACAgIAAxkBAAIHMGZVgQ1_jlFPVSfN3gocovK1kClPAALMDwACTZvgS7iT3BYl6-jONQQ",
            "P21":"BQACAgIAAxkBAAIHPGZVrXOFd0rOJSMn0r06kd_YJbbgAALSDwACQ0_gS_-o4FWfAXv6NQQ",
            "P22":"BQACAgIAAxkBAAIHPmZVrZASX0EQn_94OUtgfMaLk8zSAAIOEAACbMOZSj0v6KHU7fgENQQ",
            "P23":"BQACAgIAAxkBAAIHQGZVra4RAlv0s9RvAAG_rBssYVat3gACpSIAAiFHqUioHu6OLJV2UTUE",
        },
        "Illustrator":{
            "I14":"BQACAgIAAxkBAAIHQmZVrhmny_uaYoz5XUtyv1g6LaJGAAI8EAACQ0_gS8fyp2bph_qHNQQ",
            "I15":"BQACAgIAAxkBAAIHRGZVrjTu7Mtwm3NLoMpl5Yki8yxbAAJDEAACQ0_gSz_hDdyJ6XS3NQQ",
            "I17":"BQACAgIAAxkBAAIHRmZVrmAmrRnCvUsZXrwn-iIECBfLAAJcEAACQ0_gS4_dcXeFbvWDNQQ",
            "I18":"BQACAgIAAxkBAAIHSGZVrnoZfoa4QkYOqfH5-7vCSqeFAAKPEAACQ0_gS5waCZd2KR7SNQQ",
            "I19":"BQACAgIAAxkBAAIHSmZVrp_AVGNduMeFpmJgjMybC_71AAKaEAACQ0_gS5ax2D1zxhxeNQQ",
            "I20":"BQACAgIAAxkBAAIHTGZVrsUZ0HZMh6IVNaNKb1D7GbD5AAKfEAACQ0_gS_wckZ6TtFo1NQQ",
            "I21":"BQACAgIAAxkBAAIHTmZVruDs_yhHJjVh9muUyQIEk02ZAAKjEAACQ0_gS3rqUiogKsjhNQQ",
            "I22":"BQACAgIAAxkBAAIHUGZVrvZixZuLFbcSIntFwGB0drmVAALhDwACbMOZSqMpomFlyQbWNQQ",
        }
    }
}

@dp.message_handler(commands=["addLesson"] , is_admin=True)
async def AddLesson(message : Message , state : FSMContext):

    await Add_Lesson_State.videoId.set()
    await message.answer("Assaolmu alayekum yangi dars videosini tashlang")

@dp.message_handler(content_types=types.ContentTypes.VIDEO , state=Add_Lesson_State.videoId)
async def AddLessonNumberOfLesson(message:Message ,state : FSMContext):
    video_file_id = message.video.file_id

    await bot.send_message(chat_id=message.from_user.id , text=f"Video qabul qilindi \nVideo Id: {video_file_id}")
    await state.finish()

@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def Dasturlar(message: Message ):
    await message.answer(message.document.file_id)
