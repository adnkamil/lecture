
from tkinter import *
from time import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

photoList = [None] * 9
num = 0
name = fnameList[0]

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file="GIF/"+ fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photoList
    nameImage.config(text=fnameList[num]) 

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file= "GIF/"+ fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    nameImage.config(text=fnameList[num]) 

window = Tk()
window.geometry("700x500")
window.title("View Photo Album")

btnPrev = Button(window, text="<<Previous", command=clickPrev )
nameImage = Label(window, text = name)    #declaration name immage
btnNext = Button(window, text="Next >>", command=clickNext)


photo = PhotoImage(file ="GIF/"+fnameList[0])
pLabel = Label(window, image= photo)

btnPrev.place(x = 250, y = 10)
nameImage.place(x = 335, y = 10)  # widget label name location
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()