import tkinter as tk

def tinh_tong():
    cua_so = tk.Tk()
    cua_so.title("Tính tổng từ 1 đến N")

    def tinh():
        try:
            n = int(nhap_so.get())
            if n < 1:
                ket_qua.set("Vui lòng nhập số nguyên dương!")
            else:
                tong = sum(range(1, n + 1))
                ket_qua.set(f"Tổng: 1 + 2 + ... + {n} = {tong}")
        except ValueError:
            ket_qua.set("Vui lòng nhập một số nguyên hợp lệ!")

    tk.Label(cua_so, text="Nhập N:").pack()
    nhap_so = tk.Entry(cua_so)
    nhap_so.pack()

    ket_qua = tk.StringVar()
    tk.Label(cua_so, textvariable=ket_qua).pack()

    tk.Button(cua_so, text="Tính tổng", command=tinh).pack()

    cua_so.mainloop()

tinh_tong()
