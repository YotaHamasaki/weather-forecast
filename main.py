import datetime
import urllib.request as req
import requests
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import TextSendMessage

def send_line(ddd, telop, highlists, lowlists, row):
    CHANNEL_ACCESS_TOKEN = "6RU+xZXYgAoHAc8WWX2357evzm9DNVE+SM4fYNV5fT1tFGDAdpXixNhI5eQ8dYRNeaqZ11IILXS6emjTG3c5K67OTs9uYddPbK+6j4flYqAUaXJPECRVxa6DIZqhreoZBElc/aFgczV4kEij7FXk3QdB04t89/1O/w1cDnyilFU="
    USER_ID = "Uaa5346493dbf7a5692cd56a446edc781"
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
    messages = TextSendMessage(text=ddd.text + "\n" + telop + "\n" + "最高　" + highlists.text + "\n" + "最低　" + lowlists.text + "\n"+ "---------" + "\n" +row[1].text +"\n" + "~6  : " + row[3].text + "\n" + "~12 : " + row[5].text +"\n" + "~18 : " + row[7].text +"\n" + "~24 : " + row[9].text)
    line_bot_api.push_message(USER_ID, messages=messages)
    
def main():
    #天気サイトから欲しい情報を取得する
    url2 = "https://tenki.jp/forecast/3/16/4410/13112/"   #欲しい情報があるURLを指定
    res = requests.get(url2)                              #上記URL情報を取得する
    soup = BeautifulSoup(res.content, 'html.parser')      #取得した情報をhtmlで解析する

    # 以下各種情報を取得
    ddd = soup.find(class_="left-style")                  

    telop = soup.find("p", class_="weather-telop").string

    highlists = soup.find("dd",class_="high-temp temp")

    lowlists = soup.find("dd",class_="low-temp temp")

    ttt = soup.find(class_="rain-probability")

    row=[]
    for t in ttt:
        row.append(t)

    send_line(ddd, telop, highlists, lowlists, row)

if __name__ == "__main__":
    main()
