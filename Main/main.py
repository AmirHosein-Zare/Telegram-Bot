from decouple import config

# config api token bot
api_token = config("API_TOKEN")

from telegram import Update
from telegram.ext import CallbackContext, Updater, dispatcher, CommandHandler

# requests library
import requests

# set telegram bot
updater = Updater(api_token)
dispatcher = updater.dispatcher

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
    context.bot.send_message(chat_id, text)

from package import getMovie
def movie(update:Update, context:CallbackContext):
    chat_id = update.message.chat_id
    result = getMovie('Troll')
    context.bot.send_message(chat_id, result[0])

# set command for start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('movie',movie))

# start bot to work
updater.start_polling()