import tkinter as tk
from tkinter import messagebox
def gui_thong_tin():
    ten = hop_ten.get()
    id_sv = hop_id.get()
    mat_khau = hop_mat_khau.get()
    messagebox.showinfo("Thông tin sinh viên", f"Tên: {ten}\nID: {id_sv}\nMật khẩu: {mat_khau}")

cua_so = tk.Tk()
cua_so.title("Điền thông tin sinh viên")

tk.Label(cua_so, text="Tên sinh viên:").pack()
hop_ten = tk.Entry(cua_so)
hop_ten.pack()

tk.Label(cua_so, text="ID sinh viên:").pack()
hop_id = tk.Entry(cua_so)
hop_id.pack()

tk.Label(cua_so, text="Mật khẩu:").pack()
hop_mat_khau = tk.Entry(cua_so, show="*")
hop_mat_khau.pack()

nut_gui = tk.Button(cua_so, text="Gửi", command=gui_thong_tin)
nut_gui.pack()

cua_so.mainloop()
