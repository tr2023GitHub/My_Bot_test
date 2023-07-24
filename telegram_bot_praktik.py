import telebot
from telebot import types

bot = telebot.TeleBot('6121247749:AAFM8BmBaAyoD_mUMdpyYnbohakGSjT3Jw0')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton(' Мои фото', callback_data='photo')
    item2 = types.InlineKeyboardButton(' Мои увличения', callback_data='post')
    item3 = types.InlineKeyboardButton(' Мои войсы ', callback_data='voices')
    item4 = types.InlineKeyboardButton(' Мой контак ', callback_data='contact')
    item5 = types.InlineKeyboardButton(' Python код бота ', callback_data='Pycode')
    markup.add(item1, item2, item3, item4, item5)
    mess =  'Выбери действия: \n'\
            '/start - вызов меню\n' \
            '/help - вызов справки\n' \
            '/nextstep - ввод следующих шагов'

    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['nextstep'])
def nextstep_run(message):
    a = bot.send_message(message.chat.id, 'Введите текст следующих шагов теста:', parse_mode='html')
    bot.register_next_step_handler(a, returning)


@bot.message_handler(commands=['returning'])
def returning(message):
    bot.send_message(message.chat.id, f'Ваши следующие шаги: {message.text}')


@bot.message_handler(commands=['help'])
def help(message):
    mess =  '<u>Команды: </>\n'\
            ' /start    - вызов меню\n' \
            ' /help     - вызов справки\n' \
            ' /nextstep - ввод следующих шагов по тестированию \n\n' \
            '<u> Кнопки: </u>\n'\
            '<b> "Мои фото" </b>     - выбор фото     :<b> "Фото школьное",\n "Фото сейчас"</b> \n' \
            '<b> "Мои увличения"</b> - выбор поста    : <b>"Перейти на instagram", "Перейти на vk" </b> \n' \
            '<b> "Мои войсы"   </b>  - выбор рассказа : <b>"GPT",\n "SQL and NoSQL","First love"</b>   \n' \
            '<b> "Мой контак" </b>   - вывод моего контактного телефона \n' \
            '<b> "Python код бота"</b>- ссылка репзитория с кодом Бота \n' \
            '<b> "Назад", "Back" </b> - переход на главное меню '
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.callback_query_handler(func=lambda call:True) # нажата та или другая кнопка
def callback(call):
   if call.message:
      if call.data == 'photo':
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text='Bot пошел искать мои фото', parse_mode='html')
          markup = types.InlineKeyboardMarkup(row_width=2)
          button1 = types.InlineKeyboardButton(' Фото школьное', callback_data='school photo')
          button2 = types.InlineKeyboardButton(' Фото сейчас', callback_data='now photo')
          button3 = types.InlineKeyboardButton(' Назад ', callback_data='back')
          markup.add(button1, button2, button3)
          bot.send_message(call.message.chat.id, 'Bot пошел искать мои фото', parse_mode='html', reply_markup=markup)

      elif call.data == 'school photo':
          photo = open('School portrait.jpg', 'rb')
          bot.send_photo(call.message.chat.id, photo)
          bot.send_message(call.message.chat.id, 'Школа', parse_mode='html')
      elif call.data == 'now photo':
          photo = open('Now portrait.jpg', 'rb')
          bot.send_photo(call.message.chat.id, photo)
          bot.send_message(call.message.chat.id, 'Сейчас', parse_mode='html')
      elif call.data == 'back':
          start(call.message)
      elif call.data == 'post':
          keyboard = types.InlineKeyboardMarkup(row_width=1)
          url_button1 = types.InlineKeyboardButton(text="Перейти на instagram",
                     url="https://www.instagram.com/p/B8qtH_eIxgAmSMPdwsxJVirBgAP5XNn4lr6Cz00/?igshid=NTc4MTIwNjQ2YQ==")
          url_button2 = types.InlineKeyboardButton(text="Перейти на vk",
                     url="https://vk.com/id2559866?z=photo2559866_456239083%2Fphotos2559866")
          keyboard.add(url_button1, url_button2)
          bot.send_message(call.message.chat.id, 'Bot пошел на мои посты', parse_mode='html', reply_markup=keyboard)
      elif call.data == 'contact':
          bot.send_message(call.message.chat.id, 'Мой контактный телефон: +7(921)338-48-66', parse_mode='html')
      elif call.data == 'Pycode':
          keyboard = types.InlineKeyboardMarkup(row_width=1)
          url_button = types.InlineKeyboardButton(text="Перейти на Pythonanywhere.com",
                     url="https://www.pythonanywhere.com/user/tr2023Pywhere/files/home/tr2023Pywhere/bot")
          keyboard.add(url_button)
          bot.send_message(call.message.chat.id, 'Bot пошел на мой Python code bot', parse_mode='html', reply_markup=keyboard)
      elif call.data == 'voices':
          markup = types.InlineKeyboardMarkup(row_width=2)
          button1 = types.InlineKeyboardButton(' GPT', callback_data='gpt')
          button2 = types.InlineKeyboardButton(' SQL and NoSQL', callback_data='database')
          button3 = types.InlineKeyboardButton(' First love ', callback_data='love')
          button4 = types.InlineKeyboardButton(' Back ', callback_data='back')
          markup.add(button1, button2, button3, button4)
          bot.send_message(call.message.chat.id, 'Bot пошел искать мои войсы', parse_mode='html', reply_markup=markup)
      elif call.data == 'gpt':
          voice1 = open('voice(2).m4a', 'rb')
          bot.send_audio(call.message.chat.id, voice1)
          bot.send_message(call.message.chat.id, 'GPT chat ', parse_mode='html')
      elif call.data == 'database':
          voice = open('voice 11.m4a', 'rb')
          bot.send_audio(call.message.chat.id, voice)
          bot.send_message(call.message.chat.id, 'SQL and NoSQL', parse_mode='html')
      elif call.data == 'love':
          voice = open('Imany - You Will Never Know.mp3', 'rb')
          bot.send_audio(call.message.chat.id, voice)
          bot.send_message(call.message.chat.id, 'First love', parse_mode='html')


bot.polling(none_stop=True)
