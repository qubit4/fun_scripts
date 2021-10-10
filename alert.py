import tkinter
import tkinter.messagebox


window = tkinter.Tk()
window.title("Antivirus Response")

tkinter.messagebox.showinfo("Alert Message", "Antivirus identified dangerous malware. Action needed.")


response = tkinter.messagebox.askquestion("Antivirus Response", "Do you want to delete Operation System?")

if response == 0:
    tkinter.Label(window, text = "Operation System will be deleted in 20 seconds").pack()
else:
    tkinter.Label(window, text = "Operation System will be deleted in 20 seconds.").pack()

window.mainloop()
