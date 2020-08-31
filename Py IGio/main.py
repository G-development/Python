from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram, logging

#BotFather token of IGioBot
token = "1335344501:AAESQvRuusrB8IFbEbw3PY3UHoFuUq8abiQ"

#Create the object 'bot'
bot = telegram.Bot(token)

#Messaggio di Bevenuto (/start)
welcomeMsg = "Heyo, welcome in IGIOBot!\nGuide coming soon...\nConsult the command list!\n\nSupport me on paypal.me/giocuo "

def start (update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcomeMsg)

def extract_text(msg):
     return msg.split()[1].strip()

def favorites (update, context):
   # context.bot.send_message(update.effective_chat.id, text='Dimmi il nome del profilo da aggiungere alla lista:')
    update.message.reply_text('Send me the name of the IG profile to put in the favourite list, please')
    lol = extract_text(update.message.text)
    update.message.reply_text(f'{lol} e a bucchin e nonnt')
    

def msg(update, context):
    update.message.reply_text(update.message.text)

def main():
    #Updater and Dispatcher
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    #Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("favourites", favorites))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()






##Start handler
#start_handler = CommandHandler('start', start)
#dispatcher.add_handler(start_handler)
#updater.start_polling()