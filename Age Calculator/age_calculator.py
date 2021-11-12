'''A simple age calculator in python'''
'''age_calculator.py'''
from tkinter import *
from tkinter import ttk
from datetime import date
from tkinter import messagebox

class Age_Calculator:
    def __init__(self, root):
        self.window = root
        self.window.title("Age Calculator")
        self.window.geometry("640x240+0+0")

        self.month_list = ['January', 'February', 'March', 'April', 'May', 
        'June', 'July', 'August', 'September', 'October', 'November', 'December']

        self.label1 = Label(self.window, text="Date of Birth", 
        font=("times new roman",20,"bold")).place(x=90, y=30)
        self.label2 = Label(self.window, text="Age at the date of", 
        font=("times new roman",20,"bold")).place(x=40, y=80)

        # Taking the birth month
        self.month1 = StringVar()
        self.month_combo = ttk.Combobox(self.window, width= 10,
        textvariable=self.month1)
        self.month_combo['values'] = self.month_list
        self.month_combo.current(0)
        self.month_combo.place(x = 250, y = 35)

        # Birth date
        self.date1 = StringVar()
        self.date_entry = Entry(self.window, 
        textvariable=self.date1, width=10)
        self.date_entry.insert(0, "1")
        self.date_entry.place(x = 360, y = 35)

        # Birth Year
        self.year1 = StringVar()
        self.year_entry = Entry(self.window, textvariable=self.year1, width=10)
        self.year_entry.insert(0, "2021")
        self.year_entry.place(x= 470, y = 35)

        # Taking the current month
        self.month2 = StringVar()
        self.month2_combo = ttk.Combobox(self.window, width= 10,
        textvariable=self.month2)
        self.month2_combo['values'] = self.month_list
        self.month2_combo.current(0)
        self.month2_combo.place(x = 250, y = 87)

        # Current Date
        self.date2 = StringVar()
        self.date2_entry = Entry(self.window, 
        textvariable=self.date2, width=10)
        self.date2_entry.insert(0, "1")
        self.date2_entry.place(x = 360, y = 87)

        # Current Year
        self.year2 = StringVar()
        self.year2_entry = Entry(self.window, 
        textvariable=self.year2, width=10)
        self.year2_entry.insert(0, "2021")
        self.year2_entry.place(x= 470, y = 87)

        self.calculate_button = Button(self.window, text="Calculate",bg="green", 
        fg="white", font=("times new roman",12,"bold"),
        command=self.calculate_age).place(x = 270, y=150)
    
    def LeapYear(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def NumOfDays(self, date1, date2):
        return (date2 - date1).days

    
    def calculate_age(self):
        self.Months = {
            1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31,
            8:31, 9:30, 10:31, 11:30, 12:31}

        self.month_sequence = {
        "January":1, "February":2, "March":3, "April":4, "May":5, 
        "June":6, "July":7,"August":8, "September":9, "October":10, 
        "November":11, "December":12}

        try:
            day1 = int(self.date1.get())
            mon1 = int(self.month_sequence[self.month_combo.get()])
            year1=  int(self.year1.get())

            day2 = int(self.date2.get())
            mon2 = int(self.month_sequence[self.month2_combo.get()])
            year2=  int(self.year2.get())

            # Converting given dates into date format
            date1 = date(year1, mon1, day1)
            date2 = date(year2, mon2, day2)

            # Calculating age in days
            TotalDays = self.NumOfDays(date1, date2)

            # If Birth year and the current year is same
            if year1 == year2:
                month = TotalDays/30
                day = TotalDays%30
                year = 0
            else:
                year = TotalDays/365
                month = (TotalDays%365)/30

                # Check if the given year is leap year or not.
                # If Yes, then Make the total number of days in the month of 
                # February 29 instead of 28.
                if self.LeapYear(year1):
                    self.Months[2] = 29
                    
                if day2 >= day1:
                    day = day2 - day1
                # If the current month is February and the current year is leap 
                # year or not
                elif mon2 == 2 & (self.LeapYear(year2) or (not self.LeapYear(year2))):
                    year = year - 1
                    month = 11
                    # prevMonth stores total days of the (current month - 1)
                    prevMonth = self.Months[mon2 - 1]
                    days = prevMonth - day1 + day2
                    day = days
                else:
                    prevMonth = self.Months[mon2 - 1]
                    days = prevMonth - day1 + day2
                    day = days
                    month = month - 1
            
            day = int(day)
            month = int(month)
            year = int(year)

            messagebox.showinfo("Your Age",f"{year} years {month} months {day} days")

        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")

if __name__ == "__main__":
    root = Tk()
    obj = Age_Calculator(root)
    root.mainloop()