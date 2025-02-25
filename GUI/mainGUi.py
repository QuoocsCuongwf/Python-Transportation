import tkinter as tk

class MainGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Main GUI")
        self.master.geometry("800x900")
        self.master.resizable(False, False)

        self.label = tk.Label(self.master, text="Hello World")
        self.label.pack()

        self.button = tk.Button(self.master, text="Click Me", command=self.click_me)
        self.button.pack()

    def click_me(self):
        self.label.config(text="Button Clicked")

root = tk.Tk()
app = MainGUI(root)
root.mainloop()
# End of GUI/mainGUi.py