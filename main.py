import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import random

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class Picture:
    def __init__(self, link, caption):
        self.picture = link
        self.text = "**Source:** " + caption
    def get_picture(self):
        return self.picture
    def get_caption(self):
        return self.text

cats = []
c=Picture("https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg",
              "Pixabay on Pexels")
cats.append(c)
c=Picture("https://images.pexels.com/photos/96938/pexels-photo-96938.jpeg",
              "Francesco Ungaro on Pexels")
cats.append(c)
c=Picture("https://images.pexels.com/photos/735423/pexels-photo-735423.jpeg",
              "Eftodii Aurelia on Pexels")
cats.append(c)
c=Picture("https://images.pexels.com/photos/1317844/pexels-photo-1317844.jpeg",
            "Guillaume Meurice on Pexels")
cats.append(c)

hedgehogs = []
h=Picture("https://images.pexels.com/photos/50577/hedgehog-animal-baby-cute-50577.jpeg",
          "Pixabay on Pexels")
hedgehogs.append(h)
h=Picture("https://images.pexels.com/photos/20080177/pexels-photo-20080177/free-photo-of-manos-mujer-primavera-flores.jpeg",
          "Marina Riijik on Pexels")
hedgehogs.append(h)
h=Picture("https://images.pexels.com/photos/207028/pexels-photo-207028.jpeg",
          "Pixabay on Pexels")
hedgehogs.append(h)
h=Picture("https://images.pexels.com/photos/209246/pexels-photo-209246.jpeg",
          "Pixabay on Pexels")
hedgehogs.append(h)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=
                                   "Let's begin!")

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=
                                   "Hello there!")

async def cat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pic = cats[random.randint(0, len(cats) - 1)]
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=pic.get_picture(),
                                 caption=pic.get_caption(),
                                 parse_mode="Markdown")

async def hedgehog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pic = hedgehogs[random.randint(0, len(hedgehogs) - 1)]
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=pic.get_picture(),
                                 caption=pic.get_caption(),
                                 parse_mode="Markdown")

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
