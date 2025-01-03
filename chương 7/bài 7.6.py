import tkinter as tk

def dao_nguoc_chuoi():
    cua_so = tk.Tk()
    cua_so.title("Đảo ngược chuỗi")
    def validate():
        chuoi = nhap_chuoi.get()
        ket_qua.set(chuoi[::-1])  
   
    tk.Label(cua_so, text="Enter a word:").pack()
    nhap_chuoi = tk.Entry(cua_so)
    nhap_chuoi.pack()

    ket_qua = tk.StringVar()
    tk.Label(cua_so, textvariable=ket_qua).pack()

    tk.Button(cua_so, text="Validate", command=validate).pack()

    cua_so.mainloop()

dao_nguoc_chuoi()

