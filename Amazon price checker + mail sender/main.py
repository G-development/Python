import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.it/Apple-iPhone-11-Pro-64GB/dp/B07XS48L9C?th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

def checkPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").getText()
    price = soup.find(id="priceblock_ourprice").getText()
    conv_price = float(price[0:5])

    print (title.strip())
    print (conv_price)

    if(conv_price<1200):
        sendMail()

def sendMail():
    print ("Funzione sendMail() usando Gmail")

    username = "cuozzogiovanni03"
    password = "Giovils3520"
    destinatario = "cuozzogiovanni03@gmail.com"
    oggetto = "Price fell down!"
    messaggio = f"Il prezzo è diminuito! + str(title.strip()) + str(conv_price)"
    contenuto = f"Subject: {oggetto} \n\n Go check Amazon, \n{URL}"
    print("Sto effettuando la connessione col Server...")
    email = smtplib.SMTP("smtp.gmail.com",587)
    email.ehlo()
    email.starttls()
    email.login(username,password)
    print("Sto inviando...")
    email.sendmail(username, destinatario, contenuto)
    email.quit()
    print("Messaggio Inviato!")

while(True):
    checkPrice()
    time.sleep(60*60*24) #check once a day 
