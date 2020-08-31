from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import exchange
import newig

# IMPORTANTE: inserire il token fornito dal BotFather nella seguente stringa
TOKEN="1335344501:AAESQvRuusrB8IFbEbw3PY3UHoFuUq8abiQ"

def extract_text(text):
     return text.split()[1].strip()

def view_profile(update, context):
    print(f'Profilo')
    update.message.reply_text(f'Il profilo che mi hai mandato è')
    update.message.reply_text(f'https://instagram/{extract_text(update.message.text)}')
    update.message.reply_text(f'<a href="https://instagram/{extract_text(update.message.text)}">{extract_text(update.message.text)}</a')

def convert_usd(update, context):
     usd=float(extract_text(update.message.text))
     eur=exchange.from_usd_to_eur(usd)
     print(f'Eseguita conversione da {usd} USD a {eur} EUR')
     update.message.reply_text(f'{eur} EUR')
     update.message.reply_text(f'porcoddiiiiiiii')

def convert_eur(update, context):
     eur=float(extract_text(update.message.text))
     usd=exchange.from_eur_to_usd(eur)
     print(f'Eseguita conversione da {eur} EUR a {usd} USD')
     update.message.reply_text(f'{usd} USD')

def main():
   upd= Updater(TOKEN, use_context=True)
   disp=upd.dispatcher

   disp.add_handler(CommandHandler("usd", convert_usd))
   disp.add_handler(CommandHandler("eur", convert_eur))
   disp.add_handler(CommandHandler("p", view_profile))

   upd.start_polling()

   upd.idle()

if __name__=='__main__':
   main()