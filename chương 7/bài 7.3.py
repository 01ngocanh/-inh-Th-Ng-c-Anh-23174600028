import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Thay đổi kiểu nhãn")
nhan = tk.Label(
    cua_so,
    text="Nhãn với kiểu chữ tùy chỉnh",
    font=("Arial", 16, "bold")
)
nhan.pack()
cua_so.mainloop()
