import logging
import os
from datetime import datetime

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

token = os.getenv("token")


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text("Hi!")


def help_command(update, context):
    update.message.reply_text("Help!")


def image_handler(update, context):
    fid = update.message.photo[-1].file_id
    fname = datetime.today().strftime(r"%Y%m%d") + f"_{fid}.jpg"
    logger.info(f"{fname}")
    file = context.bot.getFile(fid)
    file.download(fname)


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(
        MessageHandler(~Filters.document.image & ~Filters.command, image_handler)
    )
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
