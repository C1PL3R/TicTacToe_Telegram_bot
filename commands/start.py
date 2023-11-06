from aiogram.types import Message
from aiogram import F, Router
import asyncio

router_start = Router()

@router_start.message(F.text == '/start')
async def start(message: Message):
    await message.answer(text=f"Привіт <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>, тут є міні ігри які ти зможеш зіграти! Щоб зіграти подивися у вкладці 'Меню'.")