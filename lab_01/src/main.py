"""
    На плоскости дано множество точек. Найти такой треугольник
    с вершинами в этих точках, у которого высота имеет максимальную длину.
    (Для каждого треугольника берется та из трех высот, длина которой максимальна.)

"""


from tkinter import *

from task_info import task_info
from point_create import point_create
from point_del import point_delete
from point_change import point_change
from solve_task import solve_task


def window_settings(root):
    root.geometry("1300x700+100+50")
    root.title("Lab 1")
    root.configure(background="#899ad5")
    root.resizable(False, False)


def ui(root):
    canvas = Canvas(root, width=845, height=694, cursor="tcross")
    canvas.place(x=450, y=0)

    lab_set = Label(
        root,
        text="Множество точек",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
    )
    lab_set.place(x=60, y=5)

    listb_set = Listbox(root, width=50, height=15) #расположение множества
    listb_set.place(x=30, y=30)

    but_task = Button(
        root, height=3, width=20, text="Условие", bg="#899ad5", command=task_info
    )
    but_task.place(x=30, y=320)

    but_ins_point = Button(
        root,
        height=3,
        width=20,
        text="Добавить точку",
        bg="#899ad5",
        command=lambda: point_create(root, listb_set),
    )
    but_ins_point.place(x=188, y=320)

    but_del_point = Button(
        root,
        height=3,
        width=20,
        text="Удалить точку",
        bg="#899ad5",
        command=lambda: point_delete(root, listb_set),
    )
    but_del_point.place(x=188, y=390)

    but_change_point = Button(
        root,
        height=3,
        width=20,
        text="Изменить точку",
        bg="#899ad5",
        command=lambda: point_change(root, listb_set),
    )
    but_change_point.place(x=188, y=460)

    but_clear_listb = Button(
        root,
        height=3,
        width=20,
        text="Очистить множество",
        bg="#899ad5",
        command=lambda: listb_set.delete(0, END),
    )
    but_clear_listb.place(x=188, y=530)

    but_solve_task = Button(
        root,
        height=3,
        width=20,
        text="Решить задачу",
        bg="#899ad5",
        command=lambda: solve_task(canvas, listb_set),
    )
    but_solve_task.place(x=188, y=610)

    but_exit = Button(
        root,
        height=3,
        width=20,
        text="Выйти",
        bg="#899ad5",
        command=lambda: root.destroy(),
    )
    but_exit.place(x=30, y=610)


def main():
    root = Tk()

    window_settings(root)
    ui(root)

    root.mainloop()


if __name__ == "__main__":
    main()
