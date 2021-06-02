import tkinter as tk
from tkinter import ttk

screen = tk.Tk()

sunday = []
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []


def addHour(day):
    exec("global " + day + "EntrysNeedToPack")
    exec(day + ".append(ttk.Entry(screen, textvariable=tk.StringVar()))")
    exec(day + "[-1].grid(row=daysToPack['" + day +
         "EntrysNeedToPack'] + 2, column=" + day + "Column)")
    exec("daysToPack['" + day + "EntrysNeedToPack'] += 1")
    exec("print(daysToPack['" + day + "EntrysNeedToPack'])")


def printMarechet():
    subjectsInSunday = []
    subjectsInMonday = []
    subjectsInTuesday = []
    subjectsInWednesday = []
    subjectsInThursday = []
    subjectsInFriday = []
    for i in sunday:
        subjectsInSunday.append(i.get())
    for i in monday:
        subjectsInMonday.append(i.get())
    for i in tuesday:
        subjectsInTuesday.append(i.get())
    for i in wednesday:
        subjectsInWednesday.append(i.get())
    for i in thursday:
        subjectsInThursday.append(i.get())
    for i in friday:
        subjectsInFriday.append(i.get())

    print("weekly_cal = (" + str(subjectsInSunday).replace(
        "[", "(").replace("]", ")").replace("'", "") + ",# sunday")
    print(str(subjectsInMonday).replace(
        "[", "(").replace("]", ")").replace("'", "") + ",# monday")
    print(str(subjectsInTuesday).replace(
        "[", "(").replace("]", ")").replace("'", "") + ",# tuesday")
    print(str(subjectsInWednesday).replace(
        "[", "(").replace("]", ")").replace("'", "") + ",# wednesday")
    print(str(subjectsInThursday).replace(
        "[", "(").replace("]", ")").replace("'", "") + ",# thursday")
    print(str(subjectsInFriday).replace(
        "[", "(").replace("]", ")").replace("'", "") + ")" + "# friday")

    print("string_cal = (" +
          str(subjectsInSunday).replace("[", "(").replace("]", ")") + ",# sunday")
    print(str(subjectsInMonday).replace(
        "[", "(").replace("]", ")") + ",# monday")
    print(str(subjectsInTuesday).replace(
        "[", "(").replace("]", ")") + ",# tuesday")
    print(str(subjectsInWednesday).replace(
        "[", "(").replace("]", ")") + ",# wednesday")
    print(str(subjectsInThursday).replace(
        "[", "(").replace("]", ")") + ",# thursday")
    print(str(subjectsInFriday).replace(
        "[", "(").replace("]", ")") + ")" + "# friday")


ttk.Button(screen, text="add hour on friday",
           command=lambda: addHour("friday")).grid(row=0, column=0)
ttk.Button(screen, text="add hour on thursday",
           command=lambda: addHour("thursday")).grid(row=0, column=1)
ttk.Button(screen, text="add hour on wednesday",
           command=lambda: addHour("wednesday")).grid(row=0, column=2)
ttk.Button(screen, text="add hour on tuesday",
           command=lambda: addHour("tuesday")).grid(row=0, column=3)
ttk.Button(screen, text="add hour on monday",
           command=lambda: addHour("monday")).grid(row=0, column=4)
ttk.Button(screen, text="add hour on sunday",
           command=lambda: addHour("sunday")).grid(row=0, column=5)
ttk.Button(screen, text="print marechet",
           command=printMarechet).grid(row=0, column=6)

tk.Label(screen, text="friday").grid(row=1, column=0)
tk.Label(screen, text="thursday").grid(row=1, column=1)
tk.Label(screen, text="wednesday").grid(row=1, column=2)
tk.Label(screen, text="tuesday").grid(row=1, column=3)
tk.Label(screen, text="monday").grid(row=1, column=4)
tk.Label(screen, text="sunday").grid(row=1, column=5)

daysToPack = {
    "sundayEntrysNeedToPack": 0,
    "mondayEntrysNeedToPack": 0,
    "tuesdayEntrysNeedToPack": 0,
    "wednesdayEntrysNeedToPack": 0,
    "thursdayEntrysNeedToPack": 0,
    "fridayEntrysNeedToPack": 0
}

fridayColumn = 0
thursdayColumn = 1
wednesdayColumn = 2
tuesdayColumn = 3
mondayColumn = 4
sundayColumn = 5

screen.mainloop()
