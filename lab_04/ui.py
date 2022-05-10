from tkinter import *
from tkinter import messagebox, ttk

prog_info = 'Реализация и исследование генерации окружности и эллипса'


def about_author():
    messagebox.showinfo(title='Об авторе', message='Салатов Хамит ИУ7-44Б')


def about_program():
    messagebox.showinfo(title='О программе', message=prog_info)


def clear_screen(canvas):
    canvas.delete('all')


def ui(root):
    root.title("cg lab 4")
    root.geometry("1300x700+100+50")
    root.configure(background="#899ad5")
    root.update()

    canvas = Canvas(root, width=955, height=690, bg='white', cursor="tcross")
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

    algorithms_available = ['Canonical', 'Parametric', 'Bresenham', 'Middle point', 'Tk lib']
    variable_algs = StringVar()
    variable_algs.set(algorithms_available[3])

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
        # choice = variable_bg_colors.get()
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
        text="Цвет эллипса",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
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

    separator = ttk.Separator(root, orient='horizontal')
    separator.place(relx=0,
                    rely=150/root.winfo_height(),
                    relwidth=340/root.winfo_width())

    # ____________________________________________________________________________________________

    label_segment = Label(
        root,
        text="Эллипс",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_segment.place(relx=20/root.winfo_width(),
                        rely=155/root.winfo_height(),
                        relwidth=label_segment.winfo_reqwidth()/root.winfo_width(),
                        relheight=label_segment.winfo_reqheight()/root.winfo_height())

    label_xc = Label(
        root,
        text="xс",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_xc.place(relx=20/root.winfo_width(),
                   rely=185/root.winfo_height(),
                   relwidth=label_xc.winfo_reqwidth()/root.winfo_width(),
                   relheight=label_xc.winfo_reqheight()/root.winfo_height())

    spinBox_xc = Spinbox(root,
                         width=10,
                         from_=-1000,
                         to=1000,
                         textvariable=StringVar(value=0))
    spinBox_xc.place(relx=50/root.winfo_width(),
                     rely=185/root.winfo_height(),
                     relwidth=spinBox_xc.winfo_reqwidth()/root.winfo_width(),
                     relheight=spinBox_xc.winfo_reqheight()/root.winfo_height())

    label_yc = Label(
        root,
        text="yс",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_yc.place(relx=130/root.winfo_width(),
                   rely=185/root.winfo_height(),
                   relwidth=label_yc.winfo_reqwidth()/root.winfo_width(),
                   relheight=label_yc.winfo_reqheight()/root.winfo_height())

    spinBox_yc = Spinbox(root,
                         width=10,
                         from_=-1000,
                         to=1000,
                         textvariable=StringVar(value=0))
    spinBox_yc.place(relx=160/root.winfo_width(),
                     rely=185/root.winfo_height(),
                     relwidth=spinBox_yc.winfo_reqwidth()/root.winfo_width(),
                     relheight=spinBox_yc.winfo_reqheight()/root.winfo_height())

    label_Ra = Label(
        root,
        text="Ra",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_Ra.place(relx=20/root.winfo_width(),
                   rely=215/root.winfo_height(),
                   relwidth=label_Ra.winfo_reqwidth()/root.winfo_width(),
                   relheight=label_Ra.winfo_reqheight()/root.winfo_height())

    spinBox_Ra = Spinbox(root,
                         width=10,
                         from_=-1000,
                         to=1000,
                         textvariable=StringVar(value=0))
    spinBox_Ra.place(relx=50/root.winfo_width(),
                     rely=215/root.winfo_height(),
                     relwidth=spinBox_Ra.winfo_reqwidth()/root.winfo_width(),
                     relheight=spinBox_Ra.winfo_reqheight()/root.winfo_height())

    label_Rb = Label(
        root,
        text="Rb",
        font=("Calibri", 11),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    label_Rb.place(relx=130/root.winfo_width(),
                   rely=215/root.winfo_height(),
                   relwidth=label_Rb.winfo_reqwidth()/root.winfo_width(),
                   relheight=label_Rb.winfo_reqheight()/root.winfo_height())

    spinBox_Rb = Spinbox(root,
                         width=10,
                         from_=-1000,
                         to=1000,
                         textvariable=StringVar(value=0))
    spinBox_Rb.place(relx=160/root.winfo_width(),
                     rely=215/root.winfo_height(),
                     relwidth=spinBox_Rb.winfo_reqwidth()/root.winfo_width(),
                     relheight=spinBox_Rb.winfo_reqheight()/root.winfo_height())

    but_draw_ellipse = Button(
        root,
        height=2,
        width=9,
        text="Отрисовать",
        bg="#899ad5",
        # command=lambda: draw_segment(canvas,
        #                              spinBox_x1.get(),
        #                              spinBox_y1.get(),
        #                              spinBox_x2.get(),
        #                              spinBox_y2.get(),
        #                              variable_line_colors.get(), variable_algs.get())
    )
    but_draw_ellipse.update()
    but_draw_ellipse.place(relx=100/root.winfo_width(),
                           rely=245/root.winfo_height(),
                           relwidth=but_draw_ellipse.winfo_reqwidth()/root.winfo_width(),
                           relheight=but_draw_ellipse.winfo_reqheight()/root.winfo_height())

    separator = ttk.Separator(root, orient='horizontal')
    separator.place(relx=0,
                    rely=295/root.winfo_height(),
                    relwidth=340/root.winfo_width())

    # ___________________________________________________________________________________________

    figure_rb_label = Label(
        root,
        text="Выберите фигуру для спектра",
        font=("Calibri", 15),
        background="#899ad5",
        foreground="black",
        justify=LEFT
    )
    figure_rb_label.place(
        relx=20/root.winfo_width(),
        rely=305/root.winfo_height(),
        relwidth=figure_rb_label.winfo_reqwidth()/root.winfo_width(),
        relheight=figure_rb_label.winfo_reqheight()/root.winfo_height()
    )

    # declaring widgets to be placed after radiobutton pressed
    #   circle declarations

    label_circle_spectre = Label(
            root,
            text="Спектр окружностей",
            font=("Calibri", 15),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    label_rs = Label(
            root,
            text="R_s",
            font=("Calibri", 11),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    spinBox_rs = Spinbox(root,
                         width=10,
                         from_=1,
                         to=1000,
                         textvariable=StringVar(value=30))

    label_re = Label(
            root,
            text="R_e",
            font=("Calibri", 11),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    spinBox_re = Spinbox(root,
                         width=10,
                         from_=1,
                         to=1000,
                         textvariable=StringVar(value=280))

    label_step = Label(
            root,
            text="Step",
            font=("Calibri", 11),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    spinBox_step = Spinbox(root,
                           width=10,
                           from_=1,
                           to=1000,
                           textvariable=StringVar(value=5))

    label_n = Label(
            root,
            text="N",
            font=("Calibri", 11),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    spinBox_n = Spinbox(root,
                        width=10,
                        from_=1,
                        to=1000,
                        textvariable=StringVar(value=50))

    but_draw_cir_spectre = Button(
            root,
            height=2,
            width=9,
            text="Отрисовать",
            bg="#899ad5",
            # command=lambda: draw_beam(canvas,
            #                           float(spinBox_seg_len.get()),
            #                           float(spinBox_angle.get()),
            #                           variable_line_colors.get(), variable_algs.get())
        )

    # ellipse declarations
    label_ellipse_spectre = Label(
            root,
            text="Спектр эллипсов",
            font=("Calibri", 15),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    label_ra = Label(
            root,
            text="R_a",
            font=("Calibri", 11),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    spinBox_ra = Spinbox(root,
                         width=10,
                         from_=1,
                         to=1000,
                         textvariable=StringVar(value=30))

    label_rb = Label(
            root,
            text="R_b",
            font=("Calibri", 11),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    spinBox_rb = Spinbox(root,
                         width=10,
                         from_=1,
                         to=1000,
                         textvariable=StringVar(value=280))

    label_step_e = Label(
            root,
            text="Step",
            font=("Calibri", 11),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    spinBox_step_e = Spinbox(root,
                             width=10,
                             from_=1,
                             to=1000,
                             textvariable=StringVar(value=5))

    label_n_e = Label(
            root,
            text="N",
            font=("Calibri", 11),
            background="#899ad5",
            foreground="black",
            justify=LEFT
        )

    spinBox_n_e = Spinbox(root,
                          width=10,
                          from_=1,
                          to=1000,
                          textvariable=StringVar(value=50))

    but_draw_ell_spectre = Button(
            root,
            height=2,
            width=9,
            text="Отрисовать",
            bg="#899ad5",
            # command=lambda: draw_beam(canvas,
            #                           float(spinBox_seg_len.get()),
            #                           float(spinBox_angle.get()),
            #                           variable_line_colors.get(), variable_algs.get())
        )

    def circle_interface():
        # ellipse widgets deletion
        label_ellipse_spectre.place_forget()
        label_ra.place_forget()
        spinBox_ra.place_forget()
        label_rb.place_forget()
        spinBox_rb.place_forget()
        label_step_e.place_forget()
        spinBox_step_e.place_forget()
        label_n_e.place_forget()
        spinBox_n_e.place_forget()
        but_draw_ell_spectre.place_forget()

        label_circle_spectre.place(relx=20/root.winfo_width(),
                                   rely=385/root.winfo_height(),
                                   relwidth=label_circle_spectre.winfo_reqwidth()/root.winfo_width(),
                                   relheight=label_circle_spectre.winfo_reqheight()/root.winfo_height())

        label_rs.place(relx=20/root.winfo_width(),
                       rely=415/root.winfo_height(),
                       relwidth=label_rs.winfo_reqwidth()/root.winfo_width(),
                       relheight=label_rs.winfo_reqheight()/root.winfo_height())

        spinBox_rs.place(relx=60/root.winfo_width(),
                         rely=415/root.winfo_height(),
                         relwidth=spinBox_rs.winfo_reqwidth()/root.winfo_width(),
                         relheight=spinBox_rs.winfo_reqheight()/root.winfo_height())

        label_re.place(relx=170/root.winfo_width(),
                       rely=415/root.winfo_height(),
                       relwidth=label_re.winfo_reqwidth()/root.winfo_width(),
                       relheight=label_re.winfo_reqheight()/root.winfo_height())

        spinBox_re.place(relx=210/root.winfo_width(),
                         rely=415/root.winfo_height(),
                         relwidth=spinBox_re.winfo_reqwidth()/root.winfo_width(),
                         relheight=spinBox_re.winfo_reqheight()/root.winfo_height())

        label_step.place(relx=20/root.winfo_width(),
                         rely=445/root.winfo_height(),
                         relwidth=label_step.winfo_reqwidth()/root.winfo_width(),
                         relheight=label_step.winfo_reqheight()/root.winfo_height())

        spinBox_step.place(relx=60/root.winfo_width(),
                           rely=445/root.winfo_height(),
                           relwidth=spinBox_step.winfo_reqwidth()/root.winfo_width(),
                           relheight=spinBox_step.winfo_reqheight()/root.winfo_height(),)

        label_n.place(relx=170/root.winfo_width(),
                      rely=445/root.winfo_height(),
                      relwidth=label_n.winfo_reqwidth()/root.winfo_width(),
                      relheight=label_n.winfo_reqheight()/root.winfo_height())

        spinBox_n.place(relx=210/root.winfo_width(),
                        rely=445/root.winfo_height(),
                        relwidth=spinBox_n.winfo_reqwidth()/root.winfo_width(),
                        relheight=spinBox_n.winfo_reqheight()/root.winfo_height(),)

        but_draw_cir_spectre.place(relx=100/root.winfo_width(),
                                   rely=475/root.winfo_height(),
                                   relwidth=but_draw_cir_spectre.winfo_reqwidth()/root.winfo_width(),
                                   relheight=but_draw_cir_spectre.winfo_reqheight()/root.winfo_height())

        # radio buttons for field lock needed

    def ellipse_interface():
        # circle widgets deletion
        label_circle_spectre.place_forget()
        label_rs.place_forget()
        spinBox_rs.place_forget()
        label_re.place_forget()
        spinBox_re.place_forget()
        label_step.place_forget()
        spinBox_step.place_forget()
        label_n.place_forget()
        spinBox_n.place_forget()
        but_draw_cir_spectre.place_forget()

        label_ellipse_spectre.place(relx=20/root.winfo_width(),
                                    rely=385/root.winfo_height(),
                                    relwidth=label_ellipse_spectre.winfo_reqwidth()/root.winfo_width(),
                                    relheight=label_ellipse_spectre.winfo_reqheight()/root.winfo_height())

        label_ra.place(relx=20/root.winfo_width(),
                       rely=415/root.winfo_height(),
                       relwidth=label_ra.winfo_reqwidth()/root.winfo_width(),
                       relheight=label_ra.winfo_reqheight()/root.winfo_height())

        spinBox_ra.place(relx=60/root.winfo_width(),
                         rely=415/root.winfo_height(),
                         relwidth=spinBox_ra.winfo_reqwidth()/root.winfo_width(),
                         relheight=spinBox_ra.winfo_reqheight()/root.winfo_height())

        label_rb.place(relx=170/root.winfo_width(),
                       rely=415/root.winfo_height(),
                       relwidth=label_rb.winfo_reqwidth()/root.winfo_width(),
                       relheight=label_rb.winfo_reqheight()/root.winfo_height())

        spinBox_rb.place(relx=210/root.winfo_width(),
                         rely=415/root.winfo_height(),
                         relwidth=spinBox_rb.winfo_reqwidth()/root.winfo_width(),
                         relheight=spinBox_rb.winfo_reqheight()/root.winfo_height())

        label_step_e.place(relx=20/root.winfo_width(),
                           rely=445/root.winfo_height(),
                           relwidth=label_step_e.winfo_reqwidth()/root.winfo_width(),
                           relheight=label_step_e.winfo_reqheight()/root.winfo_height())

        spinBox_step_e.place(relx=60/root.winfo_width(),
                             rely=445/root.winfo_height(),
                             relwidth=spinBox_step_e.winfo_reqwidth()/root.winfo_width(),
                             relheight=spinBox_step_e.winfo_reqheight()/root.winfo_height(),)

        label_n_e.place(relx=170/root.winfo_width(),
                        rely=445/root.winfo_height(),
                        relwidth=label_n_e.winfo_reqwidth()/root.winfo_width(),
                        relheight=label_n_e.winfo_reqheight()/root.winfo_height())

        spinBox_n_e.place(relx=210/root.winfo_width(),
                          rely=445/root.winfo_height(),
                          relwidth=spinBox_n_e.winfo_reqwidth()/root.winfo_width(),
                          relheight=spinBox_n_e.winfo_reqheight()/root.winfo_height(),)

        but_draw_ell_spectre.place(relx=100/root.winfo_width(),
                                   rely=475/root.winfo_height(),
                                   relwidth=but_draw_ell_spectre.winfo_reqwidth()/root.winfo_width(),
                                   relheight=but_draw_ell_spectre.winfo_reqheight()/root.winfo_height())

    figure_options = ['Circle', 'Ellipse']
    figure_option = IntVar()
    figure_option.set(figure_options[0])

    circle_radiobutton = Radiobutton(
        root,
        text='Окружность',
        variable=figure_option,
        value=figure_options[0],
        height=1,
        width=10,
        bg='#899ad5',
        command=lambda: circle_interface()
    )
    circle_radiobutton.place(relx=20/root.winfo_width(),
                             rely=335/root.winfo_height(),
                             relwidth=circle_radiobutton.winfo_reqwidth()/root.winfo_width(),
                             relheight=circle_radiobutton.winfo_reqheight()/root.winfo_height())

    ellipse_radiobutton = Radiobutton(
        text='Эллипс',
        variable=figure_option,
        value=figure_options[1],
        height=1,
        width=10,
        bg='#899ad5',
        command=lambda: ellipse_interface()
    )
    ellipse_radiobutton.place(relx=170/root.winfo_width(),
                              rely=335/root.winfo_height(),
                              relwidth=ellipse_radiobutton.winfo_reqwidth()/root.winfo_width(),
                              relheight=ellipse_radiobutton.winfo_reqheight()/root.winfo_height())

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
