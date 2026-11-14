from aiogram import Router, filters, types, Bot
rt = Router()
@rt.message()
async def start(msg: types.Message, bot: Bot):
   await msg.answer("ha qalesan")


