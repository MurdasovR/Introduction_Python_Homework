import logging, tools, datetime
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters


logging.basicConfig(filename='log.csv', encoding='utf_8', format='date=%(asctime)s; level=%(levelname)s; %(message)s', datefmt='%d.%m.%Y; time=%H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
Привет {update.effective_user.first_name}, я бот-калькулятор.
Выполняю операции +, -, *, / двух целых, вещественных или комплексных чисел.
Отправь сообщение с выражением, которое нужно вычислить, и я пришлю ответ.
Доступны команды:
    /start - выведет это сообщение;
    /help - покажет правила составления выражений.
Жду сообщений для вычисления...""")
    


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
Правила составления выражений:
☛ числа может быть только два;
☛ операции только \+, \-, \*, \/;
☛ дробная часть может отделяться как точкой, так и запятой;
☛ мнимая единица обозначается "j" или "J", перед ней обязателен числовой коэффициент \(не j, а 1j\);
☛ комплексные числа могут быть заключены в скобки \(необязательно\);
☛ количество пробелов значения не имеет\.
Примеры выражений:
`1,56  + 3.5J*(1-2j)
1,5 - 3.2  +4J
-1+2`""", parse_mode='MarkdownV2')



async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    terms = tools.sel_terms(message)
    if terms != 0:
        result = tools.calc(terms)
    else:
        result = f'Ошибка! Выражение "{message}" не может быть вычислено!'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    logging.info(f'chat_id={update.effective_chat.id}; user_id={update.effective_user.id}; user_first_name={update.effective_user.first_name}; message_id={update.message.message_id}; message="{update.message.text}"; answer="{result}"')    
    


if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    calc_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, calc)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(calc_handler)
    application.run_polling()