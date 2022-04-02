from copy import deepcopy
from tkinter import messagebox
from math import sin, cos

parts_x = []
parts_y = []

parts_x.append([435, 476, 422, 478, 458, 428, 422])
parts_y.append([155, 85,  145, 190, 210, 197, 145])

parts_x.append([422, 360, 403, 428, 478])
parts_y.append([145, 172, 201, 197, 190])

parts_x.append([360, 336, 430, 425, 403, 358, 334, 385, 303, 336])
parts_y.append([172, 254, 281, 256, 201, 366, 316, 268, 297, 254])

parts_x.append([334, 303, 240, 320, 334, 270, 280, 346, 324, 317])
parts_y.append([316, 297, 310, 374, 316, 336, 452, 510, 512, 485])

parts_x.append([240, 221, 182, 215, 198, 170, 182, 189, 235])
parts_y.append([310, 351, 436, 411, 442, 451, 436, 342, 321])

parts_x.append([189, 221, 272, 233, 273, 281, 258, 259, 247, 273])
parts_y.append([342, 351, 359, 444, 493, 516, 516, 496, 487, 493])

parts_x.append([187, 221, 220, 198])
parts_y.append([369, 351, 388, 402])

parts_x.append([272, 220, 215])
parts_y.append([359, 388, 411])

parts_x.append([247, 233])
parts_y.append([487, 444])

parts_x.append([220, 257, 257])
parts_y.append([388, 440, 473])

parts_x.append([257, 320, 319, 295])
parts_y.append([440, 374, 406, 400])

parts_x.append([346, 326, 280, 300, 326])
parts_y.append([510, 479, 452, 446, 479])

parts_x.append([300, 319])
parts_y.append([446, 406])

parts_x.append([320, 358, 416, 461, 454, 437, 437, 449, 437])
parts_y.append([374, 366, 328, 342, 376, 384, 397, 391, 384])

parts_x.append([449, 462, 454])
parts_y.append([391, 385, 376])

parts_x.append([462, 485, 467, 430, 485, 461, 460, 467])
parts_y.append([385, 345, 288, 281, 345, 342, 301, 288])

parts_x.append([460, 447, 416, 385])
parts_y.append([301, 300, 328, 268])

parts_x.append([422, 368, 388, 351, 360, 324, 351])
parts_y.append([145, 128, 160, 146, 172, 149, 146])

parts_x.append([350, 318, 355, 309, 348, 306, 340, 297, 336, 292, 315])
parts_y.append([165, 174, 191, 201, 216, 222, 242, 244, 254, 278, 282])

parts = []


for parts_id in range(len(parts_x)):
    new_poly = []
    for vert_id in range(len(parts_x[parts_id])):
        new_vert = list()
        new_vert.append(parts_x[parts_id][vert_id])
        new_vert.append(parts_y[parts_id][vert_id])

        new_poly.append(new_vert)
    parts.append(new_poly)


original_parts = deepcopy(parts)
prev_parts = deepcopy(parts)


def draw_sides(canvas, vertices_x):
    for i in range(len(parts)):
        for j in range(len(vertices_x[i]) - 1):
            canvas.create_line(parts[i][j], parts[i][j + 1])


def draw_model(canvas):
    canvas.delete("all")
    draw_sides(canvas, parts_x)


def ret_to_prev_action(canvas):
    global parts, prev_parts

    if parts == prev_parts:
        messagebox.showerror(title='Только вперед', message='Назад пути нет .-.')
        return

    parts = deepcopy(prev_parts)

    draw_model(canvas)


def draw_original_model(canvas):
    global parts, prev_parts

    if parts == original_parts:
        messagebox.showerror(title='Лучше уже не будет', message='Куда еще исходнее? 0_o')
        return

    prev_parts = deepcopy(parts)
    parts = deepcopy(original_parts)

    draw_model(canvas)


def deg_to_rad(deg):
    return deg * 3.14159265359 / 180


def point_rotate(point, angle, center):
    angle_rad = deg_to_rad(angle)
    point[0] = (point[0] - center[0]) * cos(angle_rad) - (point[1] - center[1]) * sin(angle_rad) + center[0]
    point[1] = (point[0] - center[0]) * sin(angle_rad) + (point[1] - center[1]) * cos(angle_rad) + center[1]


def point_scale(point, kx, ky, center):
    point[0] = center[0] + (point[0] - center[0]) * kx
    point[1] = center[1] + (point[1] - center[1]) * ky


def point_move(point, dx, dy):
    point[0] += dx
    point[1] += dy


def move_model(canvas, dx, dy):
    global prev_parts
    prev_parts = deepcopy(parts)
    for i in range(len(parts)):
        for j in range(len(parts[i])):
            point_move(parts[i][j], dx, dy)

    draw_model(canvas)


def scale_model(canvas, kx, ky, center):
    global prev_parts
    prev_parts = deepcopy(parts)
    for i in range(len(parts)):
        for j in range(len(parts[i])):
            point_scale(parts[i][j], kx, ky, center)

    draw_model(canvas)


def rotate_model(canvas, angle, center):
    global prev_parts
    prev_parts = deepcopy(parts)
    for i in range(len(parts)):
        for j in range(len(parts[i])):
            point_rotate(parts[i][j], angle, center)

    draw_model(canvas)
