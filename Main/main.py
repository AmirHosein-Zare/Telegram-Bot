from decouple import config

# config api token bot
api_token = config("API_TOKEN")

from telegram import Update, InputMediaPhoto
from telegram.ext import CallbackContext, Updater, dispatcher, CommandHandler

# requests library
import requests

# set telegram bot
updater = Updater(api_token)
dispatcher = updater.dispatcher

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
inline_keys = [
    [InlineKeyboardButton('Search Movie', callback_data='1'), InlineKeyboardButton('About IMDB Bot', callback_data='2')],
    [InlineKeyboardButton('Cancel', callback_data='3')]
]

# start function
def start(update:Update, context:CallbackContext):
    chat_id = update.message.chat_id
    # set text for start of bot
    text = '''
Hello :)
wellcome to IMDB_bot
to get information about your favorite movie
please enter the name of the movie:
:)
    '''
    # Add buttons
    inline_markup = InlineKeyboardMarkup(inline_keys)
    update.message.reply_text(text=text, reply_markup=inline_markup)

from package import getMovie, getStatus,getpic,getPicture
def movie(update:Update, context:CallbackContext):
    chat_id = update.message.chat_id
    result = getMovie('Troll')
    media_group = []
    if result[1] != "-1":
        text = result[0]
        url = f'https://www.themoviedb.org/t/p/w600_and_h900_bestv2{result[1]}'
        getPicture(url=url)
        media_group.append(InputMediaPhoto(open('new.jpg', 'rb'),caption = text))
        context.bot.send_media_group(chat_id = chat_id, media = media_group)
    else:
        context.bot.send_message(chat_id, result[0]);

# set command for start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('movie',movie))

# start bot to work
updater.start_polling()