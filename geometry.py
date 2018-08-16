import cmath

def twoPointsNormal(point1, point2, left = True):
    if point2[1] == point1[1] and point2[0] == point1[0]:
        print('ERROR: Same point?!?!?!?!', point1, point2)
        return (0,0)
    else:
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        if left:
            # normal to the left
            return (dy, -dx)
        else:
            # normal to the right
            return (-dy, dx)


def unitVector2p(vector):
    length = (vector[0]**2 + vector[1]**2)**(1/2)
    if length == 0:
        print('v[0]:',vector[0],' v[1]:',vector[1])
        return (0,0)
    return (vector[0]/length, vector[1]/length)


def middlePoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)


def pointOverNormal(point, normal, scale = 1.0):
    return (point[0] + normal[0] * scale, point[1] + normal[1] * scale)


def distance(p1, p2):
    """
    Computer the Euclidean distance between two points in 2D or 3D
    :param p1:
    :param p2:
    :return: distance between the points
    """
    len_p1 = len(p1)
    len_p2 = len(p2)
    if len_p1 < 2 or len_p1 > 3:
        raise ValueError("p1 has invalid dimension")
    if len_p2 < 2 or len_p2 > 3:
        raise ValueError("p2 has invalid dimension")
    if len_p1 != len_p2:
        raise ValueError("p1 and p2 dimensions must match")

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if len_p1 == 2:
        return cmath.sqrt(dx*dx + dy*dy)
    else:
        dz = p2[2] - p1[2]
        return cmath.sqrt(dx*dx + dy*dy + dz*dz)
