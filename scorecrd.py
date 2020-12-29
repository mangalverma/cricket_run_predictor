from tkinter import *
import csv
import os
# create a root window.
def getscore():
    filename = 'data.csv'
    top = Tk()
    w = top.winfo_screenwidth()
    h = top.winfo_screenheight()
    top.geometry(f"{int(w / 3)}x{int(h / 4)}")
    # create listbox object
    listbox = Listbox(top, height=h//3,
                      width=w//3,
                      bg="orange",
                      activestyle='dotbox',
                      font="calibre",
                      fg="Black")

    # Define the size of the window.

    # Define a label for the list.
    label = Label(top, text=" Scorecard", bg = "orange", font = ('calibre', 10, 'bold'), borderwidth = 2)

    # insert elements by their
    # index and names.
    listbox.insert(0, "RUN" +"                         "+"BALL")
    file_exists = os.path.isfile(filename)
    with open(filename, 'rt') as csvfile:
        data = csv.reader(csvfile)
        data=list(data)
        for row in range(1,len(data)):
            listbox.insert(row,data[row][0]+"                         "+data[row][1])

        label.pack()
        listbox.pack()
        top.mainloop()

        if not file_exists:
            print("scorecard not found")  # file doesn't exist yet, write a header

    csvfile.close()


