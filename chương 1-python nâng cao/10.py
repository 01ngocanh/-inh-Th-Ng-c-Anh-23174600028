class Diem:
    def __init__(self,x,y):
        self.x=x  
        self.y=y  
class Elip(Diem):
    def __init__(self,x,y,ban_kinh_a,ban_kinh_b):
        Diem.__init__(self,x,y)
        self.ban_kinh_a=ban_kinh_a  
        self.ban_kinh_b=ban_kinh_b 
    def tinh_dien_tich(self):
        return 3.14 * self.ban_kinh_a * self.ban_kinh_b
class DuongTron(Elip):
    def __init__(self,x,y,ban_kinh):
        Elip.__init__(self,x,y,ban_kinh,ban_kinh) 

diem=Diem(1,3)
print(f"Tọa độ điểm: ({diem.x},{diem.y})")
elip=Elip(3,2,4,6)
print(f"Diện tích elip: {elip.tinh_dien_tich()}")
duong_tron=DuongTron(0,0,2)
print(f"Diện tích đường tròn: {duong_tron.tinh_dien_tich()}")