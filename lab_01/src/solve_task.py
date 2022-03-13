from tkinter import *
from tkinter.messagebox import showerror, showinfo
from sympy.geometry import Point, Triangle
from math import sqrt
from copy import deepcopy
from itertools import combinations

canvas_height = 694
canvas_width = 845


def form_coord_matrix(set_points):
    for i in range(len(set_points)):
        set_points[i] = set_points[i].split(";")

        set_points[i][0] = float(set_points[i][0])
        set_points[i][1] = float(set_points[i][1])


def is_n_gon(polygon):
    comb = combinations(polygon, 3)
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
    comb = combinations(coord_set, n_vertices)
    for i in comb:
        if is_n_gon(i):
            polygons.append(i)


def gauss_area_algorithm(polygon, n_vertices):  # trapezoid formula
    # trapezoid_sum = 0
    # for i in range(0, n_vertices - 1):
    #     trapezoid_sum += abs((polygon[i][0] - polygon[i+1][0]) * (polygon[i][1] + polygon[i+1][1]))
    # return trapezoid_sum / 2
    pos_sum = 0
    neg_sum = 0
    for i in range(0, n_vertices - 1):
        pos_sum += polygon[i][0] * polygon[i+1][1]
        neg_sum += polygon[i+1][0] * polygon[i][1]
    return 0.5 * abs(pos_sum + polygon[n_vertices - 1][0] * polygon[0][1] -
                     neg_sum - polygon[0][0] * polygon[n_vertices - 1][1])



def find_desired_polygon(desired_polygon, polygons, n_vertices):
    max_area = 0
    for polygon in polygons:
        cur_area = gauss_area_algorithm(polygon, n_vertices)
        print('current polygon:', polygon)
        print('its area:', cur_area)
        if cur_area > max_area:
            max_area = cur_area
            print('new poligon arrived:', polygon)
            desired_polygon = deepcopy(polygon)
    return max_area


def section_len(sx, sy, ex, ey):
    return sqrt((sx - ex)**2 + (sy - ey)**2)


def get_vertex(side_name, triangle):
    if side_name == 'ab':
        return triangle[2]
    if side_name == 'ac':
        return triangle[1]
    if side_name == 'bc':
        return triangle[0]


def get_alt_vertex(side_name, triangle):
    if side_name == 'ab' or side_name == 'ac':
        return triangle[0]
    else:
        return triangle[1]


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
        y_indent = 0.05* canvas_height
    elif k_x != 0 and k_y == 0:
        x_indent = 0.05 * canvas_width
        y_indent = 0.5 * canvas_height
    elif k_x != 0 and k_y != 0:
        x_indent = 0.05 * canvas_width
        y_indent = 0.05 * canvas_height
        k_x = min(k_x, k_y)
        k_y = k_x

    return k_x, k_y, x_min, y_min, x_indent, y_indent
        

def draw_all_stuff(canvas, desired_triangle, desired_vertex, dash_vertex, max_x, max_y, kx, ky, x_indent, y_indent):
    ### triangle draw
    print(canvas_height-(desired_triangle[0][1]*ky) + y_indent)                   # debug info
    canvas.create_polygon(desired_triangle[0][0] * kx + x_indent, canvas_height - desired_triangle[0][1]*ky - y_indent,
                          desired_triangle[1][0] * kx + x_indent, canvas_height - desired_triangle[1][1]*ky - y_indent,
                          desired_triangle[2][0] * kx + x_indent, canvas_height - desired_triangle[2][1]*ky - y_indent,
                          fill='white', outline='black')

    ############  draw points
    for vertex in desired_triangle:
        canvas.create_oval(vertex[0]*kx+x_indent - 1, canvas_height - vertex[1]*ky-y_indent - 1,
            vertex[0]*kx+x_indent + 1, canvas_height - vertex[1]*ky-y_indent + 1, width=2)
        canvas.create_text(vertex[0]*kx+x_indent - 15, canvas_height - vertex[1]*ky-y_indent - 15,
            text = "({};{})".format(vertex[0], vertex[1]))

    ### altitude draw
    canvas.create_line(desired_vertex[0]*kx+x_indent, canvas_height - desired_vertex[1]*ky-y_indent,
                         max_x*kx+x_indent, canvas_height - max_y*ky-y_indent, activefill='red')
    canvas.create_line(dash_vertex[0]*kx+x_indent, canvas_height - dash_vertex[1]*ky-y_indent,
                         max_x*kx+x_indent, canvas_height - max_y*ky-y_indent, dash=(5, 1))
    canvas.create_oval(max_x*kx+x_indent - 1, canvas_height - max_y*ky-y_indent - 1,
        max_x*kx+x_indent + 1, canvas_height - max_y*ky-y_indent + 1, width=2)
    canvas.create_text(max_x*kx+x_indent - 15, canvas_height - max_y*ky-y_indent - 15,
            text="({};{})".format(max_x, max_y))


def solve_task(canvas, listbox_set, n_vertices):
    coord_set = list(listbox_set.get(0, END))
    form_coord_matrix(coord_set)

    polygons = []
    form_polygons_list(polygons, coord_set, n_vertices)
    print(polygons)

    if len(polygons) < 1:
        showerror("Ошибка", "Для решения задачи нужно задать хотя бы один n-угольник.")
        return

    desired_polygon = []
    area_of_dp = find_desired_polygon(desired_polygon, polygons, n_vertices)

    print(desired_polygon)
    print(area_of_dp)


    # showinfo(
    #     "Высота",
    #     "Была получена высота длиной {:.1f} , опущенная на сторону {}".format(max_h, alt_side),
    # )

    canvas.delete("all")

    # kx, ky, x_min, y_min, x_indent, y_indent = find_odds_for_drawing(desired_triangle, max_x, max_y)
    # draw_all_stuff(canvas,
    #                desired_triangle, desired_vertex, dash_vertex,
    #                max_x, max_y,
    #                kx, ky,
    #                x_indent, y_indent)
