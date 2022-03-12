from tkinter import *
from tkinter.messagebox import showerror, showinfo

from sympy.geometry import Point, Triangle

from math import sqrt

from copy import deepcopy

canvas_height = 694
canvas_width = 845


def form_coord_matrix(set_points):
    for i in range(len(set_points)):
        set_points[i] = set_points[i].split(";")

        set_points[i][0] = float(set_points[i][0])
        set_points[i][1] = float(set_points[i][1])



def form_triangles_list(triangles, set_points):
    for i in range(len(set_points)):
        for j in range(i + 1, len(set_points)):
            for k in range(j + 1, len(set_points)):
                res = Triangle(
                    Point(set_points[i][0], set_points[i][1]),
                    Point(set_points[j][0], set_points[j][1]),
                    Point(set_points[k][0], set_points[k][1]),
                )

                if type(res) is Triangle:
                    triangle = []

                    triangle.append((float(res.vertices[0][0]), float(res.vertices[0][1])))
                    triangle.append((float(res.vertices[1][0]), float(res.vertices[1][1])))
                    triangle.append((float(res.vertices[2][0]), float(res.vertices[2][1])))

                    triangles.append(triangle)


def section_len(sx, sy, ex, ey):
    return sqrt((sx - ex)**2 + (sy - ey)**2)


def get_zoom_vars(circles):
    c1x_min = circles[0][0][0] - circles[0][0][2]
    c2x_min = circles[1][0][0] - circles[1][0][2]

    c1x_max = circles[0][0][0] + circles[0][0][2]
    c2x_max = circles[1][0][0] + circles[1][0][2]

    c1y_min = circles[0][0][1] - circles[0][0][2]
    c2y_min = circles[1][0][1] - circles[1][0][2]

    c1y_max = circles[0][0][1] + circles[0][0][2]
    c2y_max = circles[1][0][1] + circles[1][0][2]

    x1 = circles[0][0][0]
    y1 = circles[0][0][1]
    x2 = circles[1][0][0]
    y2 = circles[1][0][1]

    k_l = (y2 - y1) / (x2 - x1)
    b = y1 - k_l * x1

    min_x = min(c1x_min, c2x_min, b)
    min_y = min(c1y_min, c2y_min, b)
    max_x = max(c1x_max, c2x_max, b)
    max_y = max(c1y_max, c2y_max, b)

    k_z = canvas_width / max(abs(max_x - min_x), abs(max_y - min_y))

    return [k_z, [min_x, min_y], [max_x, max_y]]


def zoom(circles, zoom_vars):
    k_z = zoom_vars[0]
    min_x = zoom_vars[1][0]
    min_y = zoom_vars[1][1]

    for i in range(len(circles) - 1):
        circles[i][0][2] *= k_z
        for j in range(len(circles[i])):
            circles[i][j][0] = k_z * (circles[i][j][0] - min_x)
            circles[i][j][1] = k_z * (circles[i][j][1] - min_y)


def get_h_of_triangle(a, b, c):                             # a = [0], b = [1], c = [2]
    # s = abs((a.x-c.x)*(b.y-c.y)-(b.x-c.x)*(a.y-c.y))/2
    ab = section_len(a[0], a[1], b[0], b[1])
    bc = section_len(b[0], b[1], c[0], c[1])
    ac = section_len(a[0], a[1], c[0], c[1])

    # use of heron formula for finding max altitude
    semi_perimeter = (ab + bc + ac)/2
    current_area = sqrt(semi_perimeter*(semi_perimeter - ab) *
                        (semi_perimeter - bc)*(semi_perimeter-ac))

    ab_h = 2 * current_area / ab
    ab_coor_x = ((b[0] - a[0]) * (b[1] - a[1]) * (c[1] - a[1]) + a[0] * ((b[1] - a[1])**2) +
                 c[0] * ((b[0] - a[0])**2)) / (((b[1] - a[1])**2) + ((b[0] - a[0])**2))
    if b[0] == a[0]:
        ab_coor_y = c[1]
    else:
        ab_coor_y = (b[1] - a[1]) * (ab_coor_x - a[0]) / (b[0] - a[0]) + a[1]


    bc_h = 2 * current_area / bc
    bc_coor_x = ((c[0] - b[0]) * (c[1] - b[1]) * (a[1] - b[1]) + b[0] * ((c[1] - b[1])**2) +
                 a[0] * ((c[0] - b[0])**2)) / (((c[1] - b[1])**2) + ((c[0] - b[0])**2))
    if c[0] == b[0]:
        bc_coor_y = a[1]
    else:
        bc_coor_y = (c[1] - b[1]) * (bc_coor_x - b[0]) / (c[0] - b[0]) + b[1]


    ac_h = 2 * current_area / ac
    ac_coor_x = ((c[0] - a[0]) * (c[1] - a[1]) * (b[1] - a[1]) + a[0] * ((c[1] - a[1])**2) +
                 b[0] * ((c[0] - a[0])**2)) / (((c[1] - a[1])**2) + ((c[0] - a[0])**2))
    if c[0] == a[0]:
        ac_coor_y = b[1]
    else:
        ac_coor_y = (c[1] - a[1]) * (ac_coor_x - a[0]) / (c[0] - a[0]) + a[1]


    if ab_h > bc_h:
        if ab_h > ac_h:
            return ab_h, ab_coor_x, ab_coor_y, "ab"
        else:
            return ac_h, ac_coor_x, ac_coor_y, "ac"
    else:
        if bc_h > ac_h:
            return bc_h, bc_coor_x, bc_coor_y, "bc"
        else:
            return ac_h, ac_coor_x, ac_coor_y, "ac"


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


def solve_task(canvas, listbox_set, spinBox_N):
    coord_set = list(listb_set.get(0, END))
    form_coord_matrix(coord_set)        # making readable form of coordinates

    n_vertices = spinBox_N.getint

    f_set = list(listb_set.get(0, END))
    form_coord_matrix(f_set)

    triangles = []
    form_triangles_list(triangles, coord_set)

    if len(triangles) < 1:
        showerror("Ошибка", "Для решения задачи нужно задать хотя бы один треугольник.")
        return

    desired_triangle = ((0, 0), (0, 0), (0, 0))
    max_h = 0
    max_x = 0
    max_y = 0
    alt_side = ''

    for triangle in triangles:
        cur_h, cur_x, cur_y, cur_side = get_h_of_triangle(triangle[0], triangle[1], triangle[2])
        if cur_h > max_h:
            desired_triangle = deepcopy(triangle)
            alt_side = cur_side
            max_h = cur_h
            max_x = cur_x
            max_y = cur_y
        
    desired_vertex = get_vertex(alt_side, desired_triangle)
    dash_vertex = get_alt_vertex(alt_side, desired_triangle)


    showinfo(
        "Высота",
        "Была получена высота длиной {:.1f} , опущенная на сторону {}".format(max_h, alt_side),
    )

    canvas.delete("all")

    kx, ky, x_min, y_min, x_indent, y_indent = find_odds_for_drawing(desired_triangle, max_x, max_y)
    print(kx, ky, x_min, y_min, x_indent, y_indent)                                                               # debug info
    draw_all_stuff(canvas, desired_triangle, desired_vertex, dash_vertex, max_x, max_y, kx, ky, x_indent, y_indent)
