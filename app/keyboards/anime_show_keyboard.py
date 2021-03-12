from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto
"""Создаёт и возвращает inline панель с кнопками с названием аниме и ссылкой на ресурс"""

async def anime_show_kb_builder(animes):
    kb = InlineKeyboardMarkup() # базовый элемент inline клавиатуры который будет наполняться дальше
    [kb.insert(InlineKeyboardButton(anime[1], url=anime[2])) for anime in animes] # добавляем жанры в базовый элемент клавиатуры (чтобы работоло ограничение row_width нужно заполнять базовый элемент методом insert)

    return kb # возвращаем готовую панель
