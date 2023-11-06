from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram import F, Router
import asyncio

router_ttt = Router()

@router_ttt.message(F.text == '/start')
async def start(message: Message):
    await message.answer(text="Привіт, заграймо у хрестики-нулики /tictactoe")


@router_ttt.message(F.text == '/tictactoe')
async def start(message: Message):
    username = message.from_user.username
    button1 = InlineKeyboardButton(text="🚫", callback_data="button1")
    button2 = InlineKeyboardButton(text="🚫", callback_data="button2")
    button3 = InlineKeyboardButton(text="🚫", callback_data="button3")
    
    button4 = InlineKeyboardButton(text="🚫", callback_data="button4")
    button5 = InlineKeyboardButton(text="🚫", callback_data="button5")
    button6 = InlineKeyboardButton(text="🚫", callback_data="button6")

    button7 = InlineKeyboardButton(text="🚫", callback_data="button7")
    button8 = InlineKeyboardButton(text="🚫", callback_data="button8")
    button9 = InlineKeyboardButton(text="🚫", callback_data="button9")

    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    
    await message.answer(text="Ти хрестик, я нулик", reply_markup=keyboard_ttt)
    
    @router_ttt.callback_query(F.data == "button1")
    async def callback_btn1(callback: CallbackQuery):
        button1 = InlineKeyboardButton(text="❌", callback_data="button1")
        keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
        await callback.message.edit_text(text="Ти хрестик, я нулик", reply_markup=keyboard_ttt)

