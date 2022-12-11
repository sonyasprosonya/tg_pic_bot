import telebot
TOKEN = 'тут должен быть токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message (message.chat.id, 'привет!')

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("вот так: 🫠")
	item2 = types.KeyboardButton("вот так: 😃")
	item3 = types.KeyboardButton("вот так: ☹️") 
	item4 = types.KeyboardButton("вот так: 😵‍💫") 
	item5 = types.KeyboardButton("вот так: 🤧") 
	item6 = types.KeyboardButton("вот так: 🤤") 
	item7 = types.KeyboardButton("вот так: 🤡") 
	item8 = types.KeyboardButton("вот так: 🤬") 
	item9 = types.KeyboardButton("вот так: 💃") 
	item10 = types.KeyboardButton("вот так: 🥳") 
	item11 = types.KeyboardButton("вот так: 😔") 
	item12 = types.KeyboardButton("вот так: 🤔") 

	#картинки
	pic1 = open('pic1.webp', 'rb')
	pic2 = open('pic2.webp', 'rb')
	pic3 = open('pic3.webp', 'rb')
	pic4 = open('pic4.webp', 'rb')
	pic5 = open('pic5.webp', 'rb')
	pic6 = open('pic6.webp', 'rb')
	pic7 = open('pic7.webp', 'rb')
	pic8 = open('pic8.webp', 'rb')
	pic9 = open('pic9.webp', 'rb')
	pic10 = open('pic10.webp', 'rb')
	pic11 = open('pic11.webp', 'rb')
	pic12 = open('pic12.webp', 'rb')


	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

	bot.send_message(message.chat.id, "как настроение, {0.first_name}? нажимай на кнопку".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
		#картинки
	pic1 = open('pic1.webp', 'rb')
	pic2 = open('pic2.webp', 'rb')
	pic3 = open('pic3.webp', 'rb')
	pic4 = open('pic4.webp', 'rb')
	pic5 = open('pic5.webp', 'rb')
	pic6 = open('pic6.webp', 'rb')
	pic7 = open('pic7.webp', 'rb')
	pic8 = open('pic8.webp', 'rb')
	pic9 = open('pic9.webp', 'rb')
	pic10 = open('pic10.webp', 'rb')
	pic11 = open('pic11.webp', 'rb')
	pic12 = open('pic12.webp', 'rb')
	if message.chat.type == 'private':
		if message.text == 'вот так: 🫠':
			bot.send_sticker(message.chat.id, pic1)
		elif message.text == 'вот так: 😃':
			bot.send_sticker(message.chat.id, pic2)
		elif message.text == 'вот так: ☹️':
			bot.send_sticker(message.chat.id, pic3)
		elif message.text == 'вот так: 😵‍💫':
			bot.send_sticker(message.chat.id, pic4)
		elif message.text == 'вот так: 🤧':
			bot.send_sticker(message.chat.id, pic5)
		elif message.text == 'вот так: 🤤':
			bot.send_sticker(message.chat.id, pic6)
		elif message.text == 'вот так: 🤡':
			bot.send_sticker(message.chat.id, pic7)
		elif message.text == 'вот так: 🤬':
			bot.send_sticker(message.chat.id, pic8)
		elif message.text == 'вот так: 💃':
			bot.send_sticker(message.chat.id, pic9)
		elif message.text == 'вот так: 🥳':
			bot.send_sticker(message.chat.id, pic10)
		elif message.text == 'вот так: 😔':
			bot.send_sticker(message.chat.id, pic11)
		elif message.text == 'вот так: 🤔':
			bot.send_sticker(message.chat.id, pic12)
		else:
			bot.send_message(message.chat.id, 'ничего не понимаю... 😿')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods