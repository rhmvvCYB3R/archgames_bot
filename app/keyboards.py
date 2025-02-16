from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

class online:
    @staticmethod  # Делаем метод статическим
    def builder(*texts):  # Теперь принимает несколько аргументов
        builder = ReplyKeyboardBuilder()
        
        for text in texts:
            builder.button(text=text)  # Добавляем каждую кнопку
        
        return builder.as_markup(resize_keyboard=True)

