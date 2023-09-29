from tkinter import *


window = Tk()
window.title("Fake News Detector")
window.geometry('700x700')
window.configure(bg='white')

# title
lb1 = Label(window, text="Paste your news article below and confirm it's truth",
            font=("Arial Bold", 14), background='white')
lb1.grid(column=0, row=1)

# variable that stores news article
news_data = Entry(window, width=100)
news_data.grid(column=0, row=2)
news_data.focus()

lb2 = Label(window, font=("Arial", 10), background='white')
lb2.grid(column=0, row=8)

# api function


def print_something():  # place holder
    lb2.configure(text=news_data.get())


# verify button
btn = Button(window, text="VERIFY",
             command=print_something, background='white')
btn.grid(column=0, row=7)


# used to run the window
window.mainloop()
