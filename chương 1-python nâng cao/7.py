class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day, self.month, self.year=day, month, year
    def display(self):
        print(f"Ngày: {self.day}/{self.month}/{self.year}")
    def is_leap_year(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)
    def next(self):
        self.day +=1
        days_in_month=[31, 29 if self.is_leap_year() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day > days_in_month[self.month-1]:
            self.day, self.month = 1, self.month+ 1
            if self.month > 12:
                self.month, self.year=1, self.year+ 1
date = Date(27, 11, 2024)
date.display()
date.next()
date.display()
