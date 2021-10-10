import tkinter
import tkinter.messagebox

# Let's create the Tkinter window
window = tkinter.Tk()
window.title("Antivirus Response")

# Let's create an alert box with 'messagebox' function
tkinter.messagebox.showinfo("Alert Message", "Antivirus identified dangerous malware. Action needed.")

# Let's also create a question for the user and based upon the response [Yes or No Question] display a message.
response = tkinter.messagebox.askquestion("Antivirus Response", "Do you want to delete Operation System?")

# A basic 'if/else' block where if user clicks on 'Yes' then it returns 1 else it returns 0. For each response you will display a message with the help of 'Label' method.
if response == 0:
    tkinter.Label(window, text = "Operation System will be deleted in 20 seconds").pack()
else:
    tkinter.Label(window, text = "Operation System will be deleted in 20 seconds.").pack()

window.mainloop()
