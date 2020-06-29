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
    def test_get_sqr_soultions(self):
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

    def test_get_intersection_points_with_line(self):
        tests = [
            {
                'input': {'k': 1, 'c': 1, 'x0': 1, 'a': 2, 'y0': 1, 'b': 1},
                'output': [(-0.6, 0.4), (1, 2)]
            },
            {
                'input': {'k': 0, 'c': 0, 'x0': 1, 'a': 2, 'y0': 1, 'b': 1},
                'output': [(1,0), ]
            },
            {
                'input': {'k': 0, 'c': 1, 'x0': 1, 'a': 2, 'y0': 1, 'b': 1},
                'output': [(-1,1), (3,1)]
            },
            {
                'input': {'k': 0, 'c': -1, 'x0': 1, 'a': 2, 'y0': 1, 'b': 1},
                'output': None
            },
        ]
        for test in tests:
            # test that calculated == true
            calculated_out = alg.get_intersection_points_with_line(**test['input'])
            if calculated_out is not None:
                calculated_out = utils.round_point_array(sorted(calculated_out))
            
            try:
                if test['output'] is not None:
                    test_out = utils.round_point_array(sorted(test['output']))
                    self.assertListEqual(calculated_out, test_out)
                else:
                    self.assertIs(calculated_out, test['output'])
            except:
                # draw if incorrect
                if test['output'] is not None:
                    graph = draw.Graph(title='Failed test plot')
                    graph.draw_ellipse(**test['input'])
                    graph.draw_line(**test['input'])
                    graph.draw_points(np.array(calculated_out)[:, 0], 
                                    np.array(calculated_out)[:, 1], 
                                    label='Calculated points')
                    graph.draw_points(np.array(test['output'])[:, 0], 
                                    np.array(test['output'])[:, 1], 
                                    label='True points')
                    graph.show()
                raise


    def test_get_lines(self):
        tests = [
            {
                'input': {'d': 5},
                'output': [{'k':-1,'c':-5,'bounds': ('-inf', -5)},
                           {'k':1,'c':5,'bounds': (-5, 0)},
                           {'k':-1,'c':5,'bounds': (0, 5)},
                           {'k':1,'c':-5,'bounds': (5, '+inf')}]
            },
            {
                'input': {'d': -5},
                'output': [{'k':-1,'c':5,'bounds': ('-inf', 0)},
                           {'k':1,'c':5,'bounds': (0, '+inf')}]
            },
            {
                'input': {'d': 0},
                'output': [{'k':-1,'c':0,'bounds': ('-inf', 0)},
                           {'k':1,'c':0,'bounds': (0, '+inf')}]
            },
        ]
        for test in tests:
            # test that calculated == true
            calculated_out = alg.get_lines(**test['input'])
            calc_out_keys = [list(i.keys()) for i in calculated_out]
            calc_out_values = [list(i.values()) for i in calculated_out]
            test_out_keys = [list(i.keys()) for i in test['output']]
            test_out_values = [list(i.values()) for i in test['output']]
            
            self.assertListEqual(calc_out_keys, test_out_keys)
            self.assertListEqual(calc_out_values, test_out_values)


class TestModule(unittest.TestCase):
    def test_check_bounds(self):
        tests = [
            {
                'input': {'x':5, 'bounds':[-5, 5]},
                'output': True
            },
            {
                'input': {'x':10, 'bounds':[-5, 5]},
                'output': False
            },
            {
                'input': {'x':0, 'bounds':[0, 5]},
                'output': True
            },
            {
                'input': {'x':1, 'bounds':[1, 1]},
                'output': True
            },
            {
                'input': {'x':-99999999, 'bounds':['-inf', 2]},
                'output': True
            },
            {
                'input': {'x':3, 'bounds':['-inf', 2]},
                'output': False
            },
            {
                'input': {'x':99999999, 'bounds':[2, '+inf']},
                'output': True
            },
            {
                'input': {'x':-3, 'bounds':[2, '+inf']},
                'output': False
            },
            {
                'input': {'x':25683, 'bounds':['-inf', '+inf']},
                'output': True
            }
        ]
        for test in tests:
            calculated_out = alg.check_bounds(**test['input'])
            self.assertEqual(calculated_out, test['output'])


if __name__ == "__main__":
    unittest.main()
    
