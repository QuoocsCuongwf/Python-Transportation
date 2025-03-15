import tkinter as tk
import sys
sys.path.append('D:/code/python-transportation/train-model-YOLOv10')
import webcam

# Tạo cửa sổ chính
gui = tk.Tk()
gui.title("My GUI")
gui.geometry("1200x700")

# Tạo các khung (Frame) để sắp xếp các thành phần giao diện
left_frame = tk.Frame(gui, width=800, height=700)
left_frame.pack(side="left")
right_frame = tk.Frame(gui, width=400, height=700, bg="blue")
right_frame.pack(side="right")

# Cấu hình lưới cho right_frame
right_frame.columnconfigure(0, weight=1)
right_frame.columnconfigure(1, weight=1)
right_frame.rowconfigure(0, weight=1)
right_frame.rowconfigure(1, weight=1)

# Tạo nhãn để hiển thị hình ảnh từ camera và sắp xếp bằng .place()
label_camera = tk.Label(left_frame)
label_camera.place(x=50, y=80)

webcam.load_gui(gui, label_camera,right_framez)

# Tạo nhãn để hiển thị giá trị biển số xe và sắp xếp bằng .grid()

# Chạy vòng lặp chính
gui.mainloop()
