from tkinter import *
from app import check_price

root = Tk()
root.title("Fiyat Takip")
root.geometry('500x250')

status = False
timeloop = 1000

def scanning():
    if status :
        print("Kontrol ediliyor...")
        url = urlEntry.get()
        target = float(targetEntry.get())
        check = check_price(url, target)
        if check :
            stopApp()
            print("Mail gönderildi")
        root.after(timeloop,scanning)



def startApp():
    global status
    status = True
    exeButton.config(text='DURDUR',command=stopApp)
    scanning()

def stopApp():
    global status
    status = False
    exeButton.config(text='BASLAT',command=startApp)


global urlLabel
urlLabel = Label(root, text='HEDEF LİNK')
urlLabel.pack(pady=10)

global urlEntry
urlEntry = Entry(root, width=40)
urlEntry.pack()


global targetLabel
targetLabel = Label(root, text='FİYAT')
targetLabel.pack(pady=10)

global targetEntry
targetEntry = Entry(root, width=40)
targetEntry.pack()

global exeButton
exeButton = Button(root,text='BASLAT',command=startApp,width=20,height=2)
exeButton.pack(pady=10) #pady=10 boşluk bırakmak için kullanılır

root.mainloop() 