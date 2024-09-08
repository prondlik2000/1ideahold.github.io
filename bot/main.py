from aiogram import Bot, Dispatcher

import asyncio

bot = Bot(token='7513111191:AAGPlyEWgZG92QTjjNhjXzMvWBs7YcTSMQg')
dp = Dispatcher(bot=@test_ham2345_bot)

async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
