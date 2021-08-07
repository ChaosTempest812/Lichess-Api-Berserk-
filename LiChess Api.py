import berserk
from tkinter import *
import requests
from matplotlib import pyplot as plt
import numpy as np


root = Tk()
root.geometry("350x350")
root.title("lichess API")

def generate_chart(entry):
    API_TOKEN = "f1KDsPUC2ucy20Xc"
    session = berserk.TokenSession(API_TOKEN)
    client = berserk.Client(session=session)
    data = client.users.get_public_data(username = entry)
        
    bullet_rating = data["perfs"]["bullet"]["rating"]
    blitz_rating = data["perfs"]["blitz"]["rating"]
    rapid_rating = data["perfs"]["rapid"]["rating"]
    classical_rating = data["perfs"]["classical"]["rating"]
    modes = ["Bullet", "Blitz", "Rapid", "Classical"]
    ratings = [bullet_rating, blitz_rating, rapid_rating, classical_rating]

    plt.bar(modes, ratings)
    plt.show()
        
def search(entry):
    API_TOKEN = "f1KDsPUC2ucy20Xc"
    try:
        session = berserk.TokenSession(API_TOKEN)
        client = berserk.Client(session=session)
        data = client.users.get_public_data(username = entry)

        status = data["online"]
        status = str(status)
        if status == "True":
            message = "is online"
        if status == "False":
            message = "is not online"
        
        finaltext = Label(text="Username: ", bg="#43bcd1")
        finaltext.place(relx = 0.11, rely = 0.3)

        finaltext2 = Label(text = entry, bg="#43bcd1")
        finaltext2.place(relx = 0.35, rely = 0.3)

        finaltext3 = Label(text = entry, bg="#43bcd1")
        finaltext3.place(relx = 0.11, rely = 0.4)
            
        finaltext4 = Label(text = message, bg="#43bcd1")
        finaltext4.place(relx = 0.25, rely = 0.4)
        
    except Exception as e:
        finaltext = Label(text="Error...", bg="#43bcd1")
        finaltext.place(relx = 0.11, rely = 0.3)
        

frame = Frame(root, bg = "#43bcd1", bd=5)
frame.place(relx=0.1, rely=0.1, relwidth=0.85, relheight=0.15)

Search_Bar = Entry(frame, border = 3, font=40)
Search_Bar.place(relx = 0, rely = 0, relheight = 1, relwidth = 0.6)

Search_Button = Button(frame, text="Search", command=lambda: search(Search_Bar.get()))
Search_Button.place(relx = 0.7, rely = 0 , relwidth = 0.3, relheight = 1)

fillerlabel = Label(bg="#43bcd1")
fillerlabel.place(relx = 0.1, rely = 0.27, relwidth = 0.85, relheight = 0.5)

Chart_Button = Button(text="Generate Rating Chart", command=lambda: generate_chart(Search_Bar.get()))
Chart_Button.place(relx = 0.35, rely = 0.65)

root.mainloop
