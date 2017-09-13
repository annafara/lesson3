import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def planet (bot, update):
    update.message.reply_text ('Введите название планеты')

def main():
    updater = Updater("431046144:AAHSr1OfniFXLbyUtW87nVNIhUA_AxsOMOI")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    updater.start_polling()
    updater.idle()
def greet_user(bot, update):
    text = 'Привет!'
    print(text)
    update.message.reply_text(text)

planet_names = {'venus':ephem.Venus, 'mars': ephem.Mars}

def talk_to_me(bot, update):
    user_text = update.message.text 
    planet_selection = planet_names.get (user_text)
    planet_pos = planet_selection(datetime.date.today())
    planet_const = ephem.constellation(planet_pos)
    update.message.reply_text(planet_const)

    # print(user_text)
    # update.message.reply_text(user_text)
main()

