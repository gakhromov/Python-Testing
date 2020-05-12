import alg
import draw

values = {'x0': 1, 'y0': 2, 'a': 3, 'b': 2, 'd': 4.2}
intersections = alg.get_intersection_points(**values)

legend = draw.draw_ellipse_line_intersections(**values, intersections=intersections)
limits = draw.compute_lims(**values)
draw.show(legend_handles=legend, **limits)
