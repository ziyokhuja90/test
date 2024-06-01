from aiogram.types.reply_keyboard import ReplyKeyboardMarkup , KeyboardButton
from loader import db 
from keyboards.default import simpleKeyboards

async def LessonKeyboards(category, subcategory):
    lessons = await db.select_lesson(category=category, subcategory=subcategory)

    LessonKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    row = []
    for lesson in lessons:
        row.append(f"{lesson['lesson_number']}-dars")
        if len(row) == 2:  # Adjust 2 to the desired row width
            LessonKeyboard.row(*row)
            row = []
    if row:  # Add the last row if it's not empty
        LessonKeyboard.row(*row)

    LessonKeyboard.add(simpleKeyboards.back_button, simpleKeyboards.main_menu_button)
    
    return LessonKeyboard
    # lesson_buttons = []



    # Subcategory_buttons = []
    # SubcategorySet = set(Subcategory[1] for Subcategory in Subcategorys)

    # # Manually arrange buttons into rows of two
    # row = []
    # for subcategory in SubcategorySet:
    #     row.append(subcategory)
    #     if len(row) == 2:
    #         Subcategory_buttons.append(row)
    #         row = []

    # # If there are any remaining buttons, add them to the last row
    # if row:
    #     Subcategory_buttons.append(row)

    # # Add buttons to the keyboard
    # for row in Subcategory_buttons:
    #     SubcategoryKeyboard.row(*row)
    