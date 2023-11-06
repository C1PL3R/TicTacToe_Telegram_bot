from aiogram import Bot, Dispatcher
import logging
import sys
import asyncio

from commands.tictactoe import router_ttt


async def main():
    proxy_url = "http://proxy.server:3128"
    TOKEN = "5957173294:AAEIgZLBSCXfZM9mfPTayI8KygPFiYQXL5Q"
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(router_ttt)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Close connection with Telegram Servers")