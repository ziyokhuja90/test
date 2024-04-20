from aiogram.types.reply_keyboard import ReplyKeyboardMarkup , KeyboardButton
from loader import db 

async def LessonKeyboards(category  , subcategory):
    lessons = db.select_lesson(category=category  , subcategory=subcategory)
    
    LessonKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)

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
    