from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "#TOKEN HERE"
BOT_USERNAME: Final = '@managetimeus_bot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a bot to help you!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a Time bot! Type the name of the time zone you want to be')


async def syntax_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Still figuring out')

addition= 0
old_time= 0
after_space = ''
#ADD TIME
def add_time(old_time, addition):
    # Calculate minutes
    total_minutes = (old_time % 100) + (addition % 100)
    new_minutes = total_minutes % 60
    
    # Calculate hours, adding in the "carry hour" if it exists
    additional_hours = addition // 100 + total_minutes // 60
    new_hours = (old_time // 100 + additional_hours) % 24
    
    # Combine hours and minutes
    combined = new_hours * 100 + new_minutes
    combined_string = str(combined)
    if len(combined_string) == 3:
        combined_with_colon = combined_string[:1] + ':' + combined_string[1:]
    else:
        combined_with_colon = combined_string[:2] + ':' + combined_string[2:]
        
    return combined_with_colon

# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    global addition
    global old_time
    global after_space
    after_name1_index = processed.lower().find('name1') + len('name1')
    after_name2_index = processed.lower().find('name2') + len('name2')
    after_name3_index = processed.lower().find('name3') + len('name3')
    after_name4_index = processed.lower().find('name4') + len('name4')
    

    if 'grace' in processed: 
        after_space = processed[after_grace_index:].strip()
        old_time = int(after_space)
        return f'Time for #NAME1 is = {add_time(old_time,1400)}\n Time for #NAME1  is = {add_time(old_time,900)}\n Time for #NAME1 is = {add_time(old_time,1600)}\n'
    if'nicole' in processed:
        after_space = processed[after_nicole_index:].strip()
        old_time = int(after_space)
        return f'Time for #NAME2 is = {add_time(old_time,1000)}\n Time for #NAME1  is = {add_time(old_time,1900)}\n Time for #NAME1 is = {add_time(old_time,200)}\n'
    if 'v' in processed :
        after_space = processed[after_v_index:].strip()
        old_time = int(after_space)
        return f'Time for #NAME3  is = {add_time(old_time,500)}\n Time for #NAME1  is = {add_time(old_time,1500)}\n Time for #NAME1 is = {add_time(old_time,700)}\n'
    if 'jane' in processed:
        after_space = processed[after_jane_index:].strip()
        old_time = int(after_space)
        return f'Time for #NAME4  is = {add_time(old_time,2200)}\n Time for #NAME1  is = {add_time(old_time,1700)}\n Time for #NAME1 is = {add_time(old_time,800)}\n'
    
    return 'I do not understand / Wrong Syntax'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if context.bot.username.lower() in text.lower():
            new_text = text.replace(context.bot.username, '').strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('syntax', syntax_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polling the bot
    print('Polling...')
    app.run_polling(poll_interval=5)
