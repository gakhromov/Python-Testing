from math import sqrt


def get_sqr_soultions(A, B, C):
    # returns solutions to Ax^2 + Bx + C = 0
    D = B**2 - 4 * A * C

    if D < 0:
        return None
    elif D == 0:
        return (-B / (2 * A),)
    else:
        x1 = (-B + sqrt(D)) / (2 * A)
        x2 = (-B - sqrt(D)) / (2 * A)
        return x1, x2



def get_intersection_points_with_line(x0, y0, a, b, k, c):
    # according to
    # https://colab.research.google.com/drive/1_S9dkafBOv-KLqmlQEW1cwP97nSKqmML?usp=sharing
    # , compute A, B, C
    c1 = (c - y0) / k

    A = (b**2 + a**2 * k**2)
    B = (-2 * b**2 * x0 + 2 * a**2 * k**2 * c1)
    C = (b**2 * x0**2 + a**2 * k**2 * c1**2 - a**2 * b**2)

    # get x soultions 
    sol = get_sqr_soultions(A, B, C)

    if sol is None:
        return None
    else:
        res = []
        for x in sol:
            # get y solutions
            y = k * x + c
            res.append((x, y))

        return tuple(res)


def get_lines(d):
    # function y = ||x|-d| is always in area y > 0.
    # if d > 0, the function will look like letter W. Intersection points
    # with x-axis and y-axis are equal to d.
    # if d <= 0, the function will look like letter V. Intersection point
    # with y-axis will be equal to |d|.
    
    # Therefore, we can create 2 (or 4) lines (with proper bounds)
    # which we will then find intersections with.

    if d > 0:
        # lines of type y = kx+c
        lines = [{'k':-1,'c':-d,'bounds': ('-inf', -d)},
                 {'k':1,'c':d,'bounds': (-d, 0)},
                 {'k':-1,'c':d,'bounds': (0, d)},
                 {'k':1,'c':-d,'bounds': (d, '+inf')}]
    else:
        # lines of type y = kx+c
        lines = [{'k':-1,'c':-d,'bounds': ('-inf', 0)},
                 {'k':1,'c':-d,'bounds': (0, '+inf')}]
    return lines


def check_bounds(x, bounds):
    left = False
    right = False

    if bounds[0] == '-inf':
        left = True
    else:
        left = x >= bounds[0]

    if bounds[1] == '+inf':
        right = True
    else:
        right = x <= bounds[1]

    return left and right



def get_intersection_points(x0, y0, a, b, d):
    lines = get_lines(d)

    res = []

    for line in lines:
        sol = get_intersection_points_with_line(x0, y0, a, b, line['k'], line['c'])
        if sol is not None:
            for sol_x, sol_y in sol:
                # check for bounds:
                if check_bounds(sol_x, line['bounds']):
                    res.append((sol_x, sol_y))
    return res


# Variable with the function that we want to test
alg_to_test = get_intersection_points