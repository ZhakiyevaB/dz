import telebot
import keyboard
from env import BOT_Token

from keyboard.inline import social_links_keyboard

bot = telebot.TeleBot(BOT_Token)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Welcome')

@bot.message_handler(commands=['links'])
def start(message: telebot.types.Message):
    markup = keyboard.inline.social_links_keyboard()
    bot.send_message(message.chat.id, 'link->', reply_markup=markup)

@bot.message_handler(commands=['fool'])
def start(message: telebot.types.Message):
    markup_2 = keyboard.inline.for_links_keyboard()
    bot.send_message(message.chat.id,'Knopki:', reply_markup = markup_2)
    
@bot.message_handler(commands=['dog'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id,
     'https://w.forfun.com/fetch/9a/9a1c52f4f3b3ad8075181750550da4bb.jpeg'
    )

@bot.message_handler(commands=['reply'])
def reply(message: telebot.types.Message):
    bot.reply_to(
        message,
        text='Answered'
    )
bot.polling()
