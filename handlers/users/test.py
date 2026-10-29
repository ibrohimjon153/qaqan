from aiogram import Router, types

rt = Router()
@rt.message()
async def test(msg: types.Message):
   await msg.answer(str(msg.from_user.first_name))
