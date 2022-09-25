import requests
from bs4 import BeautifulSoup
import telebot
from time  import sleep

API_KEY = "5195861765:AAHeyP6baTcSDvzbTzLjmESO1gNjhXUjZig"
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands = ['start'])
def start(message):
    try:
        req1_res = 0
        while True:
            if(req1_res <= 50):
                respone_one  = requests.get('https://www.coindesk.com/price/bitcoin/')
                html_one = respone_one.content
                bs = BeautifulSoup(html_one, 'lxml').body.find_all('span')
                #BTC 
                price_one_btc = bs[6].previous
                #ETH
                price_one_eth = bs[10].previous
                #XRR
                price_one_xrp = bs[14].previous
                price_message = f"\n🔸🔸 BTC: {price_one_btc} 🔸🔸\n\n🔸🔸 ETH: {price_one_eth} 🔸🔸\n\n🔸🔸 XRP: {price_one_xrp} 🔸🔸"
                bot.send_message(-1001786336536, price_message)
                sleep(60)
                req1_res +=1
            else:
                req1_res = 0
                req2_res = 0
                while True:
                    if(req2_res <= 50):
                        response_two  = requests.get('https://coinmarketcap.com/')
                        html_two = response_two.content
                        price_two_btc = BeautifulSoup(html_two, 'lxml').body.find_all('a', attrs={'href':'/currencies/bitcoin/markets/'})[0].text
                        price_two_eth = BeautifulSoup(html_two, 'lxml').body.find_all('a', attrs={'href':'/currencies/ethereum/markets/'})[0].text
                        price_two_xrp = BeautifulSoup(html_two, 'lxml').body.find_all('a', attrs={'href':'/currencies/xrp/markets/'})[0].text
                        price_message = f"\n🔸🔸 BTC: {price_two_btc} 🔸🔸 \n\n 🔸🔸 ETH: {price_two_eth} 🔸🔸 \n\n🔸🔸 XRP: {price_two_xrp} 🔸🔸"
                        bot.send_message(-1001786336536, price_message)
                        sleep(60)
                        req2_res += 1
                    else:
                        break
    except:
        sleep(60)
        start("hi there again")


try:
    bot.polling()()

except:
    sleep(60)
    bot.polling()()
