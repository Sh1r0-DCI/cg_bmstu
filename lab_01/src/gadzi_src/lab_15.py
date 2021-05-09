from math import *
from tkinter import *
from tkinter import messagebox

coordinates = []

def click(event):
    x = event.x
    y = event.y
    coordinates.append([x, y])
    R = 3.5
    MainCanvas.create_oval(x - R, y - R, x + R, y + R, width=1.2, fill =
    '#a92dd2')

def delete():
    coordinates.clear()
    MainCanvas.delete("all")

def place_dot():
    bastard = '1234567890.'
    x = entry_x.get()
    y = entry_y.get()
    for i in range(len(x)):
        if (x[i] not in bastard):
            messagebox.showinfo(message='Введено неверное значение  Х '
                                        'координаты')
            entry_x.delete(0, END)
            return
    for i in range(len(y)):
        if (y[i] not in bastard):
            messagebox.showinfo(message='Введено неверное значение  Y '
                                        'координаты')
            entry_y.delete(0, END)
            return


    R = 3.5
    coordinates.append([x, y])
    MainCanvas.create_oval(float(x) - R, float(y) - R, float(x) + R, float(y)
                           + R,
    width=1.2, fill="#a92dd2")

def build_circle():
    R1 = entry_first.get()
    R2 = entry_second.get()
    bastard = '1234567890.'
    for i in range(len(R1)):
        if (R1[i] not in bastard):
            messagebox.showinfo(message='Введено неверное значение первого '
                                        'рариуса')
            entry_first.delete(0, END)
            return
    for i in range(len(R2)):
        if (R2[i] not in bastard):
            messagebox.showinfo(message='Введено неверное значение второго '
                                        'рариуса')
            entry_second.delete(0, END)
            return
    if len(coordinates) < 1:
        messagebox.showinfo(message="Указано менее двух точек")
    else:
        R1 = float(R1)
        R2 = float(R2)
        for i in range(len(coordinates)):
            x1 = int(coordinates[i][0])
            y1 = int(coordinates[i][1])
            count_1 = calculation(i, R1)
            for j in range(len(coordinates)):
                if i == j:
                    continue
                x2 = int(coordinates[j][0])
                y2 = int(coordinates[j][1])
                count_2 = calculation(j, R2)
                if count_1 == count_2 and count_1 != 0:
                    MainCanvas.create_oval(x1 - R1, y1 - R1, x1 + R1,
                                           y1 + R1, width=2)
                    MainCanvas.create_oval(x2 - R2, y2 - R2, x2 + R2,
                                           y2 + R2, width=2)
                    return 0


def calculation(i_0, R):
    count = 0
    x_0 = int(coordinates[i_0][0])
    y_0 = int(coordinates[i_0][1])
    for i in range(len(coordinates)):
        if i == i_0:
            continue
        x = int(coordinates[i][0])
        y = int(coordinates[i][1])
        if pow(x - x_0, 2) + pow(y - y_0, 2) <= R*R:
            count += 1
    return count


root = Tk()
root.geometry("700x600")
root.title("Построение окружностей, содержащих одинаковое количество точек")
root.resizable(False, False)

MainCanvas = Canvas(root, width=700, height=500, bg = "lightgray")
MainCanvas.place(x = 0, y = 175)

MainCanvas.bind('<1>', click)

X = Label(root, text="X coordinate", font = ("Times New Roman", 14))
X.place(x=30, y=10)

Y = Label(root, text="Y coordinate", font = ("Times New Roman", 14))
Y.place(x=30, y=50)

entry_x = Entry(root)
entry_x.place(width=125, height=25, x=150, y=10)

entry_y = Entry(root)
entry_y.place(width=125, height=25, x=150, y=50)

first_circle = Label(root, text='First circle radius',
font=("Times New Roman", 14))
first_circle.place(x=385, y=10)

second_circle = Label(root, text='Second circle radius',
font=("Times New Roman", 14))
second_circle.place(x=385, y=50)

entry_first = Entry(root)
entry_first.place(width=125, height=25, x=545, y=10)

entry_second = Entry(root)
entry_second.place(width=125, height=25, x=545, y=50)

place_dot_button = Button(text="Place dot", font=("Times New Roman",
14), command=place_dot)
place_dot_button.place(x=30, y=110)

build_circle_button = Button(text="Draw circles", font=("Times New Roman",
14), command=build_circle)
build_circle_button.place(x=562, y=110, width=108)

delete_button = Button(text="Clear", font=("Times New Roman",
14), command=delete)
delete_button.place(x=299, y=110, width=56)


root.mainloop()