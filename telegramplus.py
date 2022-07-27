import time
from binance.client import Client
from telegram import *
from telegram.ext import *
import requests
import configparser
from database import user
from ticker_rules import rules
import datetime as dt

config = configparser.ConfigParser()
config.read("config.ini")
token = config["Telegram"]["token"]

print("start")

coin=''
currency=''
itme=9999
full_name=''
api_key=''
secret_key=''
itme1=9999
usdt_amount=0
quantity=0
avg_price=0
itme2=9999
price1=0
itme3=9999
balance=0
itme4=9999
itme5=9999
itme6=9999
stop_lose=''
itme7=9999
itme8=9999
itme9=9999
new_name=''
ads=''
itme11=9999
itme12=9999
itme13=9999

def send_msg(text):
   url="https://api.telegram.org/bot5163073990:AAHshQCHPuupWYgmoxmg7Xf202htZsP2Ug4/sendMessage?chat_id=@botcrypto1&parse_mode=Markdown&text="
   request = url+text
   requests.get(request)

def time_now():
    time = dt.datetime.now()
    time = time.strftime("%d-%m-%Y  %H:%M")
    return time

def get_price(a, b):
    try:
        url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"
        response = requests.get(url.format(a, b)).json()
        return response
    except:
        return False

def start(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, itme10
   global itme11, itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
         name = '*📋 ACCOUNT \n\n📍 Salam ' +str(update.effective_user.first_name).upper()+ '\n\n〽️ Accounts linked to you : '+str(api_users[1])+'\n\n⚜️ Limit accounts : '+str(acc[1])+'\n\n✳️ Limit Ads : '+str(acc[4])+'\n\n🏷 Account Type : '+str(acc[2])+'\n\n🕔 Expiration : '+str(acc[3])+'\n\n♻️ Your account status : '+acc[0]+'*'
         update.message.reply_text(name, parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def price(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, coin, currency, itme7, itme8, itme9, itme10
   global itme11, itme12, itme13
   itme=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         coin=''
         currency=''
         itme=1

         update.message.reply_text("*⚜️ Coin BTC, BNB, ETH, ONE...*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")
         itme=9999

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def addapi(update, context):
   global itme, itme2, itme1, itme4, itme5, itme6, full_name, api_key
   global secret_key, itme3, itme7, itme8, itme9, itme10, itme11, itme12
   global itme13
   itme=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         countuser = user.findapi(collection = "api", Username = str(update.message.chat_id))
         if int(countuser[1]) < int(acc[1]):
              full_name=''
              api_key=''
              secret_key=''
              itme1=5
     
              update.message.reply_text("*📍 Full Name*", parse_mode="Markdown")

         else:
            time.sleep(1)
            update.message.reply_text("*⚠️ You have reached your limit ( "+str(acc[1])+" accounts )\n\n⚠️ You cannot add other accounts at the moment\n\n📞 Contact the bot developer to upgrade your account @xx_070*", parse_mode="Markdown")
            itme1=9999

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")
         itme1=9999

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")
      itme1=9999

def getapi(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
         if int(api_users[1]) > 0:
            for ap in api_users[0]:
               FullNameUser = ap["Name"]
               Pkey= ap["Pkey"]
               Skey = ap["Skey"]
               DateCreated = ap["Date Created"]
               update.message.reply_text("*⚜️  Full Name  ⬇️\n*`"+FullNameUser+"`\n\n*⚜️  API Key  ⬇️\n*`"+Pkey+"`\n\n*⚜️  Secret Key  ⬇️\n*`"+Skey+"`\n\n*⚜️  Date Created  ⬇️*\n`"+DateCreated+"`", parse_mode="Markdown")
               time.sleep(1)

         else:
            update.message.reply_text("*⚠️ There are no accounts currently affiliated with you.*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def buy(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, coin, currency
   global usdt_amount, quantity, avg_price, itme7, itme8, itme9, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
            api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
            if int(api_users[1]) > 0:
               coin=''
               currency=''
               usdt_amount=0
               quantity=0
               avg_price=0
               itme2=10
   
               update.message.reply_text("*⚜️ Coin BTC, BNB, ETH, ONE...*", parse_mode="Markdown")
   
            else:
               update.message.reply_text("*⚠️ There are no accounts currently affiliated with you.*", parse_mode="Markdown")
               itme2=9999
      
      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")
         itme2=9999

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def buylimit(update, context):
   global itme, itme1, itme2, itme3,itme4, itme5, itme6, coin, currency, usdt_amount
   global price1, quantity, avg_price, itme7, itme8, itme9, itme10, itme11, itme12
   global itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
            api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
            if int(api_users[1]) > 0:
               coin=''
               currency=''
               usdt_amount=0
               quantity=0
               avg_price=0
               price1=0
               itme3=15
   
               update.message.reply_text("*⚜️ Coin BTC, BNB, ETH, ONE...*", parse_mode="Markdown")
   
            else:
               update.message.reply_text("*⚠️ There are no accounts currently affiliated with you.*", parse_mode="Markdown")
               itme3=9999
      
      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")
         itme3=9999

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def sale(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, coin, currency, usdt_amount
   global quantity, avg_price, balance, itme7, itme8, itme9, itme10, itme11, itme12
   global itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
            api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
            if int(api_users[1]) > 0:
               coin=''
               currency=''
               usdt_amount=0
               quantity=0
               balance=0
               avg_price=0
               itme4=25
   
               update.message.reply_text("*⚜️ Coin BTC, BNB, ETH, ONE...*", parse_mode="Markdown")
   
            else:
               update.message.reply_text("*⚠️ There are no accounts currently affiliated with you.*", parse_mode="Markdown")
               itme4=9999

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")
         itme4=9999

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def salelimit(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, coin, currency, usdt_amount
   global quantity, avg_price, balance, itme7, itme8, itme9, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
         if int(api_users[1]) > 0:
               coin=''
               currency=''
               usdt_amount=0
               quantity=0
               balance=0
               avg_price=0
               itme5=30
   
               update.message.reply_text("*⚜️ Coin BTC, BNB, ETH, ONE...*", parse_mode="Markdown")
   
         else:
               update.message.reply_text("*⚠️ There are no accounts currently affiliated with you.*", parse_mode="Markdown")
               itme5=9999
      
      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def salelimitstop(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, coin, currency, usdt_amount
   global quantity, avg_price, balance, stop_lose, itme7, itme8, itme9, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
            api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
            if int(api_users[1]) > 0:
               coin=''
               currency=''
               stop_lose=''
               usdt_amount=0
               quantity=0
               balance=0
               avg_price=0
               itme6=40
   
               update.message.reply_text("*⚜️ Coin BTC, BNB, ETH, ONE...*", parse_mode="Markdown")
   
            else:
               update.message.reply_text("*⚠️ There are no accounts currently affiliated with you.*", parse_mode="Markdown")
               itme6=9999

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def getorders(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         orders = user.findapi(collection = "orders", Username = str(update.message.chat_id))
         if int(orders[1]) > 0:
            for ap in orders[0]:
               Symbol = ap["Symbol"]
               Stat= ap["Stat"]
               Quantity = ap["Quantity"]
               Amount_USDT = ap["Amount USDT"]
               Price = ap["Price"]
               Transaction_Date = ap["Transaction Date"]
               update.message.reply_text("*🏷  Symbol  ➡️  *`"+Symbol+"`\n\n*🗳  Quantity  ➡️  *`"+str(Quantity)+"`\n\n*💵  Amount  ➡️  *`"+str(Amount_USDT)+"`\n\n*💰  Price  ➡️  *`"+str(Price)+"`\n\n*♻️  Type  ➡️  *`"+Stat+"`\n\n*🕔  Transaction Date  ➡️  *`"+Transaction_Date+"`", parse_mode="Markdown")
               time.sleep(1)

         else:
            update.message.reply_text("*⚠️ You have not placed any order yet.*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def deleteapi(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
         if int(api_users[1]) > 0:
            itme7=50
            update.message.reply_text("*⚜️  Full Name*", parse_mode="Markdown")

         else:
            update.message.reply_text("*⚠️ There are no accounts currently affiliated with you.*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def deletalleapi(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
         if int(api_users[1]) > 0:
            itme8=55
            update.message.reply_text("*⚠️ Warning, you are about to delete all accounts.*", parse_mode="Markdown")
            update.message.reply_text('*❓ Are You Sure? send yes or no*', parse_mode="Markdown")

         else:
            update.message.reply_text("*⚠️ There are no accounts currently affiliated with you.*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def editapi(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, new_name, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
         if int(api_users[1]) > 0:
            itme9=60
            new_name=''
            update.message.reply_text('*⚜️ The name of the account you want to edit*', parse_mode="Markdown")

         else:
            update.message.reply_text("*⚠️ There are no accounts currently affiliated with you.*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def addads(update, context):
   global itme, itme2, itme1, itme4, itme5, itme6, full_name
   global itme3, itme7, itme8, itme9, itme10, ads, itme11, itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         countcomment = user.countcomment(collection = "comment", Username = str(update.message.chat_id))
         if countcomment < int(acc[4]):
            ads=''
            full_name=''
            itme10=65
            update.message.reply_text("*✳️ Ads name*", parse_mode="Markdown")

         else:
            time.sleep(1)
            update.message.reply_text("*⚠️ You have reached your ads limit ( "+str(acc[5])+" ads )\n\n⚠️ You cannot add other ads at the moment\n\n📞 Contact the bot developer to upgrade your account @xx_070*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def editads(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, new_name, itme10
   global itme11, ads, full_name, itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         countcomment = user.countcomment(collection = "comment", Username = str(update.message.chat_id))
         if countcomment > 0:
            itme11=70
            ads=''
            full_name=''
            update.message.reply_text('*⚜️ The name of the ad you want to edit*', parse_mode="Markdown")

         else:
            update.message.reply_text("*⚠️ There are no ads currently affiliated with you.*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def deletead(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, itme10, itme11
   global full_name, itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         countcomment = user.countcomment(collection = "comment", Username = str(update.message.chat_id))
         if countcomment > 0:
            itme12=75
            full_name=''
            update.message.reply_text("*⚜️ Name of the ad*", parse_mode="Markdown")

         else:
            update.message.reply_text("*⚠️ There are no ads currently affiliated with you.*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def deletalleads(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         countcomment = user.countcomment(collection = "comment", Username = str(update.message.chat_id))
         if countcomment > 0:
            itme13=80
            update.message.reply_text("*⚠️ Warning, you are about to delete all ads.*", parse_mode="Markdown")
            update.message.reply_text('*❓ Are You Sure? send yes or no*', parse_mode="Markdown")

         else:
            update.message.reply_text("*⚠️ There are no ads currently affiliated with you.*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

def getads(update, context):
   global itme, itme1, itme2, itme3, itme4, itme5, itme6, itme7, itme8, itme9, itme10, itme11
   global itme12, itme13
   itme=9999
   itme1=9999
   itme2=9999
   itme3=9999
   itme4=9999
   itme5=9999
   itme6=9999
   itme7=9999
   itme8=9999
   itme9=9999
   itme10=9999
   itme11=9999
   itme12=9999
   itme13=9999
   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":
         countcomment = user.countcomment(collection = "comment", Username = str(update.message.chat_id))
         if countcomment > 0:
            findcomment = user.findapi(collection = "comment", Username = str(update.message.chat_id))
            for ap in findcomment[0]:
               Name = ap["Name"]
               Ads= ap["Ads"]
               Date = ap["Date"]
               update.message.reply_text("*🏷  Name  ➡️  *`"+Name+"`\n\n*✳️  Ads  ➡️  *`"+str(Ads)+"`\n\n*🕔  Date created  ➡️  *`"+Date+"`", parse_mode="Markdown")

         else:
            update.message.reply_text("*⚠️ There are no ads currently affiliated with you.*", parse_mode="Markdown")

      elif acc[0] == "OFF":
         update.message.reply_text("*The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")


def handlmsg(update, context):
   global itme, coin, currency
   global itme1, full_name, api_key, secret_key
   global itme2, usdt_amount, quantity, avg_price
   global itme3, price1, itme4, balance, itme5, itme6, stop_lose, itme7, itme8
   global itme9, new_name, itme10, ads, itme11, itme12, itme13

   acc = user.findacc(collection = "acc", Username = str(update.message.chat_id))
   if acc != None:
      if acc[0] == "ON":

         if itme == 1:
            coin = update.message.text
            update.message.reply_text("*⚜️ Currency USDT, USDC, BUSD...*", parse_mode="Markdown")

         if itme == 2:
            currency = update.message.text
            currency = currency.upper()
            coin = coin.upper()
            symbol = coin+currency
            if symbol in rules:
               a = get_price(coin, currency)
               a = a[currency]
               update.message.reply_text('*✅ 1 '+coin+'  ≈  '+str(a)+' '+currency+'*', parse_mode="Markdown")

            else:
               time.sleep(1)
               update.message.reply_text('*⚠️ You may have entered the name incorrectly.*', parse_mode="Markdown")
               itme=9999

         if itme1 == 5:
            full_name = update.message.text
            update.message.reply_text("*〽️ API Key*", parse_mode="Markdown")

         if itme1 == 6:
            api_key = update.message.text
            update.message.reply_text("*🔑 Secret Key*", parse_mode="Markdown")

         if itme1 == 7:
            secret_key = update.message.text
            update.message.reply_text("*⏳ Please wait to review the information you entered...*\n\n`⚠️ Reminder 📣, delete messages that contain sensitive information after you're done.`", parse_mode="Markdown")
            try:
                  client = Client(api_key=str(api_key), api_secret=str(secret_key))
                  balance = client.get_asset_balance(asset = "USDT")
                  free_balance = round(float(balance["free"]), 3)

                  user.addapi(collection = "api", Name = full_name.upper(), Pkey = str(api_key), Skey = str(secret_key), DateCreated = time_now(), Owenr = str(update.message.chat_id))
                  time.sleep(1)

                  update.message.reply_text('*✅ '+full_name.upper()+" added successfully\n\n💵 Current balance USDT: "+str(free_balance)+'$*', parse_mode="Markdown")

            except:
                  time.sleep(1)
                  update.message.reply_text("*⚠️ The information you entered is wrong or you made a lot of requests, please wait a little.*", parse_mode="Markdown")
                  itme1=9999

         if itme2 == 10:
            coin = update.message.text
            update.message.reply_text("*⚜️ Currency USDT, USDC, BUSD...*", parse_mode="Markdown")

         if itme2 == 11:
            currency = update.message.text
            currency = currency.upper()
            coin = coin.upper()
            symbol = coin+currency
            if symbol in rules:
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
               for ap in api_users[0]:
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]
               client = Client(api_key=Pkey, api_secret=Skey)
               balance = client.get_asset_balance(asset = currency)
               balance = float(balance["free"])
               if balance > 0:
                  update.message.reply_text("*🟢 Your current "+currency+" balance is *`"+str(balance)+"`", parse_mode="Markdown")
                  update.message.reply_text("*💵 Amount*\n\n`Example : ✅ 100.50 ❌ 100,50`", parse_mode="Markdown")

               else:
                  time.sleep(1)
                  update.message.reply_text('*🔴 You do not have enough '+currency+'*', parse_mode="Markdown")
                  itme2 = 9999

            else:
               time.sleep(1)
               update.message.reply_text('*⚠️ You may have entered the name incorrectly.*', parse_mode="Markdown")
               itme2 = 9999

         if itme2 == 12:
            try:
               usdt_amount = float(update.message.text)
               symbol = coin + currency
               if usdt_amount >= rules[symbol][4]:
                  itme2 = 13

               else:
                  time.sleep(1)
                  update.message.reply_text("*⚠️ Sorry, the minimum value that can be traded is "+str(rules[symbol][4])+" "+currency+" or more.*", parse_mode="Markdown")
                  itme2 = 9999

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Purchase amount must be a number.*", parse_mode="Markdown")
               itme2 = 9999

         if itme2 == 13:
            try:
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
               for ap in api_users[0]:
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]

               symbol = coin + currency
               float_format = "%."+str(rules[symbol][0])+"f"
               usdt_amount = float_format % usdt_amount

               client = Client(api_key=str(Pkey), api_secret=(Skey))
               avg_price = client.get_avg_price(symbol = symbol)
               avg_price = float(avg_price["price"])
               quantity = float(usdt_amount) / avg_price
               quantity = round(quantity, rules[symbol][3])
               time.sleep(1)
               update.message.reply_text("*🚨 Warning, if approved, the purchase will be processed for all your accounts !!*", parse_mode="Markdown")
               update.message.reply_text('*💰 You will get '+str(quantity)+' '+coin+'*\n\n❓ Are You Sure? send yes or no', parse_mode="Markdown")

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Purchase amount must be a number.*", parse_mode="Markdown")
               itme2 = 9999

         if itme2 == 14:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))

               a = 0
               b = 0
               for ap in api_users[0]:
                  FullNameUser = ap["Name"]
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]
                  try:
                     client = Client(api_key=str(Pkey), api_secret=(Skey))
                     symbol = coin + currency
                     order = client.order_market_buy(symbol=symbol, quantity=quantity)
                     OrderSymbol = order['symbol']
                     QtyOrig = order['origQty']
                     USDTQty = order['cummulativeQuoteQty']
                     time.sleep(1)
                     update.message.reply_text("*✅ $"+usdt_amount+" of "+symbol+" has been successfully purchased for "+FullNameUser+"*", parse_mode="Markdown")
                     a = a + 1

                  except:
                     b = b + 1
                     time.sleep(1)
                     update.message.reply_text("*⚠️ Purchase failed: "+FullNameUser+"*", parse_mode="Markdown")

               if a > 0:
                  user.addorder(collection = "orders", TransactionDate = time_now(), Symbol = OrderSymbol, Stat = "BUY", Quantity = QtyOrig, USDTAmount = USDTQty, Price = avg_price, Owenr = str(update.message.chat_id))

               update.message.reply_text("*✅ Successful purchases: "+str(a)+"\n\n⚠️ Purchases failed: "+str(b)+"*", parse_mode="Markdown")

            else:
               time.sleep(1)
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme2=9999

         if itme3 == 15:
            coin = update.message.text
            update.message.reply_text("*⚜️ Currency USDT, USDC, BUSD...*", parse_mode="Markdown")

         if itme3 == 16:
            currency = update.message.text
            currency = currency.upper()
            coin = coin.upper()
            symbol = coin+currency
            if symbol in rules:
               time.sleep(1)
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
               for ap in api_users[0]:
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]
               client = Client(api_key=Pkey, api_secret=Skey)
               balance = client.get_asset_balance(asset = currency)
               balance = float(balance["free"])
               if balance > 0:
                  update.message.reply_text("*🟢 Your current "+currency+" balance is *`"+str(balance)+"`", parse_mode="Markdown")
                  update.message.reply_text("*💵 Amount*\n\n`Example : ✅ 100.50 ❌ 100,50`", parse_mode="Markdown")
            
               else:
                  update.message.reply_text('*🔴 You do not have enough '+currency+'*', parse_mode="Markdown")
                  itme3 = 9999
            else:
               time.sleep(1)
               itme3 = 9999
               update.message.reply_text('*⚠️ You may have entered the name incorrectly.*', parse_mode="Markdown")

         if itme3 == 17:
            try:
               usdt_amount = float(update.message.text)
               symbol = coin + currency
               if usdt_amount >= rules[symbol][4]:
                  time.sleep(1)
                  update.message.reply_text("*💲 Price*\n\n`🚨 The price you want to buy from\n\nExample : ✅ 100.50 ❌ 100,50`", parse_mode="Markdown")

               else:
                  update.message.reply_text("*⚠️ Sorry, the minimum value that can be traded is "+str(rules[symbol][4])+" "+currency+" or more.*", parse_mode="Markdown")
                  itme3 = 9999

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Purchase amount must be a number.*", parse_mode="Markdown")
               itme3 = 9999

         if itme3 == 18:
            try:
               price1 = float(update.message.text)
               time.sleep(1)
               symbol = coin+currency
               float_format = "%."+str(rules[symbol][0])+"f"
               usdt_amount = float_format % usdt_amount
               a = get_price(coin, currency)
               a = a[currency]
               float_format = "%."+str(rules[symbol][0])+"f"
               price1 = float_format % price1
               quantity = float(float(usdt_amount) / float(price1))
               quantity = round(quantity, rules[symbol][3])

               update.message.reply_text("*🚨 Warning, if approved, the purchase will be processed for all your accounts !!*", parse_mode="Markdown")
               update.message.reply_text('*✅ 1 '+coin+'  ≈  '+str(a)+' '+currency+'*', parse_mode="Markdown")
               update.message.reply_text('*💰 You will get '+str(quantity)+' '+coin+'*\n\n❓ Are You Sure? send yes or no', parse_mode="Markdown")

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Price must be a number.*", parse_mode="Markdown")
               itme3 = 9999

         if itme3 == 19:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))

               a = 0
               b = 0
               for ap in api_users[0]:
                  FullNameUser = ap["Name"]
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]
                  try:
                     client = Client(api_key=str(Pkey), api_secret=(Skey))
                     symbol = coin + currency
                     order = client.order_limit_buy(symbol=symbol, quantity=quantity, price=price1)
                     OrderSymbol = order['symbol']
                     QtyOrig = order['origQty']
                     USDTQty = usdt_amount
                     time.sleep(1)
                     update.message.reply_text("*✅ $"+usdt_amount+" of "+symbol+" order placed successfully for "+FullNameUser+"*", parse_mode="Markdown")
                     a = a + 1

                  except:
                     b = b + 1
                     time.sleep(1)
                     update.message.reply_text("*⚠️ Purchase order has not been placed: "+FullNameUser+"*", parse_mode="Markdown")

               if a > 0:
                  user.addorder(collection = "orders", TransactionDate = time_now(), Symbol = OrderSymbol, Stat = "BUY LIMIT", Quantity = QtyOrig, USDTAmount = USDTQty, Price = price1, Owenr = str(update.message.chat_id))

               update.message.reply_text("*✅ Successful purchases: "+str(a)+"\n\n⚠️ Purchases failed: "+str(b)+"*", parse_mode="Markdown")

            else:
               time.sleep(1)
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme3=9999

         if itme4 == 25:
            coin = update.message.text
            update.message.reply_text("*⚜️ Currency USDT, USDC, BUSD...*", parse_mode="Markdown")

         if itme4 == 26:
            currency = update.message.text
            currency = currency.upper()
            coin = coin.upper()
            symbol = coin+currency
            if symbol in rules:
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
               for ap in api_users[0]:
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]

               client = Client(api_key=Pkey, api_secret=Skey)
               balance = client.get_asset_balance(asset = coin)
               balance = float(balance["free"])
               time.sleep(1)
               if float(balance) > 0:
                  update.message.reply_text("*🟢 Your current "+coin+" balance is *`"+str(balance)+"`", parse_mode="Markdown")
                  update.message.reply_text("*🗳 Quantity*\n\n`Example : ✅ 0.5130 ❌ 0,5130`", parse_mode="Markdown")

               else:
                  time.sleep(1)
                  update.message.reply_text("*🔴 Your account does not have any amount of this currency.*", parse_mode="Markdown")
                  itme4 = 9999

            else:
               time.sleep(1)
               update.message.reply_text('*⚠️ You may have entered the name incorrectly.*', parse_mode="Markdown")
               itme4 = 9999

         if itme4 == 27:
            try:
               symbol = coin + currency
               quantity = float(update.message.text)
               commission = (float(quantity) / 100) 
               quantity = float(quantity) - commission
               quantity = round(quantity, rules[symbol][3])
               quantity=float(quantity)
               if quantity <= balance:
                  try:
                     symbol = coin + currency
                     api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
                     for ap in api_users[0]:
                        Pkey= ap["Pkey"]
                        Skey = ap["Skey"]

                     client = Client(api_key=Pkey, api_secret=Skey)
                     avg_price = client.get_avg_price(symbol = symbol)
                     avg_price = float(avg_price["price"])
                     avg_price = round(avg_price, 2)
                     time.sleep(1)
                     qnt = quantity * avg_price >= rules[symbol][4]
                     usdt_amount = quantity * avg_price
                     usdt_amount = round(usdt_amount, 2)

                     if qnt:
                        update.message.reply_text("*🚨 Warning, if approved, the sale will be processed for all your accounts !!*", parse_mode="Markdown")
                        update.message.reply_text('*✅ 1 '+coin+'  ≈  '+str(avg_price)+' '+currency+'*', parse_mode="Markdown")
                        update.message.reply_text('*💰 You will get '+str(usdt_amount)+' '+currency+'*\n\n❓ Are You Sure? send yes or no', parse_mode="Markdown")

                     else:
                        time.sleep(1)
                        update.message.reply_text("*⚠️ You cannot sell this amount.*", parse_mode="Markdown")
                        itme4 = 9999

                  except:
                     time.sleep(1)
                     update.message.reply_text("*⚠️ You made a lot of requests, please wait a little..*", parse_mode="Markdown")
                     itme4 = 9999

               else:
                  time.sleep(1)
                  update.message.reply_text("*⚠️ Sorry, the quantity you entered is not available\n\n🟢 Your current "+coin+" balance is *`"+str(balance)+"`", parse_mode="Markdown")
                  itme4 = 9999

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Quantity must be a number.*", parse_mode="Markdown")
               itme4 = 9999

         if itme4 == 28:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))

               a = 0
               b = 0
               for ap in api_users[0]:
                  FullNameUser = ap["Name"]
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]
                  try:
                     client = Client(api_key=str(Pkey), api_secret=(Skey))
                     symbol = coin + currency
                     order = client.order_market_sell(symbol=symbol, quantity=quantity)
                     OrderSymbol = symbol
                     QtyOrig = quantity
                     USDTQty = usdt_amount
                     time.sleep(1)
                     update.message.reply_text("*✅ "+str(quantity)+" "+symbol+" successfully sold: "+FullNameUser+"*", parse_mode="Markdown")
                     a = a + 1

                  except:
                     b = b + 1
                     time.sleep(1)
                     update.message.reply_text("*⚠️ Sale Failed: "+FullNameUser+"*", parse_mode="Markdown")

               if a > 0:
                  user.addorder(collection = "orders", TransactionDate = time_now(), Symbol = OrderSymbol, Stat = "SALE", Quantity = QtyOrig, USDTAmount = USDTQty, Price = avg_price, Owenr = str(update.message.chat_id))

               update.message.reply_text("*✅ Successful Solds: "+str(a)+"\n\n⚠️ Sales Failed: "+str(b)+"*", parse_mode="Markdown")

            else:
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme4=9999

         if itme5 == 30:
            coin = update.message.text
            update.message.reply_text("*⚜️ Currency USDT, USDC, BUSD...*", parse_mode="Markdown")

         if itme5 == 31:
            currency = update.message.text
            currency = currency.upper()
            coin = coin.upper()
            symbol = coin+currency
            if symbol in rules:
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
               for ap in api_users[0]:
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]

               client = Client(api_key=Pkey, api_secret=Skey)
               balance = client.get_asset_balance(asset = coin)
               balance = float(balance["free"])
               time.sleep(1)
               if float(balance) > 0:
                  update.message.reply_text("*🟢 Your current "+coin+" balance is *`"+str(balance)+"`", parse_mode="Markdown")
                  update.message.reply_text("*🗳 Quantity*\n\n`Example : ✅ 0.5130 ❌ 0,5130`", parse_mode="Markdown")

               else:
                  time.sleep(1)
                  update.message.reply_text("*🔴 Your account does not have any amount of this currency.*", parse_mode="Markdown")
                  itme5 = 9999

            else:
               time.sleep(1)
               update.message.reply_text('*⚠️ You may have entered the name incorrectly.*', parse_mode="Markdown")
               itme5 = 9999

         if itme5 == 32:
            try:
               symbol = coin + currency
               quantity = float(update.message.text)
               commission = (float(quantity) / 100)
               quantity = float(quantity) - commission
               quantity = round(quantity, rules[symbol][3])
               quantity=float(quantity)
               if quantity <= balance:
                  try:
                     symbol = coin + currency
                     api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
                     for ap in api_users[0]:
                        Pkey= ap["Pkey"]
                        Skey = ap["Skey"]

                     client = Client(api_key=Pkey, api_secret=Skey)
                     avg_price = client.get_avg_price(symbol = symbol)
                     avg_price = float(avg_price["price"])
                     avg_price = round(avg_price, 2)
                     time.sleep(1)
                     qnt = quantity * avg_price >= rules[symbol][4]
                     usdt_amount = quantity * avg_price
                     usdt_amount = round(usdt_amount, 2)

                     if qnt:
                        update.message.reply_text("*💲 Price*\n\n`🚨 The price you want to sell at\n\nExample : ✅ 100.50 ❌ 100,50`", parse_mode="Markdown")

                     else:
                        time.sleep(1)
                        update.message.reply_text("*⚠️ You cannot sell this amount.*", parse_mode="Markdown")
                        itme5=9999

                  except:
                     time.sleep(1)
                     update.message.reply_text("*⚠️ You made a lot of requests, please wait a little..*", parse_mode="Markdown")
                     itme5=9999

               else:
                  time.sleep(1)
                  update.message.reply_text("*⚠️ Sorry, the quantity you entered is not available\n\n🟢 Your current "+coin+" balance is *`"+str(balance)+"`", parse_mode="Markdown")
                  itme5=9999

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Quantity must be a number.*", parse_mode="Markdown")
               itme5=9999

         if itme5 == 33:
            try:
               price1 = float(update.message.text)
               symbol = coin+currency
               float_format = "%."+str(rules[symbol][0])+"f"
               price1 = float_format % price1
               usdt_amount = quantity * float(price1)
               usdt_amount = round(float(usdt_amount), 3)

               prc = float(price1) > float(avg_price)
               if prc:
                  update.message.reply_text("*🚨 Warning, if approved, the sale will be processed for all your accounts !!*", parse_mode="Markdown")
                  update.message.reply_text('*✅ 1 '+coin+'  ≈  '+str(avg_price)+' '+currency+'*', parse_mode="Markdown")
                  update.message.reply_text('*💰 You will get '+str(usdt_amount)+' '+currency+'*\n\n❓ Are You Sure? send yes or no', parse_mode="Markdown")

               else:
                  time.sleep(1)
                  update.message.reply_text("*⚠️ You have set the selling price less than the current price.\n\n⚠️ If you want to work with the stop loss feature, click on the following command /sale_limit_stop_lose*", parse_mode="Markdown")
                  itme5 = 9999

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Price must be a number.*", parse_mode="Markdown")
               itme5 = 9999

         if itme5 == 34:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))

               a = 0
               b = 0
               for ap in api_users[0]:
                  FullNameUser = ap["Name"]
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]
                  try:
                     client = Client(api_key=str(Pkey), api_secret=(Skey))
                     symbol = coin + currency
                     order = client.order_limit_sell(symbol=symbol, quantity=quantity, price=price1)
                     OrderSymbol = symbol
                     QtyOrig = quantity
                     USDTQty = usdt_amount
                     time.sleep(1)
                     update.message.reply_text("*✅ Sell order has been placed successfully: "+FullNameUser+"*", parse_mode="Markdown")
                     a = a + 1

                  except:
                     b = b + 1
                     time.sleep(1)
                     update.message.reply_text("*⚠️ Failed to place sell order: "+FullNameUser+"*", parse_mode="Markdown")

               if a > 0:
                  user.addorder(collection = "orders", TransactionDate = time_now(), Symbol = OrderSymbol, Stat = "SALE LIMIT", Quantity = QtyOrig, USDTAmount = USDTQty, Price = price1, Owenr = str(update.message.chat_id))

               update.message.reply_text("*✅ Successful Solds: "+str(a)+"\n\n⚠️ Sales Failed: "+str(b)+"*", parse_mode="Markdown")

            else:
               time.sleep(1)
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme5=9999

         if itme6 == 40:
            coin = update.message.text
            update.message.reply_text("*⚜️ Currency USDT, USDC, BUSD...*", parse_mode="Markdown")

         if itme6 == 41:
            currency = update.message.text
            currency = currency.upper()
            coin = coin.upper()
            symbol = coin+currency
            if symbol in rules:
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
               for ap in api_users[0]:
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]

               client = Client(api_key=Pkey, api_secret=Skey)
               balance = client.get_asset_balance(asset = coin)
               balance = float(balance["free"])
               time.sleep(1)
               if float(balance) > 0:
                  update.message.reply_text("*🟢 Your current "+coin+" balance is *`"+str(balance)+"`", parse_mode="Markdown")
                  update.message.reply_text("*🗳 Quantity*\n\n`Example : ✅ 0.5130 ❌ 0,5130`", parse_mode="Markdown")

               else:
                  time.sleep(1)
                  update.message.reply_text("*🔴 Your account does not have any amount of this currency.*", parse_mode="Markdown")
                  itme6 = 9999

            else:
               time.sleep(1)
               update.message.reply_text('*⚠️ You may have entered the name incorrectly.*', parse_mode="Markdown")
               itme6 = 9999

         if itme6 == 42:
            try:
               symbol = coin + currency
               quantity = float(update.message.text)
               commission = (float(quantity) / 100)
               quantity = float(quantity) - commission
               quantity = round(quantity, rules[symbol][3])
               quantity=float(quantity)
               if quantity <= balance:
                  try:
                     symbol = coin + currency
                     api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))
                     for ap in api_users[0]:
                        Pkey= ap["Pkey"]
                        Skey = ap["Skey"]

                     client = Client(api_key=Pkey, api_secret=Skey)
                     avg_price = client.get_avg_price(symbol = symbol)
                     avg_price = float(avg_price["price"])
                     avg_price = round(avg_price, 2)
                     time.sleep(1)
                     qnt = quantity * avg_price >= rules[symbol][4]
                     usdt_amount = quantity * avg_price
                     usdt_amount = round(usdt_amount, 2)

                     if qnt:
                        update.message.reply_text('*✅ 1 '+coin+'  ≈  '+str(avg_price)+' '+currency+'*', parse_mode="Markdown")
                        update.message.reply_text("*💲 Price*\n\n`🚨 The price you want to sell at\n\nExample : ✅ 100.50 ❌ 100,50`", parse_mode="Markdown")

                     else:
                        time.sleep(1)
                        update.message.reply_text("*⚠️ You cannot sell this amount.*", parse_mode="Markdown")
                        itme6=9999

                  except:
                     time.sleep(1)
                     update.message.reply_text("*⚠️ You made a lot of requests, please wait a little..*", parse_mode="Markdown")
                     itme6=9999

               else:
                  time.sleep(1)
                  update.message.reply_text("*⚠️ Sorry, the quantity you entered is not available\n\n🟢 Your current "+coin+" balance is *`"+str(balance)+"`", parse_mode="Markdown")
                  itme6=9999

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Quantity must be a number.*", parse_mode="Markdown")
               itme6=9999

         if itme6 == 43:
            try:
               price1 = float(update.message.text)
               symbol = coin+currency
               float_format = "%."+str(rules[symbol][0])+"f"
               price1 = float_format % price1
               usdt_amount = quantity * float(price1)
               usdt_amount = round(float(usdt_amount), 3)

               prc = float(price1) < float(avg_price)
               if prc:
                  update.message.reply_text("`🚨 The price you want to sell at is less than the current price, it will be sold according to the current price in the market`", parse_mode="Markdown")

               update.message.reply_text('*✅ 1 '+coin+'  ≈  '+str(avg_price)+' '+currency+'*', parse_mode="Markdown")
               update.message.reply_text("*🛑 Stop Limit*\n\n`🚨 The price you want to use at stop lose\n\nExample : ✅ 100.50 ❌ 100,50`", parse_mode="Markdown")

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Price must be a number.*", parse_mode="Markdown")
               itme6 = 9999

         if itme6 == 44:
            try:
               stop_lose = float(update.message.text)
               symbol = coin+currency
               float_format = "%."+str(rules[symbol][0])+"f"
               stop_lose = float_format % stop_lose
               usdt_amount = quantity * float(price1)
               usdt_amount = round(float(usdt_amount), 3)

               update.message.reply_text("*🚨 Warning, if approved, the sale will be processed for all your accounts !!*", parse_mode="Markdown")
               update.message.reply_text('*✅ 1 '+coin+'  ≈  '+str(avg_price)+' '+currency+'*', parse_mode="Markdown")
               update.message.reply_text('*💰 You will get '+str(usdt_amount)+' '+currency+'*\n\n❓ Are You Sure? send yes or no', parse_mode="Markdown")

            except:
               time.sleep(1)
               update.message.reply_text("*⚠️ Stop lose must be a number.*", parse_mode="Markdown")
               itme6 = 9999

         if itme6 == 45:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               api_users = user.findapi(collection = "api", Username = str(update.message.chat_id))

               a = 0
               b = 0
               for ap in api_users[0]:
                  FullNameUser = ap["Name"]
                  Pkey= ap["Pkey"]
                  Skey = ap["Skey"]
                  try:
                     client = Client(api_key=str(Pkey), api_secret=(Skey))
                     symbol = coin + currency
                     trigger = float(stop_lose) + (float(stop_lose) * 0.001)
                     float_format = "%."+str(rules[symbol][0])+"f"
                     trigger = float_format % trigger
                     order = client.create_oco_order(symbol = symbol, side = "SELL", stopLimitTimeInForce = "GTC", quantity = quantity, stopPrice = trigger, stopLimitPrice  = stop_lose, price = price1 )
                     OrderSymbol = symbol
                     QtyOrig = quantity
                     USDTQty = usdt_amount
                     time.sleep(1)
                     update.message.reply_text("*✅ Sell order has been placed successfully: "+FullNameUser+"*", parse_mode="Markdown")
                     a = a + 1

                  except:
                     b = b + 1
                     time.sleep(1)
                     update.message.reply_text("*⚠️ Failed to place sell order: "+FullNameUser+"*", parse_mode="Markdown")

               if a > 0:
                  user.addorder(collection = "orders", TransactionDate = time_now(), Symbol = OrderSymbol, Stat = "SALE LIMIT WITH STOP LOSE", Quantity = QtyOrig, USDTAmount = USDTQty, Price = price1, Owenr = str(update.message.chat_id))

               update.message.reply_text("*✅ Successful Solds: "+str(a)+"\n\n⚠️ Sales Failed: "+str(b)+"*", parse_mode="Markdown")

            else:
               time.sleep(1)
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme6=9999

         if itme7 == 50:
            coin = str(update.message.text).upper()
            update.message.reply_text('*❓ Are You Sure? send yes or no*', parse_mode="Markdown")
         
         if itme7 == 51:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               deluser = user.deleteapi(collection = "api", Username = str(update.message.chat_id), Name = coin)
               if deluser != None:
                  update.message.reply_text("*✅ The account has been deleted successfully.*", parse_mode="Markdown")
               
               else:
                  update.message.reply_text("*⚠️ There is no account with this name.*", parse_mode="Markdown")
                  itme7=9999

            else:
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme7=9999

         if itme8 == 55:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               deluser = user.deleteallapi(collection = "api", Username = str(update.message.chat_id))
               update.message.reply_text("*✅ All accounts have been deleted successfully.*", parse_mode="Markdown")
            else:
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme8=9999
         
         if itme9 == 60:
            full_name = str(update.message.text).upper()
            eduser = user.findoneapi(collection = "api", Username = str(update.message.chat_id), Name = full_name)
            if eduser[0]>0 and eduser[0]<2:
               update.message.reply_text("*❓ Submit a new name*", parse_mode="Markdown")
            
            elif eduser[0]>1:
               update.message.reply_text("*⚠️ There is more than one account with the name you entered, delete one of them*", parse_mode="Markdown")
               itme9=9999

            else:
               update.message.reply_text("*⚠️ There is no account with the name you entered*", parse_mode="Markdown")
               itme9=9999
         
         if itme9 == 61:
            new_name = str(update.message.text).upper()
            update.message.reply_text('*❓ Are You Sure? send yes or no*', parse_mode="Markdown")

         if itme9 == 62:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               eduser = user.editapi(collection = "api", Username = str(update.message.chat_id), Name = full_name, new_info = new_name.upper())
               update.message.reply_text("*✅ The name has been updated successfully*", parse_mode="Markdown")

            else:
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme9=9999
         
         if itme10 == 65:
            full_name = str(update.message.text).upper()
            comment = user.findspecificcomment(collection = "comment", Username = str(update.message.chat_id), Name = full_name)
            if comment[1] > 0:
               update.message.reply_text("*⚠️ This name already exists, try another name*", parse_mode="Markdown")
               itme10=9999

            else:
               update.message.reply_text("*✳️ Enter the text you want to appear in your ad*", parse_mode="Markdown")

         if itme10 == 66:
            ads = str(update.message.text)
            user.insertcomment(collection = "comment", Username = str(update.message.chat_id), Comment = ads, Name = full_name, Date = time_now())
            update.message.reply_text("*🚨🚨 Ads are posted 2 times a week\n\n1️⃣ Day 1: By placing your ad in the comments of random Instagram posts related to trading\n\n2️⃣ Day 2: By placing your ad in a message on Instagram to random people interested in trading*", parse_mode="Markdown")
            update.message.reply_text("*✅ Your ad has been successfully added*`\n\n♻️ Ad results are automatically published in our channel 👉🏻 `*@botcrypto1*`\n\n🚨 If your ad does not appear within a week at most, talk to the bot developer 👉🏻` *@xx_070*", parse_mode="Markdown")

         if itme11 == 70:
            full_name = str(update.message.text).upper()
            specificcomment = user.findspecificcomment(collection = "comment", Username = str(update.message.chat_id), Name = full_name)
            if specificcomment[1]>0:
               update.message.reply_text("*✳️ Enter the text you want to appear in your ad*", parse_mode="Markdown")

            else:
               update.message.reply_text("*⚠️ There is no ad with the name you entered*", parse_mode="Markdown")
               itme11=9999

         if itme11 == 71:
            ads = str(update.message.text)
            user.editspecificcomment(collection = "comment", Username = str(update.message.chat_id), Name = full_name, new_info = ads)
            update.message.reply_text("*✅ Your ad has been successfully modified*`\n\n♻️ Ad results are automatically published in our channel 👉🏻 `*@botcrypto1*`\n\n🚨 If your ad does not appear within a day at most, talk to the bot developer 👉🏻` *@xx_070*", parse_mode="Markdown")
         
         if itme12 == 75:
            full_name = str(update.message.text).upper()
            specificcomment = user.findspecificcomment(collection = "comment", Username = str(update.message.chat_id), Name = full_name)
            if specificcomment[1]>0:
               update.message.reply_text('*❓ Are You Sure? send yes or no*', parse_mode="Markdown")

            else:
               update.message.reply_text("*⚠️ There is no ad with the name you entered*", parse_mode="Markdown")
               itme12=9999

         if itme12 == 76:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               user.deleteapi(collection = "comment", Username = str(update.message.chat_id), Name = full_name)
               update.message.reply_text("*✅ Ad has been removed successfully*", parse_mode="Markdown")

            else:
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme12=9999
         
         if itme13 == 80:
            confirmation = str(update.message.text).upper()
            if confirmation == "YES":
               user.deleteallapi(collection = "comment", Username = str(update.message.chat_id))
               update.message.reply_text("*✅ All ads removed successfully*", parse_mode="Markdown")

            else:
               update.message.reply_text("*OK  👍*", parse_mode="Markdown")
               itme13=9999

         itme += 1
         itme1 += 1
         itme2 += 1
         itme3 += 1
         itme4 += 1
         itme5 += 1
         itme6 += 1
         itme7 += 1
         itme8 += 1
         itme9 += 1
         itme10 += 1
         itme11 += 1
         itme12 += 1
         itme13 += 1

      elif acc[0] == "OFF":
         update.message.reply_text("*⚠️ The account is currently suspended 🔒, contact the bot developer @xx_070 ⚠️*", parse_mode="Markdown")

   else:
      name = '*📋 ACCOUNT \n\n📍 Salam ' + str(update.effective_user.first_name).upper() + '\n\n⛔️ You do not have an account with us at the moment, copy this ID *`'+str(update.message.chat_id)+'`* and give it to the bot developer.\n\n The official account of the bot developer @xx_070*'
      update.message.reply_text(name, parse_mode="Markdown")

updater = Updater(token, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("price", price))
dp.add_handler(CommandHandler("add_account", addapi))
dp.add_handler(CommandHandler("get_accounts", getapi))
dp.add_handler(CommandHandler("buy", buy))
dp.add_handler(CommandHandler("buy_limit", buylimit))
dp.add_handler(CommandHandler("sale", sale))
dp.add_handler(CommandHandler("sale_limit", salelimit))
dp.add_handler(CommandHandler("sale_limit_stop_lose", salelimitstop))
dp.add_handler(CommandHandler("get_orders", getorders))
dp.add_handler(CommandHandler("delete_user_account", deleteapi))
dp.add_handler(CommandHandler("delete_all_users_accounts", deletalleapi))
dp.add_handler(CommandHandler("edit_name_account", editapi))
dp.add_handler(CommandHandler("add_ads", addads))
dp.add_handler(CommandHandler("edit_ads", editads))
dp.add_handler(CommandHandler("delete_ad", deletead))
dp.add_handler(CommandHandler("delete_all_ads", deletalleads))
dp.add_handler(CommandHandler("get_ads", getads))
dp.add_handler(MessageHandler(Filters.text, handlmsg))
updater.start_polling()
updater.idle()