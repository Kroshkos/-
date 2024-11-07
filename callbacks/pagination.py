from aiogram.types import CallbackQuery, FSInputFile
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
from aiogram import Router, F
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message
from keyboards import reply, fabrics, inline, builders
from data.tems import tems

router = Router()

@router.callback_query(fabrics.Pagination.filter(F.action.in_(["prev", "next", "lek", "zad", "video"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    page_num = int(callback_data.page)
    
    # Обработка действий "prev" и "next"
    if callback_data.action == "prev":
        page = page_num - 1 if page_num > 0 else 0
    elif callback_data.action == "next":
        page = page_num + 1 if page_num < (len(tems) - 1) else page_num
    else:
        page = page_num
    
    # Отправка файла при действиях "lek", "zad" и "video"
    if callback_data.action in ["lek", "zad", "video"]:
        # Формируем путь к файлу на основе текущей страницы
        action_to_filename = {
            "lek": f"files/studi/lekzia/Лекция {page + 1}.docx",
            "zad": f"files/studi/zadanie/Задание к семинару {page + 1}.docx",
            "video": f"files/studi/video/Видео {page + 1}.mp4"
        }
        file_path = action_to_filename.get(callback_data.action)

        try:
            input_file = FSInputFile(file_path)
            await call.message.answer_document(input_file)
        except Exception as e:
            print(f"Ошибка при отправке файла: {e}")
    
    # Редактирование сообщения и отображение новой страницы
    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f"{tems[page][0]} {tems[page][1]}",
            reply_markup=fabrics.paginator(page)
        )
    
    await call.answer()