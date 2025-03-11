import tkinter as tk
import sys
sys.path.append('D:/code/python-transportation/train-model-YOLOv10')
import webcam

gui = tk.Tk()
gui.title("My GUI")
gui.geometry("1200x700")
menuButton = tk.Button(gui, text="Menu", width=10, height=2, bg="blue", fg="white")
menuButton.pack()
def start_camera():
    webcam.load_gui(gui,label_camera)
button_camera = tk.Button(gui, text="Camera", width=10, height=2, bg="blue", fg="white", command=start_camera)
button_camera.pack()
label_camera=tk.Label(gui)
label_camera.place(x=50,y=80)
gui.mainloop()
