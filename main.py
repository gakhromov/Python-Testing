import alg
import draw
import utils
import numpy as np
import unittest


# black box testing
class TestBlackBox(unittest.TestCase):
    def test_black_box(self):
        tests = [
            {
                'input': {'x0': 1, 'y0': 2, 'a': 3, 'b': 2, 'd': 4.2},
                'output': [(-1.982, 2.218), (-0.449, 3.751), (0.262, 3.938), (3.4, 0.8)]
            },
            {
                'input': {'x0': -5.4, 'y0': 2, 'a': 3, 'b': 2, 'd': 2.5},
                'output': [(-6.388, 3.888), (-3.165, 0.665)]
            },
            {
                'input': {'x0': 0, 'y0': 4, 'a': 3, 'b': 2, 'd': 1},
                'output': []
            },
            {
                'input': {'x0': 0, 'y0': 4, 'a': 3, 'b': 2, 'd': 2},
                'output': [(0.0, 2.0)]
            },
            {
                'input': {'x0': 0, 'y0': 4, 'a': 3, 'b': 2, 'd': -1},
                'output': [(-3.0, 4.0), (-1.154, 2.154), (1.154, 2.154), (3.0, 4.0)]
            },
        ]
        for test in tests:
            # test that calculated == true
            calculated_out = utils.round_point_array(sorted(alg.get_intersection_points(**test['input'])))
            test_out = utils.round_point_array(sorted(test['output']))
            try:
                self.assertListEqual(calculated_out, test_out)
            except:
                # draw if incorrect
                graph = draw.Graph(title='Failed test plot')
                graph.draw_ellipse_line_intersections(**test['input'], 
                                                            intersections_calc=calculated_out,
                                                            intersections_true=test['output'])
                graph.show()
                raise



class TestWhiteBox(unittest.TestCase):
    def test_sqr_sol(self):
        tests = [
            {
                'input': {'A': 5, 'B': 1, 'C': 1},  # no roots
                'output': None
            },
            {
                'input': {'A': 1, 'B': 2, 'C': 1},  # two same roots (one root)
                'output': (-1,)
            },
            {
                'input': {'A': 5, 'B': -4, 'C': -1},  # two roots
                'output': (1,-1/5)
            },
            {
                'input': {'A': 0, 'B': 1, 'C': -2},  # bx+c test
                'output': (2,)
            },
            {
                'input': {'A': 0, 'B': 0, 'C': -2},  # c test
                'output': None
            },
            {
                'input': {'A': 0, 'B': 1, 'C': 0},  # bx test
                'output': None
            },
            {
                'input': {'A': 2, 'B': 0, 'C': -8},  # ax^2+c test
                'output': (-2, 2)
            },
            {
                'input': {'A': 2, 'B': 0, 'C': 8},  # ax^2+c test
                'output': None
            },
            {
                'input': {'A': 2, 'B': 0, 'C': 0},  # ax^2 test
                'output': None
            },
            {
                'input': {'A': 2, 'B': -8, 'C': 0},  # ax^2+bx test
                'output': (0, 4)
            }
        ]
        for test in tests:
            # test that calculated == true
            calculated_out = alg.get_sqr_soultions(**test['input'])
            if calculated_out is not None:
                calculated_out = np.round(sorted(calculated_out), 2).tolist()

            if test['output'] is not None:
                test_out = np.round(sorted(test['output']), 2).tolist()
                self.assertListEqual(calculated_out, test_out)
            else:
                self.assertIs(calculated_out, None)


if __name__ == "__main__":
    unittest.main()
