import telebot


f = open('tokens.txt', 'r', encoding='UTF-8')
token = f.readline()
f.close()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start", "help"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Отправь мне любую фотографию, и я постараюсь найти на ней Амогуса!")


@bot.message_handler(content_types=["text", "audio", "document", "voice", "video", "sticker", "videonote",
                                                "location"])
def handle_not_photo(message):
    bot.send_message(message.chat.id, "Отправь мне любую фотографию, и я постараюсь найти на ней Амогуса!")


@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    bot.send_message(message.chat.id, "Короче, он пока не может находить амогусов, но когда-нибудь...")
    photo = open("src/amogus_1.jpg", 'rb')
    bot.send_photo(message.chat.id, photo)