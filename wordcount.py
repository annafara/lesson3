import logging
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    updater = Updater("431046144:AAHSr1OfniFXLbyUtW87nVNIhUA_AxsOMOI")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

user_text = int(input())
wordсount = [word for word in user_text.split()]

def greet_user(bot, update):
    text = 'Привет!'
    print(text)
    update.message.reply_text(text)

def wordconunt (bot, update):
    update.message.reply_text ('Введите текст')

def talk_to_me(bot, update):
    user_text = update.message.text
    b = wordconunt.get (user_text)
    c = c ([word for word in user_text.split()])
    update.message.reply_text(b)

main()

