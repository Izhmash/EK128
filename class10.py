def unit(V):
    mag = (V[0]**2 + V[1]**2 + V[2]**2)**(1/2)
    for i in range(0, len(V)):
        V[i] /= mag
    return V
print(unit([31, 21, 19]))
