from aiogram import Bot, Dispatcher
import asyncio
import config
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import CommandStart

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("SALAM!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())