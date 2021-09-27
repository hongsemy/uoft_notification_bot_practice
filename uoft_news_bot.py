import telegram

my_token = '1966844637:AAGtjaF4bHILxIGBNLE5RXzDd0HG2arwneg'

bot = telegram.Bot(token=my_token)

updates = bot.getUpdates()

for update in updates:
    print(update.message)

chat_id = bot.getUpdates()[-1].message.chat.id

bot.sendMessage(chat_id=chat_id, text="Hello, I am a bot.")
