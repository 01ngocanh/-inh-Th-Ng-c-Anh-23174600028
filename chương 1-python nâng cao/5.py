class NgamXep:
    def __init__(self, dung_luong):
        self.dung_luong=dung_luong  
        self.stack =[] 
        self.top =-1
    def isEmpty(self):
        return self.top== -1

    def isFull(self):
        return self.top >=self.dung_luong- 1
    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")
        else:
            self.stack.append(value)  
            self.top +=1 
            print(f"Đã thêm {value} vào ngăn xếp.")

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử!!")
            return None
        else:
            value= self.stack.pop()  
            self.top -= 1
            print(f"Đã lấy {value} ra khỏi ngăn xếp.")
            return value
    def count(self):
        return self.top + 1 
    def __del__(self):
        print("Đối tượng NgamXep đã bị huỷ.")

dung_luong = 5
ngam_xep = NgamXep(dung_luong)   
for i in range(dung_luong):
    ngam_xep.push(float(i))
print(f"Số phần tử hiện có trong ngăn xếp: {ngam_xep.count()}")
for i in range(dung_luong + 1):
    print(f"Phần tử lấy ra: {ngam_xep.pop()}")
print(f"Số phần tử hiện có trong ngăn xếp: {ngam_xep.count()}")
