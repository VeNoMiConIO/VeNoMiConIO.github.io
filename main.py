from aiogram import Bot, Dispatcher

import asyncio

bot = Bot(token='6723639762:AAHtebpcMg7vrYWAPWGIllBX2-IrCVmMeQI')
dp = Dispatcher(bot=bot)

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
