
import logging
import psutil
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

print("started.")

logger = logging.getLogger(__name__)

def main():
 
    updater = Updater("TOKEN HERE", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("example",example_command))
    dispatcher.add_handler(CommandHandler("usage", ram))
    updater.start_polling()

    updater.idle()
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('/help')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('/example\n/usage\n')

def example_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('This bot was made by Jitski')

def ram(update: Update, context: CallbackContext) -> None:
    cpuUsage = psutil.cpu_percent(interval=1)
    ramTotal = int(psutil.virtual_memory().total/(1024*1024)) #GB
    ramUsage = int(psutil.virtual_memory().used/(1024*1024)) #GB
    ramFree = int(psutil.virtual_memory().free/(1024*1024)) #GB
    ramUsagePercent = psutil.virtual_memory().percent
    update.message.reply_text('''
CPU & RAM Info

CPU Usage = {} %
RAM
Total = {} MB
Usage = {} MB
Free  = {} MB
Used = {} %\n'''.format(cpuUsage,ramTotal,ramUsage,ramFree,ramUsagePercent))
 
if __name__ == '__main__':
    main()
