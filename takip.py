import requests
from bs4 import BeautifulSoup 
import smtplib
import time
url = 'https://www.hepsiburada.com/oppo-realme-7-pro-128-gb-realme-turkiye-garantili-p-HBV00000YE30Y'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}



def check_price():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id ='offering-price').get('content')
    price = float(title)
    print(title)

    if(price < 4000):
        
        send_mail()
    else:
        print("İndirim yok")


def send_mail():
    sender = 'asaydinnecmi@gmail.com'
    reciever = 'necmi_as1@hotmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender,'lzpbsctwwolqssor')
        subject = ("Istedigin fiyata dustu")
        body = ("Bu linkten gidebilirisin: " + url)
        mailContent = f"To:{reciever}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender,reciever,mailContent)
        print("Mail gonderildi")
        
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

while(True):

    check_price()
    time.sleep(60*60) #Bir saatlik zaman aralığı






    

