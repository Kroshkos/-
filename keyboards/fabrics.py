from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton

class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int

def paginator(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅", callback_data=Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text="➡", callback_data=Pagination(action="next", page=page).pack()),
        InlineKeyboardButton(text="Лекция", callback_data=Pagination(action="lek", page=page).pack()),
        InlineKeyboardButton(text="Видеоматериалы", callback_data=Pagination(action="video", page=page).pack()),
        InlineKeyboardButton(text="Задание к семинару", callback_data=Pagination(action="zad", page=page).pack()),
        width=2
    )
    
    return builder.as_markup()