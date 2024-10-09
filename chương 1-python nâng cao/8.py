class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day, self.month, self.year=day, month, year
    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")
    def next(self):
        self.day+= 1
        days_in_month=[31, 29 if self.year%4==0 and (self.year % 100!=0 or self.year%400==0) else 28,31,30,31,30,31,31,30,31,30,31]
        if self.day > days_in_month[self.month - 1]:
            self.day, self.month = 1, self.month + 1
            if self.month > 12:
                self.month, self.year = 1, self.year + 1

class Employee:
    def __init__(self, name, birth_date, start_date):
        self.name, self.birth_date, self.start_date = name, birth_date, start_date
    def display(self):
        print(f"Họ tên: {self.name}\nNgày sinh: ", end="")
        self.birth_date.display()
        print("Ngày vào công ty: ", end="")
        self.start_date.display()
employee=Employee("Đinh Thị Ngọc Anh", Date(12,6,2005), Date(11,9,2018))
employee.display()
