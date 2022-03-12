"""
    Дано множество точек на плоскости. Найти выпуклый N-угольник
    максимальной площади. N вводится пользователем.
"""
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from point_create import point_create
from point_del import point_delete
from point_change import point_change
from solve_task import solve_task


def about_author():
    messagebox.showinfo(title='Об авторе', message='Салатов Хамит ИУ7-44Б')


def task_info():
    tkinter.messagebox.showinfo(
        "Условие",
        "Дано множество точек на плоскости. Найти выпуклый N-угольник "
        "максимальной площади. N вводится пользователем."
    )


def window_settings(root):
    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label='Об авторе',
                         command=lambda: about_author())

    mainmenu.add_cascade(label='Справка',
                         menu=helpmenu)

    root.geometry("1300x700+100+50")
    root.title("Lab 1")
    root.configure(background="#899ad5")


def ui(root):
    root.update()
    canvas = Canvas(root, width=845, height=694, cursor="tcross")
    canvas.place(relx=450/root.winfo_width(), y=0)

    label_set = Label(
        root,
        text="Множество точек",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    print(label_set.winfo_reqheight())
    print(root.winfo_height())
    label_set.place(relx=60/root.winfo_width(),
                    rely=5/root.winfo_height(),
                    relheight=label_set.winfo_reqheight()/root.winfo_height(),
                    relwidth=label_set.winfo_reqwidth()/root.winfo_width())

    listbox_set = Listbox(root, width=50, height=15)  # расположение множества
    listbox_set.update()
    listbox_set.place(relx=30/root.winfo_width(),
                      rely=30/root.winfo_height(),
                      relwidth=listbox_set.winfo_reqwidth()/root.winfo_width(),
                      relheight=listbox_set.winfo_reqheight()/root.winfo_height())

    label_spinbox = Label(
        root,
        text="N (Количество вершин многоугольника)",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_spinbox.place(relx=30/root.winfo_width(),
                        rely=295/root.winfo_height(),
                        relwidth=label_spinbox.winfo_reqwidth()/root.winfo_width(),
                        relheight=label_spinbox.winfo_reqheight()/root.winfo_height())

    spinBox_N = Spinbox(root,
                        width=20,
                        from_=3,
                        to=20,
                        textvariable=3)
    spinBox_N.place(relx=30/root.winfo_width(),
                    rely=320/root.winfo_height(),
                    relwidth=spinBox_N.winfo_reqwidth()/root.winfo_width(),
                    relheight=spinBox_N.winfo_reqheight()/root.winfo_height())

    but_ins_point = Button(
        root,
        height=3,
        width=20,
        text="Добавить точку",
        bg="#899ad5",
        command=lambda: point_create(root, listbox_set),
    )
    but_ins_point.update()
    but_ins_point.place(relx=30/root.winfo_width(),
                        rely=390/root.winfo_height(),
                        relwidth=but_ins_point.winfo_reqwidth()/root.winfo_width(),
                        relheight=but_ins_point.winfo_reqheight()/root.winfo_height())

    but_del_point = Button(
        root,
        height=3,
        width=20,
        text="Удалить точку",
        bg="#899ad5",
        command=lambda: point_delete(root, listbox_set),
    )
    but_del_point.update()
    but_del_point.place(relx=30/root.winfo_width(),
                        rely=460/root.winfo_height(),
                        relwidth=but_del_point.winfo_reqwidth()/root.winfo_width(),
                        relheight=but_del_point.winfo_reqheight()/root.winfo_height())

    but_change_point = Button(
        root,
        height=3,
        width=20,
        text="Изменить точку",
        bg="#899ad5",
        command=lambda: point_change(root, listbox_set),
    )
    but_change_point.update()
    but_change_point.place(relx=188/root.winfo_width(),
                           rely=390/root.winfo_height(),
                           relwidth=but_change_point.winfo_reqwidth()/root.winfo_width(),
                           relheight=but_change_point.winfo_reqheight()/root.winfo_height())

    but_clear_listb = Button(
        root,
        height=3,
        width=20,
        text="Очистить множество",
        bg="#899ad5",
        command=lambda: listbox_set.delete(0, END),
    )
    but_clear_listb.update()
    but_clear_listb.place(relx=188/root.winfo_width(),
                          rely=460/root.winfo_height(),
                          relwidth=but_clear_listb.winfo_reqwidth()/root.winfo_width(),
                          relheight=but_clear_listb.winfo_reqheight()/root.winfo_height())

    but_task = Button(
        root,
        height=3,
        width=20,
        text="Условие",
        bg="#899ad5",
        command=task_info
    )
    but_task.update()
    but_task.place(relx=30/root.winfo_width(),
                   rely=530/root.winfo_height(),
                   relwidth=but_task.winfo_reqwidth()/root.winfo_width(),
                   relheight=but_task.winfo_reqheight()/root.winfo_height())

    but_solve_task = Button(
        root,
        height=3,
        width=20,
        text="Решить задачу",
        bg="#899ad5",
        command=lambda: solve_task(canvas, listbox_set, spinBox_N),
    )
    but_solve_task.update()
    but_solve_task.place(relx=188/root.winfo_width(),
                         rely=610/root.winfo_height(),
                         relwidth=but_solve_task.winfo_reqwidth()/root.winfo_width(),
                         relheight=but_solve_task.winfo_reqheight()/root.winfo_height())

    but_exit = Button(
        root,
        height=3,
        width=20,
        text="Выйти",
        bg="#899ad5",
        command=lambda: root.destroy(),
    )
    but_exit.update()
    but_exit.place(relx=30/root.winfo_width(),
                   rely=610/root.winfo_height(),
                   relwidth=but_exit.winfo_reqwidth()/root.winfo_width(),
                   relheight=but_exit.winfo_reqheight()/root.winfo_height())


def main():
    root = Tk()

    window_settings(root)
    ui(root)

    root.mainloop()


if __name__ == "__main__":
    main()
