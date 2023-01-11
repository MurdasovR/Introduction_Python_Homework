import logging, tools
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
Привет, {update.effective_user.first_name}!
Я бот, который ведет телефонную книгу.
Доступны команды:
    /start или /help - покажут это сообщение;
    /1 - просмотр всех записей;
    /2 "подстрока" - поиск записи с "подстрокой";
    /3 "запись" - добавить "запись";
    /4 "id" - удалить запись с "id";
    /5 "id" - экспорт записи с "id" в .vcard.""", parse_mode='Markdown')


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tools.init_dict(tools.read_phonebook(), context.chat_data)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=tools.str_phonebook(context.chat_data, context.chat_data.keys()))
    context.chat_data.clear()


async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        tools.init_dict(tools.read_phonebook(), context.chat_data)
        str_find = ''.join(context.args)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=
        f'По подстроке "{str_find}" найдены записи:\n'+ tools.str_phonebook(context.chat_data, tools.phonebook_find(context.chat_data, ''.join(str_find.split()))))
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=
        'Для поиска нужна подстрока\! Например, для поиска записей, содержащих подстроку "`ол`", отправьте сообщение:\n`/2 ол`', parse_mode='MarkdownV2')
    context.chat_data.clear()


async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if context.args:
        tools.init_dict(tools.read_phonebook(), context.chat_data)
        record = ' '.join(context.args).split(',')
        if len(record) > 1:
            temp = record[0].rstrip() + ','
            for i in range(1, len(record) - 1,):
                temp += record[i].strip() + ','
            temp += record[len(record) - 1].lstrip()
            record = temp.split()
        else:
            record = record[0].split()
        if len(record) < 4:
            for i in range(len(record), 4):
                record.append('')
        context.user_data[0] = record
        text = f'Добавить новую запись:\nИмя: {record[0]} {record[1]}\nТел: {", ".join(record[2].split(","))}\nОписание: {", ".join(record[3].split(","))}'
        keyboard = [[InlineKeyboardButton('Да', callback_data='31'), InlineKeyboardButton('Нет', callback_data='32')]]
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
        return 0
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=
        'Для добавления записи отправьте сообщение:\n`/3 Фамилия Имя Телефон Описание`\n\(если нужно несколько значений в поле "Телефон" или "Описание", запишите их через ","\)', parse_mode='MarkdownV2')
        return ConversationHandler.END
        

async def three1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == '31':
        name_record = ''.join([context.user_data[0][i] for i in [0, 1]])
        find_records = tools.phonebook_find(context.chat_data, name_record)
        i = 0
        while len(find_records) > 0 and i < len(find_records):
            if ''.join([context.chat_data[find_records[i]][j] for j in [0, 1]]) == name_record:
                i += 1
            else:
                find_records.pop(i)
        print(find_records)
        if len(find_records) == 0:
            context.chat_data[tools.new_id(context.chat_data)] = context.user_data[0]
            await query.edit_message_text(text='Новая запись добавлена.')
            tools.write_phonebook(context.chat_data)
            context.chat_data.clear()
            context.user_data.clear()
            return ConversationHandler.END
        else:
            text = f'ВНИМАНИЕ!\nЗапись "{""" """.join([context.user_data[0][i] for i in [0, 1]])}" уже существует:\n'+ tools.str_phonebook(context.chat_data, find_records)
            keyboard = [[InlineKeyboardButton('Добавить новую запись', callback_data='33')], [InlineKeyboardButton(f'Добавить в id={find_records[i]}', callback_data=('33' + str(i))) for i in range(len(find_records))]]
            context.user_data[1] = find_records
            await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
            return 1
    else:
        await query.edit_message_text(text='Новая запись добавлена не будет.')
        context.chat_data.clear()
        context.user_data.clear()
        return ConversationHandler.END


async def three12(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == '33':
        context.chat_data[tools.new_id(context.chat_data)] = context.user_data[0]
        await query.edit_message_text(text='Новая запись добавлена.')
        tools.write_phonebook(context.chat_data)
        context.chat_data.clear()
        context.user_data.clear()
        return ConversationHandler.END
    else:
        union_key = context.user_data[1][int(query.data.replace('33', ''))]
        for i in range(2, 4):
            context.chat_data[union_key][i] += ',' + context.user_data[0][i]
        await query.edit_message_text(text=f'Данные по "{context.user_data[0][0]} {context.user_data[0][1]}" объединены с записью id={union_key}')
        tools.write_phonebook(context.chat_data)
        context.chat_data.clear()
        context.user_data.clear()
        return ConversationHandler.END


async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if context.args:
        tools.init_dict(tools.read_phonebook(), context.chat_data)
        del_key = ''.join(''.join(context.args).split())
        if del_key in context.chat_data.keys():
            context.user_data[2] = del_key
            text = f'Удалить запись?\n'+ tools.str_phonebook(context.chat_data, [del_key])
            keyboard = [[InlineKeyboardButton('Да', callback_data='41'), InlineKeyboardButton('Нет', callback_data='42')]]
            await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
            return 2
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=
            f'Записи с id={del_key} не существует. Уточните id записи для удаления.')
            return ConversationHandler.END
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=
        'Для удаления нужен id записи\. Например, для удаления записи с id\=3, отправьте сообщение:\n`/4 3`', parse_mode='MarkdownV2')
        return ConversationHandler.END


async def four1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == '41':
        del context.chat_data[context.user_data[2]]
        await query.edit_message_text(text=f'Запись с id={context.user_data[2]} удалена.')
        tools.write_phonebook(context.chat_data)
        context.chat_data.clear()
        context.user_data.clear()
        return ConversationHandler.END
    else:
        await query.edit_message_text(text=f'Запись с id={context.user_data[2]} удалена не будет.')
        context.chat_data.clear()
        context.user_data.clear()
        return ConversationHandler.END


async def five(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if context.args:
        tools.init_dict(tools.read_phonebook(), context.chat_data)
        export_key = ''.join(''.join(context.args).split())
        if export_key in context.chat_data.keys():
            context.user_data[3] = export_key
            text = f'Экспортировать запись в .vcard?\n'+ tools.str_phonebook(context.chat_data, [export_key])
            keyboard = [[InlineKeyboardButton('Да', callback_data='51'), InlineKeyboardButton('Нет', callback_data='52')]]
            await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
            return 3
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=
            f'Записи с id={export_key} не существует. Уточните id записи для экспорта.')
            return ConversationHandler.END
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=
        'Для экспорта нужен id записи\. Например, для экспорта записи с id\=3, отправьте сообщение:\n`/5 3`', parse_mode='MarkdownV2')
        return ConversationHandler.END


async def five1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == '51':
        if tools.write_vcard(context.chat_data[context.user_data[3]]):
            await query.edit_message_text(text=f'Запись с id={context.user_data[3]} экспортирована в файл _export.vcard_.', parse_mode='Markdown')
            await context.bot.send_document(chat_id=update.effective_chat.id, document=open('export.vcard', 'r'))
            context.chat_data.clear()
            context.user_data.clear()
            return ConversationHandler.END
        else:
            await query.edit_message_text(text=f'Запись с id={context.user_data[3]} не может быть экспортирована.')
            context.chat_data.clear()
            context.user_data.clear()
            return ConversationHandler.END
    else:
        await query.edit_message_text(text=f'Запись с id={context.user_data[3]} экспортирована не будет.')
        context.chat_data.clear()
        context.user_data.clear()
        return ConversationHandler.END


async def other(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Я, конечно, хотел бы поболтать, но пока научился только команды обрабатывать.')



if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('3', three), CommandHandler('4', four), CommandHandler('5', five), MessageHandler(filters.TEXT & ~filters.COMMAND, other)],
        states={0: [CallbackQueryHandler(three1)],
                1: [CallbackQueryHandler(three12)],
                2: [CallbackQueryHandler(four1)],
                3: [CallbackQueryHandler(five1)]},
        fallbacks=[CommandHandler("start", start)])
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', start)
    one_handler = CommandHandler('1', one)
    two_handler = CommandHandler('2', two)
    application.add_handler(conv_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(one_handler)
    application.add_handler(two_handler)
    application.run_polling()
    