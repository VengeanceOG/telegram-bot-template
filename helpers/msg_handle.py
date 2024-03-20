'''Functions to handle messages sent by the user to the bot.'''
from typing import Literal
from pyrogram import types
from config import Config


# Make sure command is used only by authorised person.
def check_role(bot, message: types.Message, role: Literal['owner', 'admin', 'user']):
    '''
    Check whether the user is authenticated to use a particular command.
    Sends a reply message to the user if is he is not authenticated to a proper role to use this command.
    '''
    role_id = {'owner': 1, 'admin': 2, 'user': 3}
    id = message.chat.id
    user_role = bot.user_data.get_role(id)
    if user_role <= role_id[role]:
        return True
    else:
        # A dict to see whether to add a/an/the in the reply message.
        a_an_the = {'owner': 'the', 'admin': 'an', 'user': 'a'}
        bot.send_message(
            message.chat.id, f"🚫 You are not {a_an_the[role]} {role}. You can't use this function.")
        return False


def extract_msg(message: types.Message):
    '''
    Check if the user has used a particular command by replying to another message.
    If he has replied, all the data is to be extracted from the latter message.
    '''
    if message.reply_to_message:
        return message.reply_to_message
    else:
        return message


def check_id(bot, message: types.Message):
    '''
    Check if the given message contains only digits (valid id).
    If it isn't a valid id, a reply is sent to the user.
    '''
    if message.text.isdigit():
        return message.text
    else:
        bot.send_message(message.chat.id, '❌ This is not a valid id!')
        return None


def handle_exception(bot, user_id: int):
    '''Sends a message to the user if an unexpected error is occured while executing a particular process.'''
    bot.send_message(user_id, Config.CRASH_MESSAGE)
