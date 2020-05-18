import numpy as np
import plotly.graph_objects as go


PRECISION = 10_000  # number of points for linspace
LEFT_X_LIM = -20  # "-infinity for x"
RIGHT_X_LIM = 20  # "+infinity for x"


class Graph():
    def __init__(self, title='Graph', **kwargs):
        self.fig = go.Figure()
        self.fig.update_layout(title=title,
                        xaxis_title='x', yaxis_title='y')


    def show(self):
        self.fig.show()
        del self  # destroy object


    # return x and y values for one line
    def ret_line(self, k, c, xbounds, **kwargs):
        # setup borders
        local_xbounds = list(xbounds)
        if xbounds[0] == '-inf':
            local_xbounds[0] = LEFT_X_LIM
        if xbounds[1] == '+inf':
            local_xbounds[1] = RIGHT_X_LIM
        
        xx = np.linspace(local_xbounds[0], local_xbounds[1], PRECISION)
        yy = k * xx + c

        xx = np.concatenate([xx, [None]])
        yy = np.concatenate([yy, [None]])
        return xx, yy


    def draw_line(self, k, c, **kwargs):
        xx = np.linspace(LEFT_X_LIM, RIGHT_X_LIM, PRECISION)
        yy = k * xx + c

        label = f'Line y = {k}x + {c}'
        self.fig.add_trace(go.Scatter(x=xx, y=yy, mode='lines', name=label))


    def draw_ellipse(self, x0, y0, a, b, color='blue', **kwargs):
        xx = np.linspace(x0-a, x0+a, PRECISION)
        # according to
        # https://colab.research.google.com/drive/1_S9dkafBOv-KLqmlQEW1cwP97nSKqmML?usp=sharing#scrollTo=LnelcVphsZEq
        # , compute yy+ and yy-:
        t = (xx - x0) ** 2 / (a**2)
        t = b * np.sqrt(1 - t)
        yy_plus = y0 + t
        yy_minus = y0 - t

        xx = np.concatenate([xx, np.flip(xx)])
        yy = np.concatenate([yy_minus, np.flip(yy_plus)])

        # draw
        label = f'Ellipse, centered at ({x0}, {y0}), stretched by ({a}, {b})'
        self.fig.add_trace(go.Scatter(x=xx, y=yy, mode='lines', name=label))


    def draw_points(self, x, y, color='grey', label='Intersection points', **kwargs):
        self.fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=label))
        

    # This function is almost a duplicate from alg.py
    # I copied them because I did not want to make dependencies.
    # I tried to make them as separate as possible.
    def draw_mod_line(self, d, color='red', **kwargs):
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
        
        xx = []
        yy = []
        for line in lines:
            xx1, yy1 = self.ret_line(**line)
            xx.append(xx1)
            yy.append(yy1)

        xx = np.concatenate(xx)
        yy = np.concatenate(yy)

        label = f'Line y = ||x| - {d}|'
        self.fig.add_trace(go.Scatter(x=xx, y=yy, mode='lines', name=label))


    def draw_ellipse_line_intersections(self, x0, y0, a, b, d, intersections_calc, intersections_true=None,
                                            color_l='red', color_e='blue', color_i_c='grey', color_i_t='orange', **kwargs):
        # draw line
        self.draw_mod_line(d, color_l)
        # draw ellipse
        self.draw_ellipse(x0, y0, a, b, color_e)
        # draw intersections calculated
        intersections_calc = np.array(intersections_calc)
        x_points_calc = intersections_calc[:, 0]
        y_points_calc = intersections_calc[:, 1]
        self.draw_points(x_points_calc, y_points_calc, color_i_c, label='Calculated intersections')
        # draw true intersections
        if intersections_true:
            intersections_true = np.array(intersections_true)
            x_points_true = intersections_true[:, 0]
            y_points_true = intersections_true[:, 1]
            self.draw_points(x_points_true, y_points_true, color_i_t, label='True intersections')
    