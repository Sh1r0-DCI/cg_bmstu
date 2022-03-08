from tkinter import *
from tkinter.messagebox import showerror


def point_delete(window, listbox_set):
    listbox_curselection = listbox_set.curselection()

    try:
        listbox_set.delete(listbox_curselection)
    except:
        showerror(title='Ошибка', message='Выделите координаты точки для их удаления')
