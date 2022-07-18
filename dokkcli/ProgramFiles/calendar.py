
import calendar
from tkinter import *
from turtle import screensize


def StartCalendar():
    global year_field
    global new
    new = Tk()
    new.config(background='black')
    new.title("DokkCLI CALENDAR")
    new.geometry("400x140")
    cal = Label(new, text="DOKKCLI CALENDAR", fg = "white", bg='black',font=("times", 28, "bold"))
    #Label for enter year
    year = Label(new, text="Enter year", fg = 'white', bg='black')
    #text box for year input
    year_field=Entry(new)
    button = Button(new, text='Show Calendar',fg='white',bg='black',command=showCalender)
    #adjusting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    new.mainloop()
#This function displays calendar for a given year
def showCalender():
    gui = Tk()
    gui.config(background='black')
    gui.title("DOKKCLI Calendar")
    gui.geometry("550x580")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    new.destroy()
    



