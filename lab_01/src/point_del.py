from tkinter import *
from tkinter.messagebox import showerror


def point_delete(window, listb_f_set):
    listb_f_cursel = listb_f_set.curselection()

    try:
        listb_f_set.delete(listb_f_cursel)
    except:
        showerror("Ошибка", "Выделите координаты точки для их удаления")
