from tkinter import *



WIN_WIDTH = 1300
WIN_HEIGHT = 700

CV_WIDE = 700
CV_HEIGHT = 700

#global dots1_block


dots1_list = []

def del_dot():
    place = dots1_block.curselection()[0]
    dots1_list.pop(place)
    dots1_block.delete(ANCHOR)


def change_dot():
    place = dots1_block.curselection()[0]
    #coords = [float(num) for num in dots1_block.get(place).split(",")]

    dot_win = Tk()
    dot_win.geometry("200x200")
    dot_win.resizable(False, False)

    dot_x = Entry(dot_win)
    dot_x.focus()
    #dot_x.insert(END, coords[0])
    dot_x.place(x = 10, y = 30)

    dot_y = Entry(dot_win)
    #dot_y.insert(END, coords[1])
    dot_y.place(x = 10, y = 70)

    add_but = Button(dot_win, text = "Change dot", command = lambda: read_dot(place, dot_x, dot_y))
    add_but.place(x = 50, y = 120)

    dot_win.mainloop()


def read_dot(place, dot_x, dot_y):
    try:
        coords_dot = []

        coords_dot.append(float(dot_x.get()))
        coords_dot.append(float(dot_y.get()))
        
        if (place != END): # for change dot
            dots1_block.delete(place)
            dots1_list.pop(place)
            dots1_list.insert(place, coords_dot)
        else:
            dots1_list.append(coords_dot)
            place = len(dots1_list) - 1

        dot_str = "%d) (%-3.1f,%-3.1f)" %(place + 1, float(dot_x.get()), float(dot_y.get()))
        dots1_block.insert(place, dot_str)

        print(dots1_list)
    except:
        print("Mistake!")


def add_dot():
    dot_win = Tk()
    dot_win.geometry("200x200")
    dot_win.resizable(False, False)

    dot_x = Entry(dot_win)
    dot_x.focus()
    dot_x.place(x = 10, y = 30)

    dot_y = Entry(dot_win)
    dot_y.place(x = 10, y = 70)

    add_but = Button(dot_win, text = "Add dot", command = lambda: read_dot(END, dot_x, dot_y))
    add_but.place(x = 50, y = 120)

    dot_win.mainloop()


if __name__ == "__main__":
    win = Tk()
    win['bg'] = 'lightblue'
    win.geometry("%dx%d" %(WIN_WIDTH, WIN_HEIGHT))
    win.title("Линия, соединяющая все вокруг")
    win.resizable(False, False)

    canvas_win = Canvas(win, width = CV_WIDE, height = CV_HEIGHT, bg = "lightgrey")
    canvas_win.place(x = 300, y = 0)


    dots1_block = Listbox()
    dots1_block.bind("<1>", print("Yes"))
    dots1_block.configure(font="-family {Consolas} -size 14")
    dots1_block.place(x = 40, y = 30)


    add1 = Button(text = "Add", command = lambda: add_dot())
    add1.place(x = 15, y = 300)

    del1 = Button(text = "Del", command = lambda: del_dot())
    del1.place(x = 150, y = 300)

    chg1 = Button(text = "Chg", command = lambda: change_dot())
    chg1.place(x = 250, y = 300)
















    #canvas_win.bind('<1>', click_point)
    #canvas_win.bind('<3>', click_circle)

    # Point
    # point_text = Label(win, text = "Построить точку", font = ("Times New Roman", 16), relief = SUNKEN)
    # point_text.place(x = 650, y = 5)


    # point_text1 = Label(win, text = "Построить точку", font = ("Times New Roman", 16), relief = RIDGE)
    # point_text1.place(x = 650, y = 60)

    # point_text2 = Label(win, text = "Построить точку", font = ("Times New Roman", 16), relief = RAISED)
    # point_text2.place(x = 650, y = 120)


    # point_text3 = Label(win, text = "Построить точку", font = ("Times New Roman", 16), relief = GROOVE)
    # point_text3.place(x = 650, y = 180)


    # x_point_text = Label(win, text = "X:", font = ("Times New Roman", 14))
    # x_point_text.place(x = 615, y = 35)

    # x_point = Entry(win, font = 14)
    # x_point.place(x = 640, y = 35, width = 150, height = 25)

    # y_point_text = Label(win, text = "Y:", font = ("Times New Roman", 14))
    # y_point_text.place(x = 615, y = 70)

    # y_point = Entry(win, font = 14)
    # y_point.place(x = 640, y = 70, width = 150, height = 25)

    # point_place = Button(text = "Поставить точку", font = ("Times New Roman", 14))#, command = build_point)
    # point_place.place(x = 650, y = 110)

    # #Circle
    # circle_text = Label(win, text = "Построить окружность", font = ("Times New Roman", 16))
    # circle_text.place(x = 650, y = 200)

    # x_circle_text = Label(win, text = "X:", font = ("Times New Roman", 14))
    # x_circle_text.place(x = 615, y = 235)

    # x_circle = Entry(win, font = 14)
    # x_circle.place(x = 640, y = 235, width = 150, height = 25)

    # y_circle_text = Label(win, text = "Y:", font = ("Times New Roman", 14))
    # y_circle_text.place(x = 615, y = 270)

    # y_circle = Entry(win, font = 14)
    # y_circle.place(x = 640, y = 270, width = 150, height = 25)

    # r_circle_text = Label(win, text = "R:", font = ("Times New Roman", 14))
    # r_circle_text.place(x = 615, y = 300)

    # r_circle = Entry(win, font = 14)
    # r_circle.place(x = 640, y = 300, width = 150, height = 25)

    # circle_place = Button(text = "Поставить круг", font = ("Times New Roman", 14))#, command = build_circle)
    # circle_place.place(x = 650, y = 340)

    # # Buttons

    # text = Label(text = "_" * 30 , font = ("Times New Roman", 14), bg = "lightblue")
    # text.place(x = 602, y = 460)

    # clear_button = Button(text = "Очистить поле", font = ("Times New Roman", 16))#, command = clear_all)
    # clear_button.place(x = 670, y = 410)

    # build_button = Button(text = "Построить прямую", font = ("Times New Roman", 16), bg = "lightblue")#, command = build_line)
    # build_button.place(x = 650, y = 500)

    win.mainloop()