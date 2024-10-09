class HinhChuNhat:
    def __init__(self,dai=0, rong=0):
        self.dai=dai
        self.rong=rong
    def nhap_du_lieu(self):
        self.dai=float(input("nhập độ dài cạnh t1: "))
        self.rong=float(input("nhập độ dài cạnh t2: "))
    def chuvi(self):
        return 2 *(self.dai+self.rong)
    
    def dientich(self):
        return self.dai*self.rong

    def in_thong_tin(self):
        print(f"Chiều dài: {self.dai}")
        print(f"Chiều rộng: {self.rong}")
        print(f"Chu vi: {self.chuvi()}")
        print(f"Diện tích: {self.dientich()}")

hinh_chu_nhat=HinhChuNhat()
hinh_chu_nhat.nhap_du_lieu()
hinh_chu_nhat.in_thong_tin()
