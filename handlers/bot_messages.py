from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from keyboards import reply, fabrics, inline, builders
from data.tems import tems
from handlers.questionaire_vshp import formatted_text
from handlers.questionaire_zargor import zaiv_text

import sqlite3
from datetime import datetime, timedelta
from filters.is_admin import IsAdmin
from main import Bot
router = Router()


@router.message(IsAdmin(1))
async def echo(message: Message, bot: Bot):
    msg = message.text.lower()
    if msg == "главное меню":
         await message.answer("Выберите раздел", reply_markup=reply.main)

    elif msg == "высшая школа патофизиологии":
        conn = sqlite3.connect('main.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM vshp WHERE account = ?", (message.from_user.username,))
        result = cursor.fetchone()
        conn.commit()
        conn.close()
        if result is not None:
            await message.answer("Выберите раздел", reply_markup=builders.vshp_mini())
        else:
            await message.answer("Выберите раздел", reply_markup=builders.vshp_full())

    elif msg == "царь-горы":
        await message.answer("Выберите раздел", reply_markup=builders.zar_gory())

    elif msg == "русские маяки":
        await message.answer("Выберите раздел", reply_markup=builders.rusmaik())


#ВШП
    elif msg == "ситуационные задачи":
        await message.answer("Вы перешли в раздел решения ситуациионных задач.\nВ настоящий момент работа на разделом еще не завершена.", reply_markup=builders.glmeni())

    elif msg == "обучающие материалы":
        await message.answer(f"{tems[0][0]} {tems[0][1]}", reply_markup=fabrics.paginator())

    elif msg == "учебный рейтинг":
        await message.answer("Вы перешли в раздел учебного рейтинга.\nВ настоящий момент работа на разделом еще не завершена.", reply_markup=builders.glmeni()) 
    
    elif msg == "темы для исследований":
        await message.answer_document("files/studi/lekzia/Темы для исследований.docx", reply_markup=builders.glmeni())


#Царь-горы
    elif msg == "об олимпиаде":
        await message.answer("Рассказ об олимпиде", reply_markup=builders.glmeni())

    elif msg == "подготовительные задания":
         await message.answer("Тут отправиться файл, но его еще не придумали", reply_markup=builders.glmeni())
    
    elif msg == "отборочный тур":
        await message.answer("Пока не планируется", reply_markup=builders.glmeni())

    elif msg == "результаты":
        await message.answer("Их пока нет", reply_markup=builders.glmeni())

#Русские маяки
    elif msg == "анонс":
        await message.answer("Их пока нет", reply_markup=builders.glmeni())

    elif msg == "подать тезисы":
        await message.answer("Процесс подачи тезиса", reply_markup=builders.glmeni()) 
    
    elif msg == "предложить идею":
        await message.answer("Процесс предложения идеи", reply_markup=builders.glmeni())


    elif msg == "сохранить":
        await message.answer("Ваша заявка сохранена.\nВ скором времени наш администратор даст вам обратную связь.", reply_markup=builders.glmeni())

        name = formatted_text[0].split(': ')[1]
        fak = formatted_text[1].split(': ')[1]
        gruop = formatted_text[2].split(': ')[1]
        about = formatted_text[3].split(': ')[1]
        account = message.from_user.username

        conn = sqlite3.connect('main.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO vshp (name, fak, gruop, about, account) VALUES (?, ?, ?, ?, ?)', (name, fak, gruop, about, account))
        conn.commit()
        conn.close()
        profile_summary = "\n" .join(formatted_text)
        formatted_text.clear()
        await bot.send_message(5618005272, f"Заявка на вступление:\n{profile_summary}\nПользователь: @{account}" )
    
    elif msg == "отправить заявку":
        await message.answer("Ваша заявка отправлена.\nВ скором времени наш администратор даст вам обратную связь.", reply_markup=builders.glmeni())

        school = zaiv_text[0].split(': ')[1]
        name = zaiv_text[1].split(': ')[1]
        pochta = zaiv_text[2].split(': ')[1]
        kapitan = zaiv_text[3].split(': ')[1]
        uchastnik1 = zaiv_text[4].split(': ')[1]
        uchastnik2 = zaiv_text[5].split(': ')[1]
        uchastnik3 = zaiv_text[6].split(': ')[1]
        uchastnik4 = zaiv_text[7].split(': ')[1]
        account = message.from_user.username

        conn = sqlite3.connect('main.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO zargor (school, name, pochta, kapitan, uchastnik1, uchastnik2, uchastnik3, uchastnik4, account) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                       (school, name, pochta, kapitan, uchastnik1, uchastnik2, uchastnik3, uchastnik4, account))
        conn.commit()
        conn.close()
        profile_zar_summary = "\n" .join(zaiv_text)
        zaiv_text.clear()
        await bot.send_message(965078721, f"Заявка на участие в олимпиаде:\n{profile_zar_summary}\n\nПользователь: @{account}" )

@router.message(IsAdmin(0))
async def fols(message: Message):
    await message.answer(f"Перезапустите бота нажав: /start")