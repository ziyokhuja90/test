from aiogram.types.reply_keyboard import ReplyKeyboardMarkup , KeyboardButton

# Bepul darlar tugmasi
StartLesson = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Bepul Darslar")]
    ],
    resize_keyboard=True
)
# darslar bo'limi uchun tugmalar
categoryKeyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Grafik dizayn"),
            KeyboardButton("Dasturlash")
        ]        
    ],
    resize_keyboard=True
)
