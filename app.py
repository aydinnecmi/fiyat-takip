import requests
from bs4 import BeautifulSoup 
import smtplib


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}



def check_price(url,target):
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    content = soup.find(id ='offering-price').get('content')
    price = float(content) 

    if(price < target):        
        return send_mail(url,content)

    else:
        print("İndirim yok")


def send_mail(url,content):
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
        return True
        
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()








    

