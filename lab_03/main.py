import tkinter
from tkinter import *
from tkinter import messagebox

from segment_draw import draw_beam, draw_segment


prog_info = 'Реализация и исследование алгоритмов построения отрезков'


def about_author():
    messagebox.showinfo(title='Об авторе', message='Салатов Хамит ИУ7-44Б')


def about_program():
    messagebox.showinfo(title='О программе', message=prog_info)


def clear_screen(canvas):
    canvas.delete('all')


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

    mainmenu.add_cascade(label='Справка',
                         menu=helpmenu, )

    # ___________________________________________________

    label_alg = Label(
        root,
        text="Алгоритм",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_alg.place(relx=20/root.winfo_width(),
                    rely=5/root.winfo_height(),
                    relheight=label_alg.winfo_reqheight()/root.winfo_height(),
                    relwidth=label_alg.winfo_reqwidth()/root.winfo_width())

    algorithms_available = ['DDA', 'Bresenham(float)', 'Bresenham(int)', 'Bresenham(aa)', 'Wu', 'Tk lib']
    variable_algs = StringVar()
    variable_algs.set(algorithms_available[1])

    algorithm_option_menu = OptionMenu(
        root,
        variable_algs,
        *algorithms_available
    )
    algorithm_option_menu.place(relx=20/root.winfo_width(),
                                rely=35/root.winfo_height(),
                                relwidth=algorithm_option_menu.winfo_reqwidth()/root.winfo_width(),
                                relheight=algorithm_option_menu.winfo_reqheight()/root.winfo_height())

    label_background_color = Label(
        root,
        text="Цвет фона",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_background_color.place(relx=20/root.winfo_width(),
                                 rely=80/root.winfo_height(),
                                 relheight=label_background_color.winfo_reqheight()/root.winfo_height(),
                                 relwidth=label_background_color.winfo_reqwidth()/root.winfo_width())

    colors_available = ['black', 'blue', 'red', 'green', 'white']
    variable_bg_colors = StringVar()
    variable_bg_colors.set(colors_available[4])

    def change_bg_color(choice):
        choice = variable_bg_colors.get()
        canvas.config(bg=choice)

    bg_color_menu = OptionMenu(
        root,
        variable_bg_colors,
        *colors_available,
        command=change_bg_color
    )
    bg_color_menu.place(relx=20/root.winfo_width(),
                        rely=110/root.winfo_height(),
                        relwidth=bg_color_menu.winfo_reqwidth()/root.winfo_width(),
                        relheight=bg_color_menu.winfo_reqheight()/root.winfo_height())

    label_line_color = Label(
        root,
        text="Цвет прямой",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        # width=30,
        justify=LEFT
    )
    label_line_color.place(relx=170/root.winfo_width(),
                           rely=80/root.winfo_height(),
                           relheight=label_line_color.winfo_reqheight()/root.winfo_height(),
                           relwidth=label_line_color.winfo_reqwidth()/root.winfo_width())

    variable_line_colors = StringVar()
    variable_line_colors.set(colors_available[0])

    line_color_menu = OptionMenu(
        root,
        variable_line_colors,
        *colors_available
    )
    line_color_menu.place(relx=170/root.winfo_width(),
                          rely=110/root.winfo_height(),
                          relwidth=line_color_menu.winfo_reqwidth()/root.winfo_width(),
                          relheight=line_color_menu.winfo_reqheight()/root.winfo_height())

    label_segment = Label(
        root,
        text="Отрезок",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_segment.place(relx=20/root.winfo_width(),
                        rely=185/root.winfo_height(),
                        relwidth=label_segment.winfo_reqwidth()/root.winfo_width(),
                        relheight=label_segment.winfo_reqheight()/root.winfo_height())

    label_x1 = Label(
        root,
        text="x1",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_x1.place(relx=20/root.winfo_width(),
                   rely=215/root.winfo_height(),
                   relwidth=label_x1.winfo_reqwidth()/root.winfo_width(),
                   relheight=label_x1.winfo_reqheight()/root.winfo_height())

    spinBox_x1 = Spinbox(root,
                         width=10,
                         from_=-1000,
                         to=1000,
                         textvariable=tkinter.StringVar(value=0))
    spinBox_x1.place(relx=50/root.winfo_width(),
                     rely=215/root.winfo_height(),
                     relwidth=spinBox_x1.winfo_reqwidth()/root.winfo_width(),
                     relheight=spinBox_x1.winfo_reqheight()/root.winfo_height())

    label_y1 = Label(
        root,
        text="y1",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_y1.place(relx=130/root.winfo_width(),
                   rely=215/root.winfo_height(),
                   relwidth=label_y1.winfo_reqwidth()/root.winfo_width(),
                   relheight=label_y1.winfo_reqheight()/root.winfo_height())

    spinBox_y1 = Spinbox(root,
                         width=10,
                         from_=-1000,
                         to=1000,
                         textvariable=tkinter.StringVar(value=0))
    spinBox_y1.place(relx=160/root.winfo_width(),
                     rely=215/root.winfo_height(),
                     relwidth=spinBox_y1.winfo_reqwidth()/root.winfo_width(),
                     relheight=spinBox_y1.winfo_reqheight()/root.winfo_height())

    label_x2 = Label(
        root,
        text="x2",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_x2.place(relx=20/root.winfo_width(),
                   rely=265/root.winfo_height(),
                   relwidth=label_x2.winfo_reqwidth()/root.winfo_width(),
                   relheight=label_x2.winfo_reqheight()/root.winfo_height())

    spinBox_x2 = Spinbox(root,
                         width=10,
                         from_=-1000,
                         to=1000,
                         textvariable=tkinter.StringVar(value=0))
    spinBox_x2.place(relx=50/root.winfo_width(),
                     rely=265/root.winfo_height(),
                     relwidth=spinBox_x2.winfo_reqwidth()/root.winfo_width(),
                     relheight=spinBox_x2.winfo_reqheight()/root.winfo_height())

    label_y2 = Label(
        root,
        text="y2",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_y2.place(relx=130/root.winfo_width(),
                   rely=265/root.winfo_height(),
                   relwidth=label_y2.winfo_reqwidth()/root.winfo_width(),
                   relheight=label_y2.winfo_reqheight()/root.winfo_height())

    spinBox_y2 = Spinbox(root,
                         width=10,
                         from_=-1000,
                         to=1000,
                         textvariable=tkinter.StringVar(value=0))
    spinBox_y2.place(relx=160/root.winfo_width(),
                     rely=265/root.winfo_height(),
                     relwidth=spinBox_y2.winfo_reqwidth()/root.winfo_width(),
                     relheight=spinBox_y2.winfo_reqheight()/root.winfo_height())

    but_draw_segment = Button(
        root,
        height=2,
        width=9,
        text="Отрисовать",
        bg="#899ad5",
        command=lambda: draw_segment(canvas,
                                     spinBox_x1.get(),
                                     spinBox_y1.get(),
                                     spinBox_x2.get(),
                                     spinBox_y2.get(),
                                     variable_line_colors.get(), variable_algs.get())
    )
    but_draw_segment.update()
    but_draw_segment.place(relx=100/root.winfo_width(),
                           rely=305/root.winfo_height(),
                           relwidth=but_draw_segment.winfo_reqwidth()/root.winfo_width(),
                           relheight=but_draw_segment.winfo_reqheight()/root.winfo_height())

    label_beam = Label(
        root,
        text="Пучок отрезков",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_beam.place(relx=20/root.winfo_width(),
                     rely=385/root.winfo_height(),
                     relwidth=label_beam.winfo_reqwidth()/root.winfo_width(),
                     relheight=label_beam.winfo_reqheight()/root.winfo_height())

    label_seg_len = Label(
        root,
        text="Длина Отрезка",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_seg_len.place(relx=20/root.winfo_width(),
                        rely=415/root.winfo_height(),
                        relwidth=label_seg_len.winfo_reqwidth()/root.winfo_width(),
                        relheight=label_seg_len.winfo_reqheight()/root.winfo_height())

    spinBox_seg_len = Spinbox(root,
                              width=10,
                              from_=1,
                              to=1000,
                              textvariable=tkinter.StringVar(value=350),)
    spinBox_seg_len.place(relx=130/root.winfo_width(),
                          rely=415/root.winfo_height(),
                          relwidth=spinBox_seg_len.winfo_reqwidth()/root.winfo_width(),
                          relheight=spinBox_seg_len.winfo_reqheight()/root.winfo_height())

    label_angle = Label(
        root,
        text="Угол",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_angle.place(relx=20/root.winfo_width(),
                      rely=445/root.winfo_height(),
                      relwidth=label_angle.winfo_reqwidth()/root.winfo_width(),
                      relheight=label_angle.winfo_reqheight()/root.winfo_height())

    spinBox_angle = Spinbox(root,
                            width=10,
                            from_=1,
                            to=359,
                            textvariable=tkinter.StringVar(value=15))
    spinBox_angle.place(relx=130/root.winfo_width(),
                        rely=445/root.winfo_height(),
                        relwidth=spinBox_angle.winfo_reqwidth()/root.winfo_width(),
                        relheight=spinBox_angle.winfo_reqheight()/root.winfo_height(),)

    but_draw_beam = Button(
        root,
        height=2,
        width=9,
        text="Отрисовать",
        bg="#899ad5",
        command=lambda: draw_beam(canvas,
                                  float(spinBox_seg_len.get()),
                                  float(spinBox_angle.get()),
                                  variable_line_colors.get(), variable_algs.get())
    )
    but_draw_beam.update()
    but_draw_beam.place(relx=100/root.winfo_width(),
                        rely=475/root.winfo_height(),
                        relwidth=but_draw_beam.winfo_reqwidth()/root.winfo_width(),
                        relheight=but_draw_beam.winfo_reqheight()/root.winfo_height())

    but_cmp_time = Button(
        root,
        height=2,
        width=15,
        text="Очистить экран",
        bg="#899ad5",
        command=lambda: clear_screen(canvas)
    )
    but_cmp_time.update()
    but_cmp_time.place(relx=20/root.winfo_width(),
                       rely=575/root.winfo_height(),
                       relwidth=but_cmp_time.winfo_reqwidth()/root.winfo_width(),
                       relheight=but_cmp_time.winfo_reqheight()/root.winfo_height())

    but_cmp_time = Button(
        root,
        height=2,
        width=15,
        text="Сравнить время",
        bg="#899ad5",
        # command=lambda: rotate_model(canvas, int(spinBox_rotate.get()),
        #                             [int(spinBox_center_x.get()), int(spinBox_center_y.get())])
    )
    but_cmp_time.update()
    but_cmp_time.place(relx=20/root.winfo_width(),
                       rely=625/root.winfo_height(),
                       relwidth=but_cmp_time.winfo_reqwidth()/root.winfo_width(),
                       relheight=but_cmp_time.winfo_reqheight()/root.winfo_height())

    but_cmp_step = Button(
        root,
        height=2,
        width=20,
        text="Сравнить ступенчатость",
        bg="#899ad5",
        # command=lambda: rotate_model(canvas, int(spinBox_rotate.get()),
        #                             [int(spinBox_center_x.get()), int(spinBox_center_y.get())])
    )
    but_cmp_step.update()
    but_cmp_step.place(relx=170/root.winfo_width(),
                       rely=625/root.winfo_height(),
                       relwidth=but_cmp_step.winfo_reqwidth()/root.winfo_width(),
                       relheight=but_cmp_step.winfo_reqheight()/root.winfo_height())


def main():
    root = Tk()

    # window_settings(root)
    ui(root)

    root.mainloop()


if __name__ == "__main__":
    main()
