import logging, game_kn
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
from random import randint


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat = update.effective_chat
    await context.bot.delete_message(chat_id=chat.id, message_id = update.message.message_id)
    if chat.id in context.bot_data:
        await context.bot.delete_message(chat_id=chat.id, message_id = (update.message.message_id - 1))
        del context.bot_data[chat.id]
    if 0 in context.chat_data:
        await context.bot.delete_message(chat_id=chat.id, message_id = context.chat_data[0])
    context.chat_data[0] = update.message.message_id + 1
    await context.bot.send_message(chat_id=chat.id, text=f"""
Я бот, который играет в "Крестики-нолики!"
Первый ход делается крестиком.
Кто будет делать первый ход определяется случайно.
Выигрывает тот, кто поставит в ряд три крестика или
нолика по горизонтали, вертикали или диагонали.
Доступны команды:
    /start - покажет это сообщение и завершит активную игру;
    /game - начнет игру.""", parse_mode='Markdown')


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    chat = update.effective_chat
    await context.bot.delete_message(chat_id=chat.id, message_id = update.message.message_id)
    if chat.id in context.bot_data:
        del context.bot_data[chat.id]
        await context.bot.delete_message(chat_id=chat.id, message_id = (update.message.message_id - 1))
    logger.info(f'User {user.first_name} started the conversation.')
    context.bot_data[chat.id] = [' '] * 9 + [randint(0, 1)] + [0] + [' ']
    if context.bot_data[chat.id][9]:
        context.bot_data[chat.id][game_kn.bot_turn(context.bot_data[chat.id])] = 'X'
        context.bot_data[chat.id][10] += 1
    text = f'`Я хожу первым\!\nЧтобы поставить нолик,\nнажми пустую клетку\.\.\.{chr(8199) * 2}`' if context.bot_data[chat.id][9] else \
           f'`Первый ход твой\!\nЧтобы поставить крестик,\nнажми пустую клетку\.\.\.{chr(8199) * 2}`'
    keyboard = [[InlineKeyboardButton(str(context.bot_data[chat.id][3 * i + j]), callback_data=str(3 * i + j)) for j in range(3)] for i in range(3)]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='MarkdownV2')
    return 0


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat = update.effective_chat
    query = update.callback_query
    win_bot = 0
    win_bot = 0
    if context.bot_data[chat.id][10] < 9 and context.bot_data[chat.id][11] == ' ':
        await query.answer()
        if context.bot_data[chat.id][int(query.data)] == ' ':
            context.bot_data[chat.id][int(query.data)] = 'O' if context.bot_data[chat.id][9] else 'X'
            context.bot_data[chat.id][10] += 1
            win_player = game_kn.winner(context.bot_data[chat.id])
            if win_player == 0 and context.bot_data[chat.id][10] < 9:
                context.bot_data[chat.id][game_kn.bot_turn(context.bot_data[chat.id])] = 'X' if context.bot_data[chat.id][9] else 'O'
                context.bot_data[chat.id][10] += 1
                win_bot = game_kn.winner(context.bot_data[chat.id])
                if win_bot == 0 and context.bot_data[chat.id][10] < 9:
                    text = f'`Я ход сделал\!\nЧтобы поставить нолик,\nнажми пустую клетку\.\.\.{chr(8199) * 2}`' if context.bot_data[chat.id][9] else \
                           f'`Я ход сделал\!\nЧтобы поставить крестик,\nнажми пустую клетку\.\.\.{chr(8199) * 2}`'
                    keyboard = [[InlineKeyboardButton(str(context.bot_data[chat.id][3 * i + j]), callback_data=str(3 * i + j)) for j in range(3)] for i in range(3)]
                    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='MarkdownV2')
                    return 0
                else:
                    context.bot_data[chat.id][11] = win_bot if win_bot != 0 else 'N'
            else:
                context.bot_data[chat.id][11] = win_player if win_player != 0 else 'N'
        else:
            text = f'`Клетка занята\!\nЧтобы поставить нолик,\nнажми пустую клетку\.\.\.{chr(8199) * 2}`' if context.bot_data[chat.id][9] else \
                   f'`Клетка занята\!\nЧтобы поставить крестик,\nнажми пустую клетку\.\.\.{chr(8199) * 2}`'
            keyboard = [[InlineKeyboardButton(str(context.bot_data[chat.id][3 * i + j]), callback_data=str(3 * i + j)) for j in range(3)] for i in range(3)]
            await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='MarkdownV2')
            return 0
        if context.bot_data[chat.id][11] != ' ' and win_player != 0:
            text = f'`ПОЗДРАВЛЯЮ\!\nТы победил {"ноликами" if context.bot_data[chat.id][9] else "крестиками"}\!'
        elif context.bot_data[chat.id][11] != ' ' and win_bot != 0:
            text = f'`Увы, но\nя победил {"крестиками" if context.bot_data[chat.id][9] else "ноликами"},'
        else:
            text = f'`Увы, но ничья,\nникто не победил,'
        text += f'\nнажми любую клетку \.\.\.{chr(8199) * 2}`'
        keyboard = [[InlineKeyboardButton(str(context.bot_data[chat.id][3 * i + j]), callback_data=str(3 * i + j)) for j in range(3)] for i in range(3)]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='MarkdownV2')
        return 0
    else:
        del context.bot_data[chat.id]
        await query.delete_message()
        return ConversationHandler.END

    
async def other(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id = update.message.message_id)




if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    conv_handler = ConversationHandler(entry_points=[CommandHandler('start', start), CommandHandler('game', game)], 
        states={0: [
            CommandHandler('game', game),
            CallbackQueryHandler(button)]}, 
        fallbacks=[CommandHandler('start', start)])
    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, other))
    
    application.run_polling()
    