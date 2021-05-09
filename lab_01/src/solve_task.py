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


def draw_coords(canvas, magic_circles, circles):
    coord_size = 12
    indent = 5

    for i in range(len(magic_circles) - 1):
        for j in range(len(magic_circles[i])):
            canvas.create_text(
                magic_circles[i][j][0],
                magic_circles[i][j][1] + indent,
                text="({:.1f},{:.1f})".format(circles[i][j][0], circles[i][j][1]),
                font=("Times new roman", coord_size),
            )



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



def triangle_to_plot(triangles):
    coords = ["temp_triangle"]
#       ????????
    for i in range(len(triangles)):
        for j in range(i + 1, len(triangles)):
            x1 = triangles()
    return coords


def section_len(sx, sy, ex, ey):
    return sqrt((sx - ex)**2 + (sy - ey)**2)



def form_canvas_coords(circles):
    for i in range(len(circles) - 1):
        for j in range(len(circles[i])):
            circles[i][j][1] *= -1
            circles[i][j][1] += canvas_width


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
        

# def draw_all_stuff(desired_triangle, altitude_end)
#     ############  1st  point draw
#     canvas.create_oval(desired_triangle[0][0] - 1, canvas_height - desired_triangle[0][1] - 1,
#         desired_triangle[0][0] + 1, canvas_height - desired_triangle[0][1] + 1, width=2)
#     ############  2nd
#     canvas.create_oval(desired_triangle[1][0] - 1, canvas_height - desired_triangle[1][1] - 1,
#         desired_triangle[1][0] + 1, canvas_height - desired_triangle[1][1] + 1, width=2)
#     ############  3rd
#     canvas.create_oval(desired_triangle[2][0] - 1, canvas_height - desired_triangle[2][1] - 1,
#         desired_triangle[2][0] + 1, canvas_height - desired_triangle[2][1] + 1, width=2)
#     ############

#     ### triangle draw
#     canvas.create_polygon(desired_triangle[0][0], canvas_height - desired_triangle[0][1],
#                           desired_triangle[1][0], canvas_height - desired_triangle[1][1],
#                           desired_triangle[2][0], canvas_height - desired_triangle[2][1],
#                           fill='white', outline='black')

#     ### altitude draw
#     desired_vertex = get_vertex(alt_side, desired_triangle, max_x, max_y)
#     canvas.create_line(desired_vertex[0], canvas_height - desired_vertex[1],
#                          max_x, canvas_height - max_y, activefill='red')
#     dash_vertex = get_alt_vertex(alt_side, desired_triangle)
#     canvas.create_line(dash_vertex[0], canvas_height - dash_vertex[1],
#                          max_x, canvas_height - max_y, dash=(5, 1))
#     canvas.create_oval(max_x - 1, canvas_height - max_y - 1,
#         max_x + 1, canvas_height - max_y + 1, width=2)


def solve_task(canvas, listb_set):
    coord_set = list(listb_set.get(0, END))
    form_coord_matrix(coord_set)        # making readable form of coordinates

    f_set = list(listb_set.get(0, END))
    form_coord_matrix(f_set)

    triangles = []
    form_triangles_list(triangles, coord_set)

    print("triangles before check: ", triangles)                                                                # debug info
    if len(triangles) < 1:
        showerror("Ошибка", "Для решения задачи нужно задать хотя бы один треугольник.")
        return

    desired_triangle = ((0, 0), (0, 0), (0, 0))
    max_h = 0
    max_x = 0
    max_y = 0
    alt_side = ''

    print("triangles[0]=", triangles[0])                                                                        # debug info
    for triangle in triangles:
        print("triangle = ", triangle)                                                                          # debug info
        print("triangle[0]=", triangle[0], "    ;triangle[1]=", triangle[1], "   ;triangle[2]=", triangle[2])   # debug info
        cur_h, cur_x, cur_y, cur_side = get_h_of_triangle(triangle[0], triangle[1], triangle[2])
        if cur_h > max_h:
            desired_triangle = deepcopy(triangle)
            alt_side = cur_side
            max_h = cur_h
            max_x = cur_x
            max_y = cur_y


    showinfo(
        "Высота",
        "Была получена высота длиной {:.1f} , опущенная на сторону {}".format(max_h, alt_side),
    )

    canvas.delete("all")

    ############  1st  point draw
    canvas.create_oval(desired_triangle[0][0] - 1, canvas_height - desired_triangle[0][1] - 1,
        desired_triangle[0][0] + 1, canvas_height - desired_triangle[0][1] + 1, width=2)
    ############  2nd
    canvas.create_oval(desired_triangle[1][0] - 1, canvas_height - desired_triangle[1][1] - 1,
        desired_triangle[1][0] + 1, canvas_height - desired_triangle[1][1] + 1, width=2)
    ############  3rd
    canvas.create_oval(desired_triangle[2][0] - 1, canvas_height - desired_triangle[2][1] - 1,
        desired_triangle[2][0] + 1, canvas_height - desired_triangle[2][1] + 1, width=2)
    ############

    ### triangle draw
    canvas.create_polygon(desired_triangle[0][0], canvas_height - desired_triangle[0][1],
                          desired_triangle[1][0], canvas_height - desired_triangle[1][1],
                          desired_triangle[2][0], canvas_height - desired_triangle[2][1],
                          fill='white', outline='black')

    ### altitude draw
    desired_vertex = get_vertex(alt_side, desired_triangle)
    canvas.create_line(desired_vertex[0], canvas_height - desired_vertex[1],
                         max_x, canvas_height - max_y, activefill='red')
    dash_vertex = get_alt_vertex(alt_side, desired_triangle)
    canvas.create_line(dash_vertex[0], canvas_height - dash_vertex[1],
                         max_x, canvas_height - max_y, dash=(5, 1))
    canvas.create_oval(max_x - 1, canvas_height - max_y - 1,
        max_x + 1, canvas_height - max_y + 1, width=2)
    

    '''zoom_vars = get_zoom_vars(magic_circles)

    draw_angle(canvas, magic_circles, zoom_vars)
    zoom(magic_circles, zoom_vars)
    draw_split_line(canvas, magic_circles)

    form_canvas_coords(magic_circles)

    draw_points(canvas, magic_circles)
    draw_circles(canvas, magic_circles)
    draw_ordinate(canvas, zoom_vars)
    draw_coords(canvas, magic_circles, circles)'''
