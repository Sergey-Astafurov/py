import logging
import random
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

reply_keyboard = [['/play', '/settings'],
                  ['/rules', '/close']]


markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5151717141:AAE1D-Eq91A-yG1or-PZ4ZSreTatqRCd54o'

candy = 50
step = 10

def start(update, context):
    name = f"{update.message.from_user.first_name} {update.message.from_user.last_name}"
    update.message.reply_text(
        f"{name},привет давай поиграем в игру с конфетами? \n"
        "Узнать правила - rules \n,",

        reply_markup=markup
    )
def rules(update, context):
    update.message.reply_text(
        "Правила игры.")



def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )

def settings(update, context):
    update.message.reply_text(
        "Введи кол-во конфет")
    return 1

def set_settings(update, context):
    global candy, step
    candy, step = map(int, update.message.text.split())
    update.message.reply_text("Настройки установлены")
    return ConversationHandler.END

def play(update, context):
    update.message.reply_text(  f"{candy} конфет, {step} максимальный шаг,  Ваш ход", reply_markup=ReplyKeyboardRemove() )
    return 1


# def play_game(update, context):
#     global candy
#     candys = int(update.message.text)
#     candy = candy - candys
#     if candy <= step :
#         update.message.reply_text("выйграл бот", reply_markup=markup)
#         return ConversationHandler.END
#     else :
#         update.message.reply_text(f"осталось {candy}  конфет до хода бота")

#         candy -= candy % (step + 1)
#         update.message.reply_text(f" бот забрал {candy % (step + 1)} конфет  ")
#         if candy <= step :
#             update.message.reply_text("вы выйграли!", reply_markup=markup)

#             return ConversationHandler.END


def play_game(update, context):
    global candy
    candys = int(update.message.text)
    if candys > step:
        update.message.reply_text(f"Число должно быть меньше {step}!")
        return 1
    candy -= candys
    if candy == 0:
        update.message.reply_text("Поздравляю, Вы победили!", reply_markup=markup)
        candy = 50
        return ConversationHandler.END
    if candy <= step:
        update.message.reply_text("Игра окончена, я забираю оставшиеся конфеты, я победил! ", reply_markup=markup)
        candy = 50
        return ConversationHandler.END
    else:
        if candy % (step + 1) == 0:
            update.message.reply_text(f"На кону {candy} конфет, я беру {random.randint(1, step)}, следующий ход ваш")
            candy -= random.randint(1, step)
        else:
            update.message.reply_text(f"На кону {candy} конфет, я беру {candy % (step + 1)}, следующий ход ваш")
            candy -= candy % (step + 1)
    if candy <= step:
        update.message.reply_text("Поздравляю, Вы победили!", reply_markup=markup)
        candy = 50
        return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    settings_handler = ConversationHandler(
        entry_points=[CommandHandler('settings', settings)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_settings)]
        },
        fallbacks=[CommandHandler('close', close_keyboard)]
    )
    dp.add_handler(settings_handler)

    play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_game)]
        },
        fallbacks=[CommandHandler('close', close_keyboard)]
    )
    dp.add_handler(play_handler)

    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close_keyboard))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
