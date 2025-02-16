from aiogram import F, Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
import app.keyboards



router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет {message.from_user.first_name}. \nДобро пожаловать в Мир азартных приключений!', reply_markup= app.keyboards.main)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('OK!')

