from tkinter import *
from tkinter.messagebox import showerror, showinfo
from sympy.geometry import Point, Triangle
from math import sqrt
from copy import deepcopy
from itertools import permutations

canvas_height = 694
canvas_width = 845


def form_coord_matrix(set_points):
    for i in range(len(set_points)):
        set_points[i] = set_points[i].split(";")

        set_points[i][0] = float(set_points[i][0])
        set_points[i][1] = float(set_points[i][1])


def is_n_gon(polygon):
    comb = permutations(polygon, 3)
    for i in comb:
        if i[2][0] == i[0][0] == i[1][0] or \
                i[2][1] == i[0][1] == i[1][1]:
            return False
        elif i[1][0] - i[0][0] == 0 or \
                i[1][1] - i[0][1] == 0:
            continue
        elif (i[2][0] - i[0][0]) / (i[1][0] - i[0][0]) == \
                (i[2][1] - i[0][1]) / (i[1][1] - i[0][1]):  # check if 3 points lie on the same line
            return False
    return True


def form_polygons_list(polygons, coord_set, n_vertices):
    comb = permutations(coord_set, n_vertices)
    for i in comb:
        if is_n_gon(i):
            polygons.append(i)


def gauss_area_algorithm(polygon, n_vertices):  # trapezoid formula
    pos_sum = 0
    neg_sum = 0
    for i in range(0, n_vertices - 1):
        pos_sum += polygon[i][0] * polygon[i + 1][1]
        neg_sum += polygon[i + 1][0] * polygon[i][1]
    return 0.5 * abs(pos_sum + polygon[n_vertices - 1][0] * polygon[0][1] -
                     neg_sum - polygon[0][0] * polygon[n_vertices - 1][1])


def find_desired_polygon(desired_polygon, polygons, n_vertices):
    max_area = 0
    for polygon in polygons:
        cur_area = gauss_area_algorithm(polygon, n_vertices)
        if cur_area > max_area:
            max_area = cur_area
            desired_polygon.clear()
            for i in polygon:
                desired_polygon.append(i)
    return max_area


def find_coefs_for_drawing(desired_polygon, canvas):
    xmin = canvas.winfo_reqwidth()
    xmax = -canvas.winfo_reqwidth()

    ymin = canvas.winfo_reqheight()
    ymax = -canvas.winfo_reqheight()

    for vertex in desired_polygon:
        if vertex[0] < xmin:
            xmin = vertex[0]
        if vertex[0] > xmax:
            xmax = vertex[0]
        if vertex[1] < ymin:
            ymin = vertex[1]
        if vertex[1] > ymax:
            ymax = vertex[1]

    return xmin, xmax, ymin, ymax


def find_odds_for_drawing(desired_triangle, max_x, max_y):
    x_min = min(desired_triangle[0][0], desired_triangle[1][0], desired_triangle[2][0], max_x)
    x_max = max(desired_triangle[0][0], desired_triangle[1][0], desired_triangle[2][0], max_x)

    y_min = min(desired_triangle[0][1], desired_triangle[1][1], desired_triangle[2][1], max_y)
    y_max = max(desired_triangle[0][1], desired_triangle[1][1], desired_triangle[2][1], max_y)

    k_x = (canvas_width * 0.9) / (x_max - x_min) if x_max != x_min else 0
    k_y = (canvas_height * 0.9) / (y_max - y_min) if y_max != y_min else 0

    # x_indent = 0.05 * canvas_width
    # y_indent = 0.05 * canvas_height

    if k_x == 0 and k_y == 0:
        x_indent = 0.5 * canvas_width
        y_indent = 0.5 * canvas_height
    elif k_x == 0 and k_y != 0:
        x_indent = 0.5 * canvas_width
        y_indent = 0.05 * canvas_height
    elif k_x != 0 and k_y == 0:
        x_indent = 0.05 * canvas_width
        y_indent = 0.5 * canvas_height
    elif k_x != 0 and k_y != 0:
        x_indent = 0.05 * canvas_width
        y_indent = 0.05 * canvas_height
        k_x = min(k_x, k_y)
        k_y = k_x

    return k_x, k_y, x_min, y_min, x_indent, y_indent


def make_printable_coords(printable_polygon, xmin, xmax, ymin, ymax, canvas):
    for vertex in printable_polygon:
        vertex[0] = 100 + (vertex[0] - xmin) * ((canvas.winfo_reqwidth() - 100) - 100) / (xmax - xmin)
        vertex[1] = canvas.winfo_reqheight() - 100 - \
                    (vertex[1] - ymin) * ((canvas.winfo_reqheight() - 100) - 100) / (ymax - ymin)


def draw_points(canvas, vertices, printable_vertices):
    for i in range(len(vertices)):
        canvas.create_oval(printable_vertices[i][0], printable_vertices[i][1],
                           printable_vertices[i][0], printable_vertices[i][1], width=5)
        canvas.create_text(printable_vertices[i][0] - 15, printable_vertices[i][1] - 15,
                           text="({};{})".format(vertices[i][0], vertices[i][1]))


def draw_everything(canvas, desired_polygon, printable_polygon):
    canvas.create_polygon(printable_polygon, fill='green', outline='black', activefill='cyan')
    draw_points(canvas, desired_polygon, printable_polygon)


def solve_task(canvas, listbox_set, n_vertices):
    coord_set = list(listbox_set.get(0, END))
    form_coord_matrix(coord_set)

    polygons = []
    form_polygons_list(polygons, coord_set, n_vertices)

    if len(polygons) < 1:
        showerror("Ошибка", "Для решения задачи нужно задать хотя бы один n-угольник.")
        return

    desired_polygon = []
    area_of_dp = find_desired_polygon(desired_polygon, polygons, n_vertices)

    xmin, xmax, ymin, ymax = find_coefs_for_drawing(desired_polygon, canvas)

    showinfo(
        "Площадь",
        "Была получена площадь в {:.1f} ед.".format(area_of_dp)
    )

    printable_polygon = deepcopy(desired_polygon)
    make_printable_coords(printable_polygon, xmin, xmax, ymin, ymax, canvas)

    canvas.delete("all")
    canvas.update()
    draw_everything(canvas, desired_polygon, printable_polygon)
