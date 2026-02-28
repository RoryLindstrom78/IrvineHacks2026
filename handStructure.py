class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Finger:
    def __init__(self, mcp, pip, dip, tip):
        self.mcp = mcp # lowest
        self.pip = pip
        self.dip = dip
        self.tip = tip # highest


class Thumb:
    def __init__(self, cmc, mcp, ip, tip):
        self.cmc = cmc
        self.mcp = mcp
        self.ip = ip
        self.tip = tip


class Hand:
    def __init__(self, points):
        self.wrist = points[0]

        self.thumb = Thumb(points[1], points[2], points[3], points[4])
        self.index = Finger(points[5], points[6], points[7], points[8])
        self.middle = Finger(points[9], points[10], points[11], points[12])
        self.ring = Finger(points[13], points[14], points[15], points[16])
        self.pinky = Finger(points[17], points[18], points[19], points[20])

def build_hand_from_flat(flattened):
    points = []
    for i in range(0, 63, 3):
        points.append(Point(flattened[i], flattened[i+1], flattened[i+2]))
    return Hand(points)