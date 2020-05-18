def round_point_array(point_array, ndigits=2):
    
    new_point_array = []
    for point in point_array:
        el0 = round(point[0], ndigits)
        el1 = round(point[1], ndigits)
        new_point_array.append((el0, el1))
    return new_point_array