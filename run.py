import asyncio

from aiogram import Bot, F, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from database import database
from app.keyboards import online
from aiogram.methods import SendPhoto
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
db = database("users.db")





@dp.message(Command("start"))
async def start_message(message: Message):
    user = db.get_user_cursor(message.from_user.id)
    
    if user is None:
        db.new_user(message.from_user.id)
        await message.answer(
            f"👋 Привет {message.from_user.first_name}, добро пожаловать в мир АЗАРТЫХ ИГР!! \n"
            "🗣 Наш бот предоставляет возможность играть и зарабатывать! 👾🤑\n\n"
            f"👁‍🗨 Игроков в сети: {db.get_users_in_search()}",
            reply_markup = online.builder("🔎 Найти комнату", "Создать комнату", "Баланс")


    
            
            
        )
    else:
        await message.answer(
            f"👋 Привет {message.from_user.first_name}, добро пожаловать в мир АЗАРТЫХ ИГР!! \n\n"
            "✅ Вы уже зарегистрированы!\n\n"
            f"👁‍🗨 Игроков в сети: {db.get_users_in_search()}",
            reply_markup = online.builder("🔎 Найти комнату", "Создать комнату", "Баланс")



            
        )




async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())




