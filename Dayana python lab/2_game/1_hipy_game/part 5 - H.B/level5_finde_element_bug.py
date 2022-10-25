import requests
from bs4 import BeautifulSoup
import telebot
from time import sleep


API_KEY = "5166554024:AAFH3l_HT8Nl39nLG9_vuU_HGqC4OhBerRU"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands = ['start'])
def start(message):
    while True:
        sleep(5)
        response = requests.post('https://arzdigital.com/coins/tether/')
        html = response.content
        usdt_price = BeautifulSoup(html, 'lxml').body.find('div', attrs={'class': 'arz-data__coin-toman-price'}).contents[1].text
        price_message = f"||tether price to toman|| \n\n \t {usdt_price}"
        bot.send_message(message.chat.id, price_message)

bot.polling()
