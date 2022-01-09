import tkinter
from tkinter import messagebox
import subprocess


while True:
    window = tkinter.Tk()
    window.title("Antivirus Response")

    tkinter.messagebox.showinfo(
        "Alert Message", "Antivirus identified dangerous malware. Action needed.")

    response = tkinter.messagebox.askquestion(
        "Antivirus Response", "It is advised to restart computer. Do you want to restart now?")

    if response == "yes":
        subprocess.run(["reboot"])
    else:
        continue

    window.mainloop()
