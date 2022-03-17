import asyncio
import logging
from userbot import userbot
from pystark import Stark, Message
from pyrogram.errors import UserAlreadyParticipant, FloodWait


@Stark.cmd('delall')
async def main_func(bot: Stark, msg: Message):
    # Chat type check
    if msg.chat.type == "private":
        return
    if msg.chat.type != "channel":
        # User admin check
        user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
        if user.status not in ['creator', 'administrator']:
            return
        if not user.can_delete_messages:
            await msg.react("You don't have `CanDeleteMessages` right. Sorry!")
            return
    # Bot admin rights check
    bot_id = (await bot.get_me()).id
    cm = await bot.get_chat_member(msg.chat.id, bot_id)
    if cm.status != "administrator":
        await msg.react("I'm not admin here!")
        return
    elif not cm.can_promote_members:
        await msg.react("I can't promote users here. I need that right to work.")
        return
    elif not cm.can_delete_messages:
        await msg.react("I can't delete messages here. I need that right to work.")
        return
    # Userbot work
    link = (await bot.get_chat(msg.chat.id)).invite_link
    try:
        await userbot.join_chat(link)
    except UserAlreadyParticipant:
        pass
    userbot_id = (await userbot.get_me()).id
    await bot.promote_chat_member(
        msg.chat.id,
        userbot_id,
        can_delete_messages=True
    )
    # numbers = list(range(msg.message_id-1, 0, -1))
    numbers = []
    async for m in userbot.iter_history(msg.chat.id):
        numbers.append(m.message_id)
    id_lists = [numbers[i*100:(i+1)*100] for i in range((len(numbers)+100-1) // 100)]
    status = await msg.reply("Trying to delete all messages...")
    for id_list in id_lists:
        try:
            await userbot.delete_messages(msg.chat.id, id_list)
        except FloodWait as e:
            await asyncio.sleep(e.x)
            Stark.log(str(e), logging.WARN)
            await userbot.delete_messages(msg.chat.id, id_list)
    await msg.react("Successful! Deleted Everything. For more bots visit @StarkBots")
    await status.delete()
    await userbot.leave_chat(msg.chat.id)
