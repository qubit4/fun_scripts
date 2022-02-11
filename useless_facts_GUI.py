import tkinter as tk
from tkinter import *
import requests

# window specifications
root = Tk()
root.geometry("350x280")
root.title("random_fact_generator")
T = Text(root, height=10, width=40)

# data specifications
api_url = "https://uselessfacts.jsph.pl//random.json?language=en"
response = requests.get(api_url)
data = response.json()
fact = data["text"]


# on clicking "New Fact" the window is cleared and new data fetched and printed
def get_fact():
    T.delete("1.0", tk.END)

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        fact = data['text']
    else:
        fact = "Failed to read data. Status code is : {}".format(
            response.status_code)

    T.insert(tk.END, fact)


b1 = Button(root, text="New Fact", command=get_fact)
b2 = Button(root, text="Exit", command=root.destroy)


T.pack()
b1.pack()
b2.pack()
tk.mainloop()
