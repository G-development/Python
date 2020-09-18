import logging
import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

from ig_get import getUserLink


#x = getUserLink("anabnormalguy")
#print (x)

TOKEN = "1335344501:AAE9Ig5azZFQha_nvFwdu_mfT8RUxVCBwIo"
bot = telegram.Bot(token = TOKEN)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

welcomeMsg = """
Heyo, welcome in iGioBot! 
Guide coming soon... 
Consult the command list. 
Support me on PayPal
"""

CHOICE, USER, CHECK = range(3)
user_input_text = ""

def start(update, context):
    reply_keyboard = [['See stories', 'Most liked post', 'etc']]

    context.bot.send_message(chat_id=update.effective_chat.id, text = welcomeMsg)
    update.message.reply_text('Make your choice',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return CHOICE



def choice(update, context):
    user = update.message.from_user
    logger.info("Choice of %s: %s", user.first_name, update.message.text)

    update.message.reply_text('Input a IG Username',
                              reply_markup=ReplyKeyboardRemove())

    return USER

def stories(update, context):
    user = update.message.from_user
    logger.info("Ig username of %s: %s", user.first_name, update.message.text)
    user_input_text = update.message.text

    update.message.reply_text(f'Did you say {logger.info(f"Check username of %s: {user_input_text}", user.first_name)}?')
    print(user_input_text)

    reply_keyboard = [['Yes', 'No']]
    update.message.reply_text('Is it correct?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return CHECK

def check_user(update, context):
    user = update.message.from_user
    logger.info("Sì / No of %s: %s", user.first_name, update.message.text)
    user_input_text = update.message.text

    if user_input_text == "Yes":
        update.message.reply_text('Alright!',
                                reply_markup=ReplyKeyboardRemove())
        return CHOICE
    elif user_input_text == "No":
        update.message.reply_text('Input IG Username:',
                                    reply_markup=ReplyKeyboardRemove())
        return USER


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def main():
    updater = Updater(token = TOKEN, use_context=True)
    dp = updater.dispatcher
    
    conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],

            states={
                CHOICE: [MessageHandler(Filters.regex('^(See stories|Most liked post|etc)$'), choice)],

                USER: [MessageHandler(Filters.text, stories)],

                CHECK: [MessageHandler(Filters.regex('^(Yes|No)$'), check_user)]
            },

            fallbacks=[CommandHandler('cancel', cancel)]
        )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("start", start))

    #dp.add_handler(CommandHandler("favourites", favorites))
    #dp.add_handler(CommandHandler("choice", choice))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

#print(bot)
#print(updater)
#print(bot.get_me())