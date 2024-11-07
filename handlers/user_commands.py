from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
import sqlite3
from keyboards import reply


router = Router()
@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}",reply_markup=reply.main)
    global id_user
    id_user = message.from_user.id
    first = message.from_user.first_name
    if message.from_user.last_name is not None:
        last = message.from_user.last_name
    else:
        last = "Не указан"
    nick = message.from_user.username
    conn = sqlite3.connect('main.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (id, first, last, nick) VALUES (?, ?, ?, ?)', (id_user, first, last, nick))
    conn.commit()
    conn.close()
