import tkinter as tk
from tkinter import *
import requests


root = Tk()
root.geometry("400x300")
root.title("API random useless fact")

T = Text(root, height = 10, width = 40)

l = Label(root, text = "Fact")
l.config(font = ("Courier", 14))

api_url = "https://uselessfacts.jsph.pl//random.json?language=en"
r = requests.get(api_url)
data = r.json()
fact = data["text"]

def get_fact():
    r = requests.get(api_url)
    if r.status_code == 200:
      data = r.json()
      fact = data['text']
    else:
      fact = f' Failed to read fact data. status code is : {r.status_code}'
    T.delete('1.0', tk.END)
    T.insert(tk.END, fact)


b1 = Button(root, text = "Next", command = get_fact)
b2 = Button(root, text = "Exit", command = root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

T.insert(tk.END, fact)

tk.mainloop()
