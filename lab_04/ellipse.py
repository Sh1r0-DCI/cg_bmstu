from math import sin, cos, floor, fabs
import matplotlib
import colorutils


def deg_to_rad(deg):
    return deg * 3.14159265359 / 180


def sign(difference):
    if difference < 0:
        return -1
    elif difference == 0:
        return 0
    else:
        return 1


def choose_color(color, intense):
    return colorutils.Color(color) + (intense, intense, intense)


def draw_pixel(canvas, point, color):
    canvas.create_line(point[0], point[1], point[0] + 1, point[1], fill=color)


def draw_line(canvas, points, color):
    for point in points:
        draw_pixel(canvas, point, color)


def draw_aa_line(canvas, points):
    for point in points:
        print(point[2])
        canvas.create_line(point[0], point[1], point[0] + 1, point[1], fill=point[2].hex)
