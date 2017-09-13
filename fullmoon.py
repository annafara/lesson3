import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def full_moon (bot, update):
    update.message.reply_text ('Вы хотите узнать когда ближайшее полнолуние начиная с какой даты?')

def planet (bot, update):
    update.message.reply_text ('введите название планеты?')

def main():
    updater = Updater("431046144:AAHSr1OfniFXLbyUtW87nVNIhUA_AxsOMOI")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(CommandHandler('full_moon', date))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    updater.start_polling()
    updater.idle()
def greet_user(bot, update):
    text = 'Привет!'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    from_the_date = dates.get (user_text)
    answer = from_the_date(datetime.date.today())
    planet_full = ephem.next_full_moon(answer)
    update.message.reply_text(planet_full)

date = datetime.date ()
date.strftime('%d.%m.%y')
    # print(user_text)
    # update.message.reply_text(user_text)
main()

