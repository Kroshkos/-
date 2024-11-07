from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import sqlite3
from utils.states import Form_zargor
from keyboards.builders import   zargor_save
from keyboards.reply import rmk

router =Router()
zaiv_text = []
@router.message(F.text.upper().in_(['ПОДАТЬ ЗАЯВКУ', 'ПЕРЕЗЕПОЛНИТЬ']))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form_zargor.school)
    await message.answer(
        "Давай начнем, введите название образовательной организации", reply_markup=rmk)

@router.message(Form_zargor.school)
async def form_school(message: Message, state: FSMContext):
    await state.update_data(school = message.text)
    await state.set_state(Form_zargor.name)
    await message.answer("Отлично, теперь название команды", reply_markup=rmk)
    
@router.message(Form_zargor.name)
async def form_name(message: Message, state: FSMContext):
    name = message.text.lower()
    conn = sqlite3.connect('main.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM zargor WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result is not None:
        await message.answer("Извините, но данное название уже занято", reply_markup=rmk)
    else:
        await state.update_data(name = message.text.lower())
        await state.set_state(Form_zargor.pochta)
        await message.answer("Укажите свою почту для обратной связи", reply_markup=rmk)

@router.message(Form_zargor.pochta)
async def form_pochta(message: Message, state: FSMContext):
    await state.update_data(pochta = message.text)
    await state.set_state(Form_zargor.kapitan)
    await message.answer("Введите  Фамилию Имя Отчество капитана команды", reply_markup=rmk)

@router.message(Form_zargor.kapitan)
async def form_pochta(message: Message, state: FSMContext):
    await state.update_data(kapitan = message.text)
    await state.set_state(Form_zargor.uchastnik1)
    await message.answer("Введите Фамилию Имя Отчество первого участника ", reply_markup=rmk)

@router.message(Form_zargor.uchastnik1)
async def form_pochta(message: Message, state: FSMContext):
    await state.update_data(uchastnik1 = message.text)
    await state.set_state(Form_zargor.uchastnik2)
    await message.answer("Введите Фамилию Имя Отчество второго участника ", reply_markup=rmk)

@router.message(Form_zargor.uchastnik2)
async def form_pochta(message: Message, state: FSMContext):
    await state.update_data(uchastnik2 = message.text)
    await state.set_state(Form_zargor.uchastnik3)
    await message.answer("Введите Фамилию Имя Отчество третьего участника ", reply_markup=rmk)

@router.message(Form_zargor.uchastnik3)
async def form_pochta(message: Message, state: FSMContext):
    await state.update_data(uchastnik3 = message.text)
    await state.set_state(Form_zargor.uchastnik4)
    await message.answer("Введите Фамилию Имя Отчество четвёртого участника ", reply_markup=rmk)

@router.message(Form_zargor.uchastnik4)
async def form_pochta(message: Message, state: FSMContext):
    await state.update_data(uchastnik4 = message.text)
    data = await state.get_data()
    await state.clear()

    labels = {
        "school": "ВУЗ",
        "name": "Назавние команды",
        "pochta": "Почта",
        "kapitan": "Капитан",
        "uchastnik1": "Участник 1",
        "uchastnik2": "Участник 2",
        "uchastnik3": "Участник 3",
        "uchastnik4": "Участник 4"

    }

    for key, value in data.items():
        label = labels.get(key, key)
        zaiv_text.append(f"{label}: {value}")

    profile_summary = "\n" .join(zaiv_text)

    await message.answer(f"Пожалуйста проверте ваши данные:\n{profile_summary}", reply_markup=zargor_save())


