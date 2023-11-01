from tkinter import *
from time import strftime, gmtime

myWindow = Tk()
myWindow.title('New York Time')

# Function to get New York time
def get_new_york_time():
    new_york_time = gmtime()
    return strftime('%I:%M:%S %p', new_york_time)  # Format to 12-hour time with AM/PM

def time():
    myTime = get_new_york_time()
    clock.config(text=myTime)
    clock.after(1000, time)

clock = Label(myWindow, font=('arial', 40, 'bold'), background='dark green', foreground='white')
clock.pack(anchor='center')
time()
myWindow.mainloop()
