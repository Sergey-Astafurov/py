from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import base
import logging
TOKEN = '5151717141:AAE1D-Eq91A-yG1or-PZ4ZSreTatqRCd54o'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


def start(update, context):
    base.connect()
    update.message.reply_text(
        "Привет. Выберите команду\n/all- посмотреть список контактов\n/find - поиск по фамилии\n/add - добавить"
        "\n/update - изменить номер абонента с заданной фамилией\n/delete - удалить абонента с заданной фамилией"
        "\n/stop - остановить бота")


def all(update, context):
    update.message.reply_text("Вот список всех контактов")
    base.all(update, context)


def find(update, context):
    update.message.reply_text("Введите фамилию c заглавной буквы  ")
    return 1


def add(update, context):
    update.message.reply_text("Введите Фамилию Имя телефон через пробел ")
    return 1

def update(update, context):
    update.message.reply_text("Введите Фамилию и новый номер телефона через пробел ")
    return 1

def delete(update, context):
    update.message.reply_text("Кого удалить из контактов? Введите id")
    base.all(update, context)
    return 3


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    base.disconnect()
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)

    all_handler = CommandHandler('all', all)
    dp.add_handler(all_handler)

    find_handler = ConversationHandler(
        entry_points=[CommandHandler('find', find)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, base.find)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(find_handler)

    update_handler = ConversationHandler(
        entry_points=[CommandHandler('update', update)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, base.update_info)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(update_handler)

    delete_handler = ConversationHandler(
        entry_points=[CommandHandler('delete', delete)],
        states={
            3: [MessageHandler(Filters.text & ~Filters.command, base.delete)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(delete_handler)

    add_peple_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, base.add)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(add_peple_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
