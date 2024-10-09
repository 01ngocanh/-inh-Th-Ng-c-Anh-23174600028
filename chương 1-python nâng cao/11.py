class TamGiac:
    def __init__(self, a, b, c):
        self.a=a 
        self.b=b 
        self.c=c 
    def tinh_chu_vi(self):
        return self.a+self.b+self.c
    def tinh_dien_tich(self):
        p=self.tinh_chu_vi() / 2  
        return (p*(p-self.a)*(p-self.b)*(p-self.c)) ** 0.5
class TamGiacCan(TamGiac):
    def __init__(self, canh_bang, canh_khac):
        TamGiac.__init__(self, canh_bang, canh_khac, canh_khac)
    def tinh_dien_tich(self):
        return (self.b*self.c) / 2 
class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        TamGiacCan.__init__(self, canh, canh)

tam_giac=TamGiac(3,4,5)
print(f"Chu vi tam giác: {tam_giac.tinh_chu_vi()}")
print(f"Diện tích tam giác: {tam_giac.tinh_dien_tich()}")
tam_giac_can=TamGiacCan(3,4)
print(f"Chu vi tam giác cân: {tam_giac_can.tinh_chu_vi()}")
print(f"Diện tích tam giác cân: {tam_giac_can.tinh_dien_tich()}")
tam_giac_deu=TamGiacDeu(5)
print(f"Chu vi tam giác đều: {tam_giac_deu.tinh_chu_vi()}")
print(f"Diện tích tam giác đều: {tam_giac_deu.tinh_dien_tich()}")