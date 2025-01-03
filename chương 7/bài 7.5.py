import tkinter as tk
from tkinter import PhotoImage

def hien_thi_anh():
    cua_so = tk.Tk()
    cua_so.title("Chương trình xem ảnh")

    try:
        anh = PhotoImage(file="anh.jpg") 
        label_anh = tk.Label(cua_so, image=anh)
        label_anh.pack()
    except Exception as e:
        tk.Label(cua_so, text=f"Lỗi: {e}").pack()

    cua_so.mainloop()



