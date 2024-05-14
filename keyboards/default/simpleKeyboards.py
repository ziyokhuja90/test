from aiogram.types.reply_keyboard import ReplyKeyboardMarkup , KeyboardButton

# Bepul darlar tugmasi
StartLesson = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Bepul Darslar")]
    ],
    resize_keyboard=True
)
# darslar bo'limi uchun tugmalar

HomeKeyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Grafik dizayn"),
            KeyboardButton("Dasturlash")
        ],
        [
            KeyboardButton("Kerakli dasturlar"),
            KeyboardButton("📩 Biz bilan bog'lanish")
        ],
        [
            KeyboardButton("Bot haqida")
        ]
    ],
    resize_keyboard=True
)

grafikdizayn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Photoshop"),KeyboardButton("Illustrator")],
        [KeyboardButton("CoralDraw")],
        [KeyboardButton("🔙 Orqaga")]
    ],
    resize_keyboard=True
)

dasturlashKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Front-end"),
            KeyboardButton("Back-end")
        ],
        [
            KeyboardButton("🔙 Orqaga")
        ]
    ],
    resize_keyboard=True
)

# OrqagaBoshmenu = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton("🔙 Orqaga"),
#             KeyboardButton("🔝 Asosiy Menyu")

#         ]
#     ]
# )

back_button = KeyboardButton("🔙 Orqaga")
main_menu_button = KeyboardButton("🔝 Asosiy Menyu")