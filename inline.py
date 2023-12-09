
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def social_links_keyboard():
    markup = InlineKeyboardMarkup()

    site_btn = InlineKeyboardButton(text='Site', url='https://github.com/')

    markup.add(site_btn)

    return markup

def for_links_keyboard():
    markup_2 = InlineKeyboardMarkup()

    knopka = InlineKeyboardButton(text='Вывод', url='https://github.com/')
    knopka_2 = InlineKeyboardButton(text='Пополнить', url='https://github.com/')
    markup_2.add(knopka, knopka_2)

    return markup_2