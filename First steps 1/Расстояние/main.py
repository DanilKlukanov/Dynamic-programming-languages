dot1 = [float(i) for i in input().split()]

dot2 = [float(i) for i in input().split()]


way =("%.3f" % ((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2)**0.5)
print (way)