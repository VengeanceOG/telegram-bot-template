'''Start command with a welcome message. This is used to verify that bot is online.'''
from pyrogram import filters
from telebot import Telebot
from config import Config


@Telebot.on_message(filters.command('start') & filters.private)
def start(bot: Telebot, message):
    if message.chat.username:
        name = message.chat.username.capitalize()
    else:
        name = ''
    bot.send_message(
        message.chat.id, Config.START_MESSAGE)
