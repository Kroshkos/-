from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import Form
from keyboards.builders import profile_fak, profile_save
from keyboards.reply import rmk

router =Router()
formatted_text = []
@router.message(F.text.upper().in_(['ВСТУПИТЬ', 'ЗАПОЛНИТЬ ЗАНОВО']))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        "Давай начнем, введи свою Фамилию Имя Отчество", reply_markup=rmk)

@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Form.fak)
    await message.answer("Отлично, теперь введите свой факультет", reply_markup=profile_fak())
    
@router.message(Form.fak, F.text.casefold().in_(["2", "3", "4", "5","7", "8", "преподаватель"]))
async def form_age(message: Message, state: FSMContext):
    await state.update_data(fak = message.text)
    await state.set_state(Form.group)
    await message.answer("Напиши свою учебную группу")

@router.message(Form.fak)
async def incorrect_form_age(message: Message, state: FSMContext):
    await message.answer("Нажми на кнопку")


@router.message(Form.group)
async def form_sex(message: Message, state: FSMContext):
    await state.update_data(group = message.text)
    await state.set_state(Form.about)        
    await message.answer("Расскажи о себе", reply_markup=rmk)

@router.message(Form.about)
async def form_about(message: Message, state: FSMContext):
    if len(message.text) < 5:
        await message.answer("Введите что-нибудь поинтереснее")
    else:
        await state.update_data(about = message.text)
        data = await state.get_data()
        await state.clear()

        labels = {
            "name": "Имя",
            "fak": "Факультет",
            "group": "Группа",
            "about": "Информация"

        }
        
        for key, value in data.items():
            label = labels.get(key, key)
            formatted_text.append(f"{label}: {value}")
        profile_summary = "\n" .join(formatted_text)

        await message.answer(f"Ваша анкета заполнена:\n{profile_summary}", reply_markup=profile_save())
        


