from tkinter import *
window1 = Tk()
text1 = "Tkinter Change Label Text Example"
def counter():
    global text1
    label1.config(text = text1)
button1 = Button(window1,
                text = "Update Text",
                command = counter)
label1 = Label(window1,
                text = "Tkinter Change Label Text")
label1.pack()
button1.pack()
window1.mainloop()