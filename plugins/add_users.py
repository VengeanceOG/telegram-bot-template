'''
add_user - authenticate new user.
add_admin - authenticate new admin. 
'''
from pyrogram import filters
from telebot import Telebot
from helpers import msg_handle


@Telebot.on_message(filters.command('add_user') & filters.private)
def add_user(bot: Telebot, message):
    try:
        if msg_handle.check_role(bot, message, 'admin'):
            msg = msg_handle.extract_msg(message)
            id = msg_handle.check_id(bot, msg)
            if id:
                bot.user_data.add_user(msg.text, 3)
                bot.send_message(
                    message.chat.id, f"✔️ Successfully added **{msg.text}**!")

    except:
        msg_handle.handle_exception(bot, message.chat.id)


@Telebot.on_message(filters.command('add_admin') & filters.private)
def add_admin(bot: Telebot, message):
    try:
        if msg_handle.check_role(bot, message, 'owner'):
            msg = msg_handle.extract_msg(message)
            id = msg_handle.check_id(bot, msg)
            if id:
                bot.user_data.add_user(msg.text, 2)
                bot.send_message(
                    message.chat.id, f"✔️ Successfully added **{msg.text}**!")
    except:
        msg_handle.handle_exception(bot, message.chat.id)
