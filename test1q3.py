import math


def polar_difference(P, Q):
    rP = P[0]
    thetaP = P[1]
    rQ = Q[0]
    thetaQ = Q[1]
    xP = rP*math.cos(thetaP)
    yP = rP*math.sin(thetaP)
    xQ = rQ*math.cos(thetaQ)
    yQ = rQ*math.sin(thetaQ)
    rDiff = math.sqrt((xP - xQ)**2 + (yP - yQ)**2)
    thetaDiff = math.atan2((yP-yQ), (xP-xQ))
    return (rDiff, thetaDiff)

print(polar_difference((2, math.pi/4), (8, math.pi/6)))
