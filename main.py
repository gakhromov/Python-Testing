import alg
import draw
import unittest


class TestClass(unittest.TestCase):
    def round_point_array(self, point_array, ndigits=2):
        new_point_array = []
        for point in point_array:
            el0 = round(point[0], ndigits)
            el1 = round(point[1], ndigits)
            new_point_array.append((el0, el1))
        return new_point_array
    
    # black box testing
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
        ]
        for test in tests:
            # test that calculated == true
            calculated_out = self.round_point_array(sorted(alg.get_intersection_points(**test['input'])))
            test_out = self.round_point_array(sorted(test['output']))
            try:
                self.assertListEqual(calculated_out, test_out)
            except:
                # draw if incorrect
                legend = draw.draw_ellipse_line_intersections(**test['input'], intersections=calculated_out)
                limits = draw.compute_lims(**values)
                draw.show(legend_handles=legend, **limits)
                raise
                

if __name__ == "__main__":
    unittest.main()
