from tkinter import *
from tkinter.messagebox import showerror

from toplvl_settings import window_settings


def ui(window, listbox_set):
    var = IntVar()

    lab_x = Label(
        window,
        text="X:",
        font=("Calibri", 15),
        background="#0082ff",
        foreground="black",
    )
    lab_x.place(x=25, y=78)
    lab_y = Label(
        window,
        text="Y:",
        font=("Calibri", 15),
        background="#0082ff",
        foreground="black",
    )
    lab_y.place(x=217, y=78)

    entry_x = Entry(window, width=15)
    entry_x.place(x=60, y=80)
    entry_y = Entry(window, width=15)
    entry_y.place(x=250, y=80)

    but_exit = Button(
        window,
        height=3,
        width=20,
        text="Выйти",
        bg="#0082ff",
        command=lambda: window.destroy(),
    )
    but_exit.place(x=10, y=120)
    but_add = Button(
        window,
        height=3,
        width=20,
        text="Добавить",
        bg="#0082ff",
        command=lambda: process(
            window, var, entry_x, entry_y, listbox_set
        )
    )
    but_add.place(x=205, y=120)


def process(window, var, entry_x, entry_y, listbox_set):
    var_val = var.get()

    try:
        x_c = float(entry_x.get())
        y_c = float(entry_y.get())

        listbox_set.insert(END, str(x_c) + ";" + str(y_c))

        entry_x.delete(first=0, last=END)
        entry_y.delete(first=0, last=END)
    except:
        showerror("Ошибка", "Проверьте правильность вводимых данных", parent=window)


def point_create(window, listbox_set):
    top_window = Toplevel(window)
    window_settings(top_window, "Добавление координат точки")
    ui(top_window, listbox_set)
