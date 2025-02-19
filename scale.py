def scale(toponym):
    center = toponym["Point"]["pos"]
    low_x, low_y = toponym['boundedBy']['Envelope']['lowerCorner'].split()
    up_x, up_y = toponym['boundedBy']['Envelope']['upperCorner'].split()
    delta_x = abs(float(low_x) - float(up_x))
    delta_y = abs(float(low_y) - float(up_y))
    return center, delta_x, delta_y
