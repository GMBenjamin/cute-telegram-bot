import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import random

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Let's begin!")

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hello there!")

async def cat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_id = str(random.randint(0, 3))
    path = "Cats/"+photo_id+".jpg"
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(path, "rb"))

async def hedgehog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_id = str(random.randint(0, 3))
    path = "Hedgehogs/"+photo_id+".jpg"
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(path, "rb"))

if __name__ == '__main__':
    TokenBot = "TOKEN"
    application = ApplicationBuilder().token(TokenBot).build()

    start_handler = CommandHandler('start', start)
    greetings_handler = CommandHandler('hi', hi)
    cat_handler = CommandHandler('cat', cat)
    hedgehog_handler = CommandHandler('hedgehog', hedgehog)
    application.add_handler(start_handler)
    application.add_handler(greetings_handler)
    application.add_handler(cat_handler)
    application.add_handler(hedgehog_handler)
    
    application.run_polling()
