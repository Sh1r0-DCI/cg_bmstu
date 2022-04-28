from math import sin, cos, floor, fabs
import matplotlib


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
    return hex(color) + (intense*10000 + intense*100 + intense)


def draw_pixel(canvas, point, color):
    canvas.create_line(point[0], point[1], point[0] + 1, point[1], fill=color)


def draw_line(canvas, points, color):
    for point in points:
        draw_pixel(canvas, point, color)


def draw_aa_line(canvas, points):
    for point in points:
        canvas.create_line(point[0], point[1], point[0] + 1, point[1], fill=point[2].hex)


def dda_method(x1, y1, x2, y2, step_count=False):
    if (x2 - x1 == 0) and (y2 - y1 == 0):
        return [[x1, y1]]

    dx = x2 - x1
    dy = y2 - y1

    if (abs(dx) >= abs(dy)):
        l = abs(dx)
    else:
        l = abs(dy)

    dx /= l
    dy /= l

    x = round(x1)
    y = round(y1)

    dots = [[round(x), round(y)]]

    i = 1

    steps = 0

    while (i < l):

        x += dx
        y += dy

        dot = [round(x), round(y)]

        dots.append(dot)

        if step_count:
            if not((round(x + dx) == round(x) and
                        round(y + dy) != round(y)) or
                        (round(x + dx) != round(x) and
                        round(y + dy) == round(y))):
                steps += 1

        i += 1

    if step_count:
        return steps
    else:
        return dots


def dda_seg_draw(canvas, x1, y1, x2, y2, line_color):
    points = dda_method(x1, y1, x2, y2)
    draw_line(canvas, points, line_color)


def bresenham_int(x1, y1, x2, y2, step_count=False):
    if (x2 - x1 == 0) and (y2 - y1 == 0):
        return [[x1, y1]]

    x = x1
    y = y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)

    if (dy > dx):
        tmp = dx
        dx = dy
        dy = tmp
        swaped = 1
    else:
        swaped = 0

    e = 2 * dy - dx

    i = 1

    dots = []

    steps = 0

    while (i <= dx + 1):
        dot = [x, y]
        dots.append(dot)

        x_buf = x
        y_buf = y

        while (e >= 0):
            if (swaped):
                x = x + s1
            else:
                y = y + s2

            e = e - 2 * dx

        if (swaped):
            y = y + s2
        else:
            x = x + s1

        e = e + 2 * dy

        if step_count:
            if ((x_buf != x) and (y_buf != y)):
                steps += 1

        i += 1

    if step_count:
        return steps
    else:
        return dots


def bresenham_int_seg_draw(canvas, x1, y1, x2, y2, line_color):
    points = bresenham_int(x1, y1, x2, y2)
    draw_line(canvas, points, line_color)


def bresenham_float(x1, y1, x2, y2, step_count=False):
    if (x2 - x1 == 0) and (y2 - y1 == 0):
        return [[x1, y1]]

    x = x1
    y = y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)

    if (dy > dx):
        tmp = dx
        dx = dy
        dy = tmp
        swaped = 1
    else:
        swaped = 0

    m = dy / dx
    e = m - 0.5
    i = 1

    dots = []

    steps = 0

    while (i <= dx + 1):
        dot = [x, y]
        dots.append(dot)

        x_buf = x
        y_buf = y

        while (e >= 0):
            if (swaped):
                x = x + s1
            else:
                y = y + s2

            e = e - 1

        if (swaped):
            y = y + s2
        else:
            x = x + s1

        e = e + m

        if step_count:
            if not((x_buf == x and y_buf != y) or
                    (x_buf != x and y_buf == y)):
                steps += 1

        i += 1

    if step_count:
        return steps
    else:
        return dots


def bresenham_float_seg_draw(canvas, x1, y1, x2, y2, line_color):
    points = bresenham_float(x1, y1, x2, y2)
    draw_line(canvas, points, line_color)
    return


def bresenham_aa(x1, y1, x2, y2, color, step_count = False):
    if (x2 - x1 == 0) and (y2 - y1 == 0):
        return [[x1, y1, matplotlib.colors.cnames[color]]]

    x = x1
    y = y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)

    if (dy > dx):
        tmp = dx
        dx = dy
        dy = tmp
        swaped = 1
    else:
        swaped = 0

    intens = 255

    m = dy / dx
    e = intens / 2

    m *= intens
    w = intens - m

    dots = [[x, y, choose_color(matplotlib.colors.cnames[color], round(e))]]

    i = 1

    steps = 0

    while (i <= dx):
        x_buf = x
        y_buf = y

        if (e < w):
            if (swaped):
                y += s2
            else:
                x += s1
            e += m
        else:
            x += s1
            y += s2

            e -= w

        dot = [x, y, choose_color(matplotlib.colors.cnames[color], round(e))]

        dots.append(dot)

        if step_count:
            if not((x_buf == x and y_buf != y) or
                    (x_buf != x and y_buf == y)):
                steps += 1

        i += 1

    if step_count:
        return steps
    else:
        return dots


def bresenham_aa_seg_draw(canvas, x1, y1, x2, y2, line_color):
    points = bresenham_aa(x1, y1, x2, y2, line_color)
    draw_aa_line(canvas, points)
    return


def wu(x1, y1, x2, y2, color, step_count=False):
    if (x2 - x1 == 0) and (y2 - y1 == 0):
        return [[x1, y1, matplotlib.colors.cnames[color]]]


    dx = x2 - x1
    dy = y2 - y1

    m = 1
    step = 1
    intens = 255

    dots = []

    steps = 0

    if (fabs(dy) > fabs(dx)):
        if (dy != 0):
            m = dx / dy
        m1 = m

        if (y1 > y2):
            m1 *= -1
            step *= -1

        y_end = round(y2) - 1 if (dy < dx) else (round(y2) + 1)

        for y_cur in range(round(y1), y_end, step):
            d1 = x1 - floor(x1)
            d2 = 1 - d1

            dot1 = [int(x1) + 1, y_cur, choose_color(matplotlib.colors.cnames[color], round(fabs(d2) * intens))]

            dot2 = [int(x1), y_cur, choose_color(matplotlib.colors.cnames[color], round(fabs(d1) * intens))]

            if step_count and y_cur < y2:
                if (int(x1) != int(x1 + m)):
                    steps += 1

            dots.append(dot1)
            dots.append(dot2)

            x1 += m1

    else:
        if (dx != 0):
            m = dy / dx

        m1 = m

        if (x1 > x2):
            step *= -1
            m1 *= -1

        x_end = round(x2) - 1 if (dy > dx) else (round(x2) + 1)

        for x_cur in range(round(x1), x_end, step):
            d1 = y1 - floor(y1)
            d2 = 1 - d1

            dot1 = [x_cur, int(y1) + 1, choose_color(matplotlib.colors.cnames[color], round(fabs(d2) * intens))]

            dot2 = [x_cur, int(y1), choose_color(matplotlib.colors.cnames[color], round(fabs(d1) * intens))]

            if step_count and x_cur < x2:
                if (int(y1) != int(y1 + m)):
                    steps += 1

            dots.append(dot1)
            dots.append(dot2)

            y1 += m1

    if step_count:
        return steps
    else:
        return dots


def wu_seg_draw(canvas, x1, y1, x2, y2, line_color):
    points = wu(x1, y1, x2, y2, line_color)
    draw_aa_line(canvas, points)
    return


def tk_seg_draw(canvas, x1, y1, x2, y2, line_color):
    canvas.create_line(x1, y1, x2, y2, fill=line_color)


def draw_segment(canvas, x1, y1, x2, y2, line_color, alg):
    canvas.create_line(x1, y1, x2, y2, fill=line_color)
    return


def alg_seg_handler(canvas, x1, y1, x2, y2, line_color, alg):
    # 'DDA', 'Bresenham(float)', 'Bresenham(int)', 'Bresenham(aa)', 'Wu', 'Tk lib'
    if alg == 'Tk lib':
        tk_seg_draw(canvas, x1, y1, x2, y2, line_color)
    if alg == 'DDA':
        dda_seg_draw(canvas, x1, y1, x2, y2, line_color)
    if alg == 'Bresenham(float)':
        bresenham_float_seg_draw(canvas, x1, y1, x2, y2, line_color)
    if alg == 'Bresenham(int)':
        bresenham_int_seg_draw(canvas, x1, y1, x2, y2, line_color)
    if alg == 'Bresenham(aa)':
        bresenham_aa_seg_draw(canvas, x1, y1, x2, y2, line_color)
    if alg == 'Wu':
        wu_seg_draw(canvas, x1, y1, x2, y2, line_color)
    return


def draw_beam(canvas, seg_len, angle, line_color, alg):
    center_point = [canvas.winfo_width() // 2, canvas.winfo_height() // 2]
    angle_passed = 0
    if angle <= 0:
        return

    while angle_passed < 360:
        x_beam = center_point[0] + cos(deg_to_rad(angle_passed)) * seg_len
        y_beam = center_point[1] + sin(deg_to_rad(angle_passed)) * seg_len

        alg_seg_handler(canvas, center_point[0], center_point[1], x_beam, y_beam, line_color, alg)

        angle_passed += angle
    return
