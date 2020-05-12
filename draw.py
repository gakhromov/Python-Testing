import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np


PRECISION = 10_000  # number of points for linspace
LEFT_X_LIM = -1000  # "-infinity for x"
RIGHT_X_LIM = 1000  # "+infinity for x"
DELTA = 1      # when computing limits, this will be added to final x_lim and y_lim 

def show(title='Graph', legend_handles=None, xlim=None, ylim=None, **kwargs):
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.title(title)
    if legend_handles is not None:
        plt.legend(handles=legend_handles)
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    plt.show()


def draw_line(k, c, xbounds, color='red', **kwargs):
    # setup borders
    local_xbounds = list(xbounds)
    if xbounds[0] == '-inf':
        local_xbounds[0] = LEFT_X_LIM
    if xbounds[1] == '+inf':
        local_xbounds[1] = RIGHT_X_LIM
    
    xx = np.linspace(local_xbounds[0], local_xbounds[1], PRECISION)
    yy = k * xx + c
    line = plt.plot(xx, yy, color=color, label=f'Line y = {k}x + {c}, x in ({local_xbounds[0]}, {local_xbounds[1]})')
    return line


def draw_ellipse(x0, y0, a, b, color='blue', **kwargs):
    xx = np.linspace(x0-a, x0+a, PRECISION)
    # according to
    # https://colab.research.google.com/drive/1_S9dkafBOv-KLqmlQEW1cwP97nSKqmML?usp=sharing#scrollTo=LnelcVphsZEq
    # , compute yy+ and yy-:
    t = (xx - x0) ** 2 / (a**2)
    t = b * np.sqrt(1 - t)
    yy_plus = y0 + t
    yy_minus = y0 - t
    plt.plot(xx, yy_minus, color=color)
    plt.plot(xx, yy_plus, color=color)
    return Line2D([0], [0], color=color, lw=2, label=f'Ellipse, centered at ({x0}, {y0}), stretched by ({a}, {b})')


def draw_point(x, y, color='grey', **kwargs):
    point = plt.plot([x], [y], 'o', color=color, label=f'Point at ({x}, {y})')
    return point


# This function is repeated from alg.py
# I copied them because I did not want to make dependencies.
# I tried to make them as separate as possible.
def draw_mod_line(d, color='red', **kwargs):
    # function y = ||x|-d| is always in area y > 0.
    # if d > 0, the function will look like letter W. Intersection points
    # with x-axis and y-axis are equal to d.
    # if d <= 0, the function will look like letter V. Intersection point
    # with y-axis will be equal to |d|.
    
    # Therefore, we can create 2 (or 4) lines (with proper bounds)
    # which we will then find intersections with.

    if d > 0:
        # lines of type y = kx+c
        lines = [{'k':-1,'c':-d,'xbounds': ('-inf', -d)},
                 {'k':1,'c':d,'xbounds': (-d, 0)},
                 {'k':-1,'c':d,'xbounds': (0, d)},
                 {'k':1,'c':-d,'xbounds': (d, '+inf')}]
    else:
        # lines of type y = kx+c
        lines = [{'k':-1,'c':-d,'xbounds': ('-inf', 0)},
                 {'k':1,'c':-d,'xbounds': (0, '+inf')}]
    
    for line in lines:
        draw_line(**line, color=color)
    return Line2D([0], [0], color=color, lw=2, label=f'Line y = ||x| - {d}|')


def draw_ellipse_line_intersections(x0, y0, a, b, d, intersections, color_l='red', color_e='blue', color_i='grey', **kwargs):
    legend = []
    # draw
    legend.append(draw_mod_line(d, color_l))
    legend.append(draw_ellipse(x0, y0, a, b, color_e))
    for point_x, point_y in intersections:
        draw_point(point_x, point_y, color_i)
    # add legend to points
    legend.append(Line2D([0], [0], color='w', marker='o', markerfacecolor=color_i, label='Intersection Points'))
    
    return legend


def compute_lims(x0, y0, a, b, **kwargs):
    x_left = (x0 - a) - DELTA
    x_right = (x0 + a) + DELTA
    y_left = (y0 - b) - DELTA
    y_right = (y0 + b) + DELTA

    return {'xlim': (x_left, x_right),
            'ylim': (y_left, y_right)}
    