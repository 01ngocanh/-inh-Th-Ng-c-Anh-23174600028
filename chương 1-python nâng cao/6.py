class NgamXep:
    def __init__(self, dung_luong):
        self.stack= [] 
        self.dung_luong =dung_luong  
    def isEmpty(self):
        return len(self.stack)== 0
    def isFull(self):
        return len(self.stack) >= self.dung_luong
    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")
        else:
            self.stack.append(value)  
            print(f"Đã thêm {value} vào ngăn xếp.")
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử!")
            return None
        value = self.stack.pop()  
        print(f"Đã lấy {value} ra khỏi ngăn xếp.")
        return value
    def count(self):
        return len(self.stack)
    
dung_luong=5
ngam_xep =NgamXep(dung_luong)   
for i in range(dung_luong):
    ngam_xep.push(float(i))
print(f"Số phần tử hiện có trong ngăn xếp: {ngam_xep.count()}")
for _ in range(dung_luong + 1):
    print(f"Phần tử lấy ra: {ngam_xep.pop()}")
print(f"Số phần tử hiện có trong ngăn xếp: {ngam_xep.count()}")
