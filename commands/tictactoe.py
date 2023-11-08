from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram import F, Router
import asyncio
import random

attemps = "computer"
locked = False

router_ttt = Router()

button1 = InlineKeyboardButton(text="🚫", callback_data="button1")
button2 = InlineKeyboardButton(text="🚫", callback_data="button2")
button3 = InlineKeyboardButton(text="🚫", callback_data="button3")

button4 = InlineKeyboardButton(text="🚫", callback_data="button4")
button5 = InlineKeyboardButton(text="🚫", callback_data="button5")
button6 = InlineKeyboardButton(text="🚫", callback_data="button6")

button7 = InlineKeyboardButton(text="🚫", callback_data="button7")
button8 = InlineKeyboardButton(text="🚫", callback_data="button8")
button9 = InlineKeyboardButton(text="🚫", callback_data="button9")

def game_computer():
    all_strategy = ["cross_1", "cross_2", "vertical_1", "vertical_2", "vertical_3", "horizontal_1", "horizontal_2", "horizontal_3"]
    strategy = ""
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, attemps
    btn = random.choice([button1, button2, button3 ,button4, button5, button6, button7, button8, button9])
    if button1.text == "⭕":
        strategy = random.choice(["cross_1", "vertical_1", "horizontal_1"])
        if strategy == "cross_1":
            button5.text == "⭕"
            attemps = 1
            if attemps == 1:
                button9.text = "⭕"
            if attemps == 0:
                pass            
            

@router_ttt.message(F.text == '/tictactoe')
async def tictactoe(message: Message):    
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, attemps
    button1.text = "🚫"
    button2.text = "🚫"
    button3.text = "🚫"
    button4.text = "🚫"
    button5.text = "🚫"
    button6.text = "🚫"
    button7.text = "🚫"
    button8.text = "🚫"
    button9.text = "🚫"
    
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    
    btn = random.choice([button1, button2, button3 ,button4, button5, button6, button7, button8, button9])
    button1.text = "⭕"
    attemps = "user"
    game_computer()
    
    await message.answer(text="Ти хрестик, я нулик", reply_markup=keyboard_ttt)
    
        
@router_ttt.callback_query(F.data == "button1")
async def callback_btn1(callback: CallbackQuery):
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    
    if button1.text == "⭕" or button1.text == "❌":
        global locked
        locked = True
        await callback.message.edit_text(text=f"Ти хрестик, я нулик\n\nКнопка не працює тому, що зайнята", reply_markup=keyboard_ttt)
    else:
        button1.text = "❌"
        await callback.message.edit_text(text=f"Ти хрестик, я нулик", reply_markup=keyboard_ttt)
    
    
    
    
@router_ttt.callback_query(F.data == "button2")
async def callback_btn2(callback: CallbackQuery): 
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    if button2.text == "⭕" or button2.text == "❌":
        global locked
        locked = True
        await callback.message.edit_text(text=f"Ти хрестик, я нулик\n\nКнопка не працює тому, що зайнята", reply_markup=keyboard_ttt)
    else:
        button2.text = "❌"
        await callback.message.edit_text(text=f"Ти хрестик, я нулик", reply_markup=keyboard_ttt)
    
        
        

@router_ttt.callback_query(F.data == "button3")
async def callback_btn3(callback: CallbackQuery):    
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    if button3.text == "⭕" or button3.text == "❌":
        global locked
        locked = True
        await callback.message.edit_text(text=f"Ти хрестик, я нулик\n\nКнопка не працює тому, що зайнята", reply_markup=keyboard_ttt)
    else:
        button3.text = "❌"
        await callback.message.edit_text(text=f"Ти хрестик, я нулик", reply_markup=keyboard_ttt)


@router_ttt.callback_query(F.data == "button4")
async def callback_btn4(callback: CallbackQuery):
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    if button4.text == "⭕" or button4.text == "❌":
        global locked
        locked = True
        await callback.message.edit_text(text=f"Ти хрестик, я нулик\n\nКнопка не працює тому, що зайнята", reply_markup=keyboard_ttt)
    else:
        button4.text = "❌"
        await callback.message.edit_text(text=f"Ти хрестик, я нулик", reply_markup=keyboard_ttt)


@router_ttt.callback_query(F.data == "button5")
async def callback_btn5(callback: CallbackQuery):
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    if button5.text == "⭕" or button5.text == "❌":
        global locked
        locked = True
        await callback.message.edit_text(text=f"Ти хрестик, я нулик\n\nКнопка не працює тому, що зайнята", reply_markup=keyboard_ttt)
    else:
        button5.text = "❌"
        await callback.message.edit_text(text=f"Ти хрестик, я нулик", reply_markup=keyboard_ttt)
    

@router_ttt.callback_query(F.data == "button6")
async def callback_btn6(callback: CallbackQuery):
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    if button6.text == "⭕" or button6.text == "❌":
        global locked
        locked = True
        await callback.message.edit_text(text=f"Ти хрестик, я нулик\n\nКнопка не працює тому, що зайнята", reply_markup=keyboard_ttt)
    else:
        button6.text = "❌"
        await callback.message.edit_text(text=f"Ти хрестик, я нулик", reply_markup=keyboard_ttt)
    

@router_ttt.callback_query(F.data == "button7")
async def callback_btn7(callback: CallbackQuery):
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    if button7.text == "⭕" or button7.text == "❌":
        global locked
        locked = True
        await callback.message.edit_text(text=f"Ти хрестик, я нулик\n\nКнопка не працює тому, що зайнята", reply_markup=keyboard_ttt)
    else:
        button7.text = "❌"
        await callback.message.edit_text(text=f"Ти хрестик, я нулик", reply_markup=keyboard_ttt)
    

@router_ttt.callback_query(F.data == "button8")
async def callback_btn8(callback: CallbackQuery):
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    if button8.text == "⭕" or button8.text == "❌":
        global locked
        locked = True
        await callback.message.edit_text(text=f"Ти хрестик, я нулик\n\nКнопка не працює тому, що зайнята", reply_markup=keyboard_ttt)
    else:
        button8.text = "❌"
        await callback.message.edit_text(text=f"Ти хрестик, я нулик", reply_markup=keyboard_ttt)
    

@router_ttt.callback_query(F.data == "button9")
async def callback_btn9(callback: CallbackQuery):
    keyboard_ttt = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9]
    ])
    if button9.text == "⭕" or button9.text == "❌":
        global locked
        locked = True
        await callback.message.edit_text(text=f"Ти хрестик, я нулик\n\nКнопка не працює тому, що зайнята", reply_markup=keyboard_ttt)
    else:
        button9.text = "❌"
        await callback.message.edit_text(text=f"Ти хрестик, я нулик", reply_markup=keyboard_ttt)
