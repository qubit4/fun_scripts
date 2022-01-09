import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Antivirus Response")

tkinter.messagebox.showinfo(
    "Alert Message", "Antivirus identified dangerous malware. Action needed.")


response = tkinter.messagebox.askquestion(
    "Antivirus Response", "It is advised to delete OS now. Do you want to delete OS?")

if response == "yes":
    tkinter.Label(
        window, text="Operating system will be deleted in 30 seconds").pack()
else:
    tkinter.Label(
        window, text="Operating system will not be deleted.").pack()

window.mainloop()
