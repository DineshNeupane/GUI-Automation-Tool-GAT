# import tkinter module 
from tkinter import *
from tkinter.ttk import *
import pyautogui

master = Tk(className='GUI Automating Tool')

master.geometry("1000x300")

master.columnconfigure(0, weight=0)
master.columnconfigure(1, weight=2)
e1 = Entry(master, width=60)

e2 = Entry(master, width=30)

e3 = Entry(master, width=30)

e4 = Entry(master, width=30)

path = Label(master, text="Path", font=("bold", 10))
lag = Label(master, text="Forward Lag (in seconds) (5 seconds +)", font=("bold", 10))
iteration_interval = Label(master, text="Iteration Interval(in minutes)", font=("bold", 10))
iteration_count = Label(master, text="Iteration Count", font=("bold", 10))

def divideByN(data, n):
    return [data[i * n: (i + 1) * n] for i in range(len(data) // n)]


def startClicking():
    itr_int = int(e3.get())
    itr_count = int(e4.get())

    s1 = e1.get()
    l1 = s1.split(',')
    l2 = []
    for i in l1:
        l2.append(int(i))
    fl = divideByN(l2, 2)
    master.quit()
    for item in fl:
        pyautogui.moveTo(item[0], item[1], 2)
        pyautogui.click(item[0], item[1], 1, 1, button='left')
        pyautogui.PAUSE = 2


    # for i in range(itr_count):
    # time.sleep(itr_int*60)


b1 = Button(master, text="Start Operating", command=startClicking)
b2 = Button(master, text="Exit", command=startClicking)
# this will arrange entry widgets
path.grid(row=0, column=1, pady=2)
e1.grid(row=1, column=1, pady=2)

lag.grid(row=2, column=1, pady=2)
e2.grid(row=3, column=1, pady=2)

iteration_interval.grid(row=4, column=1, pady=2)
e3.grid(row=5, column=1, pady=2)

iteration_count.grid(row=6, column=1, pady=2)
e4.grid(row=7, column=1, pady=2)

b1.grid(row=8, column=1, pady=2)


# b1.grid(row=8, column=2, pady=2)
# infinite loop which can be terminated by keyboard 
# or mouse interrupt



mainloop()
