from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    name = State()
    fak = State()
    group = State()
    about = State()

class Form_zargor(StatesGroup):
    school = State()
    name = State()
    pochta = State()
    kapitan = State()
    uchastnik1 = State()
    uchastnik2 = State()
    uchastnik3 = State()
    uchastnik4 = State()