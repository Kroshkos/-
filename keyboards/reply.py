from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

main = ReplyKeyboardMarkup(
    keyboard =
    [
        [
            KeyboardButton(text="Высшая школа патофизиологии")
            ],
        [
            KeyboardButton(text = "Царь-горы"),
            KeyboardButton(text = "Русские маяки")
            ],
        [
            KeyboardButton(text = "Патфиз.рф")
            ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True,
    input_field_placeholder = "Выберите раздел",
    selective = True
)

rmk = ReplyKeyboardRemove()