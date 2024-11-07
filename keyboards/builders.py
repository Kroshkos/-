from aiogram.utils.keyboard import ReplyKeyboardBuilder

def vshp_full():
    items = [
        "Ситуационные задачи", "Обучающие материалы",
        "Учебный рейтинг", "Темы для исследований","Вступить"
    ]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Главное меню")
    builder.adjust(2, 2, 1)

    return builder.as_markup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Выберите раздел", selective = True)

def vshp_mini():
    items = [
        "Ситуационные задачи", "Обучающие материалы",
        "Учебный рейтинг", "Темы для исследований"
    ]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Главное меню")
    builder.adjust(2, 2)

    return builder.as_markup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Выберите раздел", selective = True)

def zar_gory():
    items = [
        "Об олимпиаде", "Подать заявку",
        "Подготовительные задания", "Отборочный тур","Результаты"
    ]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Главное меню")
    builder.adjust(2, 1, 2)

    return builder.as_markup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Выберите раздел", selective = True)

def rusmaik():
    items = [
        "Анонс", "Подать тезисы",
        "Предложить идею"
    ]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Главное меню")
    builder.adjust(1, 1, 1)

    return builder.as_markup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Выберите раздел", selective = True)

def glmeni():
    items = [
        "Главное меню"
    ]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.adjust(1)

    return builder.as_markup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Скоро закончим ", selective = True)

def profile_fak():
    items =[
        "2", "3", "4", "5","7", "8", "Преподаватель"
        ]
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.adjust(3, 3, 1)

    return builder.as_markup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Выберите факультет", selective = True)

def profile_save():
    items =[
        "Сохранить", "Заполнить заново"
        ]
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.adjust(1, 1)

    return builder.as_markup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Выберите действие", selective = True)


def zargor_save():
    items =[
        "Отправить заявку", "Перезаполнить"
        ]
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.adjust(1, 1)

    return builder.as_markup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Выберите действие", selective = True)