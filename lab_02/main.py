import tkinter
from tkinter import *
from tkinter import messagebox

from model import draw_model, draw_original_model, ret_to_prev_action
from model import move_model, scale_model, rotate_model


'''
lab protection:

1.1)move (20;20)
1.2)scale(-1;-1) relative (20;20)
1.3)move(-20;-20)
1.4)scale (-1;1) relative to (0;0)
1.5)scale (1;-1) relative to (0;0)
1.6)? - nothing needed

2.1)move (20;20)
2.2)scale (-1;-1) relative to (20;20)
2.3)move (-10;-10)
2.4)scale(-1;1) relative to (0;0)
2.5)move(-10;-10)
2.6)scale(1;-1) relative to (0;0)
2.7)? - move(20;0)
'''


prog_info = "Данная программа производит преобразования исходного изображения " \
       "(Перенос, масштабирование, поворот)"


def about_author():
    messagebox.showinfo(title='Об авторе', message='Салатов Хамит ИУ7-44Б')


def about_program():
    messagebox.showinfo(title='О программе', message=prog_info)


def ui(root):
    root.title("cg lab 2")
    root.geometry("1300x700+100+50")
    root.configure(background="#899ad5")
    root.update()

    canvas = Canvas(root, width=955, height=690, cursor="tcross")
    canvas.place(relx=340/root.winfo_width(),
                 y=5,
                 relwidth=955/root.winfo_width(),
                 relheight=690/root.winfo_height())

    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label='Об авторе',
                         command=lambda: about_author())
    helpmenu.add_command(label='О программе',
                         command=lambda: about_program())
    helpmenu.add_separator()
    helpmenu.add_command(label='Выход',
                         command=lambda: root.destroy())

    editmenu = Menu(mainmenu, tearoff=0)
    editmenu.add_command(label='Отменить последнее действие',
                         command=lambda: ret_to_prev_action(canvas))
    editmenu.add_command(label='Вернуться к исходному изображению',
                         command=lambda: draw_original_model(canvas))

    mainmenu.add_cascade(label='Справка',
                         menu=helpmenu, )
    mainmenu.add_cascade(label='Правка',
                         menu=editmenu)

    # ___________________________________________________

    label_center = Label(
        root,
        text="Центр масштабирования и поворота",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_center.place(relx=10/root.winfo_width(),
                       rely=565/root.winfo_height(),
                       relheight=label_center.winfo_reqheight()/root.winfo_height(),
                       relwidth=label_center.winfo_reqwidth()/root.winfo_width())

    label_cx = Label(
        root,
        text="X",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_cx.place(relx=30/root.winfo_width(),
                   rely=590/root.winfo_height(),
                   relheight=label_cx.winfo_reqheight()/root.winfo_height(),
                   relwidth=label_cx.winfo_reqwidth()/root.winfo_width())

    spinBox_center_x = Spinbox(root,
                               width=10,
                               from_=-1000,
                               to=1000,
                               textvariable=tkinter.StringVar(value=0))
    spinBox_center_x.place(relx=60/root.winfo_width(),
                           rely=590/root.winfo_height(),
                           relwidth=spinBox_center_x.winfo_reqwidth()/root.winfo_width(),
                           relheight=spinBox_center_x.winfo_reqheight()/root.winfo_height())

    label_cy = Label(
        root,
        text="Y",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_cy.place(relx=270/root.winfo_width(),
                   rely=590/root.winfo_height(),
                   relheight=label_cy.winfo_reqheight()/root.winfo_height(),
                   relwidth=label_cy.winfo_reqwidth()/root.winfo_width())

    spinBox_center_y = Spinbox(root,
                               width=10,
                               from_=-1000,
                               to=1000,
                               textvariable=tkinter.StringVar(value=0))
    spinBox_center_y.place(relx=190/root.winfo_width(),
                           rely=590/root.winfo_height(),
                           relwidth=spinBox_center_y.winfo_reqwidth()/root.winfo_width(),
                           relheight=spinBox_center_y.winfo_reqheight()/root.winfo_height())

    label_move = Label(
        root,
        text="Перенос",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_move.place(relx=120/root.winfo_width(),
                     rely=5/root.winfo_height(),
                     relheight=label_move.winfo_reqheight()/root.winfo_height(),
                     relwidth=label_move.winfo_reqwidth()/root.winfo_width())

    label_dx = Label(
        root,
        text="dx",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_dx.place(relx=30/root.winfo_width(),
                   rely=30/root.winfo_height(),
                   relheight=label_dx.winfo_reqheight()/root.winfo_height(),
                   relwidth=label_dx.winfo_reqwidth()/root.winfo_width())

    spinBox_move_x = Spinbox(root,
                             width=10,
                             from_=-1000,
                             to=1000,
                             textvariable=tkinter.StringVar(value=0))
    spinBox_move_x.place(relx=60/root.winfo_width(),
                         rely=30/root.winfo_height(),
                         relwidth=spinBox_move_x.winfo_reqwidth()/root.winfo_width(),
                         relheight=spinBox_move_x.winfo_reqheight()/root.winfo_height())

    label_dy = Label(
        root,
        text="dy",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_dy.place(relx=270/root.winfo_width(),
                   rely=25/root.winfo_height(),
                   relheight=label_dy.winfo_reqheight()/root.winfo_height(),
                   relwidth=label_dy.winfo_reqwidth()/root.winfo_width())

    spinBox_move_y = Spinbox(root,
                             width=10,
                             from_=-1000,
                             to=1000,
                             textvariable=tkinter.StringVar(value=0))
    spinBox_move_y.place(relx=190/root.winfo_width(),
                         rely=30/root.winfo_height(),
                         relwidth=spinBox_move_y.winfo_reqwidth()/root.winfo_width(),
                         relheight=spinBox_move_y.winfo_reqheight()/root.winfo_height())

    but_move = Button(
        root,
        height=2,
        width=9,
        text="Перенести",
        bg="#899ad5",
        command=lambda: move_model(canvas, int(spinBox_move_x.get()), int(spinBox_move_y.get()))
    )
    but_move.update()
    but_move.place(relx=120/root.winfo_width(),
                   rely=60/root.winfo_height(),
                   relwidth=but_move.winfo_reqwidth()/root.winfo_width(),
                   relheight=but_move.winfo_reqheight()/root.winfo_height())

    label_scale = Label(
        root,
        text="Масштабирование",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_scale.place(relx=80/root.winfo_width(),
                      rely=205/root.winfo_height(),
                      relheight=label_scale.winfo_reqheight()/root.winfo_height(),
                      relwidth=label_scale.winfo_reqwidth()/root.winfo_width())

    label_kx = Label(
        root,
        text="dx",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_kx.place(relx=30/root.winfo_width(),
                   rely=230/root.winfo_height(),
                   relheight=label_kx.winfo_reqheight()/root.winfo_height(),
                   relwidth=label_kx.winfo_reqwidth()/root.winfo_width())

    spinBox_scale_x = Spinbox(root,
                              width=10,
                              from_=-1000,
                              to=1000,
                              textvariable=tkinter.StringVar(value=0))
    spinBox_scale_x.place(relx=60/root.winfo_width(),
                          rely=230/root.winfo_height(),
                          relwidth=spinBox_scale_x.winfo_reqwidth()/root.winfo_width(),
                          relheight=spinBox_scale_x.winfo_reqheight()/root.winfo_height())

    label_ky = Label(
        root,
        text="dy",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_ky.place(relx=270/root.winfo_width(),
                   rely=225/root.winfo_height(),
                   relheight=label_ky.winfo_reqheight()/root.winfo_height(),
                   relwidth=label_ky.winfo_reqwidth()/root.winfo_width())

    spinBox_scale_y = Spinbox(root,
                              width=10,
                              from_=-1000,
                              to=1000,
                              textvariable=tkinter.StringVar(value=0))
    spinBox_scale_y.place(relx=190/root.winfo_width(),
                          rely=230/root.winfo_height(),
                          relwidth=spinBox_scale_y.winfo_reqwidth()/root.winfo_width(),
                          relheight=spinBox_scale_y.winfo_reqheight()/root.winfo_height())

    but_scale = Button(
        root,
        height=2,
        width=13,
        text="Масштабировать",
        bg="#899ad5",
        command=lambda: scale_model(canvas, float(spinBox_scale_x.get()), float(spinBox_scale_y.get()),
                                    [int(spinBox_center_x.get()), int(spinBox_center_y.get())])
    )
    but_scale.update()
    but_scale.place(relx=115/root.winfo_width(),
                    rely=260/root.winfo_height(),
                    relwidth=but_scale.winfo_reqwidth()/root.winfo_width(),
                    relheight=but_scale.winfo_reqheight()/root.winfo_height())

    label_rotate = Label(
        root,
        text="Поворот",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_rotate.place(relx=130/root.winfo_width(),
                       rely=405/root.winfo_height(),
                       relheight=label_rotate.winfo_reqheight()/root.winfo_height(),
                       relwidth=label_rotate.winfo_reqwidth()/root.winfo_width())

    label_angle = Label(
        root,
        text="Угол в °",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_angle.place(relx=30/root.winfo_width(),
                      rely=430/root.winfo_height(),
                      relheight=label_angle.winfo_reqheight()/root.winfo_height(),
                      relwidth=label_angle.winfo_reqwidth()/root.winfo_width())

    spinBox_rotate = Spinbox(root,
                             width=10,
                             from_=-1000,
                             to=1000,
                             textvariable=tkinter.StringVar(value=0))
    spinBox_rotate.place(relx=130/root.winfo_width(),
                         rely=430/root.winfo_height(),
                         relwidth=spinBox_rotate.winfo_reqwidth()/root.winfo_width(),
                         relheight=spinBox_rotate.winfo_reqheight()/root.winfo_height())

    but_rotate = Button(
        root,
        height=2,
        width=9,
        text="Повернуть",
        bg="#899ad5",
        command=lambda: rotate_model(canvas, int(spinBox_rotate.get()),
                                    [int(spinBox_center_x.get()), int(spinBox_center_y.get())])
    )
    but_rotate.update()
    but_rotate.place(relx=130/root.winfo_width(),
                     rely=460/root.winfo_height(),
                     relwidth=but_rotate.winfo_reqwidth()/root.winfo_width(),
                     relheight=but_rotate.winfo_reqheight()/root.winfo_height())

    def mouse_clicked(event):
        # print point
        spinBox_center_x.delete(0, END)
        spinBox_center_x.insert(0, event.x)
        spinBox_center_y.delete(0, END)
        spinBox_center_y.insert(0, event.y)

    canvas.bind("<Button-1>", mouse_clicked)

    draw_model(canvas)


def main():
    root = Tk()

    # window_settings(root)
    ui(root)

    root.mainloop()


if __name__ == "__main__":
    main()
