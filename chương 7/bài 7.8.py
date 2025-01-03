import tkinter as tk

def liet_ke_uoc():
    cua_so = tk.Tk()
    cua_so.title("Liệt kê các ước của N")

    def validate():
        try:
            n = int(nhap_so.get())
            if n <= 0:
                ket_qua.set("Vui lòng nhập số nguyên dương!")
            else:
                uoc = [str(i) for i in range(1, n + 1) if n % i == 0]
                ket_qua.set("Các ước của N: " + ", ".join(uoc))
        except ValueError:
            ket_qua.set("Vui lòng nhập số nguyên hợp lệ!")

    tk.Label(cua_so, text="Nhập số nguyên N:").pack()
    nhap_so = tk.Entry(cua_so)
    nhap_so.pack()
    ket_qua = tk.StringVar()
    tk.Label(cua_so, textvariable=ket_qua).pack()
    tk.Button(cua_so, text="Xác nhận", command=validate).pack()
    cua_so.mainloop()

liet_ke_uoc()
