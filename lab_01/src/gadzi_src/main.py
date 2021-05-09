from tkinter import *
from tkinter import messagebox
from itertools import *
from copy import *
from math import *

WINDOW_WIDTH = 1065
WINDOW_HEIGHT = 700
CANVAS_WIDTH = 695
CANVAS_HEIGHT = 695
R = 3
EPS = 1e-6

dots = []
new_dots = []
triangles = []

def input_dot(position, x, y):
    try:
        if (position == END):
            dots.append([float(x.get()), float(y.get())])
            position = len(dots) - 1
        else:
            dot_list.delete(position)
            dots.pop(position)
            dots.insert(position, [float(x.get()), float(y.get())])

        string = "%d. (%-3.2f, %-3.2f)" %(position + 1, float(x.get()), float(y.get()))
        dot_list.insert(position, string)
    except:
        messagebox.showwarning(title = "Ошибка!", message='Введено неверное значение координат')


def change_dot():
    try:
        position = dot_list.curselection()[0]
    except:
        messagebox.showwarning(title = "Ошибка!", message='Сначала выберите точку для изменения')
        return

    dot_window = Tk()
    dot_window.title("Изменить координаты точки")
    dot_window.geometry("450x170")
    dot_window.resizable(FALSE, FALSE)
    dot_window.tk_setPalette("#7BA36D")
    
    x_coord = Label(dot_window, text = "Х", font = ("Arial", 13))
    x_coord.focus()
    x_coord.place(x = 45, y = 25)

    entry_x = Entry(dot_window, bg = "#FFF8FB", font = ("Arial", 13))
    entry_x.place(x = 75, y = 28, width = 100, height = 22)

    y_coord = Label(dot_window, text = "Y", font = ("Arial", 13))
    y_coord.focus()
    y_coord.place(x = 265, y = 25)

    entry_y = Entry(dot_window, bg = "#FFF8FB", font = ("Arial", 13))
    entry_y.place(x = 295, y = 28, width = 100, height = 22)

    add_dot_button = Button(dot_window, text = "Изменить", font=("Arial", 13), bg = "#FFF8FB", command = lambda: input_dot(position, entry_x, entry_y))
    add_dot_button.place(x = 45, y = 100, width = 150)

    exit_button = Button(dot_window, text = "Выйти", font=("Arial", 13), bg = "#FFF8FB", command = dot_window.destroy)
    exit_button.place(x = 265, y = 100, width = 150)

    dot_window.mainloop()


def delete_dot():
    try:
        position = dot_list.curselection()[0]
    except:
        messagebox.showwarning(title = "Ошибка!", message='Сначала выберите точку для изменения')
        return

    dots.pop(position)
    dot_list.delete(0, END)

    for i in range(len(dots)):
        string = "%d. (%-3.2f, %-3.2f)" %(i + 1, dots[i][0], dots[i][1])
        dot_list.insert(i, string)


def add_dot():
    dot_window = Tk()
    dot_window.title("Добавить точку")
    dot_window.geometry("450x170")
    dot_window.resizable(FALSE, FALSE)
    dot_window.tk_setPalette("#7BA36D")
    
    x_coord = Label(dot_window, text = "Х", font = ("Arial", 13))
    x_coord.focus()
    x_coord.place(x = 45, y = 25)

    entry_x = Entry(dot_window, bg = "#FFF8FB", font = ("Arial", 13))
    entry_x.place(x = 75, y = 28, width = 100, height = 22)

    y_coord = Label(dot_window, text = "Y", font = ("Arial", 13))
    y_coord.focus()
    y_coord.place(x = 265, y = 25)

    entry_y = Entry(dot_window, bg = "#FFF8FB", font = ("Arial", 13))
    entry_y.place(x = 295, y = 28, width = 100, height = 22)

    add_dot_button = Button(dot_window, text = "Добавить точку", font=("Arial", 13), bg = "#FFF8FB", command = lambda: input_dot(END, entry_x, entry_y))
    add_dot_button.place(x = 45, y = 100, width = 150)

    exit_button = Button(dot_window, text = "Выйти", font=("Arial", 13), bg = "#FFF8FB", command = dot_window.destroy)
    exit_button.place(x = 265, y = 100, width = 150)

    dot_window.mainloop()


def coefficients_scale(dots_copy):
    x_min = dots_copy[0][0]
    x_max = dots_copy[0][0]
    
    y_min = dots_copy[0][1]
    y_max = dots_copy[0][1]

    for dot in dots_copy:
        x_min = min(dot[0], x_min)
        x_max = max(dot[0], x_max)

        y_min = max(dot[1], y_min)
        y_max = min(dot[1], y_max)

    y_min = return_axis(y_min)
    y_max = return_axis(y_max)

    k_x = (CANVAS_WIDTH * 0.9) / (x_max - x_min) if x_max != x_min else 0
    k_y = (CANVAS_HEIGHT * 0.9) / (y_max - y_min) if y_max != y_min else 0

    if k_x == 0 and k_y == 0:
        x_indent = 0.5 * CANVAS_WIDTH
        y_indent = 0.5 * CANVAS_HEIGHT
    elif k_x == 0 and k_y != 0:
        x_indent = 0.5 * CANVAS_WIDTH
        y_indent = 0.05* CANVAS_HEIGHT
    elif k_x != 0 and k_y == 0:
        x_indent = 0.05 * CANVAS_WIDTH
        y_indent = 0.5 * CANVAS_HEIGHT
    elif k_x != 0 and k_y != 0:
        x_indent = 0.05 * CANVAS_WIDTH
        y_indent = 0.05 * CANVAS_HEIGHT
        k_x = min(k_x, k_y)
        k_y = k_x

    return k_x, k_y, x_min, y_min, x_indent, y_indent


def change_axis(y):
    return y * (-1) + CANVAS_HEIGHT

def return_axis(y):
    return (CANVAS_HEIGHT - y)


def solve_task():
    triangles.clear()
    new_dots.clear()
    MainCanvas.delete("all")
    dots_copy = deepcopy(dots)

    if len(dots) == 0:
        messagebox.showerror(title = "Ошибка", message = "Точки не введены!")
        return

    for i in range(len(dots_copy)):
        dots_copy[i][1] = change_axis(dots_copy[i][1])

    k_x, k_y, x_min, y_min, x_indent, y_indent = coefficients_scale(dots_copy)
    pos = 0

    for dot in dots_copy:
        pos = pos + 1
        x = k_x * (dot[0] - x_min) + x_indent
        y = change_axis(k_y * (return_axis(dot[1]) - y_min) + y_indent)

        new_dots.append([x, y])

    dots_copy.clear()
    dots_copy = deepcopy(dots)
    
    for triangle in combinations(dots_copy, 3):
        a, b, c = triangle_exist_check(triangle)

        if (a != 0 and b != 0 and c != 0):
            triangles.append(triangle)

    if len(triangles) == 0:
        messagebox.showerror(title = "Ошибка", message = "Для данного набора точек невозможно построить треугольник, так как точки лежать на одной прямой")
        return

    x0, y0, position, sum = find_max_distance()

    draw_triangle(x0, y0, position)
    output_result(sum, triangles, position, x0, y0)


def draw_triangle(x0, y0, position):
    MainCanvas.delete("all")

    triangle_dots = deepcopy(triangles[position])
    triangle_dots = list(triangle_dots)
    triangle_dots.append([x0, y0])
    triangle_dots.append([0, 0])

    k_x, k_y, x_min, y_min, x_indent, y_indent = coefficients_scale(triangle_dots)
    pos = 0

    triangle_dots.pop(4)

    for dot in triangle_dots:
        pos = pos + 1
        dot[0] = k_x * (dot[0] - x_min) + x_indent
        dot[1] = k_y * (return_axis(dot[1]) - y_min) + y_indent

        x = dot[0]
        y = dot[1]

        MainCanvas.create_oval(x - R, y - R, x + R, y + R, width = 1, fill = "black", outline = "black")
        MainCanvas.create_text(x - 15, y - 15, text = "%d" %(pos))

    x_axis = change_axis(k_y * (return_axis(0) - y_min) + y_indent)
    y_axis = k_x * (0 - x_min) + x_indent

    MainCanvas.create_line(-CANVAS_WIDTH, CANVAS_HEIGHT - x_axis, CANVAS_WIDTH, CANVAS_HEIGHT - x_axis, width = 2, fill = "black")
    MainCanvas.create_line(abs(y_axis), -CANVAS_HEIGHT, abs(y_axis), CANVAS_HEIGHT, width = 2, fill = "black")

    MainCanvas.create_line(triangle_dots[0], triangle_dots[3], width = 2, fill = "red")
    MainCanvas.create_line(triangle_dots[1], triangle_dots[3], width = 2, fill = "red")
    MainCanvas.create_line(triangle_dots[2], triangle_dots[3], width = 2, fill = "red")
    
    MainCanvas.create_line(triangle_dots[0], triangle_dots[1], width = 2, fill = "green")
    MainCanvas.create_line(triangle_dots[0], triangle_dots[2], width = 2, fill = "green")
    MainCanvas.create_line(triangle_dots[1], triangle_dots[2], width = 2, fill = "green")


def find_max_distance():
    pos = 0
    index = 0
    max = 0 

    for triangle in triangles:
        x1 = triangle[0][0]
        y1 = triangle[0][1]
        x2 = triangle[1][0]
        y2 = triangle[1][1]
        x3 = triangle[2][0]
        y3 = triangle[2][1]

        x0, y0 = find_height_inters(x1, y1, x2, y2, x3, y3)

        if (abs(y0) + abs(x0) > max):
            max = abs(y0) + abs(x0)
            index = pos

        pos = pos + 1

    return x0, y0, index, max


def find_height_inters(x1, y1, x2, y2, x3, y3):
    '''
        Функция для нахождения точки пересечения высот.
    '''
    # Уравнение прямой рассматривается как Dy = Kx + B

    # Коэффициенты прямой BC
    # Если точки В и С лежат на одной вертикальной прямой
    if abs((x3 - x2)) <= EPS:
        k_bc = 1
        b_bc = -x3
        d_bc = 0
    else:
        k_bc = (y3 - y2) / (x3 - x2)
        b_bc = y3 - (k_bc * x3)
        d_bc = 1
    
    # Коэффициенты высоты из А
    # Когда прамая ВС лежит параллельно Ох
    if abs(k_bc) <= EPS:
        k_ah = 1
        b_ah = -x1
        d_ah = 0     
    # Когда ВС параллельна Оу
    elif abs(k_bc - 1) <= EPS and abs(d_bc) <= EPS:
        k_ah = 0
        b_ah = y1
        d_ah = 1
    else:
        k_ah = -1 / k_bc
        b_ah = y1 - k_ah * x1
        d_ah = 1

    # Коэффициенты прямой АС
    # Если точки A и С лежат на одной вертикальной прямой
    if abs((x3 - x1)) <= EPS:
        k_ac = 1
        b_ac = -x3
        d_ac = 0
    else:
        k_ac = (y3 - y1) / (x3 - x1)
        b_ac = y3 - (k_ac * x3)
        d_ac = 1

    # Коэффициенты высоты из В
    # Когда прамая АС лежит параллельно Ох
    if abs(k_ac) <= EPS:
        k_bh = 1
        b_bh = -x2
        d_bh = 0
    # Когда АС параллельна Оу
    elif abs(k_ac - 1) <= EPS and abs(d_ac) <= EPS:
        k_bh = 0
        b_bh = y2
        d_bh = 1
    else:
        k_bh = -1 / k_ac
        b_bh = y2 - k_bh * x2
        d_bh = 1

    # Нахождение координаты х (тока пересечение высот)
    x0 = (d_ah * b_bh - d_bh * b_ah) / (d_bh * k_ah - d_ah * k_bh)

    # Подставляем найденное х в уравнение той прямой,
    # которая НЕ параллельна Оу
    y0 = k_ah * x0 + b_ah if abs(d_bh) <= EPS else k_bh * x0 + b_bh

    return x0, y0


def output_result(sum, triangles, position, x0, y0):
    messagebox.showinfo("Результат работы программы", "Вершины треугольника:\
    \n[%.2f, %.2f]\n[%.2f, %.2f]\n[%.2f, %.2f]\n\
Координаты точки пересечения вершин треугольника: [%.2f, %.2f]\n\
Максимальная сумма расстояний от точки пересечения высот треугольника до осей координат: %.2f"\
    %(triangles[position][0][0], triangles[position][0][1], triangles[position][1][0], triangles[position][1][1], \
    triangles[position][2][0], triangles[position][2][1], x0, y0, sum))

def triangle_exist_check(triangle):
    x1 = triangle[0][0]
    y1 = triangle[0][1]

    x2 = triangle[1][0]
    y2 = triangle[1][1]

    x3 = triangle[2][0]
    y3 = triangle[2][1]

    a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    if a < b + c and b < a + c and c < a + b:
        return a, b, c
    else:
        return 0, 0, 0


def clear_field():
    dot_list.delete(0, END)
    dots.clear()
    MainCanvas.delete("all")


def show_task():
    messagebox.showinfo(title = "Условие задачи", message = "На плоскости дано множество точек, найти такой треугольник с вершинами в этих точках,\
    у которого сумма расстояний от точки пересечения высот до координатных осей максимальна")

if __name__ == "__main__":
    window = Tk()
    window.geometry("1065x700")
    window.title("Лабораторная №1")
    window.tk_setPalette("#7BA36D")
    window.resizable(FALSE, FALSE)

    MainCanvas = Canvas(window, width=695, height=695, bg = "#F0FAEC")
    MainCanvas.place(x = 365, y = 0)

    MainCanvas.bind('<1>')

    add_dot_button = Button(text="Добавить точку", font=("Arial", 13), bg = "#FFF8FB", command = lambda: add_dot())
    add_dot_button.place(x=25, y=15, width = 150)

    delete_dot_button = Button(text="Удалить точку", font=("Arial", 13), bg = "#FFF8FB", command = lambda: delete_dot())
    delete_dot_button.place(x=200, y=15, width = 150)

    change_dot_button = Button(text="Изменить точку", font=("Arial", 13), bg = "#FFF8FB", command = lambda: change_dot())
    change_dot_button.place(x=25, y=85, width = 150)

    delete_button = Button(text="Очистить поле", font=("Arial", 13), bg = "#FFF8FB", command = lambda: clear_field())
    delete_button.place(x=200, y=85, width=150)

    task_button = Button(text="Решить задачу", font=("Arial", 13), bg = "#FFF8FB", command = lambda: solve_task())
    task_button.place(x=25, y=650, width=325)

    dot_list = Listbox(window, bg = "#F1F0F0", font=("Arial", 13))
    dot_list.place(x = 25, y = 140, width = 325, height = 500)

    show_task()

    window.mainloop()