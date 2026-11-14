from aiogram import Router, types, Bot
from filters.group import GroupFilter
rt = Router()
@rt.message(GroupFilter())
async def test(msg: types.Message, bot: Bot):
    global type
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if msg.entities or msg.caption_entities:
        if msg.entities:
            for i in msg.entities:
                if i.type in ["url", "mention"]:
                    type = i.type
                    break
        else:
            type = msg.caption_entities[0].type
        if type in ["url", "mention"] and user.status in ["member"]:
            await msg.delete()
            await msg.answer(f"reklama tarqatmang, {msg.from_user.first_name}")

